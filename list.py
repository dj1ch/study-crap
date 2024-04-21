"""
stuff to remember
"""

# list
dataList = ["Me", "Myself", "I"]

# tuple
dataTuple = ("Me", "Myself", "I")

# dict
dataDict = {
    "Person" : "Me",
    "Location" : "Somewhere"
}

# but we can also append and/or remove from the dataList
dataList.append("Someone")

# example
for x in dataList:
    print(x)

# or we can remove
dataList.pop(3)

# then this happens
print("\nModified output: ")
for x in dataList:
    print(x)

# dictionary example
print("\nDictionary: ")
for k, v in dataDict.items(): 
    print(f"\nKey: " + k.title())
    print(f"Value: " + v.title())