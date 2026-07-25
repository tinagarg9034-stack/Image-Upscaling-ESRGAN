import cv2

# Read the image
image = cv2.imread("input_images/sample.jpg")

# Resize the image
resized = cv2.resize(image, (600, 800))

# Save the resized image
cv2.imwrite("output_images/resized_sample.jpg", resized)

print("Original Size :", image.shape)
print("Resized Size  :", resized.shape)
print("Image saved successfully!")