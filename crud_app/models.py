from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CrudModel(models.Model):
    id = models.AutoField(primary_key=True, unique= True)
    name = models.CharField(max_length= 50)
    phone = models.CharField(max_length= 14)
    email = models.EmailField(max_length= 50)
    course = models.CharField(max_length= 50)
    image = models.ImageField(upload_to= 'photos/images', null=True, default='photos/images/photo.jpg')
    description = models.TextField(max_length= 500, blank= True)
    created_date = models.DateTimeField(auto_now_add= True)
    modify_date = models.DateTimeField(auto_now= True)
    
    class Meta:
        verbose_name = 'Crud'
        verbose_name_plural = "CRUD'S"
    
    def __str__(self) -> str:
        return self.name
    

    


    