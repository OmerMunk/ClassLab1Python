from utils import birth_dates


def start_birth_dates_test():
    print("********************* Test birth_dates - Start *********************\n")
    error_count = 0
    passed_tests = 0
    print("~~~~~~~~Testing is_lucky~~~~~~~~\n")

    a = 1987
    print(f"Test with {a}")
    boolean_value = birth_dates.is_lucky(a)
    if boolean_value is False:
        print(f"OK!\t  expected boolean value : {False} actual: {boolean_value} \n ")
        passed_tests+=1
    else:
        print(f"ERROR :-(\t expected boolean value : {False} actual: {boolean_value} \n ")
        error_count+=1

    b = 2002
    print(f"Test with {b}")
    boolean_value = birth_dates.is_lucky(b)
    if boolean_value is True:
        print(f"OK!\t  expected boolean value : {True} actual: {boolean_value} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected boolean value : {True} actual: {boolean_value} \n ")
        error_count += 1

    c = 2008
    print(f"Test with {c}")
    boolean_value = birth_dates.is_lucky(c)
    if boolean_value is True:
        print(f"OK!\t  expected boolean value : {True} actual: {boolean_value} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected boolean value : {True} actual: {boolean_value} \n ")
        error_count += 1

    d = 1881
    print(f"Test with {d}")
    boolean_value = birth_dates.is_lucky(d)
    if boolean_value is True:
        print(f"OK!\t  expected boolean value : {True} actual: {boolean_value} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected boolean value : {True} actual: {boolean_value} \n ")
        error_count += 1

    e = 1883
    print(f"Test with {e}")
    boolean_value = birth_dates.is_lucky(e)
    if boolean_value is True:
        print(f"OK!\t  expected boolean value : {True} actual: {boolean_value} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected boolean value : {True} actual: {boolean_value} \n ")
        error_count += 1

    f = 1884
    print(f"Test with {f}")
    boolean_value = birth_dates.is_lucky(f)
    if boolean_value is False:
        print(f"OK!\t  expected boolean value : {False} actual: {boolean_value} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected boolean value : {False} actual: {boolean_value} \n ")
        error_count += 1


    print("~~~~~~~~Testing lucky_people~~~~~~~~\n")

    names_list_a = ["John","Mary","David"]
    dates_list_a = ["20-02-2001","03-04-2002","30-11-2012", "30-11-2012"]
    print(f"Test with names list: {names_list_a}, birth dates list: {dates_list_a}")
    lucky_list, dates_count = birth_dates.lucky_people(names_list_a, dates_list_a)
    if lucky_list == ['Mary'] and dates_count == {'20-02-2001': 1,'03-04-2002': 1,'30-11-2012': 2}:
        print("OK!\t expected returned lucky people list: ['Mary'], actual: ",lucky_list)
        print("     expected returned birth dates count dictionary: {\'20-02-2001\': 1, \'03-04-2002\': 1 ,\'30-11-2012\': 2}, actual:", dates_count, " \n")
        passed_tests += 1
    else:
        print("ERROR :-(!\t expected returned lucky people list: ['Mary'], actual: ",lucky_list)
        print("             expected returned birth dates count dictionary: {\'20-02-2001\': 1, \'03-04-2002\': 1 ,\'30-11-2012\': 2}, actual:", dates_count, " \n")
        error_count += 1

    names_list_b = ["John","Bryce","David", "Beckham"]
    dates_list_b = ["06-04-1991","06-04-1991","03-07-2009"]
    print(f"Test with names list: {names_list_b}, birth dates list: {dates_list_b}")
    lucky_list, dates_count = birth_dates.lucky_people(names_list_b, dates_list_b)
    if lucky_list == ['John', 'Bryce'] and dates_count == {'06-04-1991': 2,'03-07-2009': 1}:
        print("OK!\t expected returned lucky people list: ['John', 'Bryce'], actual: ",lucky_list)
        print("     expected returned birth dates count dictionary: {\'06-04-1991\': 2, \'03-07-2009\': 1 }, actual:", dates_count, " \n")
        passed_tests += 1
    else:
        print("ERROR :-(!\t expected returned lucky people list: ['John', 'Bryce'], actual: ",lucky_list)
        print("             expected returned birth dates count dictionary: {\'06-04-1991\': 2, \'03-07-2009\': 1 }, actual:", dates_count, " \n")
        error_count += 1

    names_list_c = []
    dates_list_c = []
    print(f"Test with names list: {names_list_c}, birth dates list: {dates_list_c}")
    lucky_list, dates_count = birth_dates.lucky_people(names_list_c, dates_list_c)
    if lucky_list == [] and dates_count == {}:
        print("OK!\t expected returned lucky people list: [], actual: ",lucky_list)
        print("     expected returned birth dates count dictionary: {}, actual:", dates_count, " \n")
        passed_tests += 1
    else:
        print("ERROR :-(!\t expected returned lucky people list: [], actual: ",lucky_list)
        print("             expected returned birth dates count dictionary: {}, actual:", dates_count, " \n")
        error_count += 1

    names_list_d = ["Omer"]
    dates_list_d = []
    print(f"Test with names list: {names_list_d}, birth dates list: {dates_list_d}")
    lucky_list, dates_count = birth_dates.lucky_people(names_list_d, dates_list_d)
    if lucky_list == [] and dates_count == {}:
        print("OK!\t expected returned lucky people list: [], actual: ",lucky_list)
        print("     expected returned birth dates count dictionary: {}, actual:", dates_count, " \n")
        passed_tests += 1
    else:
        print("ERROR :-(!\t expected returned lucky people list: [], actual: ",lucky_list)
        print("             expected returned birth dates count dictionary: {}, actual:", dates_count, " \n")
        error_count += 1

    names_list_e = []
    dates_list_e = ["30-11-2012"]
    print(f"Test with names list: {names_list_e}, birth dates list: {dates_list_e}")
    lucky_list, dates_count = birth_dates.lucky_people(names_list_e, dates_list_e)
    if lucky_list == [] and dates_count == {'30-11-2012': 1}:
        print("OK!\t expected returned lucky people list: [], actual: ",lucky_list)
        print("     expected returned birth dates count dictionary: {'30-11-2012': 1}, actual:", dates_count, " \n")
        passed_tests += 1
    else:
        print("ERROR :-(!\t expected returned lucky people list: [], actual: ",lucky_list)
        print("             expected returned birth dates count dictionary: {'30-11-2012': 1}, actual:", dates_count, " \n")
        error_count += 1

    print(f"the number of errors: {error_count}")
    print(f"you passed {passed_tests} out of 11 tests")
    grade = passed_tests/11 * 100
    print(f"you grade is: {grade}")
    print("********************* Test birth_dates - End *********************")