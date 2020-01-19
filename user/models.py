from django.db import models
from databaseuser.models import DBUSER
from pyuploadcare.dj.forms import ImageField
# Create your models here.

class Comments(models.Model):
    comment = models.TextField(max_length=100)
    loggedin_user_comment = models.ForeignKey(loggedinUser, on_delete=models.CASCADE)
    imagecaption = models.ForeignKey(Image, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
    def save_comment(self):
        self.save()

class Image(models.Model):
    image = ImageField(manualcrop="700x700")
    likes =  models.IntegerChoices()

class DBUSER(models.Model):
    name= models.CharField(max_length=100)
    image = ImageField(manual_crop="700x700")
    db_comment = CharField(max_length=100)
    likes = IntegerField()
    post_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=250)

    def __str__(self):
        return self.name
    def save_db_user(self):
        return self.save()
    def get_remote_image(self):
        if self.image_url and not self.image:
            result = request.urlretrieve(self.image_url)
        self.image.save(
                os.path.basename(self.image_url),
                File(open(result[0], 'rb'))
                )
        self.save()

class loggedinUser(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE) 
    Bio = models.TextField(max_length=700)
    dbuser = models.Foreignkey(DBUSER , on_delete= models.CASCADE)
    mycomment = models.ForeignKey(Comments, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.image
    def save_loggedin_user(self):
        return self.save()
    @classmethod
    def search_dbuser_by_name(cls,search):
        return cls.objects.filter(dbuser__name__icontains=search)
    @classmethod
    def update_image():
    
    @classmethod
    def delete_image(cls, id):
        return cls.objects.filter(image_id=id)

    @classmethod
    def delete_comment(cls, id):
        return cls.object.filter(mycomment=id)