from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.


class NonDeletedTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Event_Details_Model(models.Model):
    event_name = models.CharField(max_length=500)
    organizer = models.CharField(max_length=100)
    notification_start_date = models.DateField()
    notification_end_date = models.DateTimeField()
    start_date = models.DateField()
    time = models.TimeField()
    end_date = models.DateTimeField()
    cost = models.CharField(max_length=50, blank=True, null=True)
    main_image = models.ImageField(upload_to='images/')
    event_description = models.CharField(max_length=1000)
    description_image = models.ImageField(upload_to='images/')
    event_venue = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    event_gallery_image = models.ImageField(upload_to='images/', blank=True, null=True)
    deleted = models.BooleanField(default=False)

    objects = models.Manager()
    non_deleted_objects = NonDeletedTaskManager()

    def soft_delete(self):
        self.deleted = True
        self.save()

    def restore(self):
        self.deleted = False
        self.save()
    
    def is_active(self):
        return self.notification_end_date >= timezone.now()



class MinistriesModel(models.Model):
    mass_times = models.ImageField(upload_to='images/')
    ask_for_prayer = models.ImageField(upload_to='images/')
    obitury = models.ImageField(upload_to='images/')


class Daily_Mass(models.Model):
    mass_days = models.CharField(max_length=100)
    mass_date = models.DateField()
    mass_time = models.TimeField()
    end_time = models.TimeField()
    mass_description = models.CharField(max_length=1000)
    deleted = models.BooleanField(default=False)

    objects = models.Manager()
    non_deleted_objects = NonDeletedTaskManager()

    def soft_delete(self):
        self.deleted = True
        self.save()

    def restore(self):
        self.deleted = False
        self.save()


    def __str__(self):
        return self.mass_days
    # def is_active(self):
    #     return self.mass_date >= timezone.now()


class Special_Masses(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.event_name


class Obituary_Model(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class UploadedImage(models.Model):
    main_heading = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')

class GalleryModel(models.Model):
    gallery_name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.gallery_name

class Blog_News_Model(models.Model):
    blog_image = models.ImageField(upload_to='images/')
    date = models.DateField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.description

class Contact_Model(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    Phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    pincode = models.CharField(max_length=6)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.name

class Gallery(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    gallery_image = models.ImageField(upload_to='images/',null=True,blank=True)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.name

class News_Category(models.Model):
    image = models.ImageField(upload_to='images/')
    news_heading = models.CharField(max_length=600)
    date = models.DateField()
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.news_heading

class News_Updates(models.Model):
    news_category = models.ForeignKey(News_Category,on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='images/',null=True,blank=True)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=1000)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.description


class UserRegisterModel(models.Model):
    catchchoice = [
        ('St.VincentDePaulSociety', 'St.VincentDePaulSociety'),
        ('StarsPithruvedi', 'StarsPithruvedi'),
        ('MathruJyothi', 'MathruJyothi'),
        ('STYF', 'STYF'),
        ('AltarServants', 'AltarServants'),
        ('BibleReadersForum', 'BibleReadersForum'),
        ('Choir','Choir'),
        ('CML','CML'),
        ('HolyChildhood','HolyChildhood'),
    ]
    username = models.CharField(max_length=200)
    privilege = models.CharField(max_length=80,choices=catchchoice,null=False,blank=False)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)
    confirmpassword = models.CharField(max_length=20)
    deleted = models.BooleanField(default=False)

    objects = models.Manager()
    non_deleted_objects = NonDeletedTaskManager()

    def soft_delete(self):
        self.deleted = True
        self.save()

    def restore(self):
        self.deleted = False
        self.save()

    def __str__(self):
        return self.username


class UserLoginModel(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class St_Vincent_Association(models.Model):
    activities = models.CharField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    
    def __str__(self):
        return self.description

class Stars_Pithruvedi_Association(models.Model):
    activities = models.CharField(max_length=500,null=True,blank=True)
    objectives = models.CharField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.description

class Mathrujyothi_Association(models.Model):
    activities = models.CharField(max_length=500,null=True,blank=True)
    objectives = models.CharField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.description

class Styf_Association(models.Model):
    main_image = models.ImageField(upload_to='images/',null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    member_image = models.ImageField(upload_to='images/',null=True,blank=True)
    member_name = models.CharField(max_length=20,null=True,blank=True)
    member_designation = models.CharField(max_length=50,null=True,blank=True)
    deleted = models.BooleanField(default=False)

    objects = models.Manager()
    non_deleted_objects = NonDeletedTaskManager()

    def soft_delete(self):
        self.deleted = True
        self.save()

    def restore(self):
        self.deleted = False
        self.save()


class Auditorium_Booking(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    deleted = models.BooleanField(default=False)

    objects = models.Manager()
    non_deleted_objects = NonDeletedTaskManager()

    def soft_delete(self):
        self.deleted = True
        self.save()

    def restore(self):
        self.deleted = False
        self.save()

    def __str__(self):
        return self.name

    



