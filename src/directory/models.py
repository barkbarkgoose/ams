from django.db import models

# ------------------------------------------------------------------------------
class Member(models.Model):
    household = models.ForeignKey('Household', null=True, on_delete=models.SET_NULL)
    name = models.TextField()
    number = models.TextField(null=True)
    email = models.TextField(null=True)
    moved_out = models.BooleanField(default=False) # manually marked, (show these members on separate page from the rest)
    missing_record = models.BooleanField(default=False) # when new csv from lds.org doesn't have this member on it

    def __str__(self):
        return self.name

# ------------------------------------------------------------------------------
class Household(models.Model):
    TYPE_CHOICES = [
        ('MEN', 'Men'),
        ('WOMEN', 'Women'),
    ]
    type = models.TextField(choices=TYPE_CHOICES, null=True)
    address = models.TextField()

    def __str__(self):
        return str(self.address) + " --- " + str(self.type)

    def get_members(self):
        return Member.objects.filter(household=self)

# ------------------------------------------------------------------------------
# SOME MODEL STATS
# HOMELESS = Member.objects.filter(household=None)

# ------------------------------------------------------------------------------
