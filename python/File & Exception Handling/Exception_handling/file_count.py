def count_lines(file):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        file = input("enter corrrect file name : ")
        count = count_lines(file)
        return count
    else:
        lines = f.readlines()
        c = len(lines)
        return c


# print(count_lines("File & Exception Handling/d2.txt"))


def count_words(file):
    f = open(file, "r")
    data = f.read()
    list_words = data.split()
    return len(list_words)


count_words("File & Exception Handling/d2.txt")


def count_word(file, word):
    f = open(file, "r")
    data = f.read()
    data.count(word)


data = "python is fun"
print(data.count("fun"))
