import base64

# Encode the image to a base64 string.
with open("h-img-fire.jpg", "rb") as img:
    s = base64.b64encode(img.read())

print(s)

# Save the encoded string to a file.
with open('encode.bin', "wb") as f:
    f.write(s)