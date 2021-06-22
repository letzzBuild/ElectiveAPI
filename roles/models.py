from django.db import models

# Create your models here.
class Roles(models.Model):
    role_id = models.CharField(max_length=5,primary_key=True)
    role_name = models.CharField(max_length=30,unique=True)


    class Meta:
        db_table = 'roles'
        verbose_name_plural = "roles"

    def  __str__(self,):
        return self.role_name   