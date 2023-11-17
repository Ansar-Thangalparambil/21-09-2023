def areacuboid():
    l=int(input("length of the cuboid"))
    b=int(input("Breadth of the cuboid"))
    h=int(input("Height of the cuboid"))
    area=2*(l*b+b*h+l*h)
    print("Area of cuboid is:",area)

def perimetercuboid():
    l=int(input("length of the cuboid"))
    b=int(input("Breadth of the cuboid"))
    h=int(input("Height of the cuboid"))
    perimeter=4*(l+b+h)
    print("Perimeter of cuboid is",perimeter)
