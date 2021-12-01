from utils import numbers


def start_numbers_test():
    print("********************* Test numbers - Start *********************\n")
    error_count = 0
    passed_tests = 0
    print("~~~~~~~~Testing dividable_by_10~~~~~~~~\n")

    a = 3
    print(f"Test with {a}")
    boolean_value = numbers.dividable_by_10(a)
    if boolean_value is True:
        print(f"ERROR :-(\t {a} is not dividable by 10 without a reminder, expected boolean_value: {False}, actual: {True} \n ")
        error_count+=1
    else:
        print(f"OK!\t {a} is not dividable by 10 without a reminder, expected boolean_value: {False}, actual: {False} \n ")
        passed_tests+=1

    b = 70
    print(f"Test with {b}")
    boolean_value = numbers.dividable_by_10(b)
    if boolean_value is False:
        print(f"ERROR :-(\t  {b} is dividable by 10 without a reminder, expected boolean_value: {True}, actual: {False} \n ")
        error_count += 1
    else:
        print(f"OK!\t {b} is dividable by 10 without a reminder, expected boolean_value: {True}, actual: {True} \n ")
        passed_tests += 1

    c = 0
    print(f"Test with {c}")
    boolean_value = numbers.dividable_by_10(c)
    if boolean_value is False:
        print(f"ERROR :-(\t {c} is dividable by 10 without a reminder, expected boolean_value: {True}, actual: {False} \n ")
        error_count += 1
    else:
        print(f"OK!\t {c} is dividable by 10 without a reminder, expected boolean_value: {True}, actual: {True} \n ")
        passed_tests += 1

    d = -5670
    print(f"Test with {d}")
    boolean_value = numbers.dividable_by_10(d)
    if boolean_value is False:
        print(f"ERROR :-(\t {d} is dividable by 10 without a reminder, expected boolean_value: {True}, actual: {False} \n ")
        error_count += 1
    else:
        print(f"OK!\t {d} is dividable by 10 without a reminder, expected boolean_value: {True}, actual: {True} \n ")
        passed_tests += 1

    e = -16
    print(f"Test with {e}")
    boolean_value = numbers.dividable_by_10(e)
    if boolean_value is True:
        print(f"ERROR :-(\t {e} is not dividable by 10 without a reminder, expected boolean_value: {False}, actual: {True} \n ")
        error_count += 1
    else:
        print(f"OK!\t {e} is not dividable by 10 without a reminder, expected boolean_value: {False}, actual: {False} \n ")
        passed_tests += 1

    f = 99
    print(f"Test with {f}")
    boolean_value = numbers.dividable_by_10(f)
    if boolean_value is True:
        print(f"ERROR :-(\t {f} is not dividable by 10 without a reminder, expected boolean_value: {False}, actual: {True} \n ")
        error_count += 1
    else:
        print(f"OK!\t {f} is not dividable by 10 without a reminder, expected boolean_value: {False}, actual: {False} \n ")
        passed_tests += 1


    print("~~~~~~~~Testing sum_of_digits~~~~~~~~\n")

    a = 234
    print(f"Test with {a}")
    calculated_digit_sum = numbers.sum_of_digits(a)
    if calculated_digit_sum == 9:
        print(f"OK!\t expected sum of digits: 9, actual: {calculated_digit_sum} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected sum of digits: 9, actual: {calculated_digit_sum} \n ")
        error_count += 1

    b = 94867497583
    print(f"Test with {b}")
    calculated_digit_sum = numbers.sum_of_digits(b)
    if calculated_digit_sum == 70:
        print(f"OK!\t expected sum of digits: 70, actual: {calculated_digit_sum} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected sum of digits: 70, actual: {calculated_digit_sum} \n ")
        error_count += 1

    c = 8
    print(f"Test with {c}")
    calculated_digit_sum = numbers.sum_of_digits(c)
    if calculated_digit_sum == 8:
        print(f"OK!\t expected sum of digits: 8, actual: {calculated_digit_sum} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected sum of digits: 8, actual: {calculated_digit_sum} \n ")
        error_count += 1

    d = 0
    print(f"Test with {d}")
    calculated_digit_sum = numbers.sum_of_digits(d)
    if calculated_digit_sum == 0:
        print(f"OK!\t expected sum of digits: 0, actual: {calculated_digit_sum} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected sum of digits: 0, actual: {calculated_digit_sum} \n ")
        error_count += 1

    e = -123
    print(f"Test with {e}")
    calculated_digit_sum = numbers.sum_of_digits(e)
    if calculated_digit_sum == 6:
        print(f"OK!\t expected sum of digits: 6, actual: {calculated_digit_sum} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected sum of digits: 6, actual: {calculated_digit_sum} \n ")
        error_count += 1

    print("~~~~~~~~Testing is_palindrome~~~~~~~~\n")

    a = 32123
    print(f"Test with {a}")
    boolean_value = numbers.is_palindrome(a)
    if boolean_value is True:
        print(f"OK!\t {a} is a palindrome, expected boolean value: {True} actual: {True} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t {a} is a palindrome, expected boolean value: {True} actual: {False} \n ")
        error_count += 1

    b = 9889
    print(f"Test with {b}")
    boolean_value = numbers.is_palindrome(b)
    if boolean_value is True:
        print(f"OK!\t {b} is a palindrome, expected boolean value: {True} actual: {True} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t {b} is a palindrome, expected boolean value: {True} actual: {False} \n ")
        error_count += 1

    c = 5
    print(f"Test with {c}")
    boolean_value = numbers.is_palindrome(c)
    if boolean_value is True:
        print(f"OK!\t {c} is a palindrome, expected boolean value: {True} actual: {True} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t {c} is a palindrome, expected boolean value: {True} actual: {False} \n ")
        error_count += 1

    d = 123
    print(f"Test with {d}")
    boolean_value = numbers.is_palindrome(d)
    if boolean_value is False:
        print(f"OK!\t {d} is NOT a palindrome, expected boolean value: {False} actual: {False} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t {d} is a palindrome, expected boolean value: {False} actual: {True} \n ")
        error_count += 1

    e = -1478741
    print(f"Test with {e}")
    boolean_value = numbers.is_palindrome(e)
    if boolean_value is True:
        print(f"OK!\t {e} is a palindrome, expected boolean value: {True} actual: {True} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t {e} is a palindrome, expected boolean value: {True} actual: {False} \n ")
        error_count += 1

    f = -5985
    print(f"Test with {f}")
    boolean_value = numbers.is_palindrome(f)
    if boolean_value is False:
        print(f"OK!\t {f} is NOT a palindrome, expected boolean value: {False} actual: {False} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t {f} is a palindrome, expected boolean value: {False} actual: {True} \n ")
        error_count += 1

    g = 0
    print(f"Test with {g}")
    boolean_value = numbers.is_palindrome(g)
    if boolean_value is True:
        print(f"OK!\t {g} is a palindrome, expected boolean value: {True} actual: {True} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t {g} is a palindrome, expected boolean value: {True} actual: {False} \n ")
        error_count += 1

    print(f"the number of errors: {error_count}")
    print(f"you passed {passed_tests} out of 18 tests")
    grade = passed_tests/18 * 100
    print(f"you grade is: {grade}")
    print("********************* Test numbers - End *********************\n\n")


