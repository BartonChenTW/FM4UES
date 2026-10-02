"""Link the first mention of each model on each page to its Appendix D row.

Run from the repository root:  python3 scripts/link_models.py _data/models.yml [--dry]
Names come from the data file's `name` plus ALIASES below. Models already
linked on a page are skipped, so re-running only adds missing links.
"""
import re, sys, glob, os

ALIASES = {  # extra spellings used in the text -> id
    'GridFM-v0': 'gridfm',
    'Tiny Time Mixers': 'ttm',
    'ScaleMAE': 'scale-mae',
    'SAM2': 'sam-2',
    'TabPFN': 'tabpfn-v2',
    'GPT-5-class': 'gpt-5',
    'LLaMA': 'llama',
}
# index.md names Claude only in the AI-assistance credit, which is not a model mention
SKIP_FILES = {'appendices/a-glossary.md', 'appendices/c-version-history.md', 'appendices/d-model-index.md', 'index.md'}


def load_names(path):
    names = {}
    cur = None
    for line in open(path):
        m = re.match(r'^- id:\s*(\S+)', line)
        if m:
            cur = m.group(1).strip('"\'')
            continue
        m = re.match(r'^\s+name:\s*(.+?)\s*$', line)
        if m and cur:
            names[m.group(1).strip('"\'')] = cur
    names.update(ALIASES)
    return names


# Regions where a name must not be linked
MASK = re.compile(
    r'\[\^[^\]]+\]'              # footnote refs
    r'|!?\[[^\]]*\]\([^)]*\)'    # links and images
    r'|`[^`]*`'                  # inline code
    r'|<[^>]+>'                  # HTML tags
    r'|\{%.*?%\}|\{\{.*?\}\}'    # Liquid
    r'|\{:[^}]*\}'               # kramdown attributes
    r'|https?://\S+'             # bare URLs
)


def rel_prefix(path):
    d = os.path.dirname(path)
    if d == '':
        return 'appendices/d-model-index.html'
    if d == 'appendices':
        return 'd-model-index.html'
    return '../appendices/d-model-index.html'


def link_file(path, names, dry):
    lines = open(path).read().split('\n')
    pattern = re.compile(
        r'(?<![\w.-])(' + '|'.join(re.escape(n) for n in sorted(names, key=len, reverse=True)) + r')(?![\w-]|\.\d)')
    # Models already linked on this page count as done, so re-running the
    # script only adds links for new mentions.
    done = set(re.findall(r'd-model-index\.html#([a-z0-9-]+)', '\n'.join(lines)))
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
        if in_fence or line.startswith('#') or re.match(r'^\[\^[^\]]+\]:', line) or '<pre' in line:
            continue
        masked = [(m.start(), m.end()) for m in MASK.finditer(line)]
        out, pos = [], 0
        for m in pattern.finditer(line):
            if any(a <= m.start() < b for a, b in masked):
                continue
            mid = names[m.group(1)]
            if mid in done:
                continue
            done.add(mid)
            out.append(line[pos:m.start()])
            out.append('[%s](%s#%s)' % (m.group(1), rel_prefix(path), mid))
            pos = m.end()
            changes.append((i + 1, m.group(1)))
        if out:
            out.append(line[pos:])
            lines[i] = ''.join(out)
    if changes and not dry:
        open(path, 'w').write('\n'.join(lines))
    return changes


if __name__ == '__main__':
    names = load_names(sys.argv[1])
    dry = '--dry' in sys.argv
    total = 0
    files = sorted(glob.glob('chapter-*/*.md') + glob.glob('appendices/*.md') + ['index.md'])
    for f in files:
        if f in SKIP_FILES:
            continue
        ch = link_file(f, names, dry)
        total += len(ch)
        if ch:
            print(f, ', '.join('%s@%d' % (n, l) for l, n in ch))
    print('links', total)
