# HeptadecagonConstruction

from manim import *

class HeptadecagonConstruction(Scene):
    def construct(self):
        # 标题与历史背景
        title = Tex(r"正十七边形尺规作图", font_size=48)
        subtitle = Tex(r"高斯 (1796) 解决2000年数学难题", font_size=36)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), FadeIn(subtitle, shift=UP))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # 高斯名言
        quote = Tex(r"\"数学是科学的女王，而数论是数学的女王。\"", font_size=32)
        author = Tex(r"- 卡尔·弗里德里希·高斯", font_size=28).next_to(quote, DOWN)
        self.play(Write(quote), Write(author))
        self.wait(2)
        self.play(FadeOut(quote), FadeOut(author))
        
        # 初始化圆和半径
        self.show_initial_construction()

        # 构造关键点
        self.construct_key_points()

        # 确定顶点
        self.locate_vertices()

        # 完成正十七边形
        self.form_polygon()

    def show_initial_construction(self):
        # 创建圆和垂直直径
        circle = Circle(radius=3, color=WHITE)
        center = Dot(ORIGIN)
        label_o = Tex("O").next_to(center, DL, buff=0.1)
        
        # 垂直直径 OA 和 OB
        A = circle.point_at_angle(PI/2)
        B = circle.point_at_angle(3*PI/2)
        C_point = circle.point_at_angle(0)
        D_point = circle.point_at_angle(PI)
        
        line_OA = Line(ORIGIN, A, color=BLUE)
        line_OB = Line(ORIGIN, B, color=BLUE)
        label_A = Tex("A").next_to(A, UP)
        label_B = Tex("B").next_to(B, DOWN)
        label_C = Tex("C'", font_size=24).next_to(C_point, RIGHT)
        label_D = Tex("D'", font_size=24).next_to(D_point, LEFT)
        
        # 动画展示初始构造
        self.play(Create(circle), Create(center))
        self.play(Write(label_o))
        self.play(Create(line_OA), Create(line_OB), 
                 Write(label_A), Write(label_B))
        self.wait(1)
        
        # 保存初始元素
        self.circle = circle
        self.center = center
        self.label_o = label_o
        self.line_OA = line_OA
        self.line_OB = line_OB
        self.label_A = label_A
        self.label_B = label_B
        self.A = A
        self.B = B
        self.C_prime = C_point
        self.D_prime = D_point

    def construct_key_points(self):
        # 步骤1：在OB上取OC = 1/4 OB
        O = self.center.get_center()
        B_point = self.B
        OB_vector = B_point - O
        OC_point = O + 0.25 * OB_vector
        dot_C = Dot(OC_point, color=YELLOW)
        label_C = Tex("C").next_to(dot_C, LEFT, buff=0.1)
        
        self.play(Create(dot_C), Write(label_C))
        self.wait(0.5)
        
        # 步骤2：作∠OCD = 1/4∠OCA
        A_point = self.A
        line_CA = Line(OC_point, A_point, color=PINK)
        angle_OCA = Angle(self.line_OB, line_CA, radius=0.4, color=GREEN)
        angle_label = Tex(r"$\angle OCA$", font_size=20).next_to(angle_OCA, UR, buff=0.1)
        
        self.play(Create(line_CA), Create(angle_OCA), Write(angle_label))
        self.wait(1)
        
        # 构造1/4角度
        quarter_angle = angle_OCA.angle * 0.25
        line_CD = Line(
            OC_point,
            OC_point + [np.cos(3*PI/2 + quarter_angle), np.sin(3*PI/2 + quarter_angle), 0],
            color=ORANGE
        )
        dot_D = Dot(line_CD.get_end(), color=RED)
        label_D = Tex("D").next_to(dot_D, DOWN, buff=0.1)
        
        self.play(Create(line_CD), Create(dot_D), Write(label_D))
        self.wait(1)
        
        # 步骤3：在AO延长线上作E点使∠DCE=45°
        AO_extension = Line(O, O + (A_point - O)*1.5, color=BLUE_E)
        self.play(Create(AO_extension))
        
        # 45度角构造
        angle_DCE = 45 * DEGREES
        line_CE = Line(
            OC_point,
            OC_point + [np.cos(angle_DCE), np.sin(angle_DCE), 0],
            color=PURPLE
        )
        E_point = line_CE.get_end()
        dot_E = Dot(E_point, color=GREEN)
        label_E = Tex("E").next_to(dot_E, UP, buff=0.1)
        
        self.play(Create(line_CE), Create(dot_E), Write(label_E))
        self.wait(1)
        
        # 保存关键点
        self.dot_C = dot_C
        self.label_C = label_C
        self.dot_D = dot_D
        self.label_D = label_D
        self.dot_E = dot_E
        self.label_E = label_E
        self.line_CE = line_CE

    def locate_vertices(self):
        # 步骤4：作AE中点M
        A_point = self.A
        E_point = self.dot_E.get_center()
        M_point = (A_point + E_point)/2
        dot_M = Dot(M_point, color=YELLOW)
        label_M = Tex("M").next_to(dot_M, UR, buff=0.1)
        
        circle_M = Circle(radius=np.linalg.norm(A_point - M_point), color=TEAL).move_to(M_point)
        
        self.play(Create(dot_M), Write(label_M))
        self.play(Create(circle_M))
        self.wait(0.5)
        
        # 步骤5：圆M交OB于F点
        O = self.center.get_center()
        B_point = self.B
        OB_line = Line(O, B_point)
        
        # 计算交点
        intersections = self.intersect_circle_line(circle_M, OB_line)
        F_point = intersections[1] if np.linalg.norm(intersections[0]-O) < np.linalg.norm(intersections[1]-O) else intersections[0]
        dot_F = Dot(F_point, color=ORANGE)
        label_F = Tex("F").next_to(dot_F, LEFT, buff=0.1)
        
        self.play(Create(dot_F), Write(label_F))
        self.wait(0.5)
        
        # 步骤6：以D为圆心，DF为半径作圆
        D_point = self.dot_D.get_center()
        radius_DF = np.linalg.norm(F_point - D_point)
        circle_D = Circle(radius=radius_DF, color=LIGHT_BROWN).move_to(D_point)
        
        self.play(Create(circle_D))
        self.wait(0.5)
        
        # 步骤7：圆D交OA于G4和G6
        OA_line = Line(O, self.A)
        intersections = self.intersect_circle_line(circle_D, OA_line)
        G4_point, G6_point = intersections
        
        dot_G4 = Dot(G4_point, color=RED)
        dot_G6 = Dot(G6_point, color=RED)
        label_G4 = Tex("G4", font_size=24).next_to(dot_G4, UP, buff=0.1)
        label_G6 = Tex("G6", font_size=24).next_to(dot_G6, DOWN, buff=0.1)
        
        self.play(
            Create(dot_G4), Create(dot_G6),
            Write(label_G4), Write(label_G6)
        )
        self.wait(1)
        
        # 保存关键点
        self.dot_M = dot_M
        self.label_M = label_M
        self.dot_F = dot_F
        self.label_F = label_F
        self.dot_G4 = dot_G4
        self.dot_G6 = dot_G6
        self.label_G4 = label_G4
        self.label_G6 = label_G6

    def form_polygon(self):
        # 步骤8：过G4、G6作垂线得顶点P4、P6
        O = self.center.get_center()
        OA_line = self.line_OA
        
        # 创建垂线
        perp_G4 = Line(
            self.dot_G4.get_center(),
            self.dot_G4.get_center() + [0, 3, 0],
            color=PURPLE
        )
        perp_G6 = Line(
            self.dot_G6.get_center(),
            self.dot_G6.get_center() + [0, -3, 0],
            color=PURPLE
        )
        
        self.play(Create(perp_G4), Create(perp_G6))
        self.wait(0.5)
        
        # 计算交点
        circle = self.circle
        P4 = self.intersect_circle_line(circle, perp_G4)[0]
        P6 = self.intersect_circle_line(circle, perp_G6)[0]
        
        dot_P4 = Dot(P4, color=GOLD)
        dot_P6 = Dot(P6, color=GOLD)
        label_P4 = Tex("P4", font_size=24).next_to(dot_P4, UR, buff=0.1)
        label_P6 = Tex("P6", font_size=24).next_to(dot_P6, DR, buff=0.1)
        
        self.play(
            Create(dot_P4), Create(dot_P6),
            Write(label_P4), Write(label_P6)
        )
        self.wait(1)
        
        # 步骤9：以1/2弧P4P6为半径截取所有顶点
        arc_P4P6 = ArcBetweenPoints(P4, P6, angle=-TAU/17, color=YELLOW)
        half_arc = arc_P4P6.copy().set_color(RED)
        half_arc.rotate(-TAU/(17*2), about_point=O)
        
        self.play(Create(arc_P4P6))
        self.play(Transform(arc_P4P6, half_arc))
        self.wait(1)
        
        # 生成所有顶点
        all_vertices = []
        current_angle = np.arctan2(P4[1]-O[1], P4[0]-O[0])
        angle_step = TAU/17
        
        for i in range(17):
            angle = current_angle + i * angle_step
            vertex = circle.point_at_angle(angle)
            all_vertices.append(vertex)
        
        # 绘制正十七边形
        polygon = Polygon(*all_vertices, color=MAROON_B, fill_opacity=0.2)
        self.play(Create(polygon), run_time=3)
        
        # 数学原理说明
        math_text = MathTex(
            r"\cos\frac{2\pi}{17} = \frac{-1 + \sqrt{17} + \sqrt{34-2\sqrt{17}} + 2\sqrt{17+3\sqrt{17} - \sqrt{34-2\sqrt{17}} - 2\sqrt{34+2\sqrt{17}}}}{16}",
            font_size=28
        ).to_edge(DOWN)
        
        self.play(Write(math_text))
        self.wait(3)
        
        # 高斯签名
        signature = Tex(r"- Carl Friedrich Gauss, 1796 -", font_size=24).to_edge(DOWN)
        self.play(Transform(math_text, signature))
        self.wait(2)

    def intersect_circle_line(self, circle, line):
        # 计算圆和直线的交点
        C = circle.get_center()
        r = circle.radius
        P = line.get_start()
        Q = line.get_end()
        
        # 参数化直线方程: L(t) = P + t*(Q-P)
        dx = Q[0] - P[0]
        dy = Q[1] - P[1]
        
        a = dx**2 + dy**2
        b = 2*(dx*(P[0]-C[0]) + dy*(P[1]-C[1]))
        c = (P[0]-C[0])**2 + (P[1]-C[1])**2 - r**2
        
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return []  # 无交点
        
        t1 = (-b + np.sqrt(discriminant)) / (2*a)
        t2 = (-b - np.sqrt(discriminant)) / (2*a)
        
        point1 = np.array([P[0] + t1*dx, P[1] + t1*dy, 0])
        point2 = np.array([P[0] + t2*dx, P[1] + t2*dy, 0])
        
        return [point1, point2]

# 运行命令: manim -pql GaussSeventeen.py GaussSeventeen