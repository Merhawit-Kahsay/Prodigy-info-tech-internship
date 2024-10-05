from PIL import Image
image = Image.open("C:\\Users\\hp\\Desktop\\Prodigy info tech tasks\\PRODIGY_CS_02\\to be_encrypted.jpeg")

width, height = image.size

key = 0x12345678

for x in range(width):
    for y in range(height):
        pixel = image.getpixel((x, y))

        encrypted_pixel = (
            pixel[0] ^ (key & 0xFF),
            pixel[1] ^ ((key >> 8) & 0xFF),
            pixel[2] ^ ((key >> 16) & 0xFF)
        )

        image.putpixel((x, y), encrypted_pixel)

image.save("C:\\Users\\hp\\Desktop\\Prodigy info tech tasks\\PRODIGY_CS_02\\encrypted.jpeg")
