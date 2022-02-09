from PIL import Image, ImageFilter
# filter grey
img = Image.open('./aw/bag-apc.jpg')
filtered_img = img.convert('L')
filtered_img.save('aw/bag-apc-grey.jpg')
