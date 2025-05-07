from manim import Scene, Circle, Create, PINK, Text, Point, Group, Axes, Line, Arrow, ImageMobject, Add, AnimationGroup
import numpy as np

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class CreateGaussian(Scene):
    def construct(self):

        # Randomly generate 100 points in a gaussian distribution
        number_of_points = 5000
        for i in range(number_of_points):
            x = np.random.normal(0, 1)
            y = np.random.normal(0, 1)

            # Limit to within 3 of the center
            if np.sqrt(x**2 + y**2) > 3:
                continue

            point = Point(location=[x, y, 0], color=PINK)  # create a point at the random location
            self.add(point)

            if i % (number_of_points / 2) == 0:
                self.wait(0.2)

        
        self.wait(2)

        point = Point(location=[1.7, -0.4, 0], color=PINK)  # create a point at the random location
        self.add(point)

        noise = ImageMobject("noise.png")  # load the image
        noise.scale(0.3)
        noise.move_to([4, 0, 0])
        noise.z_index = 1

        # Add line from image to a random point
        line = Line(start=noise.get_center(), end=point.get_center(), color=PINK)
        # Create both line and nosie
        self.add(noise)
        self.play(AnimationGroup(Create(line), Add(noise)))
        self.wait(2)


        self.wait(2)