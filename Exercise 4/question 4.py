class NumberTriangle:
    def __init__(self, lines):
        self.lines = lines

    def print_triangle(self):
        for i in range(1, self.lines + 1):
            print(str(i) * i)

# Create an instance of the NumberTriangle class with 7 lines (as in the example)
triangle = NumberTriangle(7)

# Print the triangle
triangle.print_triangle()
