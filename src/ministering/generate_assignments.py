from django.db.models import Prefetch

from directory.models import Member, Household
from ministering.models import BrotherComp
import pdb


def generate_eq_companionships():
    # todo jake - docstring
    already_assigned = []

    brother_comps = BrotherComp.objects.prefetch_related(
        Prefetch('companions')
    )

    for comp in brother_comps:
        already_assigned.extend(comp.companions.all())

    elders_needing_assignment = []

    # get all elders not already in a companionship who live with others and put them in the assignment
    # list first. This creates locality so when assignments are made housemates will be together
    for house in Household.objects.filter(gender='M'):
        house_members = list(house.get_members())

        house_assignments_pending = []
        for member in house_members:
            if member not in already_assigned and member.do_not_assign_comp is False:
                house_assignments_pending.append(member)

        if len(house_assignments_pending) > 1:
            # if there is an odd number remove the last person from house_assignments_pending
            # (they'll go in the pool later)
            if len(house_assignments_pending) % 2 == 1:
                house_assignments_pending.pop()

            for member in house_assignments_pending:
                elders_needing_assignment.append(member)

    # --- 2nd pass to add everyone else to the assignments list ---
    for elder in Member.objects.filter(gender='M', do_not_assign_comp=False):
        if elder not in elders_needing_assignment and elder not in already_assigned:
            elders_needing_assignment.append(elder)

    print(f"elders needing assignment: {len(elders_needing_assignment)}")
    # --- now create the companionships ---
    previous_comp = None
    for i in range(0, len(elders_needing_assignment), 2):
        elder_pair = elders_needing_assignment[i:i + 2]
        # if only one elder left, add them to the last companionship
        if len(elder_pair) == 1:
            previous_comp.companions.add(elder_pair[0])
            previous_comp.save()
            break

        else:
            comp = BrotherComp.objects.create()
            previous_comp = comp
            comp.companions.add(*elder_pair)
            comp.save()


def make_eq_ministering_assignments():
    # todo jake - docstring, also separate out any duplicate logic
    # create male and female list of members needing an assigned ministering companionship (put housemates next to each other)
    brother_assignment_list = []

    for house in Household.objects.filter(gender='M'):
        for member in house.get_members():
            if member.brother_comp is None and member.do_not_minister is False:
                brother_assignment_list.append(member)

    sister_assignment_list = []

    for house in Household.objects.filter(gender='F'):
        for member in house.get_members():
            if member.brother_comp is None and member.do_not_minister is False:
                sister_assignment_list.append(member)

    # determine how many companionships already have ministering assignments
    assigned_companionships = []
    for member in Member.objects.all():
        if member.brother_comp is not None:
            assigned_companionships.append(member.brother_comp)

    # get list of companionships that don't have any ministering assignments
    unassigned_companionships = []
    for comp in BrotherComp.objects.all():
        if comp not in assigned_companionships:
            unassigned_companionships.append(comp)

    if len(unassigned_companionships) == 0:
        print('no unassigned companionships')
        return

    # want to add in sisters and brothers in pairs until we know we are through all the households
    # once we hit individuals living alone we will assign them one by one to the companionships until
    # no one is left
    pdb.set_trace()
    more_assignments_needed = True
    while more_assignments_needed:
        for comp in unassigned_companionships:
            # break from loop if both assignment lists are empty
            if len(brother_assignment_list) == 0 and len(sister_assignment_list) == 0:
                more_assignments_needed = False
                break

            # check if we should still be assigning brothers in pairs (2 per household) or as individuals
            if len(brother_assignment_list) > 2 and brother_assignment_list[0].household == brother_assignment_list[1].household:
                brother_batch_count = 2
            else:
                brother_batch_count = 1

            for _ in range(0, brother_batch_count):
                if len(brother_assignment_list) > 0:
                    member = brother_assignment_list.pop(0)
                    member.brother_comp = comp
                    member.save()

            # check if we should still be assigning sisters in pairs (2 per household) or as individuals
            if len(sister_assignment_list) > 2 and sister_assignment_list[0].household == \
                    sister_assignment_list[1].household:
                sister_batch_count = 2
            else:
                sister_batch_count = 1

            for _ in range(0, sister_batch_count):
                if len(sister_assignment_list) > 0:
                    member = sister_assignment_list.pop(0)
                    member.brother_comp = comp
                    member.save()

    # end make_eq_ministering_assignments ---
