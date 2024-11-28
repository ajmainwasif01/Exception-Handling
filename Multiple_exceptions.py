try:
    x1,x2 = eval(input("Enter two numbers and seperate them with comma: "))
    result = x1/x2
    print("Result is:" , result)

except ZeroDivisionError:
    print("Error! You have divided by 0")

except SyntaxError:
    print("Error! Your comma is missing.")

except:
    print("Wrong input")

finally:
    print("Thank You")