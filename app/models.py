from django.db import models

# Create your models here.
class tble(models.Model):
    tittle=models.CharField(max_length=50)
    img1=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    discription= models.CharField(max_length=150)
    link= models.CharField(max_length=50, default='')


    def __str__(self):
        return self.tittle

class tble1(models.Model):
    tittle1=models.CharField(max_length=50)
    img2=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    discription1= models.CharField(max_length=50)
    link= models.CharField(max_length=50, default='')


    def __str__(self):
        return self.tittle1

class projects(models.Model):
    tittle=models.CharField(max_length=50)
    img=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    discription= models.CharField(max_length=50)
    link= models.CharField(max_length=50, default='')

    def __str__(self):
        return self.tittle

class blogs(models.Model):
    tittle=models.CharField(max_length=50)
    img=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    discription= models.CharField(max_length=50)
    link= models.CharField(max_length=50, default='')

    def __str__(self):
        return self.tittle
        
class service(models.Model):
    tittle=models.CharField(max_length=50)
    img=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    discription= models.CharField(max_length=50)
    link= models.CharField(max_length=50, default='')

    def __str__(self):
        return self.tittle 

class promotions(models.Model):
    tittle=models.CharField(max_length=50)
    img=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    discription= models.CharField(max_length=50)
    link= models.CharField(max_length=50, default='')

    def __str__(self):
        return self.tittle

class contact_tble(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)

class about(models.Model):
    tittle=models.CharField(max_length=50)
    img=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    discription= models.CharField(max_length=50)
    link= models.CharField(max_length=50, default='')

    def __str__(self):
        return self.tittle

class team(models.Model):
    tittle=models.CharField(max_length=50)
    img=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    discription= models.CharField(max_length=50)
    link= models.CharField(max_length=50, default='')

    def __str__(self):
        return self.tittle

class careers(models.Model):
    tittle=models.CharField(max_length=50)
    img=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    discription= models.CharField(max_length=50)
    link= models.CharField(max_length=50, default='')

    def __str__(self):
        return self.tittle

class backgroundimages(models.Model):
    Brandimg=models.ImageField(upload_to='img', verbose_name="file",null=True,blank=True)
    Blogimg=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    Projectimg=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    Knowusimg=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    Serviceimg=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    Whatweimg=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    Careersimg=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    Aboutusimg=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)
    Contactusimg=models.ImageField(upload_to='img',verbose_name="file",null=True,blank=True)

    def __img__(self):
        return self.Brandimg




    