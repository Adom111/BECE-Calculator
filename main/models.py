from typing import Any
from django.db import models

# Create your models here.

class Becedb(models.Model):
    subj_name = models.CharField(max_length=200)
    subj_type = models.CharField(max_length=200)
    subj_grade = models.IntegerField()
    subj_add = models.BooleanField(False)
    #subj_remove = models.BooleanField(True)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)