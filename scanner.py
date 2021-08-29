import cv2
import numpy as np
import writer
import config

def scan():
    camera = cv2.VideoCapture(config.get_camera_index(), cv2.CAP_DSHOW)
    camera.set(cv2.CAP_PROP_FPS, 30.0)
    qrCodeDetector = cv2.QRCodeDetector()

    codes = {}

    while 1:
        success, image = camera.read()
        decodedText, points, _ = qrCodeDetector.detectAndDecode(image)

        if(decodedText):
            if points is not None:
                    point_len = len(points)

            hashedCode = hash(decodedText)
            if(not hashedCode in codes):
                codes[hashedCode] = decodedText
                print('Adding ' + decodedText + ' to list')

                pts = np.array(points, np.int32)
                pts = pts.reshape(-1,1,2)
                cv2.polylines(image, [pts], True, (255,0,255), 5)
            else:
                    pts = np.array(points, np.int32)
                    pts = pts.reshape(-1,1,2)
                    cv2.polylines(image, [pts], True, (0,255,0), 5)

        cv2.imshow("QR Scanner", image)
        k = cv2.waitKey(1)
        if k == 27 or k == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

    return list(codes.values())
