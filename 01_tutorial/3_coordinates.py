from manim import *
import numpy as np

class Coordinates(Scene):
    def construct(self):
        p1 = [-1, -1, 0]
        p2 = [1, -1, 0]
        p3 = [1, 1, 0]
        p4 = [-1, 1, 0]
        a = Line(p1, p2)\
            .append_points(Line(p2, p3).points)\
            .append_points(Line(p3, p4).points)
        point_start = a.get_start()
        point_center = a.get_center()
        point_end = a.get_end()
        point_top = a.get_top()
        point_bottom = a.get_bottom()
        point_half = a.point_from_proportion(0.5)

        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24)\
                 .to_edge(UR)\
                 .set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24)\
                 .next_to(self.mobjects[-1],DOWN)\
                 .set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24)\
                 .next_to(self.mobjects[-1],DOWN)\
                 .set_color(BLUE))

        self.add(Dot(point_start).set_color(YELLOW).scale(2))
        self.add(Dot(point_end).set_color(RED).scale(2))
        self.add(Dot(point_top).set_color(GREEN_A).scale(2))
        self.add(Dot(point_bottom).set_color(GREEN_D).scale(2))
        self.add(Dot(point_center).set_color(BLUE).scale(2))
        self.add(Dot(point_half).set_color(ORANGE).scale(2))
        self.add(*[Dot(x).set_color(PINK) for x in a.points])
        self.add(a)