from PIL import Image
import io
from googleSearchLib import googleSearchLib

gif = "image.gif"


im = Image.open(gif)
num_key_frames=im.n_frames

out= open('image.gif', 'rb')


for i in range(num_key_frames):
    im.seek(im.n_frames // num_key_frames * i)

    img_byte_arr = io.BytesIO()
    im.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()


    lib=googleSearchLib()
    lib.searchImage(img_byte_arr)
    #print(img_byte_arr)
    #im.save('{}.png'.format(i))
