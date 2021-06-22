from django.db import models

# Create your models here.
class Electives(models.Model):
    elective_id = models.AutoField(primary_key=True)
    elective_name = models.CharField(max_length=70,unique=True)
    elective_short_name = models.CharField(max_length=10,unique=True)
    
    class Meta:
        db_table = 'electives'
        verbose_name_plural = "electives"

    def __str__(self,):
        return self.elective_name   

class ElectiveSemester(models.Model):
    id = models.AutoField(primary_key=True)
    elective_id = models.ForeignKey(Electives,db_column='elective_id',on_delete=models.CASCADE)
    semester_id = models.ForeignKey('semesters.Semesters',db_column='semester_id',on_delete=models.CASCADE)
    branch_id = models.ForeignKey('branches.Branches',db_column='branch_id',on_delete=models.CASCADE)

    class Meta:
        db_table = 'elective_semesters'
        verbose_name_plural = "elective_semesters"
        unique_together =  (("elective_id","semester_id","branch_id"),)
    
    # def __str__(self,):
    #     return self.elective_id

class ElectiveFaculty(models.Model):
    id = models.AutoField(primary_key=True)
    elective_id = models.ForeignKey(Electives,db_column='elective_id',on_delete=models.CASCADE)
    faculty_id = models.ForeignKey('faculty.Faculty',db_column='faculty_id',on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'faculty_electives'
        verbose_name_plural = "faculty_electives"
        unique_together =  (("elective_id",'faculty_id'),) 


class ElectiveStudent(models.Model):
    id = models.AutoField(primary_key=True)
    elective_id = models.ForeignKey(Electives,db_column='elective_id',on_delete=models.CASCADE)
    student_id = models.ForeignKey('students.Students',db_column='student_id',on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'student_electives'
        verbose_name_plural = "student_electives"
        unique_together =  (("elective_id","student_id"),)

class ElectiveDetails(models.Model):
    id = models.AutoField(primary_key=True)
    elective_id = models.ForeignKey(Electives,db_column='elective_id',on_delete=models.CASCADE)
    total_intake = models.IntegerField()
    scope =  models.TextField()
    syllabus_pdf = models.TextField()
    company_names = models.TextField()
    introduction_video = models.TextField()    