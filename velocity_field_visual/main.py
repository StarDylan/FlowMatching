from manim import Scene, Circle, Create, PINK, Text, Point, VGroup, Axes, Line, Arrow, ImageMobject
import numpy as np

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class CreateGaussian(Scene):
    def construct(self):

        noise = ImageMobject("noise.png")  # load the image

        # Randomly generate 100 points in a gaussian distribution
        for _ in range(1000):
            x = np.random.normal(0, 1)
            y = np.random.normal(0, 1)

            # Limit to within 3 of the center
            if np.sqrt(x**2 + y**2) > 3:
                continue

            point = Point(location=[x, y, 0], color=PINK)  # create a point at the random location
            self.add(point)


        # Create a list of circles to represent the points


        # Add some text to the scene
        text = Text("Gaussian Surface")
        self.play(Create(text))  # show the text on screen
        self.wait(2)