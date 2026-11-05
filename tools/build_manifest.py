#!/usr/bin/env python3
"""重新生成 manifest.json（在仓库根目录运行）。新增或替换字体后执行。"""
import hashlib, json, os, re

def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()

def main():
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    css = open('web/fonts.css').read()
    web = []
    for m in re.finditer(r'font-family: "([^"]+)"; src: url\("([^"]+)"\)[^;]*; font-weight: ([^;]+); font-style: (\w+)', css):
        fam, src, w, st = m.groups(); p = 'web/' + src
        web.append(dict(key=os.path.basename(src)[:-6], cssFamily=fam, weight=w, style=st, path=p, bytes=os.path.getsize(p), sha256=sha(p)))
    full = []
    for root, _, fs in os.walk('full/fonts'):
        for f in sorted(fs):
            p = os.path.join(root, f)
            full.append(dict(file=f, family=os.path.basename(root), path=p, bytes=os.path.getsize(p), sha256=sha(p), license='OFL-1.1', licenseFile=f'full/licenses/{f}.LICENSE.txt'))
    full.sort(key=lambda x: x['path'])
    styles = [dict(style=x['style'], chinese=['full/' + f for f in x.get('chineseFiles', [])], latin=['full/' + f for f in x.get('latinFiles', [])], note=x.get('note', ''))
              for x in json.load(open('full/8类风格字体映射.json'))]
    old = json.load(open('manifest.json')) if os.path.exists('manifest.json') else {}
    M = {k: old.get(k) for k in ('name', 'version', 'repo', 'rawBase', 'license') if k in old}
    M['web'] = {'about': old.get('web', {}).get('about', ''), 'css': 'web/fonts.css', 'fonts': web, 'licenses': sorted('web/licenses/' + f for f in os.listdir('web/licenses'))}
    M['full'] = {'about': old.get('full', {}).get('about', ''), 'fonts': full, 'styles': styles}
    for f in web + full:
        assert os.path.exists(f['path'])
    for s in styles:
        for p in s['chinese'] + s['latin']:
            assert os.path.exists(p), p
    open('manifest.json', 'w').write(json.dumps(M, ensure_ascii=False, indent=2) + '\n')
    print(f'web {len(web)} · full {len(full)} · styles {len(styles)}')

if __name__ == '__main__':
    main()
