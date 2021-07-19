from django.db import models
from ...gym_trainer.models import CustomModel
# Create your models here.


class PrimaryMuscle(CustomModel):
    name = models.CharField(
        max_length=50,
        null=False,
        unique=True
    )


class SecondaryMuscle(CustomModel):

    name = models.CharField(
        max_length=50,
        null=False,
        unique=True
    )

    primary_muscle = models.OneToOneField(
        PrimaryMuscle,
        on_delete=models.CASCADE
    )


