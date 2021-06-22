from django.db import models

# Create your models here.
class Semesters(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=20,unique=True)
    
    class Meta:
        db_table = 'semesters'
        verbose_name_plural = "semesters"
    def __str__(self):
        return self.semester_name    