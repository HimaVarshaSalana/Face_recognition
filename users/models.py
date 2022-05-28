from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from PIL import Image
from django.db.models import CharField
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from datetime import datetime



class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

  def __str__(self):   
    return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
      super().save(*args, **kwargs)

      img = Image.open(self.image.path)

      if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)

class CardDetails(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name_on_card = models.CharField(max_length=50)
  cc_number = CardNumberField('card number')
  cc_expiry = CardExpiryField('expiration date', default = datetime.strptime('0101', '%m%y').date())
  cc_code = SecurityCodeField('security code')
  face_id = models.ImageField(upload_to='face_id') 
  def __str__(self):
    return f'{self.user.username} Details'
    def save(self, *args, **kwargs):
      super().save(*args, **kwargs)


