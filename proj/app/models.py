from django.db import models
from django.urls import reverse


class Dog(models.Model):
    name = models.CharField(max_length=128, verbose_name="Имя")
    age = models.IntegerField(verbose_name="Возраст")
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE, verbose_name="Порода")
    gender = models.CharField(max_length=64, verbose_name="Пол")
    color = models.CharField(max_length=64, verbose_name="Цвет")
    favorite_food = models.CharField(max_length=256, verbose_name="Любимая еда")
    favorite_toy = models.CharField(max_length=256, verbose_name="Любимая игрушка")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ("name",)
        constraints = [
            models.CheckConstraint(
                check=models.Q(age__gt=0),
                name="age_gt_1"
            ),
        ]


class Breed(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")
    size = models.CharField(
        max_length=6,
        choices={
            "T": "Tiny",
            "S": "Small",
            "M": "Medium",
            "L": "Large"
        },
        verbose_name="Размер"
    )
    friendliness = models.IntegerField(verbose_name="Дружелюбность")
    trainability = models.IntegerField(verbose_name="Обучаемость")
    shedding_amount = models.IntegerField(verbose_name="Линька")
    exercise_needs = models.IntegerField(verbose_name="Необходимость дрессировки")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
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
