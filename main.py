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
# translator.resize("images/original.png", "images/resized2.png", 2)
# translator.resize("images/original.png", "images/resized4.png", 4)
# translator.resize("images/original.png", "images/resized8.png", 8)

zigzag_matrix = [
    [1, 2,3,4,5,6,7,8],
    [9, 10,11,12,13,14,15,16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56],
    [57, 58, 59, 60, 61, 62, 63, 64]
]   

zigzag_result = translator.zigzag(zigzag_matrix)
print(f"Zigzag: {zigzag_result}")

inverse_zigzag_result = translator.inverse_zigzag(zigzag_result)
print(f"Inverse Zigzag: {inverse_zigzag_result}")