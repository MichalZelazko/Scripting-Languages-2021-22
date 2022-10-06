
PESEL_LENGTH = 11
PESEL_WEIGHT = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)

# functions


def checksum_verification(pesel):
    checksum = 0
    for i in range(PESEL_LENGTH - 1):
        checksum += PESEL_WEIGHT[i] * int(pesel[i], 10)
    checksum = (10 - (checksum % 10)) % 10
    if checksum == int(pesel[10], 10):
        return True


def length_verification(pesel):
    if len(pesel) == PESEL_LENGTH:
        return True


def digit_verification(pesel):
    if pesel.isdigit():
        return True


def date_verification(pesel):
    m = int(pesel[2:4], 10)
    d = int(pesel[4:6], 10)
    year = int(pesel[0:2], 10)
    if (int(pesel[2], 10) == 8 or int(pesel[2], 10) == 9):
        year += 1800
        m = m - 80
    elif (int(pesel[2], 10) == 0 or int(pesel[2], 10) == 1):
        year += 1900
    elif (int(pesel[2], 10) == 2 or int(pesel[2], 10) == 3):
        year += 2000
        m = m - 20
    elif (int(pesel[2], 10) == 4 or int(pesel[2], 10) == 5):
        year += 2100
        m = m - 40
    elif (int(pesel[2], 10) == 6 or int(pesel[2], 10) == 7):
        year += 2200
        m = m - 60
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days[1] = 29
    if (1 <= m <= 12 and 1 <= d <= days[m-1]):
        return True

# counters


total = correct = male = female = 0
invalid_length = invalid_digit = invalid_date = invalid_checksum = 0
file = open("1e6.dat", 'r')
# main processing loop
for pesel in file:
    pesel = pesel.strip()
    total += 1
    if length_verification(pesel) is True:
        if digit_verification(pesel) is True:
            if date_verification(pesel) is True:
                if checksum_verification(pesel) is True:
                    correct += 1
                    if int(pesel[9]) % 2 == 0:
                        female += 1
                    else:
                        male += 1
                else:
                    invalid_checksum += 1
            else:
                invalid_date += 1
        else:
            invalid_digit += 1
    else:
        invalid_length += 1

file.close()
# show results
print(total, correct, female, male)
print(invalid_length, invalid_digit, invalid_date, invalid_checksum)
