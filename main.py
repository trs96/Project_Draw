import random
import cv2
import numpy as np

image = cv2.imread("test2.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply binary thresholding
ret, thresh = cv2.threshold(image_gray, 254, 255, cv2.THRESH_BINARY)
thresh = (255-thresh)
# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(
    image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE
)


image_created = np.full((image.shape), 255, dtype=np.uint8)

print(contours[3].size)
contours.sort(key=len)
contours.reverse()


for list in contours:
    list.resize(list.shape[0], list.shape[2])

    for tuple in list:
        cv2.line(image_created, tuple, tuple+1, (0, 0, 0), 1)
        #cv2.imshow("Drawing Lines", image_created)
        #cv2.waitKey(1)

# see the results
cv2.imshow("None approximation", image_created)
cv2.waitKey(0)
cv2.imwrite("contours_none_image1.jpg", image_created)
cv2.destroyAllWindows()