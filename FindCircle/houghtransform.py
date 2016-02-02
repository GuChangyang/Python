import numpy as np
import cv2



    
def houghTransform(edged,x0,x1,y0,y1):
    maxVote = 0
    # loop the region and find the edge pixel
    for x in range(x0,x1):   
        for y in range(y0,y1):       
            if edged[y,x] > 0:                                             
                    for a in range(x0,x1):
                        for b in range(y0,y1):           
                              for rIdx in range (len(radii)): 
                                  # if the a,b,r satisfies the circle's equation,the accumulator
                                  #  is incremented by 1                  
                                 if((x - a)**2 + (y - b)**2 == (radii[rIdx])**2):                       
                                     accu[a][b][rIdx] += 1  
    # find the local largest numberof vote  and draw the circle (a,b,r)
    # a,b is the position of the center, and r is the radius of the circle                              
    for x2 in range(x0,x1) :
        for y2 in range(y0,y1):  
            for rIdx1 in range(len(radii)):     
                if(accu[x2,y2,rIdx1] > maxVote):
                    cX = x2
                    cY = y2
                    cR = radii[rIdx1]
                    maxVote = accu[x2,y2,rIdx1]   
    if maxVote > 3:           
     cv2.circle(img, (cX,cY),cR,255,1)
   
     
if __name__ == "__main__":
    img = cv2.imread('Houghcircles.jpg',0)
    blur = cv2.GaussianBlur(img,(3,3),1)
    v = np.median(blur) 
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - 0.43) * v))
    upper = int(min(255, (1.0 + 0.43) * v))
    edged = cv2.Canny(blur, lower, upper)
    cX=0
    cY=0
    cR = 0
    h,w = edged.shape
    radii = range(20,60,2)
    accu = np.zeros((w,h,len(radii)))
    
   
    houghTransform(edged,450,600,1,400) #10th 
    houghTransform(edged,0,300,0,100)#  First circle
    houghTransform(edged,100,240,100,240)# Second
    houghTransform(edged,0,140,240,340) # Third
    houghTransform(edged,240,320,100,180) #Forth
    houghTransform(edged,160,240,280,360) # 5th
    houghTransform(edged,232,340,240,360) #6th
    houghTransform(edged,340,460,40,150) #7th
    houghTransform(edged,340,460,170,280) #8th
    houghTransform(edged,360,460,300,390) #9th
   
    cv2.imshow('result1',img)
    cv2.imwrite('myhough.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    