# if its your first time start with this
print("hello world")
# now learn about input
input("whats your name")
# if statements and variables
run = True
if run == True:
    print("hi")
# now lets combine our knowledge
print("Whats your name")
name = input("")
print("Hello, " + name)
print(3//2)


def fizzbuzz(num):


print('What is age?')
age = int(input('number:'))  # user gives number as input
if num % 3 == 0:
    print('fizz')
elif num % 5 == 0:
    print('buzz')
elif num % 5 == 0 and num % 3 == 0:
    print('fizzbuzz')
else:
    print('still underage')

fizzbuzz(15)

"""Example function returning string interpolation of parameters."""
def function_example(param_one, param_two):
	my_str = f"What a splendid function! I've got my {param_one} and {param_two}"
  return my_str
