#!/usr/bin/env python3
"""Bundelt de pagina's in src/ tot één bestand: index.html.

De gekozen pagina wordt bij het laden in het document geschreven; wisselen
herlaadt het bestand met een andere pagina. Zo gebruikt nooit meer dan één
pagina tegelijk de camera's, en werkt cameratoegang ook als los bestand.
Standen, namen en instellingen blijven bewaard via localStorage.

Gebruik:  python3 build.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
PAGES = ['een-bord.html', 'twee-borden.html', 'klassement.html']

pages = {p: (ROOT / 'src' / p).read_text(encoding='utf-8') for p in PAGES}
# '</' escapen zodat '</script>' in een pagina het buitenste script niet afsluit
data = json.dumps(pages).replace('</', '<\\/')

html = """<!doctype html>
<meta charset="utf-8">
<script>
// Darttoernooi – alle pagina's in één bestand.
// De gekozen pagina wordt bij het laden in dit document geschreven; wisselen = herladen
// met een andere pagina. Zo draait alles op hetzelfde adres en blijft cameratoegang werken.
(function () {
  var P = __DATA__;
  var key = function (n) { return '#' + n.replace('.html', ''); };
  // ?tv in het adres = TV-scherm: geen bediening, volgt de pagina en alle wijzigingen van de laptop
  var display = window.dartsDisplay = /[?&](tv|scherm)(?![a-z])/i.test(location.search);
  window.dartsShow = function (n) {
    if (!P[n] || display) return;
    try { localStorage.setItem('darts-shell-page', n); } catch (e) {}
    location.hash = key(n);
    location.reload();
  };
  var s = location.hash.slice(1) + '.html', stored = null;
  try { stored = localStorage.getItem('darts-shell-page'); } catch (e) {}
  if (display || !P[s]) s = stored;
  if (!P[s]) s = 'twee-borden.html';
  if (!display) { try { localStorage.setItem('darts-shell-page', s); } catch (e) {} }
  if (location.hash !== key(s)) history.replaceState(null, '', key(s));
  if (display) {
    window.addEventListener('storage', function (e) {
      if (e.key === 'darts-shell-page' && P[e.newValue] && e.newValue !== s) { location.hash = key(e.newValue); location.reload(); }
    });
    document.title = 'TV-scherm';
  }
  document.write(P[s]);
})();
</script>
""".replace('__DATA__', data)

(ROOT / 'index.html').write_text(html, encoding='utf-8')
print('index.html geschreven:', len(html) // 1024, 'kB')
