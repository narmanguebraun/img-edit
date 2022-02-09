from PIL import Image, ImageFilter
# filter grey and rotate
img = Image.open('./aw/bag-apc.jpg')
filtered_img = img.convert('L')
rotated_img = filtered_img.rotate(90)
rotated_img.save('bag-apc-grey-rotate.png', 'png')
