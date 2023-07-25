from django.db import models

GENDER_CHOICES = [
    ('F', 'F'),
    ('M', 'M')
]


class Member(models.Model):
    household = models.ForeignKey('Household', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    gender = models.TextField(choices=GENDER_CHOICES)
    birth_date = models.CharField(max_length=14)
    address = models.TextField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    email = models.CharField(null=True, blank=True, max_length=100)
    # manually marked, (show these members on separate page from the rest)
    moved_out = models.BooleanField(default=False)
    # when new csv from lds.org doesn't have this member on it
    absent_record = models.BooleanField(default=False)

    brother_comp = models.ForeignKey(
        'ministering.BrotherComp',
        related_name='members',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    sister_comp = models.ForeignKey(
        'ministering.SisterComp',
        related_name='members',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name + f" [{self.gender}]")


class Household(models.Model):
    gender = models.TextField(choices=GENDER_CHOICES, null=True)
    address = models.TextField()

    def __str__(self):
        return f"[{self.gender}] {self.address}"

    def get_members(self):
        return Member.objects.filter(household=self)
