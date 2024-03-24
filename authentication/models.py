from django.db import models
from django.contrib.auth.models import AbstractUser
from FuelSupply.models import CustomModel


class MilitaryRank(CustomModel):
    title = models.CharField(max_length=255, verbose_name="Nomi")
    short_title = models.CharField(max_length=255, verbose_name="Qisqartma")

    class Meta:
        verbose_name = "Harbiy unvonlar"
        verbose_name_plural = "Harbiy unvonlar"

    def __str__(self) -> str:
        return "{}.{}".format(self.pk, self.short_title)


class CustomUser(AbstractUser):
    avatar = models.ImageField(
        upload_to="avatars/", null=True, blank=True, verbose_name="Rasm"
    )
    military_rank = models.ForeignKey(
        MilitaryRank,
        on_delete=models.PROTECT,
        verbose_name="Harbiy unvon",
        blank=True,
        null=True,
    )
    is_driver = models.BooleanField(default=False, verbose_name="Haydovchimi")

    def __str__(self):
        return self.username

    def get_short_name(self) -> str:
        if self.military_rank:
            return "{} {} {}.".format(
                self.military_rank.short_title, self.first_name, self.last_name[:1]
            )
        else:
            return "{} {}.".format(self.first_name, self.last_name[:1])

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"
