"""Reconstruct the tested viewport release from verified earlier archives and source deltas."""
import hashlib, json, subprocess, tempfile, zipfile, zlib
from pathlib import Path

def sha(data):
    return hashlib.sha256(data).hexdigest()

old20=Path('base20.zip').read_bytes()
old198=Path('base198.zip').read_bytes()
delta=Path('source.delta').read_bytes()
assert sha(old20)=='5778e22937008fdaf73b960fcf4857e296a891489df5cb48604f5d50c97507a8'
assert sha(old198)=='69dfb42a80fdb605674c097316b0eedd82fcea2d0eb3db0bf65292b386c4b284'
assert sha(delta)=='17b08c105d514aa985ff533d49d6f9948e3c02f67c8733f34b6a5a9bd9ea4fda'
changes=json.loads(zlib.decompress(delta))
with zipfile.ZipFile('base20.zip') as z:
    assert z.testzip() is None
    payload={p[len('payload/'):]:z.read(p) for p in z.namelist() if p.startswith('payload/')}
with zipfile.ZipFile('base198.zip') as z:
    assert z.testzip() is None
    payload['engine/application.py']=z.read('payload/engine/application.py')
assert sha(payload['engine/application.py'])=='fbff8e8ebda4fe500509602d6717a81a9f1001e5411c35c06cffdd69a1538d9c'
with tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp)
    for name in ('engine/application.py','engine/editor.py'):
        f=root/name
        f.parent.mkdir(parents=True,exist_ok=True)
        f.write_bytes(payload[name])
        subprocess.run(['patch','--batch','--forward','--fuzz=0','-p1'],cwd=root,input=changes[name].encode(),check=True)
        payload[name]=f.read_bytes()
for name in ('engine/viewport_tools.py','VERSION'):
    payload[name]=changes[name].encode()
expected={
    'engine/application.py':'bb9bd2cd7bc9ebb1259c6b2d00bb3b60a77ab54bac0f295f8ca463244b094e5f',
    'engine/editor.py':'6c25093f2a0d4202c20e79f4ffe644893daa7abf9b8c999d898adf2e0b2751c9',
    'engine/viewport_tools.py':'e183cf1761fb5556bde8c5c691ef0bf72aed6ea080a2d5382cece4e95e7960e7',
    'VERSION':'374c2ee0c45e53453feeea1e53ed7bacea934f7658b6b2c4ff1f1226379f99cf'
}
for name,digest in expected.items():
    assert sha(payload[name])==digest, name
    if name.endswith('.py'):compile(payload[name],name,'exec')
for base in ('0.0.20','0.0.19.9'):
    manifest=changes['manifest_'+base]
    assert manifest['base']==base and manifest['target']=='0.0.21'
    assert manifest['format']=='aftershock-engine-update-v1'
    assert not manifest['remove']
    assert manifest['files'].keys() == (expected.keys() if base=='0.0.20' else payload.keys())
    path=Path(f'Aftershock_Update_{base}_to_0.0.21.zip')
    with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        z.writestr('manifest.json',json.dumps(manifest,sort_keys=True,indent=2))
        for name,digest in manifest['files'].items():
            assert sha(payload[name])==digest, name
            z.writestr('payload/'+name,payload[name])
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        assert json.loads(z.read('manifest.json'))==manifest
        for name,digest in manifest['files'].items():
            assert sha(z.read('payload/'+name))==digest
    print(path, path.stat().st_size, sha(path.read_bytes()), flush=True)
