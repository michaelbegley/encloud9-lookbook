import sys
from PIL import Image
f,out,h=sys.argv[1],sys.argv[2],int(sys.argv[3])
im=Image.open(f);W,H=im.size;tiles=[]
for y in range(0,H,h): tiles.append(im.crop((0,y,W,min(H,y+h))))
# put 3 columns side by side
for k in range(0,len(tiles),3):
    grp=tiles[k:k+3];canvas=Image.new('RGB',(W*3+40,h),'white')
    for n,t in enumerate(grp): canvas.paste(t,(n*(W+20),0))
    canvas.save(f"{out}-{k//3}.jpg",quality=70)
print(len(tiles))
