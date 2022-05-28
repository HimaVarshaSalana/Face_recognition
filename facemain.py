import face_recognition
import cv2

cam = cv2.VideoCapture(0)
s, img = cam.read()
if s:
    face_1_image = face_recognition.load_image_file('faces/jk1.jpg')
    face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]
    
    face_2_face_encoding = face_recognition.face_encodings(img)[0]
    
    check=face_recognition.compare_faces([face_1_face_encoding], face_2_face_encoding)
    print(check)
    if check[0]:
        print("true")
    else:
        print("false")