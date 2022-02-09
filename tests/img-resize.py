from PIL import Image, ImageFilter
# filter grey and resize
img = Image.open('./aw/bag-apc.jpg')
filtered_img = img.convert('L')
resized_img = filtered_img.resize((300, 400)) #brackets
resized_img.save('bag-apc-grey-resized.png', 'png')
