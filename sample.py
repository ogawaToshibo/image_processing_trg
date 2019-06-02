from PIL import Image, ImageFilter, ImageOps

im = Image.open('/Users/ogawa/Downloads/1.JPG')

print(im.format, im.size, im.mode)
print(im.getextrema())
print(im.getpixel((256, 256)))

# new_im = im.convert('L').rotate(90).filter(ImageFilter.GaussianBlur())
# new_im.show()
# new_im.save('/Users/ogawa/Downloads/1_1.JPG', quality=95)

# im_invert = ImageOps.invert(im)
# im_invert.save('/Users/ogawa/Downloads/1_2.JPG', quality=95)