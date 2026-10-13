import os
from PIL import Image
B=os.path.dirname(os.path.abspath(__file__)); F=os.path.join(B,'..','..','Figures'); O=os.path.join(B,'work','img'); os.makedirs(O,exist_ok=True)
im=Image.open(os.path.join(F,'Figure_6_kitchenphoto.jpg')); im.crop((0,0,1440,800)).save(os.path.join(O,'kitchen_reg.png'))
