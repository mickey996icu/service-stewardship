#!/usr/bin/env python3
"""Static packaging checks, not a behavioral evaluation or complete secret scanner."""
from pathlib import Path
import re
import shutil
import tempfile

root = Path(__file__).resolve().parents[1]
skill = root / 'skills' / 'service-stewardship'
required = [root / 'LICENSE', root / 'NOTICE.md', root / 'README.md',
            root / 'validation' / 'REPORT.md', skill / 'SKILL.md', skill / 'LICENSE', skill / 'NOTICE.md']
for path in required:
    assert path.is_file(), f'Missing: {path.relative_to(root)}'
files = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts]
patterns = {
    'absolute home path': r'/(?:Users|home)/[^\s/]+/',
    'GitHub token': r'gh[pousr]_[A-Za-z0-9]{20,}',
    'fine-grained token': r'github_pat_[A-Za-z0-9_]{20,}',
    'private key header': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
}
links = 0
for path in files:
    if path.suffix not in {'.md', '.py', '.yaml', '.yml'}:
        continue
    content = path.read_text()
    for label, pattern in patterns.items():
        assert not re.search(pattern, content), f'{label}: {path.relative_to(root)}'
    if path.suffix == '.md':
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            dest = (path.parent / target.split('#')[0]).resolve()
            assert dest.is_relative_to(root), f'Link escapes package: {target}'
            assert dest.exists(), f'Broken local link in {path.relative_to(root)}: {target}'
            links += 1
with tempfile.TemporaryDirectory(prefix='service-skill-check-') as tmp:
    dest = Path(tmp) / 'skills' / skill.name
    shutil.copytree(skill, dest)
    original = sorted(p.relative_to(skill) for p in skill.rglob('*') if p.is_file())
    copied = sorted(p.relative_to(dest) for p in dest.rglob('*') if p.is_file())
    assert original == copied
    for rel in original:
        assert (skill / rel).read_bytes() == (dest / rel).read_bytes()
print(f'Package checks passed: {len(files)} files inspected; {links} local links; isolated copy verified.')
print('No host discovery, model behavior, scheduling, or exhaustive secret scan is verified.')
