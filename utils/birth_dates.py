from utils import numbers
from utils import col


def is_lucky(year):
    if numbers.is_palindrome(year) is True or numbers.dividable_by_10(numbers.sum_of_digits(year)) is True:
        return True
    else:
        return False


def lucky_people(names_list, birth_dates_list):
    lucky_list = []
    for i in range(min(len(names_list),len(birth_dates_list))):
        if is_lucky(int(birth_dates_list[i][6:])) is True:
            lucky_list.append(names_list[i])
    return lucky_list, col.elems_count(birth_dates_list)


