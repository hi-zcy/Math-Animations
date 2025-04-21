# StepOne_DrawCircleAndPoints

from manim import *

class StepOne_DrawCircleAndPoints(Scene):
    def construct(self):
        # 创建一个圆
        circle = Circle(radius=2).shift(LEFT * 2)
        self.play(Create(circle))
        self.wait(1)

        # 标记圆心 O
        O = Dot(circle.get_center())
        O_label = Text("O").next_to(O, UP)
        self.play(Create(O), Write(O_label))
        self.wait(1)

        # 构造两圆交点来确定垂直点 V
        # 画一个辅助圆来找到一个垂直点
        aux_circle1 = Circle(radius=2).shift(LEFT * 2 + UP * 2)
        self.play(Create(aux_circle1))
        self.wait(1)

        # 画另一个辅助圆来找到垂直点
        aux_circle2 = Circle(radius=2).shift(LEFT * 2 + DOWN * 2)
        self.play(Create(aux_circle2))
        self.wait(1)

        # 找到两个辅助圆的交点之一作为 V
        V = Dot(circle.point_at_angle(0))  # 这里只是一个示例点，实际应用中需要找到两个辅助圆的交点
        V_label = Text("V").next_to(V, RIGHT)
        self.play(Create(V), Write(V_label))
        self.wait(1)

        # 画出与 OV 垂直的半径 OA
        OA = Line(circle.get_center(), circle.point_at_angle(PI/2))
        A = Dot(OA.get_end())
        A_label = Text("A").next_to(A, UP)
        self.play(Create(OA))
        self.play(Create(A), Write(A_label))
        self.wait(1)