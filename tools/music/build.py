#!/usr/bin/env python3
"""Inline the music engine and the nine stage songs into pages/nine-404.html.
Sources: tools/music/engine.js and tools/music/stage1.js .. stage9.js (copy finished songs here).
Run from the repo root: python3 tools/music/build.py"""
import os, re, sys
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
page = os.path.join(root, 'pages', 'nine-404.html')
m = os.path.join(root, 'tools', 'music')
s = open(page, encoding='utf-8').read()
def put(tag, body):
    global s
    a, b = '/*@@%s@@*/' % tag, '/*@@/%s@@*/' % tag
    i, j = s.index(a) + len(a), s.index(b)
    s = s[:i] + '\n' + body.strip() + '\n' + s[j:]
put('ENGINE', open(os.path.join(m, 'engine.js'), encoding='utf-8').read())
songs, missing = [], []
for n in range(1, 10):
    f = os.path.join(m, 'stage%d.js' % n)
    if os.path.exists(f):
        songs.append(open(f, encoding='utf-8').read().strip())
    else:
        missing.append(n)
put('SONGS', '\n'.join(songs))
open(page, 'w', encoding='utf-8').write(s)
print('songs in page: %d; missing stages: %s' % (len(songs), missing or 'none'))
