import csv, pdb, re, os
from directory.models import Member, Household

# todo jake - not used
# def parse_email(e_in):
#     """
#     returns email from string
#     - if no email found returns False
#     """
#     try:
#         matches = re.findall('[^<>,\\s]+@[^<>,\\s]+\..+', str(e_in))
#         if len(matches) > 0:
#             return matches[0]
#         else:
#             return False
#     except:
#         return False


# todo jake - not used
# def parse_number(num_in):
#     """
#     will return a 10 or 11 digit phone number, otherwise returns false
#     """
#     temp = re.findall(r'\d+', str(num_in))
#     num_found = "".join(temp)
#     if len(num_found) == 10 or len(num_found) == 11:
#         return num_found
#     else:
#         return False


def import_from_csv():
    with open('directory/data_management/memberlist.csv') as f:
        for row in csv.reader(f):
            # todo jake - see about confirming the order of these fields if there is a header row.  Would help to make
            #  sure data remains standardized
            name, gender, birth_date, address, phone_number, email = row
            address = address.replace('\n', ', ')

            # set up household
            member_household, created_household = Household.objects.get_or_create(
                gender=gender,
                address=address
            )

            if created_household:
                member_household.save()

            # search for member with matching name, gender, and birth_date.  If not found create
            # new one and populate with data from current row in csv
            new_member, created_member = Member.objects.get_or_create(
                name=name,
                gender=gender,
                birth_date=birth_date
            )

            if created_member:
                new_member.household = member_household
                new_member.address = address
                new_member.phone_number = phone_number
                new_member.email = email
                new_member.save()


# todo jake - not used
# def valid_number(phone_nuber):
#     pattern = re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
#     return pattern.match(phone_nuber) is not None


# todo jake - not used
# def has_numbers(inputString):
#     """
#     returns True or False depeding on if a number is in the string
#     """
#     return any(char.isdigit() for char in inputString)
