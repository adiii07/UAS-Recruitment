import numpy as np
import cv2

img = cv2.imread("images/image.png")

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# green ranges
g_lower_range = (33, 25, 25)
g_upper_range = (100, 255, 255)

mask1 = cv2.inRange(hsv_img, g_lower_range, g_upper_range)
img[mask1>0] = (200, 255, 0)


# brown ranges
b_lower_range = (6, 100, 20)
b_upper_range = (32, 255, 255)

mask2 = cv2.inRange(hsv_img, b_lower_range, b_upper_range)
img[mask2>0] = (100, 255, 255)


cv2.imshow('Image', img)    


# counting number of houses in each section

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Image grey', grey)


# counting number of houses in green grass
green_houses_count = 0
red_houses_in_green = 0
blue_houses_in_green = 0

_, threshold = cv2.threshold(mask1, 220, 255, cv2.THRESH_BINARY)
contours, heirarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i, contour in enumerate(contours):
    if i == 0:
        continue
    epsilon = 0.01*cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    cv2.drawContours(img, contour, 0, (0, 0, 0), 4)
    
    
    
    if len(approx) == 3:
        
        # checking color of triangle
        x, y, w, h = cv2.boundingRect(approx)
        x_mid = int(x + w/2)
        y_mid = int(y + h/2)
        print("coords", x_mid, y_mid)
        
        center_pixel = hsv_img[x_mid, y_mid]
        hue_value = center_pixel[0]
        print(center_pixel, hue_value)
        
        if hue_value < 140 and hue_value > 100:
            blue_houses_in_green += 1
        if hue_value < 5:
            red_houses_in_green += 1
        
        green_houses_count += 1
        
print(blue_houses_in_green, red_houses_in_green, "green")
# print(green_houses_count)


#counting number of houses in burnt grass
brown_houses_count = 0
red_houses_in_burnt = 0
blue_houses_in_burnt = 0

_, threshold = cv2.threshold(mask2, 220, 255, cv2.THRESH_BINARY)
contours, heirarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i, contour in enumerate(contours):
    if i == 0:
        continue
    epsilon = 0.01*cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    cv2.drawContours(img, contour, 0, (0, 0, 0), 4)
    
        
    
    if len(approx) == 3:
        
        # checking color of triangle
        x, y, w, h = cv2.boundingRect(approx)
        x_mid = int(x + w/2)
        y_mid = int(y + h/2)
        print("coords", x_mid, y_mid)
        
        center_pixel = hsv_img[x_mid, y_mid]
        hue_value = center_pixel[0]
        print(center_pixel, hue_value)
        
        if hue_value < 140 and hue_value > 100:
            blue_houses_in_burnt += 1
        if hue_value < 5:
            red_houses_in_burnt += 1
        
        brown_houses_count += 1
        
print(blue_houses_in_burnt, red_houses_in_burnt, "burnt")
# print(brown_houses_count)

num_houses = [brown_houses_count, green_houses_count]
print(num_houses, "There are", brown_houses_count, "houses on the burnt grass and", green_houses_count, "houses on the green grass")

    

key = cv2.waitKey(0)

# get_color()
# get_shape()


