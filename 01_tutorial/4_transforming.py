from manim import *

class Transforming(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        a = Square().set_color(BLACK)
        a2 = Rectangle().set_color(BLACK).set_fill(GREEN, opacity=1).rotate(TAU/8)
        a3 = Square().set_color(BLACK)
        a4 = Square().set_color(RED).shift(LEFT * 2)
        b = Square().set_color(BLACK)
        b4 = Square().set_color(BLUE).shift(RIGHT * 2)

        self.play(Create(a))
        self.play(Transform(a, a2))
        self.play(Transform(a, a3))
        self.add(b)
        self.play(Transform(a, a4), Transform(b, b4))
        self.wait()