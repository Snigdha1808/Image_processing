from PIL import Image
import matplotlib.pyplot as plt

image_path = "image_path"
image = Image.open(image_path)

#Original Image
plt.figure(figsize=(6, 6))
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')
plt.show()

#Resized image
resized_image = image.resize((400, 300))
plt.figure(figsize=(6, 6))
plt.imshow(resized_image)
plt.title('Resized Image (400x300)')
plt.axis('off')
plt.show()

#Grayscale Image
gray_image = image.convert('L')
plt.figure(figsize=(6, 6))
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()
