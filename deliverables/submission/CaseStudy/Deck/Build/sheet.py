import sys, glob
from PIL import Image
a,b=int(sys.argv[1]),int(sys.argv[2]); cols=int(sys.argv[3]) if len(sys.argv)>3 else 2
fs=sorted(glob.glob('slide-*.png'))[a-1:b]
ims=[Image.open(f) for f in fs]
w,h=ims[0].size; sc=0.9 if cols==2 else 1.0
rows=(len(ims)+cols-1)//cols
s=Image.new('RGB',(w*cols,h*rows),'white')
for i,im in enumerate(ims): s.paste(im,((i%cols)*w,(i//cols)*h))
s=s.resize((int(s.width*sc),int(s.height*sc)))
s.save(f'sheet_{a}_{b}.png'); print(s.size)
