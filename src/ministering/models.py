from django.db import models
from directory.models import Member


class BrotherComp(models.Model):
    companions = models.ManyToManyField(
        Member,
        limit_choices_to={'gender': 'M'},
        related_name='brother_comps'
    )

    def __str__(self):
        member_names = [member.name for member in self.companions.all()]
        return f"[M] {' | '.join(member_names)}"


class SisterComp(models.Model):
    companions = models.ManyToManyField(
        Member,
        limit_choices_to={'gender': 'F'},
        related_name='sister_comps'
    )

    def __str__(self):
        member_names = [member.name for member in self.companions.all()]
        return f"[F] {' | '.join(member_names)}"


class Assignment(models.Model):
    brother_comps = models.ManyToManyField(BrotherComp, null=True, blank=True)
    sister_comps = models.ManyToManyField(SisterComp, null=True, blank=True)
    ministering = models.ManyToManyField(
        Member,
        related_name='assignments'
    )

    def __str__(self):
        ministering_names = [m.name for m in self.ministering.all()]
        brother_comp = self.brother_comps.first()
        sister_comp = self.brother_comps.first()

        if brother_comp:
            return f"{brother_comp} --> {' | '.join(ministering_names)}"

        if sister_comp:
            return f"{sister_comp} --> {' | '.join(ministering_names)}"

        return "No members assigned"
