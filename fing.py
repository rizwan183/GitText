import cv2
import numpy as np
positions=[]
positions2=[]
count=0
hand_cascade = cv2.CascadeClassifier('fing.xml')
img = cv2.imread("new85.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hands = hand_cascade.detectMultiScale(gray_img, scaleFactor=1.10,minNeighbors=15)
print(hands)
#draw the rectangle
for x, y, w, h in hands:
    print(x,y,w,h)
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 100, 5), 4)



f=[]
i=0
for (x, y, w, h) in hands:
    r=max(w,h)/2
    centerx=x+w/2
    centery=y+h/2
    nx=int(centerx-r)
    ny=int(centery-r)
    nr=int(r*2)
    faceimg = img[ny:ny + nr, nx:nx + nr]
    i=i+1
    f=faceimg
    #print(faceimg)
    iar = np.asarray(faceimg)
    print(iar)
    h1, w1 = faceimg.shape[:2]
    cv2.waitKey(0)
    mask2 = cv2.bitwise_not(faceimg)
    cv2.imshow("fingure", mask2)
    cv2.imwrite("cr%d.jpg" % i, faceimg)





a3 = np.array( [[[114,114],[116,114],[114,116],[139,139]]], dtype=np.int32 )
color = np.uint8(np.random.rand(3) * 255).tolist()
n=cv2.fillConvexPoly(img,a3,0)
cv2.imshow("fingure",n)
cv2.waitKey(0)
cv2.destroyAllWindows()
