from graphics import circle,rectangle
from graphics.threedgraphics import cuboid as cub
from graphics.threedgraphics import sphere as sph

circle.areacircle(int(input("Enter the radius of circle:")))
circle.areaperimeter(int(input("Enter the radius of the circle")))

rectangle.arearectangle(int(input("Enter the length of the rectangle")),int(input("Enter the breadth of the rectangle")))
rectangle.rectangleperimeter(int(input("Enter the length of the rectangle")),int(input("Enter the breadth of the rectangle")))

cub.areacuboid()
cub.perimetercuboid()
sph.areasphere(int(input("Enter the radius of sphere:")))
sph.perimeterspher(int(input("Enter the radius of sphere:")))



