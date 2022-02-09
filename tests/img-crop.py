from PIL import Image, ImageFilter

img = Image.open('./aw/bag-apc.jpg')
filtered_img = img.convert('L')
box = (100, 100, 400, 400)
cropped_img = filtered_img.crop(box)
cropped_img.save('bag-apc-grey-crop.png', 'png')
