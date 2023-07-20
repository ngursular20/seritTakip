import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines):
    img_copy = np.copy(img)
    threshold_x = 500
    lane_change_detected = True

    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(img_copy, (x1, y1), (x2, y2), (0, 255, 0), thickness=10)
                if x1 > threshold_x or x2 > threshold_x:
                    lane_change_detected = False

    return img_copy, lane_change_detected

def process(image):
    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [
        (0, height),
        (width // 2, height // 2),
        (width, height)
    ]
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))
    lines = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi/180, threshold=50, lines=np.array([]), minLineLength=40, maxLineGap=100)
    image_with_lines, lane_change_detected = draw_lines(image, lines)
    return image_with_lines, lane_change_detected

cap = cv2.VideoCapture('yol.mp4')
lane_change_detected = True

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame, lane_change_detected = process(frame)
  
    if lane_change_detected:
        cv2.putText(frame, "Serit Degisikligi!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
