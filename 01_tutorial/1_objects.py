from manim import *

class Objects(Scene):
    def construct(self):
        title = Text('Creating and displaying mobjects').to_edge(UP)
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)

        self.play(Transform(title, Text('Placing mobjects in relative move').to_edge(UP)))
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)
        self.remove(circle, square, triangle)
        self.wait(1)

        self.play(Transform(title, Text('Placing mobjects in absolute move').to_edge(UP)))
        circle.move_to(LEFT * 2)
        square.next_to(circle, LEFT)
        triangle.align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)
        self.remove(circle, square, triangle)
        self.wait(1)

        self.play(Transform(title, Text('Styling mobjects').to_edge(UP)))
        circle = Circle()\
            .shift(LEFT)\
            .set_stroke(color=GREEN, width=20)
        square = Square()\
            .shift(UP)\
            .set_fill(YELLOW, opacity=1.0)
        triangle = Triangle()\
            .shift(DOWN)\
            .set_fill(PINK, opacity=0.5)
        
        self.add(circle, square, triangle)
        self.wait(1)
        self.remove(circle, square, triangle)
        self.wait(1)

        self.play(Transform(title, Text('Screen order').to_edge(UP)))
        self.add(triangle, square, circle)
        self.wait(1)
        self.remove(triangle, square, circle)
        self.wait(1)

        self.play(Transform(title, Text('Animations').to_edge(UP)))
        square = Square().set_fill(WHITE, opacity=0.3)
        self.play(Create(square))
        self.play(square.animate.set_fill(WHITE, opacity=1))
        self.play(square.animate.shift(UP), runtime=1)
        self.play(square.animate.shift(DOWN * 2).rotate(PI / 3), run_time=1)
        self.play(square.animate.shift(UP).rotate(PI / 3), run_time=1)
        self.play(FadeOut(square))
