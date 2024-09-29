import cv2
import numpy as np

image = cv2.imread("image.png")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define color range for red cones in HSV
lower_red = np.array([0, 150, 170])    # Lower bound for red
upper_red = np.array([5, 230, 255])  # Upper bound for red

# Create a mask for the red areas
mask = cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow('image', mask)
cv2.waitKey(0)

# Perform morphological operations to reduce noise
kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Find contours of the red cones
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Separate cone positions based on their x coordinates for left and right boundary fitting
left_cones = []
right_cones = []
image_center_x = image.shape[1] // 2

for contour in contours:
    # Get the bounding box for each contour
    x, y, w, h = cv2.boundingRect(contour)
    center_x = x + w // 2
    center_y = y + h // 2

    # Divide into left and right based on the center of the image
    if center_x < image_center_x:
        left_cones.append((center_x, center_y))
    else:
        right_cones.append((center_x, center_y))

# Function to fit a line to the cone points
def fit_line_and_draw(cones, color):
    if len(cones) > 1:
        # Fit a polynomial line (degree 1, i.e., a straight line)
        [vx, vy, x, y] = cv2.fitLine(np.array(cones), cv2.DIST_L2, 0, 0.01, 0.01)
        slope = vy.item() / vx.item()   # Extract scalar values using .item()
        intercept = y.item() - slope * x.item()  # Use .item() to extract scalar
        
        # Define two points for drawing the line
        pt1 = (0, int(intercept))
        pt2 = (image.shape[1], int(slope * image.shape[1] + intercept))
        
        # Draw the line on the original image
        cv2.line(image, pt1, pt2, color, 3)

# Fit lines to the left and right cones
fit_line_and_draw(left_cones, (0, 0, 255))  # Red line for left cones
fit_line_and_draw(right_cones, (0, 0, 255)) # Red line for right cones

cv2.imwrite('answer.png', image)