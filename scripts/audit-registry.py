#!/usr/bin/env python3
import json
from pathlib import Path
data=json.loads(Path('repos.json').read_text())
repos=data['repositories']
print('Total:',len(repos))
print('Verified:',sum(bool(r['verified']) for r in repos))
print('Pending:',sum(not bool(r['verified']) for r in repos))
print('\nPending verification:')
for r in repos:
    if not r['verified']:
        print(f"- {r['name']}: {r['license']} — {r['upstream']}")
