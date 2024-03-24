from django.db import models
from FuelSupply.models import CustomModel
from django.utils.translation import gettext, gettext_lazy as _





class MilitaryUnit(CustomModel):
    number = models.CharField(max_length=255, verbose_name="Raqami")
    name = models.CharField(max_length=255, verbose_name="Nomi")
    short_name = models.CharField(max_length=255, verbose_name="Qisqa nomi")

    def __str__(self):
        return "{}-{}".format(self.pk, self.short_name)

    class Meta:
        verbose_name = "Harbiy qism"
        verbose_name_plural = "Harbiy qism"


class FuelType(CustomModel):
    title = models.CharField(max_length=100, verbose_name="Nomi")
    comment = models.CharField(
        max_length=255, verbose_name="Izoh", null=True, blank=True
    )

    class Meta:
        verbose_name = "Yoqilg'i turi"
        verbose_name_plural = "Yoqilg'i turilari"

    def __str__(self) -> str:
        return "{}.{}".format(self.pk, self.title)


class Vehicles(CustomModel):
    AUTOMOBILE_TYPES = [("armored", "Zirxli texnika"), ("unarmored", "Zirxsiz texnika")]
    number = models.CharField(
        max_length=50,
        verbose_name="Raqami",
        unique=True,
    )
    tex_passport = models.CharField(
        max_length=100,
        verbose_name="Tex. passport",
        unique=True,
    )
    model = models.CharField(
        max_length=255,
        verbose_name="Modeli",
    )
    color = models.CharField(
        max_length=100,
        verbose_name="Rangi",
    )
    year = models.IntegerField(
        verbose_name="Ishlab chiqarilgan yili",
    )
    automobile_type = models.CharField(
        choices=AUTOMOBILE_TYPES,
        max_length=50,
        verbose_name="Texnika turi",
    )

    odometr = models.IntegerField(
        verbose_name="Odometr",
    )
    fuel_consumption = models.IntegerField(
        verbose_name="Yoqilg'i sarfi(100 km, litr)",
    )
    fuel_type = models.ManyToManyField(
        FuelType,
        verbose_name="Yoqilg'i turi",
    )
    driver = models.ForeignKey(
        "authentication.CustomUser",
        verbose_name="Haydovchi",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="vehicles",
    )

    class Meta:
        verbose_name = "Texnika"
        verbose_name_plural = "Texnikalar"

    def __str__(self) -> str:
        return "{}.{}({})".format(self.pk, self.number, self.model)


class Application(CustomModel):
    STATUS_CHOICES = [
        ("new", "Yangi"),
        ("accepted", "Qabul qilingan"),
        ("inspection", "Texnik ko'rikda"),
        ("petrol_station", "AYOQSHda"),
        ("ready", "Amaliyotga tayyor"),
        ("in_progress", "Bajarilmoqda"),
        ("successful", "Muvaffaqiyatli bajarildi"),
        ("canceled", "Bekor qilindi"),
        ("rejected", "Rad etildi"),
    ]

    AUTOMOBILE_TYPES = [("armored", "Zirxli texnika"), ("unarmored", "Zirxsiz texnika")]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="new")
    military_unit = models.ForeignKey(MilitaryUnit, on_delete=models.PROTECT)
    automobile_type = models.CharField(
        choices=AUTOMOBILE_TYPES,
        max_length=50,
        default="unarmored",
        verbose_name="Texnika turi",
    )
    date_time = models.DateTimeField()
    route = models.CharField(max_length=50, verbose_name="Yo'nalish")
    passengers_count = models.IntegerField(
        null=True, blank=True, verbose_name="Yo'lovchilar soni"
    )
    file = models.FileField(
        upload_to="applications/",
        max_length=100,
        verbose_name="Bildirgi fayli",
        null=True,
        blank=True,
    )
    comment = models.CharField(
        max_length=255, verbose_name="Izoh", null=True, blank=True
    )

    author = models.ForeignKey(
        "authentication.CustomUser",
        verbose_name="Ariza beruvchi",
        on_delete=models.PROTECT,
        related_name="author",
    )

    vehicles = models.ManyToManyField(
        Vehicles,
        verbose_name="Moshina",
        blank=True,
    )

    def __str__(self):
        return "{}.{}-{}".format(self.pk, self.military_unit, self.route)

    class Meta:
        verbose_name = "Ariza"
        verbose_name_plural = "Ariza"


class Inspection(CustomModel):
    INSPECTION_STATUS = [
        ("unsatisfactory", "Qoniqarsiz"),
        ("satisfactory", "Qoniqarli"),
        ("good", "Yaxshi"),
        ("excellent", "A'lo"),
    ]
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    application = models.ForeignKey(
        Application,
        verbose_name="Ariza",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    vehicles = models.ForeignKey(
        Vehicles, verbose_name="Texnika", on_delete=models.CASCADE
    )
    status = models.CharField(choices=INSPECTION_STATUS, max_length=50)

    class Meta:
        verbose_name = "Texnik ko'rik"
        verbose_name_plural = "Texnik ko'rik"

    def __str__(self) -> str:
        return "{}.{}-{}".format(self.pk, self.vehicles.number, self.status)


class Refuel(CustomModel):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    application = models.ForeignKey(
        Application,
        verbose_name="Ariza",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    vehicles = models.ForeignKey(
        Vehicles, verbose_name="Texnika", on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        FuelType, verbose_name="Yoqilg'i turi", on_delete=models.CASCADE
    )
    valume = models.IntegerField(default=0, verbose_name="Hajmi")


    #add_fuel
     
class Add_fuels(CustomModel):
    yoq_nomi = models.TextField(max_length=255, verbose_name="Yoqilg'i nomi")
    tank = models.IntegerField(verbose_name="Tanklar SAU")
    art = models.IntegerField(verbose_name="ARt tiyagachi ")
    bmp = models.IntegerField(verbose_name="BMP, BTR, mototsikillar ")
    avto = models.IntegerField(verbose_name="Avtomobillar")
    uchuv = models.IntegerField(verbose_name=" Uchuvchi aparatlar")   
    trak = models.IntegerField(verbose_name="Traktor va muxandislik texnikalari va qurilish mexanizmlar")
    maxs = models.IntegerField(verbose_name="Maxsus mashinalarning avtonom divigatellari statsionar divigatellar ")
    ishab = models.IntegerField(verbose_name=" Ishlab chiqarish va texnik extiyojlar")
    rim1 = models.IntegerField(verbose_name=" I")
    rim2 = models.IntegerField(verbose_name="II")
    rim3 = models.IntegerField(verbose_name="III")
    rim4 = models.IntegerField(verbose_name="IV")
    time = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Yaratilgan vaqts")
        

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.yoq_nomi
        







    
