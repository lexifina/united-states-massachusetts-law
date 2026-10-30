"""Bring repo/README.md, repo/LICENSE and repo/jurisdiction.json up to date with the verified General Laws parts
(corpus.d/gl-*.json that have a .PUBLISH sign-off). Idempotent; no network.
    python -X utf8 docs_gl.py
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, 'repo')
NL = '\n'
parts = sorted(p for p in os.listdir(os.path.join(HERE, 'corpus.d')) if p.endswith('.json')
               and os.path.exists(os.path.join(HERE, 'corpus.d', p[:-5] + '.PUBLISH')))
acts = [json.load(open(os.path.join(HERE, 'corpus.d', p), encoding='utf-8'))['acts'][0] for p in parts]
acts.sort(key=lambda a: a['slug'])

rd = os.path.join(R, 'README.md')
t = open(rd, encoding='utf-8').read()
t = re.sub(r'\n\| `gl-chapter-[^\n]*', '', t)
rows = ''.join(
    f"{NL}| `{a['slug']}/` | {a['title']} | {len(a['versions'][0]['units'])} | One version: the General Court's online text, "
    f"each section from its newest web capture (captured {a['versions'][0]['note'].split('between ')[1].split(':')[0].replace(' and ', ' to ')}), dated {a['versions'][0]['from']} |"
    for a in acts)
i = t.index('| `constitution/` |')
j = t.index(NL, i)
t = t[:j] + rows + t[j:]
t = re.sub(r'The Constitution of the Commonwealth of Massachusetts as a git repository: one file per article, section or article of amendment,',
           'The Constitution of the Commonwealth of Massachusetts and chapters of the General Laws as a git repository: one file per article, section or article of amendment of the Constitution and one per section of the General Laws,', t)
t = re.sub(r'That is all the law this repository holds today\.[^\n]*',
           'That is all the law this repository holds today. This is a first build: most chapters of the General Laws, the session laws and regulations are not in it, and it has no amendment history yet.', t)
gl_src = ('\n\nThe General Laws are published one page per section (malegislature.gov/Laws/GeneralLaws/...), with a table of '
          'contents page per chapter. A chapter is included only when every section its table of contents lists was read: '
          'each section page comes from its newest **Common Crawl** capture, or, where Common Crawl had none, its newest '
          '**Internet Archive** capture from 2025 on. The sha256 of the pages read for each chapter is in `data/versions.json`.')
t = t.replace(gl_src, '')
k = t.index('## Dates')
t = t[:k].rstrip(NL) + gl_src + NL + NL + t[k:]
gl_date = ("- Each General Laws chapter is one version, dated by the newest capture day of its section pages (or, if "
           "later, the day of the newest law already in the repository, so the history only grows), and credited to the "
           "publisher as \"oldest version available\". Its sections were captured on different days, which the commit's "
           "note gives; a section amended after its capture would show its older text here.")
t = re.sub(r'\n- Each General Laws chapter is one version[^\n]*', '', t)
t = t.replace(NL + gl_date, '')
k = t.index('## What it does not show')
t = t[:k].rstrip(NL) + NL + gl_date + NL + NL + t[k:]
t = t.replace('- The General Laws. Common Crawl holds only part of those pages, so they were not taken.',
              '- The other chapters of the General Laws: web archives hold only part of their section pages, so a chapter is left out until every one of its sections can be read.')
open(rd, 'w', encoding='utf-8', newline=NL).write(t)

lp = os.path.join(R, 'LICENSE')
lt = open(lp, encoding='utf-8').read()
para = ('The General Laws chapters are the text published by the General Court at https://malegislature.gov/Laws/GeneralLaws ,'
        + NL + 'read from Common Crawl and Internet Archive captures of its section pages (2025 and 2026). Statute text is not'
        + NL + 'copyrightable in the United States (Georgia v. Public.Resource.Org, above); no annotations are used.')
if acts and para not in lt:
    k = lt.index('The arrangement of this repository')
    lt = lt[:k] + para + NL + NL + lt[k:]
    open(lp, 'w', encoding='utf-8', newline=NL).write(lt)

jp = os.path.join(R, 'jurisdiction.json')
j = json.load(open(jp, encoding='utf-8'))
base = j['build'].split('; plus General Laws')[0]
if acts:
    base += '; plus General Laws chapters ' + ', '.join(a['short'].split('c. ')[1] for a in acts) + ' (one version each, from web captures)'
j['build'] = base
open(jp, 'w', encoding='utf-8', newline=NL).write(json.dumps(j, ensure_ascii=False, indent=2) + NL)
print(len(acts), 'chapters in docs')
