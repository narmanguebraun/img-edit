from PIL import Image, ImageFilter

img = Image.open('./aw/bag-apc.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('aw/bag-apc-blur.jpg')
