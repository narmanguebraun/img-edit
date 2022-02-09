# from PIL import Image, ImageFilter

# img = Image.open('./aw/bag-apc.jpg')
# img.thumbnail((400,400))
# img.save('thumbnail.jpg')

# from PIL import Image, ImageFilter

# img = Image.open('./aw/bag-apc.jpg')
# resized_img = img.resize((400, 400)) #brackets
# resized_img.save('resized.png', 'png')

from PIL import Image, ImageFilter

img = Image.open('./aw/bag-apc.jpg')
img.thumbnail((400,400), Image.LANCZOS)
img.save('thumbnail-lanczos.jpg')

print(img.size)

