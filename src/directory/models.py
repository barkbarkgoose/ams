from django.db import models


# ------------------------------------------------------------------------------
class Member(models.Model):
    household = models.ForeignKey('Household', null=True, on_delete=models.SET_NULL)
    name = models.TextField()
    gender = models.TextField()
    birth_date = models.TextField()
    address = models.TextField()
    phone_number = models.TextField(null=True)
    email = models.TextField(null=True)
    # manually marked, (show these members on separate page from the rest)
    moved_out = models.BooleanField(default=False)
    # when new csv from lds.org doesn't have this member on it
    absent_record = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name + f" [{self.gender}]")


# ------------------------------------------------------------------------------
class Household(models.Model):
    TYPE_CHOICES = [
        ('F', 'F'),
        ('M', 'M')
    ]
    gender = models.TextField(choices=TYPE_CHOICES, null=True)
    address = models.TextField()

    def __str__(self):
        return f"[{self.gender}] {self.address}"

    def get_members(self):
        return Member.objects.filter(household=self)


# ------------------------------------------------------------------------------
# SOME MODEL STATS
# HOMELESS = Member.objects.filter(household=None)

# ------------------------------------------------------------------------------
