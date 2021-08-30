import cv2
import numpy as np
import writer
import config


def scan():

    def drawLines(image, points, r, g, b):
        pts = np.array(points, np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(image, [pts], True, (r,g,b), 5)

    camera = cv2.VideoCapture(config.get_camera_index(), cv2.CAP_DSHOW)
    camera.set(cv2.CAP_PROP_FPS, 30.0)
    qrCodeDetector = cv2.QRCodeDetector()

    codes = set()

    while 1:
        success, image = camera.read()
        decodedText, points, _ = qrCodeDetector.detectAndDecode(image)

        if(decodedText):
            if points is not None:
                    point_len = len(points)

            if(not decodedText in codes):
                codes.add(decodedText)
                print('Adding ' + decodedText + ' to list')

                drawLines(image, points, 255, 0, 255)

            else:
                    drawLines(image, points, 0, 255, 0)

        cv2.imshow("QR Scanner", image)
        k = cv2.waitKey(1)
        if k == 27 or k == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

    return list(codes)
