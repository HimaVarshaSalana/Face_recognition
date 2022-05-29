# Face_recognition
face recognition for secure paymnets using django

To run the server:

1. Go you your command prompt
2. Change directory to django_project
3. manage.py is the main file
4. In your command prompt enter: python manage.py runserver
5. Please make sure to include "runserver" in the end otherwise the localhost link will not be generated.
6. Copy and paste the above HTTP link into your browser to view the page.
7. You can exit the server in your command prompt by entering (break): CTRL+C
8. Please note that the localhost cannot be activated unless you properly host it in the command prompt.

How the application works:

1. As with any other online website you can register and login into the server.
2. First time users will be asked their Card Details to perform transactions
3. You can see your profile and update it and also have option for reseting password
5. Go to the required payments option on the homepage, enter the details and click on the 'Verify Face' Button
6. The webcam will open to capture your face for verification
7. Upon Successful Verification of your face the payment confirmation window opens and the payments are done!
8. You may choose different payment optons like qrcode , mobile transfer , banktransfer
9. You also have features like mobilerecharege ,bill payments

Requirements:

(To use the facepay.py outside) Please note that facepay.py is not used anywhere in the project. It is a file I created to use face recognition in python. The following Python modules/packages have to be installed in your System:

1. cmake
2. dlib
3. wheel
4. face_recognition
5. opencv-python
