from django.db import models

EXAM_CHOICES = (
  ('pass', 'PASS'),
  ('fail', 'FAIL'),
)

class StudentRecord(models.Model):
  first_name                  = models.CharField(max_length=50)
  last_name                   = models.CharField(max_length=50)
  dob                         = models.DateField(max_length=50, default='11/11/1111')
  address                     = models.CharField(max_length=100)
  phone                       = models.CharField(max_length=50)
  email                       = models.CharField(max_length=100)
  date_of_enrollment = models.DateField(default='11/11/1111')
  quiz_score        = models.IntegerField(default=0)
  python_entry_level = models.CharField(max_length=4, choices=EXAM_CHOICES, default='pass')
  # aws_practitioner_exam = models.CharField(max_length=4, choices=EXAM_CHOICES, default='pass')
  python_associate_exam = models.CharField(max_length=4, choices=EXAM_CHOICES, default='pass')
  blockchain_exam = models.CharField(max_length=4, choices=EXAM_CHOICES, default='pass')
  aws_ml_exam = models.CharField(max_length=4, choices=EXAM_CHOICES, default='pass')
  dissertation = models.CharField(max_length=50, default='pass')
  date_of_graduation = models.DateField(default='11/11/1111')
  job_placement = models.CharField(max_length=100, default='R&D Lab')

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


