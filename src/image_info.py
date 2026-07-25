from PIL import Image

# Replace with the path of your image
image = Image.open("input_images/sample.jpg")

print("Image Size:", image.size)
print("Image Format:", image.format)
print("Image Mode:", image.mode)