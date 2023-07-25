from django.db import models
from directory.models import Member


class Assignment(models.Model):
    comps = models.ManyToManyField(Member, related_name="companions")
    ministerees = models.ManyToManyField(Member, related_name="ministerees", blank=True)

    def __str__(self):
        mystr = ""
        for i, person in enumerate(self.comps.all()):
            mystr += person.name
            if not i:
                mystr += " | "
        return mystr


# class BrotherComp(models.Model):
#     comp = models.ManyToManyField(
#         Member,
#         limit_choices_to={'gender': 'M'},
#         related_name="brother_companions"
#     )
#     assignment = models.ManyToManyField(
#         Member,
#         related_name="brothercomp_assignments",
#         blank=True
#     )
#
#
# class SisterComp(models.Model):
#     comp = models.ManyToManyField(
#         Member,
#         related_name="sister_companions"
#     )
#     assignment = models.ManyToManyField(
#         Member,
#         limit_choices_to={'gender': 'F'},
#         related_name="sistercomp_assignments",
#         blank=True
#     )