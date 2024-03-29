from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE)
    gender = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    favorite_food = models.CharField(max_length=256)
    favorite_toy = models.CharField(max_length=256)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(age__gt=0),
                name="age_gt_1"
            ),
        ]


class Breed(models.Model):
    name = models.CharField(max_length=256)
    size = models.CharField(
        max_length=6,
        choices={
            "T": "Tiny",
            "S": "Small",
            "M": "Medium",
            "L": "Large"
        }
    )
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    shedding_amount = models.IntegerField()
    exercise_needs = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(friendliness__gte=1) & models.Q(friendliness__lte=5),
                name="friendliness_gte_1_lte_5"
            ),
            models.CheckConstraint(
                check=models.Q(trainability__gte=1) & models.Q(trainability__lte=5),
                name="trainability_gte_1_lte_5"
            ),
            models.CheckConstraint(
                check=models.Q(shedding_amount__gte=1) & models.Q(shedding_amount__lte=5),
                name="shedding_amount_gte_1_lte_5"
            ),
            models.CheckConstraint(
                check=models.Q(exercise_needs__gte=1) & models.Q(exercise_needs__lte=5),
                name="exercise_needs_gte_1_lte_5"
            ),
        ]
