# (I)Cabinets and Boxes are objects that are mostly in cubic shape.

height = int(input("Enter Height: "))
width = int(input("Enter Width: "))
depth = int(input("Enter Depth: "))

volume = height * width * depth

if (volume >= 1) and (volume <= 10):
    print("Extra Small")
elif (volume >= 11) and (volume <= 25):
    print("Small")
elif (volume >= 26) and (volume <= 75):
    print("Medium")
elif (volume >= 76) and (volume <= 100):
    print("Large")
elif (volume >= 101) and (volume <= 250):
    print("Extra Large")
elif volume >= 251:
    print("Extra-Extra Large")    
