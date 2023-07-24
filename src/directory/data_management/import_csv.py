import csv, pdb, re, os
from directory import models as dmods

# ------------------------------------------------------------------------------
def parse_email(e_in):
    """
    returns email from string
    - if no email found returns False
    """
    try:
        matches = re.findall('[^<>,\\s]+@[^<>,\\s]+\..+', str(e_in))
        if len(matches) > 0:
            return matches[0]
        else:
            return False
    except:
        return False

# ------------------------------------------------------------------------------
    # NOTIFY OR MARK PEOPLE WHO'S RECORDS WEREN'T ON lds.ORG FROM RECENT IMPORT
# ------------------------------------------------------------------------------
    #
# ------------------------------------------------------------------------------
def parse_number(num_in):
    """
    will return a 10 or 11 digit phone number, otherwise returns false
    """
    temp = re.findall(r'\d+', str(num_in))
    num_found = "".join(temp)
    if len(num_found) == 10 or len(num_found) == 11:
        return num_found
    else:
        return False

# ------------------------------------------------------------------------------
def read_csv():
    with open('directory/data_management/12_09_19.csv') as f:
        reader = csv.reader(f)
        pdb.set_trace()
        for row in reader:
            rowlen = len(row)
            # vvv on lds.org name will always be first field vvv
            name = row[0]
            newmember, created = dmods.Member.objects.get_or_create(name=name)
            if created:
                if rowlen > 1:
                    if parse_number(row[1]):
                        newmember.number = parse_number(row[1])
                    elif parse_email(row[1]):
                        newmember.email = row[1]
                if rowlen > 2:
                    if parse_number(row[2]):
                        newmember.number = parse_number(row[2])
                    elif parse_email(row[2]):
                        newmember.email = row[2]
                newmember.save()
                # print(row)

# ------------------------------------------------------------------------------
def validNumber(phone_nuber):
    pattern = re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
    return pattern.match(phone_nuber) is not None

# ------------------------------------------------------------------------------
def hasNumbers(inputString):
    """
    returns True or False depeding on if a number is in the string
    """
    return any(char.isdigit() for char in inputString)
