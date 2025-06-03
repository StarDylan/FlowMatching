from manim import Scene, Circle, Create, PINK, Text, Point, Group, Axes, Line, Arrow, ImageMobject, Add, AnimationGroup, VectorField, Dot, GRAY, LEFT, RIGHT, UP, ArrowVectorField
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

from manim import *

class EvolvingVectorField(Scene):
    def construct(self):
        # Axes setup
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": GREY},
        )
        self.add(axes)

        # Time tracker
        time_tracker = ValueTracker(0)

        # Vector field function that evolves over time
        def evolving_field_func(pos):
            x, y = pos[:2]
            t = time_tracker.get_value()
            return np.array([
                np.sin(y + t),
                np.cos(x - t),
                0
            ])

        # Always redraw the vector field
        vector_field = always_redraw(
            lambda: ArrowVectorField(
                evolving_field_func,
                x_range=[-5, 5, 1],
                y_range=[-3, 3, 1],
                colors=[BLUE, GREEN, YELLOW],
                vector_config={"stroke_width": 2},
            )
        )

        self.add(vector_field)

        # Animate time progression
        self.play(time_tracker.animate.increment_value(2 * PI), run_time=10, rate_func=linear)
