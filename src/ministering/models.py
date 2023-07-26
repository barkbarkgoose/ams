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
        return f"{self.id}: [M] {' | '.join(member_names)}"

    def print_assignments(self):
        for member in Member.objects.filter(brother_comp=self):
            print(member.name, end="\t")

    def get_assignment_string(self):
        member_string = ''
        for member in Member.objects.filter(brother_comp=self):
            member_string += member.name + '\t'

        return member_string


class SisterComp(models.Model):
    companions = models.ManyToManyField(
        Member,
        limit_choices_to={'gender': 'F', 'sister_comp': None},
        related_name='sister_comps'
    )

    def __str__(self):
        member_names = [member.name for member in self.companions.all()]
        return f"{self.id}: [F] {' | '.join(member_names)}"
