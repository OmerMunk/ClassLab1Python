from utils import col


def start_col_test():
    print("********************* Test col - Start *********************\n")
    error_count = 0
    passed_tests = 0
    print("~~~~~~~~Testing unique_values~~~~~~~~\n")

    a = [34, 5, 1, 34, 6, 1]
    print(f"Test with {a}")
    returned_value = col.unique_values(a)
    if returned_value == [34, 5, 1, 6]:
        print(f"OK!\t  expected returned value : [34, 5, 1, 6], actual: {returned_value} \n ")
        passed_tests+=1
    else:
        print(f"ERROR :-(\t expected returned value : [34, 5, 1, 6], actual: {returned_value} \n ")
        error_count+=1

    b = [1, 7, 99]
    print(f"Test with {b}")
    returned_value = col.unique_values(b)
    if returned_value == [1, 7, 99]:
        print(f"OK!\t  expected returned value : [1, 7, 99], actual: {returned_value} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected returned value : [1, 7, 99], actual: {returned_value} \n ")
        error_count += 1

    c = [0]
    print(f"Test with {c}")
    returned_value = col.unique_values(c)
    if returned_value == [0]:
        print(f"OK!\t  expected returned value : [0], actual: {returned_value} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected returned value : [0], actual: {returned_value} \n ")
        error_count += 1

    d = []
    print(f"Test with {d}")
    returned_value = col.unique_values(d)
    if returned_value == []:
        print(f"OK!\t  expected returned value : [], actual: {returned_value} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected returned value : [], actual: {returned_value} \n ")
        error_count += 1

    e = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    print(f"Test with {e}")
    returned_value = col.unique_values(e)
    if returned_value == [5]:
        print(f"OK!\t  expected returned value : [5], actual: {returned_value} \n ")
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected returned value : [5], actual: {returned_value} \n ")
        error_count += 1




    print("~~~~~~~~Testing lists2dic~~~~~~~~\n")

    keys_a = ["a","b","c","d"]
    values_a = [1, 23, "ttt"]
    print(f"Test with keys: {keys_a}, values: {values_a}")
    new_dict = col.lists2dict(keys_a,values_a)
    if new_dict == {"a":1, "b":23, "c":"ttt"}:
        print("OK!\t expected returned dictionary: {\'a\': 1, \'b\': 23, \'c\': \'ttt\'}, actual:", new_dict, "\n")
        passed_tests += 1
    else:
        print("ERROR :-(!\t expected returned dictionary: {\'a\': 1, \'b\': 23, \'c\': \'ttt\'}, actual:", new_dict, "\n")
        error_count += 1

    keys_b = ["E","F","G"]
    values_b = ["John", 100, "Bryce","matrix"]
    print(f"Test with keys: {keys_b}, values: {values_b}")
    new_dict = col.lists2dict(keys_b,values_b)
    if new_dict == {"E": "John", "F": 100, "G": "Bryce"}:
        print("OK!\t expected returned dictionary: {\'E\': \'John\', \'F\': 100, \'G\': \'Bryce\'}, actual:", new_dict, "\n")
        passed_tests += 1
    else:
        print("ERROR :-(!\t expected returned dictionary: {\'E\': \'John\', \'F\': 100, \'G\': \'Bryce\'}, actual:", new_dict, "\n")
        error_count += 1

    keys_c = ["a","b","c","a"]
    values_c = [1, 23, "ttt",500, 400]
    print(f"Test with keys: {keys_c}, values: {values_c}")
    try:
        new_dict = col.lists2dict(keys_c,values_c)
        print(f"ERROR :-(!\t keys list has duplicates, the function should be unable to create a dictionary.\n "
              f"            expected: exception raise, actual: no exception raised\n")
        error_count += 1
    except:
        print(f"OK!\t  keys list has duplicates, the function should be unable to create a dictionary\n"
              f"      expected: exception raise, actual: exception raise   \n")
        passed_tests += 1

    keys_d = []
    values_d = []
    print(f"Test with keys: {keys_d}, values: {values_d}")
    new_dict = col.lists2dict(keys_d,values_d)
    if new_dict == {}:
        print("OK!\t expected returned dictionary: {}, actual:", new_dict, "\n")
        passed_tests += 1
    else:
        print("ERROR :-(!\t expected returned dictionary: {}, actual:", new_dict, "\n")
        error_count += 1

    keys_e = ["a"]
    values_e = []
    print(f"Test with keys: {keys_e}, values: {values_e}")
    new_dict = col.lists2dict(keys_e,values_e)
    if new_dict == {}:
        print("OK!\t expected returned dictionary: {}, actual:", new_dict, "\n")
        passed_tests += 1
    else:
        print("ERROR :-(!\t expected returned dictionary: {}, actual:", new_dict, "\n")
        error_count += 1

    keys_f = []
    values_f = [3]
    print(f"Test with keys: {keys_f}, values: {values_f}")
    new_dict = col.lists2dict(keys_f,values_f)
    if new_dict == {}:
        print("OK!\t expected returned dictionary: {}, actual:", new_dict, "\n")
        passed_tests += 1
    else:
        print("ERROR :-(!\t expected returned dictionary: {}, actual:", new_dict, "\n")
        error_count += 1



    print("~~~~~~~~Testing elems_count~~~~~~~~\n")

    a = ["apple","pear","banana","apple"]
    print(f"Test with {a}")
    returned_value = col.elems_count(a)
    if returned_value == {'apple':2, 'pear':1, 'banana':1}:
        print("OK!\t  expected returned value: {'apple': 2, 'pear': 1, 'banana': 1} actual: ",returned_value, "\n" )
        passed_tests += 1
    else:
        print(f"ERROR :-(\t expected returned value: {'apple':2, 'pear':1, 'banana':1} actual: ",returned_value, "\n" )
        error_count += 1

    b = ["tesla","tesla","tesla","microsoft"]
    print(f"Test with {b}")
    returned_value = col.elems_count(b)
    if returned_value == {'tesla':3, 'microsoft':1}:
        print("OK!\t  expected returned value: {'tesla':3, 'microsoft':1} actual: ",returned_value, "\n" )
        passed_tests += 1
    else:
        print("ERROR :-(\t expected returned value: {'tesla':3, 'microsoft':1} actual: ",returned_value, "\n" )
        error_count += 1

    c = []
    print(f"Test with {c}")
    returned_value = col.elems_count(c)
    if returned_value == {}:
        print("OK!\t  expected returned value: {} actual: ",returned_value, "\n" )
        passed_tests += 1
    else:
        print("ERROR :-(\t expected returned value: {} actual: ",returned_value, "\n" )
        error_count += 1

    d = ["the amount of brains i have"]
    print(f"Test with {d}")
    returned_value = col.elems_count(d)
    if returned_value == {'the amount of brains i have': 1}:
        print("OK!\t  expected returned value: {'the amount of brains i have': 1} actual: ",returned_value, "\n" )
        passed_tests += 1
    else:
        print("ERROR :-(\t expected returned value: {'the amount of brains i have': 1} actual: ",returned_value, "\n" )
        error_count += 1

    print(f"the number of errors: {error_count}")
    print(f"you passed {passed_tests} out of 15 tests")
    grade = passed_tests/15 * 100
    print(f"you grade is: {grade}")
    print("********************* Test col - End *********************\n\n")