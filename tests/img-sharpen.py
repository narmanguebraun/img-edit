from PIL import Image, ImageFilter

img = Image.open('./aw/bag-apc.jpg')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('aw/bag-apc-sharpen.jpg')
