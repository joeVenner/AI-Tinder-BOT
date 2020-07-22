from skimage import io
import cv2
import cvlib



def checker(link):
    result = 0
    img = io.imread(link,plugin='matplotlib')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    font = cv2.FONT_HERSHEY_PLAIN

    faces,conf = cvlib.detect_face(img)

    if len(faces) > 0:
        for x, y, w, h in faces:
            roi = img[y:y + h, x:x + w]
            label, confidence = cvlib.detect_gender(roi)
            if confidence[0]>confidence[1]:
                gender = label[0]
            else:
                gender=label[1]

            cv2.rectangle(img, (x, y), (w, h), (0, 255, 0), 2)

            cv2.rectangle(img, (50, 50), (220, 80), (0, 255, 0), -1)
            cv2.putText(img, "Face Detected [+]", (55, 70), font, 1, (0, 0, 0), 1, cv2.LINE_AA)

            if gender == "female":

                    cv2.rectangle(img, (50, 90), (220, 120), (0, 255, 0), -1)
                    cv2.putText(img, gender + " [+]", (55, 110), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
                    result = 1
                    cv2.rectangle(img, (50, 130), (220, 160), (0, 255, 0), -1)
                    cv2.putText(img, " Like [+]  ", (55, 150), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
            else:
                    cv2.rectangle(img, (50, 90), (220, 120), (0, 0, 255), -1)
                    cv2.putText(img, gender + " [+]", (55, 110), font, 1, (0, 0, 0), 1, cv2.LINE_AA)


    elif len(faces) == 0:
                cv2.rectangle(img, (50, 50), (220, 80), (0,0 , 255), -1)
                cv2.putText(img, "Face Not Detected", (55, 70), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.rectangle(img, (50, 90), (220, 120), (0, 0, 255), -1)
                cv2.putText(img,"Dislike [-]", (55, 110), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow('Tinder Detector', img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    return result

#checker("https://images-ssl.gotinder.com/5f11acfcb1a96f0100e144a6/640x800_75_d28efa30-4c3e-4a30-b1be-b8e0c1b7c35a.webp")

