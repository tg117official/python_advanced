from pl2 import div

try :
    x = int(input("Enter x : "))
    y = int(input("Enter y : "))
    print(div(x,y))
except ZeroDivisionError as error :
    print("Error Occured ZeroDivision: ")
except ValueError as error :
    print("Error Occured ValueError: ")
except Exception as error :
    print("Error Occured UnexpectedError")
else :
    print("Program Executed Successfully !!!")
finally:
    print("I don't care, i'll get executed Anyways !!")

