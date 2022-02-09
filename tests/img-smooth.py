from PIL import Image, ImageFilter
# filter smooth
img = Image.open('./aw/bag-apc.jpg')
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('aw/bag-apc-smooth.jpg')
# filtered_img.show()
