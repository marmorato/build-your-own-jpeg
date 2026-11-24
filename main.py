from first_seminar import ColorTranslator

#SEMINAR 1 COMPROBATION
r = int(input("Enter value r "))
g = int(input("Enter value g "))
b = int(input("Enter value b "))
translator = ColorTranslator()
yuv = translator.rgb_to_yuv(r, g, b)
print(f"YUV: {yuv}")    
rgb=translator.yuv_to_rgb(*yuv)
print(f"RGB: {rgb}")
translator.resize("images/original.png", "images/resized2.png", 2)
translator.resize("images/original.png", "images/resized4.png", 4)
translator.resize("images/original.png", "images/resized8.png", 8)