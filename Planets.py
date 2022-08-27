import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img , "Mercury" , (120,190), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color= (255 , 255 , 255))

cv2.putText(img , "Venus" , (190,170), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color= (255 , 255 , 255))

cv2.putText(img , "Earth" , (280,150), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color= (255 , 255 , 255))

cv2.putText(img , "Mars" , (390,160), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color= (255 , 255 , 255))

cv2.putText(img , "Jupiter" , (560,50), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color= (255 , 255 , 255))

cv2.putText(img , "Saturn" , (750,90), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color= (255 , 255 , 255))

cv2.putText(img , "Uranus" , (960,120), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color= (255 , 255 , 255))

cv2.putText(img , "Neptune" , (1130,130), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color= (255 , 255 , 255))

cv2.imshow("Rocket", img)
cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.waitKey(0)
