from django.db import models

# Create your models here.
class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(max_length=50)
    branch_id = models.ForeignKey('branches.Branches',db_column='branch_id',on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.Users',db_column='user_id',on_delete=models.CASCADE)
    
    class Meta:
        db_table = "faculty"
        verbose_name_plural = "faculties"

    def __str__(self,):
        return self.faculty_name 

class Faculty_Rating(models.Model):
    id = models.AutoField(primary_key=True)
    elective_id = models.ForeignKey('electives.Electives',db_column='elective_id',on_delete=models.CASCADE)
    faculty_id = models.ForeignKey(Faculty,db_column='faculty_id',on_delete=models.CASCADE)
    ratings = models.IntegerField()
    comments = models.TextField()

    class Meta:
        db_table = "faculty_ratings"
        verbose_name_plural = "faculty_ratings"
   