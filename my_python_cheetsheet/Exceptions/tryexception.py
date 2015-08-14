while True:
    try:
        value = int(input("Enter you number"))
        print(100/value)
        break
    except ValueError:
        print("Check again and Enter integer")
    except ZeroDivisionError:
        print("Cannot divide by zero ")
    except:
        break
    finally:
        print ("End of Loop")    
        