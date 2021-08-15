from django.db import models

# Create your models here.
class CollegeName(models.Model):
    college_long_name = models.CharField(max_length=100)
    college_short_name = models.CharField(max_length=100)
    college_address = models.CharField(max_length=100)
    college_code = models.CharField(max_length=10)


    def __str__(self):
        return self.college_short_name
    class Meta:
        db_table = 'college_name'    