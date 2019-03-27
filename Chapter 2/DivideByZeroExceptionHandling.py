def divide(num):
    try:
        print( 100 / num )
    except ZeroDivisionError:
        print ("You cannot divide this number by zero!")

divide(10)
divide(0)