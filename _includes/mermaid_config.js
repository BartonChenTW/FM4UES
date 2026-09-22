{%- comment -%}
  Mermaid config, matched to the reader's light/dark choice.

  just-the-docs inlines this file as `var config = <this file>;` inside
  the <script type="module"> in _includes/components/mermaid.html, right
  after `import mermaid from ...` and right before mermaid.initialize()
  and mermaid.run() -- confirmed against the theme's own source. The
  theme's default for this file is `{}`, and overriding it here is the
  customisation point the theme documents. So what follows must be a
  single JS *expression*; it is an IIFE so it can do setup work first.

  Without this, Mermaid always rendered with its default (light) theme:
  the dark-mode toggle (nav_footer_custom.html) only swaps the theme
  stylesheet, and Mermaid draws its colours into each SVG at render
  time, so diagrams stayed light-on-dark.

  Two things are handled:
  1. First render uses the saved preference -- the same localStorage
     'theme' key that head_custom.html and nav_footer_custom.html use.
  2. Toggling mid-page re-renders. Mermaid replaces each diagram's
     source text with its SVG, so the source is stashed on the element
     before the first render, and window.fmRerenderMermaid(theme) --
     called by the toggle's click handler -- puts it back and re-runs.
     `mermaid` is in scope here because this runs inside the module
     that imported it.

  No Liquid output tags may appear below: this file goes through Liquid
  as an include.
{%- endcomment -%}
(function () {
  function mermaidTheme(theme) {
    return theme === 'dark' ? 'dark' : 'default';
  }

  var saved = null;
  try { saved = localStorage.getItem('theme'); } catch (e) { /* ignore */ }
  var initial = saved || (typeof jtd !== 'undefined' && typeof jtd.getTheme === 'function' ? jtd.getTheme() : 'light');

  var nodes = document.querySelectorAll('.language-mermaid');
  for (var i = 0; i < nodes.length; i++) {
    nodes[i].setAttribute('data-fm-source', nodes[i].textContent);
  }

  window.fmRerenderMermaid = function (theme) {
    if (typeof mermaid === 'undefined' || typeof mermaid.run !== 'function') { return; }
    var diagrams = document.querySelectorAll('.language-mermaid[data-fm-source]');
    if (!diagrams.length) { return; }
    for (var j = 0; j < diagrams.length; j++) {
      diagrams[j].textContent = diagrams[j].getAttribute('data-fm-source');
      diagrams[j].removeAttribute('data-processed');
    }
    mermaid.initialize({ theme: mermaidTheme(theme) });
    mermaid.run({ querySelector: '.language-mermaid' });
  };

  return { theme: mermaidTheme(initial) };
})()
