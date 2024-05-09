"""
stuff to remember
"""

# list
dataList = ["Me", "Myself", "I"]

# tuple
# however we cannot modify this
dataTuple = ("Me", "Myself", "I")
dataTupleInt = ("1", "2", "3")

# dict
dataDict = {
    "Person" : "Me",
    "Location" : "Somewhere"
}

# but we can also append and/or remove from the dataList
dataList.append("Someone")

# example
print("List: ", dataList)

# or
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

# tuple example
print("\nTuple: ", dataTuple)

# or 
for x in dataTuple:
    print(x)