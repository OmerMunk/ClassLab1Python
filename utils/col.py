def unique_values(list1):
    return list(dict.fromkeys(list1))


def lists2dict(keys_list, values_list):
    if keys_list != unique_values(keys_list):
        raise Exception("There are duplicates in the keys list, cannot create the dictionary")
    new_dict={}
    dict_length = min(len(keys_list),len(values_list))
    for i in range(dict_length):
        new_dict.update({keys_list[i]:values_list[i]})
    return new_dict


def elems_count(list1):
    new_dict = {}
    for i in range(len(list1)):
        if list1[i] in new_dict.keys():
            new_dict[list1[i]] +=1
        else:
            new_dict.update({list1[i]:1})
    return new_dict

