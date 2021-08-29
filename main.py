import cv2
import numpy as np

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FPS, 30.0)

qrCodeDetector = cv2.QRCodeDetector()

while 1:
    success, image = camera.read()
    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)

    if(decodedText):

        if points is not None:
            point_len = len(points)

            pts = np.array(points, np.int32)
            pts = pts.reshape(-1,1,2)
            cv2.polylines(image, [pts], True, (255,0,255), 5)

            print(decodedText)

    cv2.imshow("QR Scanner", image)

    k = cv2.waitKey(1)
    if k == 27 or k == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()