from manim import *

class Quickstart(Scene):
    def construct(self):
        # Animating a circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))

        # Transforming a circle into a square
        square = Square()
        square.set_fill(BLUE, opacity=1)
        square.rotate(PI / 4)
        self.play(Transform(circle, square))
        self.play(FadeOut(square))

        # Positioning Mobject
        triangle = Triangle()
        triangle.next_to(square, RIGHT, buff=0.5)
        self.play(Create(triangle))

        # .animate syntax
        self.play(triangle.animate.set_fill(GREEN, opacity=0.7))
        self.play(triangle.animate.shift(UP))
        self.play(triangle.animate.rotate(TAU / 2))
        self.play(triangle.animate.shift(2 * DOWN))
        self.play(triangle.animate.flip())
        self.play(triangle.animate.shift(UP))