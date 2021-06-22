from django.db import models

# Create your models here.
class Branches(models.Model):

    branch_id = models.AutoField(primary_key=True)
    branch_full_name = models.CharField(unique=True,max_length=50)
    branch_short_name = models.CharField(max_length=10,unique=True,default=None)
    
    class Meta:
        db_table = "branches"
        verbose_name_plural = "branches"

    def __str__(self):
        return self.branch_full_name   