import math

class Point(object):
    """Represents a 2D point."""
class Circle(object):
    """Represents center and radius."""
class Rectangle(object):
    """Represents width, height and center."""

circle_center = Point()
circle_center.x = 0
circle_center.y = 0

circle = Circle()
circle.radius = 100

box = Rectangle()
box.center = Point()
box.center.x = 140
box.center.y = 0
box.width = 100
box.height = 200
box.lower_left_corner = Point()
box.lower_left_corner.x = box.center.x - (box.width/2)
box.lower_left_corner.y = box.center.y - (box.height/2)
box.lower_right_corner = Point()
box.lower_right_corner.x = box.center.x + (box.width/2)
box.lower_right_corner.y = box.center.y - (box.height/2)
box.upper_left_corner = Point()
box.upper_left_corner.x = box.center.x - (box.width/2)
box.upper_left_corner.y = box.center.y + (box.height/2)
box.upper_right_corner = Point()
box.upper_right_corner.x = box.center.x + (box.width/2)
box.upper_right_corner.y = box.center.y + (box.height/2)

def point_in_circle(x,y):
    """Determines if point is inside circle."""
    if (circle_center.x - circle.radius) < x < (circle_center.x + circle.radius) and (circle_center.y - circle.radius) < y < (circle_center.y + circle.radius):
        return True
    return False

def rect_in_circle():
    """Determines if rectangle is in circle."""
    distance = math.sqrt(((box.center.x - circle_center.x) ** 2) + ((box.center.y - circle_center.y) ** 2))
    if distance < circle.radius:
        lower_distance = math.sqrt(((box.lower_left_corner.x - circle_center.x) ** 2) + ((box.lower_left_corner.y - circle_center.y) ** 2))
        upper_distance = math.sqrt(((box.upper_right_corner.x - circle_center.x) ** 2) + ((box.upper_right_corner.y - circle_center.y) ** 2))
        if lower_distance <= circle.radius and upper_distance <= circle.radius:
            return True
    return False

def rect_circle_corner_overlap():
    """Determines if a rectangle corner is in circle."""
    lower_left_distance = math.sqrt(((box.lower_left_corner.x - circle_center.x) ** 2) + ((box.lower_left_corner.y - circle_center.y) ** 2))
    lower_right_distance = math.sqrt(((box.lower_right_corner.x - circle_center.x) ** 2) + ((box.lower_right_corner.y - circle_center.y) ** 2))
    upper_left_distance = math.sqrt(((box.upper_left_corner.x - circle_center.x) ** 2) + ((box.upper_left_corner.y - circle_center.y) ** 2))
    upper_right_distance = math.sqrt(((box.upper_right_corner.x - circle_center.x) ** 2) + ((box.upper_right_corner.y - circle_center.y) ** 2))
    if circle.radius >= lower_left_distance:
        return True
    elif circle.radius >= lower_right_distance:
        return True
    elif circle.radius >= upper_left_distance:
        return True
    elif circle.radius >= upper_right_distance:
        return True
    return False

print("Example of point outside circle:          " + str(point_in_circle(50,150)))
print("Example of point in circle:               " + str(point_in_circle(100,150)))
print("Rectangle in circle:                      " + str(rect_in_circle()))
print("One(-plus) rectangle corner(s) in circle: " + str(rect_circle_corner_overlap()))