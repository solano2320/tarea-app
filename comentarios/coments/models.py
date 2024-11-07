from django.db import models

# Create your models here.
#Aca creo la clase de comentarios
class Coments(models.Model):

    name = models.CharField(max_length=50,null=False)
    email = models.EmailField(null=False)
    coment = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
