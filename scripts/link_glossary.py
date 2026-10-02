"""Link the first mention of each glossary term on each page to its row.

Run from the repository root:  python3 scripts/link_glossary.py [--dry]
Terms already linked on a page are skipped, so re-running is safe.
"""
import re, sys, glob, os

# (regex, glossary id, case-sensitive?)  Longer phrases first.
TERMS = [
    (r'agent-based models?', 'agent-based-model-abm', False),
    (r'ABMs?', 'agent-based-model-abm', True),
    (r'amortised optimisation', 'amortised-optimisation', False),
    (r'any-variate attention', 'any-variate-attention', False),
    (r'basic elements?', 'basic-element', False),
    (r'co-simulation', 'co-simulation', False),
    (r'cross-attention|cross-attending|cross-attends?', 'cross-attention', False),
    (r'DAEs?', 'dae', True),
    (r'decision spaces?', 'decision-space', False),
    (r'embodied emissions', 'embodied-emissions', False),
    (r'energy burden', 'energy-burden', False),
    (r'energy hubs?', 'energy-hub', False),
    (r'energy justice', 'energy-justice', False),
    (r'energy poverty', 'energy-poverty', False),
    (r'EPDs?', 'epd', True),
    (r'fine-tuning', 'fine-tuning', False),
    (r'foundation models?', 'foundation-model', False),
    (r'in-context learning', 'in-context-learning', False),
    (r'LCI databases?', 'lci-database', True),
    (r'LCA', 'lca', True),
    (r'MILPs?', 'milp', True),
    (r'multimodality|multimodal', 'multimodality', False),
    (r'neural operators?', 'neural-operator', False),
    (r'patches|patch', 'patch', False),
    (r'prior-data fitted networks?', 'pfn-prior-data-fitted-network', False),
    (r'PFNs?', 'pfn-prior-data-fitted-network', True),
    (r'retrofit measures?', 'retrofit-measure', False),
    (r'reduced-order models?', 'rom', False),
    (r'ROMs?', 'rom', True),
    (r'cells?', 'cell', False),
    (r'self-supervised', 'self-supervised-pretraining', False),
    (r'silicon samples?', 'silicon-sample', False),
    (r'surrogates?', 'surrogate', False),
    (r'tokenisation|tokeniser', 'tokenisation', False),
    (r'transformers?', 'transformer', False),
    (r'TSFMs?', 'tsfm', True),
    (r'units? of observation', 'unit-of-observation', False),
    (r'whole-life carbon', 'whole-life-carbon', False),
    (r'zero-shot', 'zero-shot', False),
    (r'zoning ambiguity', 'zoning-ambiguity', False),
]
# Words that, directly before the term, make it part of a longer name
BLOCK_BEFORE = {
    'foundation-model': {'series', 'time-series', 'grid', 'power-grid', 'geospatial', 'weather', 'tabular',
                         'energy', 'energy-domain', 'load', 'vision', 'language', 'graph', 'building', 'hub',
                         'ues', 'multimodal', 'domain', 'district', 'stock', 'earth-system', 'observation',
                         'clean-energy', 'thermal', 'meter', 'smart-meter', 'general-purpose', 'pde', 'brain',
                         'ecg', 'federated', 'eo', 'demand', 'generation', 'renewable', 'foundational', 'on'},
    'transformer': {'swin', 'vision', 'fusion', 'time-series', 'series', 'standard', 'temporal'},
}
# Electrical transformers, not the ML architecture: (file, line)
SKIP_AT = {'transformer': {('chapter-4-directions/4-5-screening-fields.md', 42),
                           ('chapter-5-case-study/5-2-representation-problem.md', 37),
                           ('chapter-5-case-study/5-4-concrete-representation.md', 55)}}
# Terms linked only on pages that use them in the glossary's sense
ONLY_IN = {'cell': {'chapter-2-fm-foundations/2-3-choosing-a-basic-element.md', 'chapter-2-fm-foundations/2-4-4-tabular-fms.md'}}
SKIP_FILES = {'appendices/a-glossary.md', 'appendices/c-version-history.md', 'appendices/d-model-index.md'}

MASK = re.compile(
    r'\[\^[^\]]+\]'
    r'|!?\[[^\]]*\]\([^)]*\)'
    r'|`[^`]*`'
    r'|<[^>]+>'
    r'|\{%.*?%\}|\{\{.*?\}\}'
    r'|\{:[^}]*\}'
    r'|https?://\S+'
    r'|"[^"\n]{1,80}"'           # quoted strings, e.g. search terms
)


def rel(path):
    d = os.path.dirname(path)
    if d == '':
        return 'appendices/a-glossary.html'
    if d == 'appendices':
        return 'a-glossary.html'
    return '../appendices/a-glossary.html'


def link_file(path, dry):
    lines = open(path).read().split('\n')
    done = set(re.findall(r'a-glossary\.html#([a-z0-9-]+)', '\n'.join(lines)))
    compiled = [(re.compile(r'(?<![\w.-])(' + rx + r')(?![\w-])', 0 if cs else re.I), gid) for rx, gid, cs in TERMS]
    in_front = in_fence = False
    changes = []
    for i, line in enumerate(lines):
        if i == 0 and line == '---':
            in_front = True
            continue
        if in_front:
            if line == '---':
                in_front = False
            continue
        if line.lstrip().startswith('```'):
            in_fence = not in_fence
            continue
        if (in_fence or line.startswith('#') or re.match(r'^\[\^[^\]]+\]:', line) or '<pre' in line
                or line.startswith('[← ') or line.startswith('{:') or line.strip() in ('1. TOC', '{:toc}')):
            continue
        # collect candidate matches on this line, earliest first, no overlaps
        cands = []
        for rx, gid in compiled:
            if gid in done or (gid in ONLY_IN and path not in ONLY_IN[gid]):
                continue
            for m in rx.finditer(line):
                cands.append((m.start(), m.end(), gid))
        cands.sort()
        masked = [(m.start(), m.end()) for m in MASK.finditer(line)]
        taken, out, pos = [], [], 0
        for a, b, gid in cands:
            if gid in done or any(x <= a < y for x, y in masked) or any(x < b and a < y for x, y in taken):
                continue
            if (path, i + 1) in SKIP_AT.get(gid, ()):
                continue
            prev = re.findall(r'([\w-]+)\s+$', line[:a])
            if prev and prev[-1].lower() in BLOCK_BEFORE.get(gid, ()):
                continue
            done.add(gid)
            taken.append((a, b))
            out.append(line[pos:a])
            out.append('[%s](%s#%s)' % (line[a:b], rel(path), gid))
            pos = b
            changes.append((i + 1, line[a:b]))
        if out:
            out.append(line[pos:])
            lines[i] = ''.join(out)
    if changes and not dry:
        open(path, 'w').write('\n'.join(lines))
    return changes


if __name__ == '__main__':
    dry = '--dry' in sys.argv
    total = 0
    for f in sorted(glob.glob('chapter-*/*.md') + glob.glob('appendices/*.md') + ['index.md']):
        if f in SKIP_FILES:
            continue
        ch = link_file(f, dry)
        total += len(ch)
        if ch and '--quiet' not in sys.argv:
            print(f, ', '.join('%s@%d' % (n, l) for l, n in ch))
    print('links', total)
