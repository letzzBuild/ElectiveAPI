from django.db import models

# Create your models here.
class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    semester_id = models.ForeignKey('semesters.Semesters',db_column='semester_id',on_delete=models.CASCADE)
    usn = models.CharField(max_length=10,unique=True)
    cgpa = models.FloatField(default=6.0)
    branch_id = models.ForeignKey('branches.Branches',db_column='branch_id',on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.Users',db_column='user_id',on_delete=models.CASCADE)


    class Meta:
        db_table = 'students'
        verbose_name_plural = "students"

    def __str__(self,):
        return self.usn    