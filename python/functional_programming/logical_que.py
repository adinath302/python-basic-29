# python logical que -


# last -
# globle keyword
# return staement

# today -
# practice
# lambda function -

# ------------------------------------------


# ---------------------------------------
# que - wap to check no is even or not
def is_even(num):
    return num % 2 == 0


# x = is_even(24)
# print(x)


# ---------------------------------------
# que - wap to count total count number of char in string
def is_char(stri):
    count = 0
    for i in stri:
        if i.isspace():
            continue  # it will skip the space between words
        count = count + 1
    return count


# print(is_char("pintus"))  # 6
# print(is_char("rekha gupta"))  # 11


# ---------------------------------------
# que - wap to count perticular character in string
def count_char(str, chr):
    count1 = 0
    for k in str:
        if k == chr:
            count1 = count1 + 1
    return count1


x = count_char("hello world", "o")

# print(x)

# ---------------------------------------
# find char


def find_char(str, ch):
    for o in str:
        if o == ch:
            return True
    return False


# print(find_char("hello world", "o"))
# print(find_char("hello world", "i"))

# ---------------------------------------
# return max number


def max_number(num):
    n = 0
    for i in num:
        if i > n:
            n = i
    return n


# print(max_number([1,2,34,543,576,78,232,3]))

# ---------------------------------------


def min(list):
    min = list[0]
    for num in list:
        if num < min:
            min = num
    return min


# print(min([2,34,543,576,78,232,3]))


# ---------------------------------------
#
def frq(word):
    f = {}
    for char in word:
        if char not in f:
            f[char] = 1
        else:
            f[char] = f[char] + 1  # this is a dict method
    return f


# print(frq('hello world'))

# ---------------------------------------
# revision -


def half(num):
    res = num / 2
    return res


# print(half(24))  # 12 half of 24

# --------------------------------------------
# reverse word without slicing -


def reverse(word):
    rev = ""
    for char in word:
        rev = char + rev
    return rev


print(reverse("hello world"))
# --------------------------------------------

# timeframe - 52:26
