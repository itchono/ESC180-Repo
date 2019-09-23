# input()   the function on its own will pause the console and wait for the user to type in input and press enter
# however, on its own, it does basically nothing

# note that a function can return a value
# so we can do ex. x = input(); which assigns the value we got from input into x.

# see this example:
x = input()
print(x)  # this basically repeats back what you typed in


# you can also put a prompt in the input function in the form input("Message")

y = input("Please enter a value for y")
print(y)

# keep in mind that input returns a STRING type aka like a word. So, you can't directly perform math using something
# that you got from the input function

# print(3 + input("Enter a number")) will return an error
# so we use a CAST to "translate" the string into a datatype that we can work with

print(3 + int(input("Enter a number")))
