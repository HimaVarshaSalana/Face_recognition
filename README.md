# Face_recognition
face recognition for secure paymnets using django

I have used django frame work for creating this web application
I have used html,js,css for frontend and sql database for backend
I have used python language to develop the face recognition application

To run the server:

1. Go you your command prompt
2. Change directory to paybyface
3. manage.py is the main file
4. In your command prompt enter: python manage.py runserver
5. Please make sure to include "runserver" in the end otherwise the localhost link will not be generated.

  ![Screenshot (2)](https://user-images.githubusercontent.com/94437043/171025219-fdd57707-2145-43ee-92f6-d03b128bdba0.png)


6. Copy and paste the above HTTP link into your browser to view the page.
7. You can exit the server in your command prompt by entering (break): CTRL+C
8. Please note that the localhost cannot be activated unless you properly host it in the command prompt.
9. You can see the website on the browser

![Screenshot (3)](https://user-images.githubusercontent.com/94437043/171025665-f2947fde-2524-45c6-b9f6-10d98d129b24.png)


Requirements:


please not that the project doesnot work in any external system without certain libraraies installed . To run the project make sure the following are installed

1. python
2. django
3. cmake
4. wheel
5. dlib
6. face-recognition
7. opencv-python
8. django-credit-cards (for database models )

How the application works:

1. As with any other online website you can register and login into the server.
2. First time users will be asked their Card Details to perform transactions   

    ![Screenshot (48)](https://user-images.githubusercontent.com/94437043/171028634-a4ed63b8-0eb2-4059-bec6-b09e80a033e5.png)

3. You can see your profile and update it and also have option for reseting password
4. Go to the required payments option on the homepage, enter the details and click on the 'Verify Face' Button
5. The webcam will open to capture your face for verification
    

6. Upon Successful Verification of your face the payment confirmation window opens and the payments are done!
  
     ![Screenshot (54)](https://user-images.githubusercontent.com/94437043/171029221-01602a46-fd92-462f-91e5-88e1d9e72333.png)

     ![Screenshot (55)](https://user-images.githubusercontent.com/94437043/171029258-11947581-6ce9-43ea-8d9d-608e8aa7c365.png)



7. You may choose different payment optons like qrcode , mobile transfer , banktransfer
      
     ![WhatsApp Image 2022-05-30 at 9 47 55 PM](https://user-images.githubusercontent.com/94437043/171030720-c31604d2-651a-4593-8591-29541383faec.jpeg)

     
8. You also have features like mobilerecharege ,bill payments
