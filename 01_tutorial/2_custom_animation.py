from manim import *

# Should override interpolate_mobject(alpha)
class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs):
        super().__init__(number, **kwargs)
        self._start = start
        self._end = end

    def interpolate_mobject(self, alpha: float) -> None:
        value = self._start + (alpha * (self._end - self._start))
        self.mobject.set_value(value)

class CustomAnimation(Scene):
    def construct(self):
        number = DecimalNumber().set_color(WHITE).scale(5)
        number.add_updater(lambda number: number.move_to(ORIGIN))
        self.add(number)
        self.play(Count(number, 0, 100), run_time=3, rate_func=linear)
        self.wait(1)
        self.remove(number)
        self.wait(1)