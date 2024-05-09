"""File opening"""

# here's how we can open a file
try:
    file = open("test.txt", "w")
    try:
        file.write("abc")
    except:
        print("An error has occured")
    finally:
        file.close()
except OSError:
    print("File not found")

# a simple(r) way
with open("test.txt", "w") as file:
    file.write("123")
    file.close()