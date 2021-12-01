def dividable_by_10(num):
    return num%10 == 0


def sum_of_digits(num):
    num = abs(num)
    digit_sum = 0
    while num != 0:
        digit_sum+= num%10
        num = num//10
    return digit_sum


def num_length(num):
    num = abs(num)
    count = 0
    while num != 0:
        count+=1
        num = num//10
    return count


def is_palindrome(num):
    num = abs(num)
    for i in range(num_length(num)//2):
        left_dig = str(num)[i]
        right_dig = str(num)[num_length(num)-1-i]
        if left_dig!=right_dig:
            return False
    return True
