from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Compulsory', 'Compulsory'),
        ('Elective', 'Elective'),
    ]

    TYPE_CHOICES = [
        ('Theory', 'Theory'),
        ('Practical', 'Practical'),
        ('Dissertation', 'Dissertation'),
        ('Project', 'Project'),
        ('Field Work', 'Field Work'),
    ]

    CBCS_CATEGORY_CHOICES = [
        ('Major', 'Major'),
        ('Minor', 'Minor'),
        ('Core', 'Core'),
        ('DSE', 'DSE'),  # Discipline Specific Elective
        ('GE', 'GE'),    # Generic Elective
        ('OE', 'OE'),    # Open Elective
        ('VAC', 'VAC'),  # Value Added Course
        ('AEC', 'AEC'),  # Ability Enhancement Course
    ]

    name = models.CharField(max_length=200, verbose_name='Course Name', help_text='Enter the full name of the course')
    code = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Compulsory')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Theory')
    cbcs_category = models.CharField(max_length=20, choices=CBCS_CATEGORY_CHOICES, default='Major')
    maximum_credit = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(0, 21)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['code']
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        unique_together = ('name', 'code')

    def clean(self):
        if self.maximum_credit not in range(1, 21):
            raise ValidationError('Maximum credit must be between 1 and 20.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Course, self).save(*args, **kwargs)
