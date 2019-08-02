from django.db import models

# Create your models here.
class tble(models.Model):
    tittle=models.CharField(max_length=50)
    img1=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    discription= models.CharField(max_length=50)

    def __str__(self):
        return self.tittle

class tble1(models.Model):
    tittle1=models.CharField(max_length=50)
    img2=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    discription1= models.CharField(max_length=50)
    link= models.CharField(max_length=50, default='')


    def __str__(self):
        return self.tittle1




