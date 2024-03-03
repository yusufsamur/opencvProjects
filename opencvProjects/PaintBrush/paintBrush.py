import cv2
import numpy as np
from matplotlib import pyplot as plt

selected_color = (0, 0, 0)
drawing = False
radius = 5



def line_drawing(event, x, y, flags, param):
    global pt1_x, pt1_y, drawing, selected_color,radius
    
    if event == cv2.EVENT_RBUTTONDOWN:
        selected_color=(255,255,255)
        radius = 20
        
    elif event == cv2.EVENT_LBUTTONDOWN:
        drawing = True       
        b, g, r = img[y, x]
        b=int(b)
        g=int(g)
        r=int(r)
        if (b,g,r) != (255,255,255):
            selected_color = (b, g, r)
            radius = 5

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True and not is_inside_palette(x, y):
            cv2.circle(img, (x, y),radius, color=selected_color, thickness=-1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if not is_inside_palette(x, y):
            cv2.circle(img, (x, y),radius, color=selected_color, thickness=-1)

def is_inside_palette(x, y):
    # Tıklanan piksel, renk paletinde mi ?
    if -20 <= y <= 72:
            return True
    return False

font = cv2.FONT_HERSHEY_COMPLEX
img = np.ones((800, 1280, 3), np.uint8)
img.fill(255)
img = cv2.rectangle(img, (0, 0), (120, 50), (0, 0, 0), -1)
img = cv2.rectangle(img, (120, 0), (240, 50), (255, 0, 0), -1)
img = cv2.rectangle(img, (240, 0), (360, 50), (0, 255, 0), -1)
img = cv2.rectangle(img, (360, 0), (480, 50), (0, 0, 255), -1)
img = cv2.line(img,(0,50),(1280,50),(0,0,0),2)
img = cv2.putText(img,"RIGHT CLICK FOR ERASER",(800,40),font,1.0,(0,0,0),2,cv2.LINE_AA)
cv2.namedWindow("paint")
cv2.setMouseCallback("paint", line_drawing)


while 1:
    cv2.imshow("paint", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()
