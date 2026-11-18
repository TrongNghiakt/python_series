from PIL import Image, ImageFilter
import os

# print(os.getcwd())
os.chdir("D:\\python_learning\\CSV")

# size_300 = (300, 300)
# size_700 = (700, 700)

# for f in os.listdir("D:\\python_learning\\CSV"):
#     if f.endswith(".jpg"):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)

#         i.thumbnail(size_700)
#         i.save('700/{}_700{}'.format(fn, fext))

#         i.thumbnail(size_300)
#         i.save('300/{}_300{}'.format(fn, fext))

# image1 = Image.open("D:\\python_learning\\CSV\\pup1.jpg")
# # image1.show()
# image1.save("D:\\python_learning\\CSV\\pup1.png")

image1 = Image.open("D:\\python_learning\\CSV\\pup1.jpg")
# image1.rotate(90).save("D:\\python_learning\\CSV\\pup1_rotated.jpg")
image1.convert("L").save("D:\\python_learning\\CSV\\pup1_grayscale.jpg")
image1.filter(ImageFilter.GaussianBlur(15)).save(
    "D:\\python_learning\\CSV\\pup1_blurred.jpg")
