import cv2

img = cv2.imread('C:/Users/Wilbur/Pictures/Camera Roll/testing3.jpg', cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ',img.shape)

width = 512
height = 512

dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.imwrite("C:/Users/Wilbur/Pictures/Camera Roll/testing3.jpg", resized)
print('Resized Dimensions : ',resized.shape)