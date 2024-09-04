def circle(radius: float):
    area = 3.14 * radius * radius
    print(f"area of circle with radious {radius} = {area}")


def rectangle (length: float, breadth: float) -> None:
    area = length * breadth
    print(f"Area of rectangle = {area}")

def triangle(base:float, height:float) -> None:
    area = 0.5 *height *base
    print(f"Area of triangle = {area}")

print(__name__)
if __name__=="__main__":
    circle(34.54)
    triangle(100, 55)


