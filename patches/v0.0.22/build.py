"""Reconstruct the tested v0.0.22 package from verified earlier release files."""
import hashlib,json,zlib,zipfile
from pathlib import Path

def sha(b):return hashlib.sha256(b).hexdigest()
delta=b''.join(Path(f'delta-{i}').read_bytes() for i in range(5))
assert sha(delta)=='4e5e735897662be8316636e22cdcdaa9811f5681e4839b03b07224682ce83123'
data=json.loads(zlib.decompress(delta))
manifest=data['manifest']
assert manifest['base']=='0.0.21' and manifest['target']=='0.0.22'
assert manifest['base_fingerprint']=='9e6f679efed5cd193f9ace70a4ecc133d94720751cab14bad7d4970d9a594b23'
assert not manifest['remove']
assert set(data['changes'])==set(manifest['files'])
old={}
for filename,digest in (
 ('Aftershock_Update_0.0.19.6_to_0.0.19.7.zip','902db58fbea10743a1cf26b48e0125fa3111f1b367f2f733d393447a5e9251a3'),
 ('Aftershock_Update_0.0.19.8_to_0.0.19.9.zip','35d8825d794d1ebc2fa55c716f62c0af364531d7e339fc6f3ced57b76b2b5c01'),
 ('Aftershock_Update_0.0.19.9_to_0.0.21.zip','9eed1dc1bc11bae500a2108666b213b7f27499d563c210fdbe9421c0ec16993e')):
    assert sha(Path(filename).read_bytes())==digest,filename
    with zipfile.ZipFile(filename) as z:
        assert z.testzip() is None
        old.update({p[8:]:z.read(p) for p in z.namelist() if p.startswith('payload/')})
payload={}
for name,item in data['changes'].items():
    source=old.get(name,b'')
    assert sha(source)==item['old'],name
    lines=source.decode().splitlines(keepends=True)
    for i,j,content in reversed(item['edits']):lines[i:j]=[content]
    target=''.join(lines).encode()
    assert sha(target)==manifest['files'][name],name
    if name.endswith('.py'):compile(target,name,'exec')
    payload[name]=target
    print('Verified',name,flush=True)
out=Path('Aftershock_Update_0.0.21_to_0.0.22.zip')
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    z.writestr('manifest.json',json.dumps(manifest,sort_keys=True,indent=2))
    for name,target in sorted(payload.items()):z.writestr('payload/'+name,target)
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
    assert json.loads(z.read('manifest.json'))==manifest
    for name,digest in manifest['files'].items():assert sha(z.read('payload/'+name))==digest
print(out,out.stat().st_size,sha(out.read_bytes()),flush=True)
