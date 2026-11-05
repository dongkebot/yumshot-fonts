#!/usr/bin/env python3
"""按需取 YumShot 字体，逐个校验 SHA-256。只用标准库。

用法（不需要先 clone 仓库，单独下载本脚本就能跑）：
  python3 fetch_fonts.py --list                       # 列出所有字体 key / 文件
  python3 fetch_fonts.py --web --out ./fonts          # 30 款 woff2 + fonts.css（网页/画布渲染）
  python3 fetch_fonts.py --key song hei mont --out ./fonts
  python3 fetch_fonts.py --style 手写暖感 --out ./fonts  # 8 类风格之一的完整字体
  python3 fetch_fonts.py --full Yozai-Bold.ttf --out ./fonts
  python3 fetch_fonts.py --all --out ./fonts          # 全部（约 160 MB）

输出保持仓库内相对路径（web/…、full/fonts/…），所以 web/fonts.css 里的 url() 直接可用。
来源顺序：脚本所在仓库的本地文件 → $YUMSHOT_FONTS_BASE → GitHub raw。
私有仓库时设置 GITHUB_TOKEN 环境变量。
"""
import argparse, hashlib, json, os, shutil, sys, urllib.request

BASE = os.environ.get('YUMSHOT_FONTS_BASE', 'https://raw.githubusercontent.com/dongkebot/yumshot-fonts/main/')
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL = os.path.exists(os.path.join(HERE, 'manifest.json'))


def get(rel):
    if LOCAL and os.path.exists(os.path.join(HERE, rel)):
        return open(os.path.join(HERE, rel), 'rb').read()
    req = urllib.request.Request(BASE.rstrip('/') + '/' + urllib.request.quote(rel))
    tok = os.environ.get('GITHUB_TOKEN')
    if tok:
        req.add_header('Authorization', 'token ' + tok)
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def save(rel, out, want_sha=None):
    dst = os.path.join(out, rel)
    if want_sha and os.path.exists(dst) and hashlib.sha256(open(dst, 'rb').read()).hexdigest() == want_sha:
        return dst, 'cached'
    data = get(rel)
    if want_sha and hashlib.sha256(data).hexdigest() != want_sha:
        sys.exit(f'SHA 不符：{rel}')
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, 'wb').write(data)
    return dst, 'ok'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='./yumshot-fonts')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--web', action='store_true')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--key', nargs='*', default=[])
    ap.add_argument('--full', nargs='*', default=[])
    ap.add_argument('--style', nargs='*', default=[])
    a = ap.parse_args()
    M = json.loads(get('manifest.json'))
    web, full = M['web']['fonts'], M['full']['fonts']
    if a.list:
        print('web（woff2 子集）:')
        for f in web:
            print(f"  {f['key']:<11}{f['cssFamily']} {f['weight']} {f['style']}")
        print('full（完整字体）:')
        for f in full:
            print(f"  {f['file']:<36}{f['bytes'] / 1e6:5.1f} MB")
        print('8 类风格:', '、'.join(s['style'] for s in M['full']['styles']))
        return
    picks = []
    if a.web or a.all:
        picks += [(f['path'], f['sha256']) for f in web] + [('web/fonts.css', None), ('web/字体清单.md', None)] + [(x, None) for x in M['web'].get('licenses', [])]
    for k in a.key:
        hit = [f for f in web if f['key'] == k]
        if not hit:
            sys.exit(f'没有这个 key：{k}（--list 查看）')
        picks.append((hit[0]['path'], hit[0]['sha256']))
    if a.key:
        picks.append(('web/fonts.css', None))
    wanted = set(a.full)
    for s in a.style:
        st = [x for x in M['full']['styles'] if x['style'] == s]
        if not st:
            sys.exit(f'没有这个风格：{s}')
        wanted |= {os.path.basename(p) for p in st[0]['chinese'] + st[0]['latin']}
    for f in full:
        if a.all or f['file'] in wanted:
            picks.append((f['path'], f['sha256']))
            picks.append((f['licenseFile'], None))
            wanted.discard(f['file'])
    if wanted:
        sys.exit('没有这些完整字体：' + '、'.join(sorted(wanted)))
    if not picks:
        ap.print_help()
        return
    seen = set()
    for rel, h in picks:
        if rel in seen:
            continue
        seen.add(rel)
        dst, st = save(rel, a.out, h)
        print(st, dst)


if __name__ == '__main__':
    main()
