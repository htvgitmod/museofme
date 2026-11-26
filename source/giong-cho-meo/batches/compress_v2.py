# Nen anh phu v2 ve max 1000px, q78, ghi de tai cho. Chi xu ly file trong cac file v2-*.json DA MERGE (khong dung part).
import json, os, glob
from PIL import Image
files=set()
for p in ['batches/v2-DGAP.json','batches/v2-D1.json','batches/v2-D2.json','batches/v2-D3.json','batches/v2-D4.json','batches/v2-D5.json','batches/v2-D6.json','batches/v2-C1.json','batches/v2-C2.json']:
    raw=json.load(open(p))
    d = raw if isinstance(raw, list) else raw.get('giong', raw)
    for b in d:
        for ph in b.get('anh_phu',[]):
            files.add(ph['file'])
print('files:', len(files))
before=after=done=skip=err=0
log=open('batches/compress_v2.log','w')
for f in sorted(files):
    if not os.path.exists(f):
        print('MISSING', f); log.write('MISSING %s\n'%f); continue
    try:
        sz0=os.path.getsize(f)
        im=Image.open(f)
        w,h=im.size
        if im.format!='JPEG':
            print('SKIP non-JPEG', f, im.format); skip+=1; log.write('SKIP %s %s\n'%(f,im.format)); continue
        if w<=1000 and sz0<=200*1024:
            skip+=1; before+=sz0; after+=sz0; continue
        if w>1000:
            im=im.resize((1000,int(h*1000/w)), Image.LANCZOS)
        if im.mode in ('RGBA','LA','P'):
            im=im.convert('RGB')
        im.save(f,'JPEG',quality=78,optimize=True,progressive=True)
        sz1=os.path.getsize(f)
        before+=sz0; after+=sz1; done+=1
        log.write('OK %s %d->%d %dx%d\n'%(f,sz0,sz1,im.size[0],im.size[1]))
    except Exception as e:
        print('ERR', f, e); log.write('ERR %s %s\n'%(f,e)); err+=1
log.close()
print('done=%d skip=%d err=%d'%(done,skip,err))
print('before=%.1f MB after=%.1f MB saved=%.1f MB'%((before)/1048576,(after)/1048576,(before-after)/1048576))
