import cv2

img = cv2.imread('img.jpg')
gray = cv2.imread('img.jpg', 0)

ret,thresh = cv2.threshold(gray,127,255,1)

contours,h = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    approx1 = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    approx2 = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
    approx3 = cv2.approxPolyDP(cnt, 0.03 * cv2.arcLength(cnt, True), True)
    if len(approx3) == 3:
        cv2.drawContours(img,[cnt],0,(122,212,78),-1)
    elif len(approx1) == 4:
        cv2.drawContours(img,[cnt],0,(94,234,255),-1)
    elif len(approx2) == 8:
        k = cv2.isContourConvex(approx2)
        if k:
            cv2.drawContours(img, [cnt], 0, (220, 152, 91), -1)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()