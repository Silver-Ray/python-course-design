import cv2

img=cv2.imread('img.1032.jpg')

img2=cv2.blur(img,ksize=(20,20))

img4=cv2.GaussianBlur(img,ksize=3)


img3=cv2.Laplacian(img2,ddepth=6)

cv2.imshow('image show',img4)

cv2.waitKey(0)
cv2.destroyAllWindows()



print()