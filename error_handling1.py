
num1 = input ("Enter your first number : ")

num2 = input ("Enter your second number : ")

try :
    result = int(num1) / int(num2)
except ValueError :
    print('A value error has just occured ')

else :
    print(result)