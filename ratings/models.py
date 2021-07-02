from django.db import models

# Create your models here.
class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    elective_id =  models.ForeignKey('electives.Electives',db_column='elective_id',on_delete=models.CASCADE)
    faculty_id = models.ForeignKey('faculty.faculty',db_column='faculty_id',on_delete=models.CASCADE)
    student_id = models.ForeignKey('students.Students',db_column='student_id',on_delete=models.CASCADE)
    stars = models.IntegerField()
    comments = models.TextField(default="")

    class Meta:
        db_table = 'ratings'
