from django.db import models
from directory import models as dirmods

# ------------------------------------------------------------------------------
class Assignment(models.Model):
    comps = models.ManyToManyField(dirmods.Member, related_name="companions")
    ministerees = models.ManyToManyField(dirmods.Member, related_name="ministerees", blank=True)

    def __str__(self):
        mystr = ""
        for i, person in enumerate(self.comps.all()):
            mystr += person.name
            if not i:
                mystr += " | "
        return mystr

# ------------------------------------------------------------------------------
