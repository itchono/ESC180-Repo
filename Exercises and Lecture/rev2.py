print("hello world")# this program converts word numbers into numeric form and vice versa

def word_num_to_int(s):
    d = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
         "ten": 10}

    if s in d:
        return d[(str(s)).casefold()]
    else:
        return -1


def int_to_word(n):
    d = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
         "ten": 10}

    k = list(d.keys())
    if n in d.values():
        return k[n]
    else:
        return "ERROR"


def main():
    s = input("Hello!\nPlease enter a word to convert to an int\n")
    print(s, "is equal to", word_num_to_int(s))
    b = int(input("now, input a numeric to convert to word\n"))
    print(b, "is equal to", int_to_word(b))



main()