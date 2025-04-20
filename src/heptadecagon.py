from manim import *
import math
import numpy as np


class ConstructHeptadecagon(Scene):
    def construct(self):
        # 初始化所有属性
        self.jp1_line = None
        self.je_line = None
        self.jf_line = None
        self.semicircle = None
        self.arc = None
        self.perpendicular = None

        # 执行构造步骤
        self.setup_circle_and_points()
        self.construct_diameter()
        self.construct_j_point()
        self.construct_e_point()
        self.construct_f_point()
        self.construct_k_point()
        self.construct_n4_point()
        self.construct_p4_point()
        self.complete_heptadecagon()
        self.cleanup_construction()

    def setup_circle_and_points(self):
        """步骤1：创建初始圆和中心点"""
        self.circle = Circle(radius=3, color=WHITE)
        self.center = Dot(ORIGIN, color=YELLOW)
        self.play(Create(self.circle), Create(self.center))
        self.center_label = Text("O").next_to(self.center, DOWN)
        self.play(Write(self.center_label))
        self.wait()

    def construct_diameter(self):
        """步骤2：绘制直径和垂直半径"""
        # 水平直径
        self.p1 = Dot(self.circle.point_at_angle(0), color=RED)
        self.p1_label = Text("P₁").next_to(self.p1, RIGHT)
        self.diameter = Line(LEFT * 3, RIGHT * 3, color=BLUE)

        # 垂直直径
        self.p2 = Dot(self.circle.point_at_angle(PI / 2), color=GREEN)
        self.vertical = Line(UP * 3, DOWN * 3, color=BLUE)

        self.play(
            Create(self.diameter),
            Create(self.vertical),
            FadeIn(self.p1),
            FadeIn(self.p2),
            Write(self.p1_label)
        )
        self.wait()

    def construct_j_point(self):
        """步骤3：构造J点（OB的四等分点）"""
        o = self.center.get_center()
        b = self.p2.get_center()

        # 显示四等分过程
        for i in [0.25, 0.5, 0.75]:
            tick = Dot(o + (b - o) * i, color=YELLOW)
            self.play(FadeIn(tick), run_time=0.3)
            self.play(FadeOut(tick))

        # 确定J点（第一个四等分点）
        self.j_point = Dot(o + (b - o) * 0.25, color=PURPLE)
        self.j_label = Text("J").next_to(self.j_point, LEFT)
        self.play(FadeIn(self.j_point), Write(self.j_label))
        self.wait()

    def construct_e_point(self):
        """步骤4：构造E点（角OJP1的四等分线）"""
        j = self.j_point.get_center()
        o = self.center.get_center()
        p1 = self.p1.get_center()

        # 连接JP1
        self.jp1_line = Line(j, p1, color=GREEN)
        self.play(Create(self.jp1_line))
        self.wait()

        # 计算角OJP1的四等分线方向
        angle = self.calculate_angle(o, j, p1)
        quarter_angle = angle / 4
        direction = np.array([
            math.cos(quarter_angle + PI / 2),
            math.sin(quarter_angle + PI / 2),
            0
        ])

        # 确定E点位置
        e_pos = j + direction * 2
        self.e_point = Dot(e_pos, color=ORANGE)
        self.e_label = Text("E").next_to(self.e_point, UP)
        self.je_line = Line(j, e_pos, color=YELLOW)

        self.play(
            FadeIn(self.e_point),
            Write(self.e_label),
            Create(self.je_line)
        )
        self.wait()

    def construct_f_point(self):
        """步骤5：构造F点（45度角点）"""
        j = self.j_point.get_center()
        e = self.e_point.get_center()

        # 计算EJ向量
        ej_dir = (e - j) / np.linalg.norm(e - j)
        perp_dir = np.array([-ej_dir[1], ej_dir[0], 0])  # 垂直向量

        # 构造45度方向
        f_dir = (ej_dir + perp_dir) / np.linalg.norm(ej_dir + perp_dir)
        f_pos = j + f_dir * 2

        self.f_point = Dot(f_pos, color=PINK)
        self.f_label = Text("F").next_to(self.f_point, DOWN)
        self.jf_line = Line(j, f_pos, color=PINK)

        self.play(
            FadeIn(self.f_point),
            Write(self.f_label),
            Create(self.jf_line)
        )
        self.wait()

    def construct_k_point(self):
        """步骤6：构造K点（FP1为直径的半圆与OB的交点）"""
        f = self.f_point.get_center()
        p1 = self.p1.get_center()

        # 构造半圆
        fp1_mid = (f + p1) / 2
        radius = np.linalg.norm(f - p1) / 2
        self.semicircle = Arc(
            radius=radius,
            start_angle=PI,
            angle=PI,
            arc_center=fp1_mid,
            color=GREEN
        )
        self.play(Create(self.semicircle))

        # 计算与OB的交点
        ob_line = Line(self.center.get_center(), self.p2.get_center())
        k_pos = self.find_intersection(self.semicircle, ob_line)

        self.k_point = Dot(k_pos, color=TEAL)
        self.k_label = Text("K").next_to(self.k_point, LEFT)
        self.play(FadeIn(self.k_point), Write(self.k_label))
        self.wait()

    def construct_n4_point(self):
        """步骤7：构造N4点（以E为圆心，EK为半径的圆与OP1的交点）"""
        e = self.e_point.get_center()
        k = self.k_point.get_center()

        # 构造圆
        ek_radius = np.linalg.norm(e - k)
        self.arc = Circle(radius=ek_radius, color=ORANGE).move_to(e)
        self.play(Create(self.arc))

        # 计算与OP1的交点
        n4_pos = self.find_intersection(self.arc, self.diameter)

        self.n4_point = Dot(n4_pos, color=MAROON)
        self.n4_label = Text("N₄").next_to(self.n4_point, DOWN)
        self.play(FadeIn(self.n4_point), Write(self.n4_label))
        self.wait()

    def construct_p4_point(self):
        """步骤8：构造P4点（N4的垂线与圆的交点）"""
        # 构造垂线
        self.perpendicular = Line(
            self.n4_point.get_center(),
            self.n4_point.get_center() + UP * 3,
            color=PURPLE
        )
        self.play(Create(self.perpendicular))

        # 计算与圆的交点
        p4_pos = self.find_circle_line_intersection(
            self.circle,
            self.n4_point.get_center(),
            UP
        )

        self.p4_point = Dot(p4_pos, color=RED)
        self.p4_label = Text("P₄").next_to(self.p4_point, UP)
        self.play(FadeIn(self.p4_point), Write(self.p4_label))
        self.wait()

    def complete_heptadecagon(self):
        """步骤9：完成正十七边形"""
        # 创建所有顶点
        self.vertices = []
        for i in range(17):
            angle = i * 2 * PI / 17
            point = self.circle.point_at_angle(angle)
            self.vertices.append(Dot(point, color=RED))

        # 创建边
        self.edges = []
        for i in range(17):
            start = self.vertices[i].get_center()
            end = self.vertices[(i + 1) % 17].get_center()
            self.edges.append(Line(start, end, color=YELLOW))

        # 添加标签
        self.vertex_labels = []
        for i in range(17):
            if i in [0, 4]: continue  # 跳过已标记的点
            angle = i * 2 * PI / 17
            pos = UP
            if angle > 7 * PI / 4 or angle < PI / 4:
                pos = RIGHT
            elif PI / 4 <= angle < 3 * PI / 4:
                pos = UP
            elif 3 * PI / 4 <= angle < 5 * PI / 4:
                pos = LEFT
            else:
                pos = DOWN

            label = Text(f"P{i + 1}", font_size=24).next_to(
                self.vertices[i], pos, buff=0.1
            )
            self.vertex_labels.append(label)

        # 显示动画
        self.play(LaggedStart(
            *[FadeIn(v) for v in self.vertices[1:] if v not in [self.p1, self.p4_point]],
            lag_ratio=0.1
        ))
        self.play(LaggedStart(
            *[Write(l) for l in self.vertex_labels],
            lag_ratio=0.1
        ))
        self.play(LaggedStart(
            *[Create(e) for e in self.edges],
            lag_ratio=0.1
        ))
        self.wait()

    def cleanup_construction(self):
        """清理辅助元素"""
        to_remove = []
        if hasattr(self, 'jp1_line'): to_remove.append(self.jp1_line)
        if hasattr(self, 'je_line'): to_remove.append(self.je_line)
        if hasattr(self, 'jf_line'): to_remove.append(self.jf_line)
        if hasattr(self, 'semicircle'): to_remove.append(self.semicircle)
        if hasattr(self, 'arc'): to_remove.append(self.arc)
        if hasattr(self, 'perpendicular'): to_remove.append(self.perpendicular)
        if hasattr(self, 'j_point'): to_remove.append(self.j_point)
        if hasattr(self, 'e_point'): to_remove.append(self.e_point)
        if hasattr(self, 'f_point'): to_remove.append(self.f_point)
        if hasattr(self, 'k_point'): to_remove.append(self.k_point)
        if hasattr(self, 'n4_point'): to_remove.append(self.n4_point)

        if to_remove:
            self.play(*[FadeOut(obj) for obj in to_remove])
            self.wait()

    def calculate_angle(self, a, b, c):
        """计算三个点形成的角度（弧度）"""
        # 修改为直接接受坐标而非Dot对象
        if hasattr(a, 'get_center'): a = a.get_center()
        if hasattr(b, 'get_center'): b = b.get_center()
        if hasattr(c, 'get_center'): c = c.get_center()

        ba = a - b
        bc = c - b
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        return np.arccos(np.clip(cosine_angle, -1, 1))

    def find_intersection(self, curve, line):
        """计算曲线和直线的交点"""
        if isinstance(curve, Arc):
            # 圆弧与直线的交点
            circle_center = curve.arc_center
            radius = curve.radius
            line_start = line.get_start()
            line_dir = (line.get_end() - line_start) / np.linalg.norm(line.get_end() - line_start)

            # 解二次方程
            oc = line_start - circle_center
            a = np.dot(line_dir, line_dir)
            b = 2 * np.dot(oc, line_dir)
            c = np.dot(oc, oc) - radius ** 2

            discriminant = b ** 2 - 4 * a * c
            if discriminant < 0:
                return line_start  # 无解时返回默认点

            t = (-b - math.sqrt(discriminant)) / (2 * a)
            return line_start + t * line_dir
        return line.get_start()

    def find_circle_line_intersection(self, circle, point, direction):
        """计算圆与直线的交点（给定点和方向）"""
        center = circle.get_center()
        radius = circle.radius
        dir_norm = direction / np.linalg.norm(direction)

        # 解方程 (p + t*d - c)^2 = r^2
        oc = point - center
        a = np.dot(dir_norm, dir_norm)
        b = 2 * np.dot(oc, dir_norm)
        c = np.dot(oc, oc) - radius ** 2

        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return point  # 无解时返回默认点

        t1 = (-b + math.sqrt(discriminant)) / (2 * a)
        t2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return point + t2 * dir_norm  # 返回靠近起点的 
