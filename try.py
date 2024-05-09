"""using try to add things"""

try:
    # get numbers then add
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    add = num1 + num2
    print(f"Result: {add}")
except:
    print("An error has occured!")
else:
    print("Done!")