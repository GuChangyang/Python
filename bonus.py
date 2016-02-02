import numpy as np
import cv2
import random


img = cv2.imread('Houghcircles.jpg',0)
blur = cv2.GaussianBlur(img,(3,3),1)
v = np.median(blur) 
# apply automatic Canny edge detection using the computed median
lower = int(max(0, (1.0 - 0.43) * v))
upper = int(min(255, (1.0 + 0.43) * v))
edged = cv2.Canny(blur, lower, upper)
falseTime = 0

class Pixel:
    def __init__(self,x,y):
       self.x = x
       self.y = y
    
def fourEdge(edged,x0,x1,y0,y1):
    global falseTime
    # if falseTime > 500, we assume there is no circle
    if falseTime > 500:
        falseTime = 0
        return False
    
    pixels = []
    counter = 0
    isCircle = True
    for x in range(x0,x1):   
        for y in range(y0,y1):       
            if edged[y,x] > 0: 
                pixel = Pixel(x,y)
                pixels.append(pixel)
    if len(pixels)<50:
        return False
    selected = random.sample(pixels,3)
    pixels.remove(selected[0])
    pixels.remove(selected[1])
    pixels.remove(selected[2])
    
    
    forth =  random.sample(pixels,1)   
    pixels.remove(forth[0])    
    a1 = selected[0].x
    b1 = selected[0].y
    a2 = selected[1].x
    b2 = selected[1].y
    a3 = selected[2].x
    b3 = selected[2].y
    a4 = forth[0].x
    b4 = forth[0].y
    
    # if 3 pixels are on the same line they can't form a circle    
    if (a2-a1)*(b3-b1)-(a3-a1)*(b2-b1) == 0:
         isCollinear = True
    else :
         isCollinear = False
    
    
    # get the center's position of the circle created by the three edge points
    a=2*(a2-a1)
    b=2*(b2-b1)
    c=a2*a2+b2*b2-a1*a1-b1*b1
    d=2*(a3-a2)
    e=2*(b3-b2)
    f=a3*a3+b3*b3-a2*a2-b2*b2
    if b*d - e*a != 0 :
        xc=(b*f-e*c)/(b*d-e*a)
        yc=(d*c-a*f)/(b*d-e*a)
        rc=np.sqrt((xc-a1)*(xc-a1)+(yc-b1)*(yc-b1))
        p4boundary = np.abs(np.sqrt((a4 - xc)**2 + (b4 - yc)**2) - rc)
    else:
        falseTime += 1
        fourEdge(edged,x0,x1,y0,y1)
        return
        
    # any two pixels's distance should be greater than a threshold  and 
    # isCollinear should be false
    for i in range(len(selected)):
        for j in range(i + 1,len(selected)):
            dis = np.sqrt((selected[i].x - selected[j].x)**2 +
            (selected[i].y - selected[j].y)**2)
            if(dis < 5) or isCollinear == True or p4boundary < 5:
                falseTime += 1
                fourEdge(edged,x0,x1,y0,y1)
                return
                
   # get the number of edge pixel that on the circle 
    for e in pixels:
        p2cen = np.abs( np.sqrt((e.x - xc)**2 + (e.y - yc)**2) - rc)
        # if the distance between pixel and center is less than 4,counter + 1
        if (p2cen < 5):
            counter += 1
    ration = float(counter)/len(pixels)
    if(ration > 0.5):        
        isCircle = True        
    else:
        isCircle = False
        falseTime += 1
        fourEdge(edged,x0,x1,y0,y1)
        return      
    if isCircle:
        cv2.circle(img, (int(xc),int(yc)),int(rc),255,1)        
        falseTime = 0
        return True
if __name__ == "__main__":      
    fourEdge(edged,450,600,1,400) #10th 
    fourEdge(edged,0,300,0,100)#  First circle
    fourEdge(edged,100,240,100,240)# Second
    fourEdge(edged,0,140,240,340) # Third
    fourEdge(edged,240,320,100,180) #Forth
    fourEdge(edged,160,240,280,360) # 5th
    fourEdge(edged,232,340,240,360) #6th
    fourEdge(edged,340,460,40,150) #7th
    fourEdge(edged,340,460,170,280) #8th
    fourEdge(edged,360,460,300,390) #9th
   
    cv2.imshow('result1',img)
    cv2.imwrite('bonus.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    