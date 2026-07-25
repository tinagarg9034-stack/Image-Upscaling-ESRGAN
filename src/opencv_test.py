import cv2

# Read image
image = cv2.imread("input_images/sample.jpg")

# Print image information
print("Height :", image.shape[0])
print("Width  :", image.shape[1])
print("Channels:", image.shape[2])