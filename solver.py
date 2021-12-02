# the variable 'number_control' is just for making sure that the user input is under 13
number_control = 1
import random
import operator 
#this is a dictionary of strings to operators to allow me to convert the strings to operators later
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv, 
}
#this is where the user inputs their numbers and the code checks it is under 13

while number_control == 1:
  num1 = int(input('Enter your value \n'))
  num2 = int(input('Enter your value \n'))
  num3 = int(input('Enter your value \n'))
  num4 = int(input('Enter your value \n'))
  print("")
  print("--------------------------------------------")
  
  if num1 > 13 or num1 < 1 or num2 > 13 or num2 < 1 or num3 > 13 or num3 < 1 or num4 > 13 or num4 < 1:
    print("Your numbers must be between 1 and 13!")
  else:
    number_control = 2

#it checks 1000 combinations of a1 -> b1 -> c1


for count in range(1,10000):
  #declars the 2 sets of data so they can be chosen from at random
  numbers = [num1, num2, num3, num4]
  symbols = ['+', '-', '*', '/']
  macros = []
  
  #selects the randomised order of the numbers and then removes them from variable 'numbers' to leave it as an empty array
  first = random.choice(numbers)
  numbers.remove(first)
  second = random.choice(numbers)
  numbers.remove(second)
  third = random.choice(numbers)
  numbers.remove(third)
  fourth = random.choice(numbers)
  numbers.remove(fourth)
  #selects the randomised order of the symbols and then removes them from the array to leave it empty
  a = random.choice(symbols)
  #symbols.remove(a)
  b = random.choice(symbols)
  #symbols.remove(b)
  c = random.choice(symbols)
  #symbols.remove(c)
  
  #now it rebuilds the variable 'numbers', adding in the symbols that will later be turned into operators by the packege 'operator'
  numbers.append("((")
  numbers.append(first)
  numbers.append(a)
  numbers.append(second)
  numbers.append(")")
  numbers.append(b)
  numbers.append(third)
  numbers.append(")")
  numbers.append(c)
  numbers.append(fourth)
  #this is the primary code. There are 4 of them, each being a differnt combination of pairs and orders of the brackets.
  if a == '+':
    a1 = ops['+'](first, second)
    macros.append("1 q 2")
  elif a == '-':
    a1 = ops['-'](first, second)
    macros.append("1 w 2")
  elif a == '*':
    a1 = ops['*'](first, second)
    macros.append("1 e 2")
  elif a == '/':
    a1 = ops['/'](first, second)
    macros.append("1 r 2")

  if b == '+':
    b1 = ops['+'](a1, third)
    macros.append("2 q 3")
  elif b == '-':
    b1 = ops['-'](a1, third)
    macros.append("2 w 3")
  elif b == '*':
    b1 = ops['*'](a1, third)
    macros.append("2 e 3")
  elif b == '/':
    b1 = ops['/'](a1, third)
    macros.append("2 r 3")

  if c == '+':
    c1 = ops['+'](b1, fourth)
    macros.append("3 q 4")
  elif c == '-':
    c1 = ops['-'](b1, fourth)
    macros.append("3 w 4")
  elif c == '*':
    c1 = ops ['*'](b1, fourth)
    macros.append("3 e 4")
  elif c == '/':
    c1 = ops['/'](b1, fourth)
    macros.append("3 r 4")

  numbers = str(numbers)
  numbers = numbers.strip('[]')
  macros = str(macros)
  macros = macros.strip('[]')
  if c1 == 24.0:
    print(numbers)
    print(macros, "\n")
    break

#checks 1000 combinations of b1 -> a1 -> c1
for count in range(1, 10000):
  numbers = [num1, num2, num3, num4]
  symbols = ['+', '-', '*', '/']
  macros = []
  first = random.choice(numbers)
  numbers.remove(first)
  second = random.choice(numbers)
  numbers.remove(second)
  third = random.choice(numbers)
  numbers.remove(third)
  fourth = random.choice(numbers)
  numbers.remove(fourth)
  
  a = random.choice(symbols)
  #symbols.remove(a)
  b = random.choice(symbols)
  #symbols.remove(b)
  c = random.choice(symbols)
  #symbols.remove(c)
  
  numbers.append("(")
  numbers.append(first)
  numbers.append(a)
  numbers.append("(")
  numbers.append(second)
  numbers.append(b)
  numbers.append(third)
  numbers.append("))")
  numbers.append(c)
  numbers.append(fourth)

  if b == '+':
    b1 = ops['+'](second, third)
    macros.append("2 q 3")
  elif b == '-':
    b1 = ops['-'](second, third)
    macros.append("2 w 3")
  elif b == '*':
    b1 = ops['*'](second, third)
    macros.append("2 e 3")
  elif b == '/':
    b1 = ops['/'](second, third)
    macros.append("2 r 3")

  if a == '+':
    a1 = ops['+'](first, b1)
    macros.append("1 q 3")
  elif a == '-':
    a1 = ops['-'](first, b1)
    macros.append("1 w 3")
  elif a == '*':
    a1 = ops['*'](first, b1)
    macros.append("1 e 3")
  elif a == '/' and b1 != 0:
    a1 = ops['/'](first, b1)
    macros.append("1 r 3")

  if c == '+':
    c1 = ops['+'](a1, fourth)
    macros.append("3 q 4")
  elif c == '-':
    c1 = ops['-'](a1, fourth)
    macros.append("3 w 4")
  elif c == '*':
    c1 = ops ['*'](a1, fourth)
    macros.append("3 e 4")
  elif c == '/':
    c1 = ops['/'](a1, fourth)
    macros.append("3 r 4")

  numbers = str(numbers)
  numbers = numbers.strip('[]')

  macros = str(macros)
  macros = macros.strip('[]')
  if c1 == 24.0:
    print(numbers)
    print(macros, "\n")
    break
  

#checks 1000 combinations of b1 -> c1 ->a1
for count in range(1,10000):
  numbers = [num1, num2, num3, num4]
  symbols = ['+', '-', '*', '/']
  macros = []
  
  first = random.choice(numbers)
  numbers.remove(first)
  second = random.choice(numbers)
  numbers.remove(second)
  third = random.choice(numbers)
  numbers.remove(third)
  fourth = random.choice(numbers)
  numbers.remove(fourth)
  
  a = random.choice(symbols)
  #symbols.remove(a)
  b = random.choice(symbols)
  #symbols.remove(b)
  c = random.choice(symbols)
  #symbols.remove(c)
  
  
  numbers.append(first)
  numbers.append(a)
  numbers.append("((")
  numbers.append(second)
  numbers.append(b)
  numbers.append(third)
  numbers.append(")")
  numbers.append(c)
  numbers.append(fourth)
  numbers.append(")")


  if b == '+':
    b1 = ops['+'](second, third)
    macros.append("2 q 3")
  elif b == '-':
    b1 = ops['-'](second, third)
    macros.append("2 w 3")
  elif b == '*':
    b1 = ops['*'](second, third)
    macros.append("2 e 3")
  elif b == '/':
    b1 = ops['/'](second, third)
    macros.append("2 r 3")

  if c == '+':
    c1 = ops['+'](b1, fourth)
    macros.append("3 q 4")
  elif c == '-':
    c1 = ops['-'](b1, fourth)
    macros.append("3 w 4")
  elif c == '*':
    c1 = ops ['*'](b1, fourth)
    macros.append("3 e 4")
  elif c == '/':
    c1 = ops['/'](b1, fourth)
    macros.append("3 r 4")

  if a == '+':
    a1 = ops['+'](first, c1)
    macros.append("1 q 4")
  elif a == '-':
    a1 = ops['-'](first, c1)
    macros.append("1 w 4")
  elif a == '*':
    a1 = ops['*'](first, c1)
    macros.append("1 e 4")
  elif a == '/' and c1 != 0:
    a1 = ops['/'](first, c1)
    macros.append("1 r 4")

  numbers = str(numbers)
  numbers = numbers.strip('[]')
  macros = str(macros)
  macros = macros.strip('[]')
  if a1 == 24.0:
    print(numbers)
    print(macros, "\n")
    break

#checks 1000 combinations of a1 -> c1 -> b1
for count in range (1,10000):
  numbers = [num1, num2, num3, num4]
  symbols = ['+', '-', '*', '/']
  macros = []

  first = random.choice(numbers)
  numbers.remove(first)
  second = random.choice(numbers)
  numbers.remove(second)
  third = random.choice(numbers)
  numbers.remove(third)
  fourth = random.choice(numbers)
  numbers.remove(fourth)
  
  a = random.choice(symbols)
  #symbols.remove(a)
  b = random.choice(symbols)
  #symbols.remove(b)
  c = random.choice(symbols)
  #symbols.remove(c)
  
  numbers.append("(")
  numbers.append(first)
  numbers.append(a)
  numbers.append(second)
  numbers.append(")")
  numbers.append(b)
  numbers.append("(")
  numbers.append(third)
  numbers.append(c)
  numbers.append(fourth)
  numbers.append(")")

  if a == '+':
    a1 = ops['+'](first, second)
    macros.append("1 q 2")
  elif a == '-':
    a1 = ops['-'](first, second)
    macros.append("1 w 2")
  elif a == '*':
    a1 = ops['*'](first, second)
    macros.append("1 e 2")
  elif a == '/':
    a1 = ops['/'](first, second)
    macros.append("1 r 2")

  if c == '+':
    c1 = ops['+'](third, fourth)
    macros.append("3 q 4")
  elif c == '-':
    c1 = ops['-'](third, fourth)
    macros.append("3 w 4")
  elif c == '*':
    c1 = ops ['*'](third, fourth)
    macros.append("3 e 4")
  elif c == '/':
    c1 = ops['/'](third, fourth)
    macros.append("3 r 4")

  if b == '+':
    b1 = ops['+'](a1, c1)
    macros.append("2 q 4")
  elif b == '-':
    b1 = ops['-'](a1, c1)
    macros.append("2 w 4")
  elif b == '*':
    b1 = ops['*'](a1, c1)
    macros.append("2 e 4")
  elif b == '/' and c1 != 0:
    b1 = ops['/'](a1, c1)
    macros.append("2 r 4")

  numbers = str(numbers)
  macros = str(macros)
  macros = macros.strip('[]')
  if b1 == 24.0:
    print(numbers)
    print(macros, "\n")
    break


#checks 1000 combinations of c1 -> b1(reversed) -> a1
for count in range(1, 10000):
  numbers = [num1, num2, num3, num4]
  symbols = ['+', '-', '*', '/']
  macros = []

  first = random.choice(numbers)
  numbers.remove(first)
  second = random.choice(numbers)
  numbers.remove(second)
  third = random.choice(numbers)
  numbers.remove(third)
  fourth = random.choice(numbers)
  numbers.remove(fourth)
  
  a = random.choice(symbols)
  #symbols.remove(a)
  b = random.choice(symbols)
  #symbols.remove(b)
  c = random.choice(symbols)
  #symbols.remove(c)
  
  numbers.append(first)
  numbers.append(a)
  numbers.append("(")
  numbers.append(second)
  numbers.append(b)
  numbers.append("(")
  numbers.append(third)
  numbers.append(c)
  numbers.append(fourth)
  numbers.append("))")

  if c == '+':
    c1 = ops['+'](third, fourth)
    macros.append("3 q 4")
  elif c == '-':
    c1 = ops['-'](third, fourth)
    macros.append("3 w 4")
  elif c == '*':
    c1 = ops ['*'](third, fourth)
    macros.append("3 e 4")
  elif c == '/' and fourth != 0:
    c1 = ops['/'](third, fourth)
    macros.append("3 r 4")

  if b == '+':
    b1 = ops['+'](second, c1)
    macros.append("2 q 4")
  elif b == '-':
    b1 = ops['-'](second, c1)
    macros.append("2 w 4")
  elif b == '*':
    b1 = ops['*'](second, c1)
    macros.append("2 e 4")
  elif b == '/' and c1 !=0:
    b1 = ops['/'](second, c1)
    macros.append("2 r 4")

  if a == '+':
    a1 = ops['+'](first, b1)
    macros.append("1 q 4")
  elif a == '-':
    a1 = ops['-'](first, b1)
    macros.append("1 w 4")
  elif a == '*':
    a1 = ops['*'](first, b1)
    macros.append("1 e 4")
  elif a == '/' and b1 != 0:
    a1 = ops['/'](first, b1)
    macros.append("1 r 4")

  numbers = str(numbers)
  numbers = numbers.strip('[]')
  macros = str(macros)
  macros = macros.strip('[]')
  if a1 == 24.0:
    print(numbers)
    print(macros, "\n")
    break
