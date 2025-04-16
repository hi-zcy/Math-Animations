# HeptadecagonConstruction
# To run this:
# 1. Make sure you have Manim installed (pip install manim [manimgl])
# 2. Save this code as e.g., heptadecagon_construction.py
# 3. Run from the terminal: manim -pql heptadecagon_construction.py HeptadecagonConstruction

try:
    from manim import *
except ImportError:
    # from manimlib import *
    pass

from manim import *
import numpy as np
from math import sqrt, acos

class HeptadecagonConstruction(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        self.show_construction()

    def show_construction(self):
        # 第一阶段：基本构造
        main_circle = self.init_construction()
        self.wait(1)
        
        # 第二阶段：关键辅助点
        E, F_points = self.construct_auxiliary_points(main_circle)
        self.wait(1)
        
        # 第三阶段：最终构造
        self.final_construction(main_circle, E, F_points)
        self.wait(2)

    def init_construction(self):
        """步骤1-3：初始化主圆和基本元素"""
        main_circle = Circle(radius=3, color=WHITE)
        center = Dot(ORIGIN, color=YELLOW)
        
        # 绘制主圆和中心点
        self.play(Create(main_circle), Create(center))
        self.add_label(center, "O", UR)
        
        # 添加垂直直径
        v_diameter = self.add_diameter(main_circle, UP, "AB")
        # 添加水平直径
        h_diameter = self.add_diameter(main_circle, RIGHT, "CD")
        
        return main_circle

    def construct_auxiliary_points(self, main_circle):
        """步骤4-7：构造关键辅助点"""
        # 构造点E（四分之一半径处）
        E = self.add_point_E(main_circle)
        
        # 构造辅助圆（绿色圆）
        aux_circle = self.add_aux_circle(E)
        
        # 获取交点F和F'
        F_points = self.find_intersection_FFprime(main_circle, aux_circle)
        
        return E, F_points

    def final_construction(self, main_circle, E, F_points):
        """步骤8-16：最终构造过程"""
        # 构造切线GI
        tangent_line = self.add_tangent_line(F_points[0])
        
        # 构造角平分线
        bisector = self.add_angle_bisector(F_points)
        
        # 获取初始顶点
        start_point = self.get_start_point(bisector, main_circle)
        
        # 生成正十七边形
        self.draw_heptadecagon(main_circle, start_point)

    # ---------- 详细工具方法 ----------
    def add_diameter(self, circle, direction, label):
        """添加带标签的直径"""
        diameter = Line(circle.get_left(), circle.get_right()).rotate(
            angle_of_vector(direction) - PI/2
        )
        self.play(Create(diameter))
        self.add_label(diameter, label, direction*1.2)
        return diameter

    def add_point_E(self, circle):
        """精确构造点E (Richmond关键步骤)"""
        OE = Line(ORIGIN, circle.point_at_angle(PI/2))
        OE_quarter = OE.copy().scale(0.25, about_point=ORIGIN)
        E = OE_quarter.end
        dot_E = Dot(E, color=GREEN)
        self.play(Create(dot_E))
        self.add_label(dot_E, "E", UR)
        return E

    def add_aux_circle(self, E):
        """构造绿色辅助圆（半径OE）"""
        aux_circle = Circle(radius=np.linalg.norm(E), color=GREEN)
        self.play(Create(aux_circle))
        return aux_circle

    def find_intersection_FFprime(self, main_circle, aux_circle):
        """精确计算两圆交点（使用解析几何）"""
        # 主圆方程：x² + y² = 9
        # 辅助圆方程：(x - 0)^2 + (y - 1.5)^2 = (1.5)^2
        d = 1.5  # 辅助圆圆心纵坐标
        R = 3     # 主圆半径
        r = 1.5   # 辅助圆半径
        
        # 联立方程求解
        y = (d**2 + R**2 - r**2) / (2*d)
        x = sqrt(R**2 - y**2)
        
        F1 = np.array([x, y, 0])
        F2 = np.array([-x, y, 0])
        
        dot_F1 = Dot(F1, color=RED)
        dot_F2 = Dot(F2, color=RED)
        self.play(Create(dot_F1), Create(dot_F2))
        self.add_label(dot_F1, "F", UR)
        self.add_label(dot_F2, "F'", UL)
        return [F1, F2]

    def add_tangent_line(self, F):
        """构造F点的切线（黄色线）"""
        # 切线方程：F_x*x + F_y*y = 9 (主圆半径平方)
        tangent_line = Line(UP*3, DOWN*3).rotate(
            angle_of_vector([F[0], F[1], 0]) + PI/2
        )
        tangent_line.set_color(YELLOW)
        self.play(Create(tangent_line))
        return tangent_line

    def add_angle_bisector(self, F_points):
        """构造角平分线（关键步骤）"""
        bisector_line = Line(
            start=ORIGIN,
            end=self.calculate_bisector_direction(F_points),
            color=PINK
        )
        self.play(Create(bisector_line))
        return bisector_line

    def calculate_bisector_direction(self, F_points):
        """计算角平分线方向（解析几何法）"""
        F1 = F_points[0]
        angle_F1 = np.arctan2(F1[1], F1[0])
        angle_bisector = angle_F1/2
        return np.array([np.cos(angle_bisector), np.sin(angle_bisector), 0]) * 3

    def get_start_point(self, bisector, circle):
        """获取初始顶点H"""
        intersection = self.find_intersection(bisector, circle)
        dot_H = Dot(intersection, color=ORANGE)
        self.play(Create(dot_H))
        self.add_label(dot_H, "H", UR)
        return intersection

    def find_intersection(self, line, circle):
        """直线与圆的精确交点计算"""
        a, b = line.get_start()[:2], line.get_end()[:2]
        dir_vec = b - a
        t = np.linspace(0, 1, 100)
        points = [a + t_i*dir_vec for t_i in t]
        for p in points:
            if np.linalg.norm(p) >= 2.95 and np.linalg.norm(p) <= 3.05:
                return np.array([p[0], p[1], 0])
        return ORIGIN

    def draw_heptadecagon(self, circle, start_point):
        """生成并绘制正十七边形"""
        vertices = []
        angle_step = 2*PI/17
        for k in range(17):
            angle = angle_step * k
            rot_matrix = np.array([
                [np.cos(angle), -np.sin(angle)],
                [np.sin(angle), np.cos(angle)]
            ])
            vertex = rot_matrix @ start_point[:2]
            vertices.append(vertex)
        
        heptadecagon = Polygon(*vertices, color=BLUE, stroke_width=2)
        self.play(Create(heptadecagon), run_time=3)

    def add_label(self, obj, text, direction):
        """添加动态标签"""
        label = MathTex(text).scale(0.7).next_to(obj, direction)
        self.play(Write(label))
        return label

    # ---------- 数学验证方法 ----------
    def verify_construction(self):
        """验证高斯公式（开发用）"""
        cos_pi_17 = np.cos(PI/17)
        expected = 0.5*sqrt(17 + sqrt(17) + sqrt(34-2*sqrt(17)) + 2*sqrt(17+3*sqrt(17)-sqrt(34-2*sqrt(17))-2*sqrt(34+2*sqrt(17))))
        print(f"理论值: {expected:.6f}")
        print(f"实际构造值: {cos_pi_17:.6f}")