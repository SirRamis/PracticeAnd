class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x=0 , y=0):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point()
pt.set_coords(35,64)
print(pt.__dict__)
print(pt.get_coords())
