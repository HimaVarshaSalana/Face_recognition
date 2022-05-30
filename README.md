# Face_recognition
face recognition for secure paymnets using django

To run the server:

1. Go you your command prompt
2. Change directory to paybyface
3. manage.py is the main file
4. In your command prompt enter: python manage.py runserver
5. Please make sure to include "runserver" in the end otherwise the localhost link will not be generated.

  ![Screenshot (2)](https://user-images.githubusercontent.com/94437043/171025219-fdd57707-2145-43ee-92f6-d03b128bdba0.png)


7. Copy and paste the above HTTP link into your browser to view the page.
8. You can exit the server in your command prompt by entering (break): CTRL+C
9. Please note that the localhost cannot be activated unless you properly host it in the command prompt.
10. You can see the website on the browser

![Screenshot (3)](https://user-images.githubusercontent.com/94437043/171025665-f2947fde-2524-45c6-b9f6-10d98d129b24.png)


Requirements:


please not that the project doesnot work in any external system without certain libraraies installed . To run the project make sure the following are installed

1. python
2. django
3. cmake
4. dlib
5. wheel
6. face_recognition
7. opencv-python
8. django-credit-cards (for database models )

How the application works:

1. As with any other online website you can register and login into the server.
2. First time users will be asked their Card Details to perform transactions
3. You can see your profile and update it and also have option for reseting password
5. Go to the required payments option on the homepage, enter the details and click on the 'Verify Face' Button
6. The webcam will open to capture your face for verification
7. Upon Successful Verification of your face the payment confirmation window opens and the payments are done!
8. You may choose different payment optons like qrcode , mobile transfer , banktransfer
9. You also have features like mobilerecharege ,bill payments
