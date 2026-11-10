import sys
from PIL import Image
f,out,h=sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 2200
im=Image.open(f);W,H=im.size;i=0
for y in range(0,H,h):
    c=im.crop((0,y,W,min(H,y+h)))
    if W>800: c=c.resize((W//2,c.size[1]//2))
    c.save(f"{out}-{i}.jpg",quality=70);i+=1
print(i)
