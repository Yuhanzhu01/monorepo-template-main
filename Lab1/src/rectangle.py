"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""

# Task 2
class Shape():
    def set_values(self, width, height):
        pass

class Rectangle(Shape):
    # Define the constructor for width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
    
    def set_values(self, x, y):
        self.width = x
        self.height = y

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
