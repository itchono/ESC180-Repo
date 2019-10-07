# Week 4 Exercises

# ex 1
def name_checker():
    s = input("Please enter a string:\n")
    if (s.find("Mingde") == 0):
        print("How did you know my name?\n")
        # loweest index of substring must be 0 so that it begins with my name
    else:
        print("it's rude to not know my name.\n")

# ex 2
def number_length(num):
    l = len(str(num))
    print(num, "is a", l, "digit number")

def remover(s):
    print(s.replace('?',"").replace('!', ""))

if __name__ == "__main__":
    name_checker()
    s = input("Remove::")
    remover(s)
    for n in range(1, 10000, 10):
        number_length(n)