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

class HeptadecagonConstruction(Scene):
    def construct(self):
        # Title
        title = Tex("Construction of a Regular Heptadecagon", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step 1: Draw circle with center C and point A
        radius = 4
        circle = Circle(radius=radius, color=WHITE)
        dot_C = Dot([0,0,0], color=WHITE)
        dot_A = Dot([radius,0,0], color=WHITE)
        label_C = Tex("C").next_to(dot_C, DOWN)
        label_A = Tex("A").next_to(dot_A, RIGHT)
        step1_text = Tex("Step 1: Draw circle with center C and point A", font_size=36).to_edge(DOWN)
        self.play(Write(step1_text))
        self.play(Create(circle), FadeIn(dot_C, dot_A), Write(label_C, label_A))
        self.wait(1)
        self.play(FadeOut(step1_text))

        # Step 2: Draw diameter AB
        dot_B = Dot([-radius,0,0], color=WHITE)
        label_B = Tex("B").next_to(dot_B, LEFT)
        diameter = Line(dot_B.get_center(), dot_A.get_center(), color=BLUE)
        step2_text = Tex("Step 2: Draw diameter AB", font_size=36).to_edge(DOWN)
        self.play(Write(step2_text))
        self.play(FadeIn(dot_B), Write(label_B), Create(diameter))
        self.wait(1)
        self.play(FadeOut(step2_text))

        # Step 3: Draw perpendicular radius and point D
        perp_radius = Line([0,0,0], [0,radius,0], color=GREEN)
        d_y = radius / 4
        dot_D = Dot([0,d_y,0], color=WHITE)
        label_D = Tex("D").next_to(dot_D, UP)
        step3_text = Tex("Step 3: Draw perpendicular radius, mark D at 1/4 radius", font_size=36).to_edge(DOWN)
        self.play(Write(step3_text))
        self.play(Create(perp_radius), FadeIn(dot_D), Write(label_D))
        self.wait(1)
        self.play(FadeOut(step3_text))

        # Step 4: Find point E by bisecting angle BDC twice
        line_DC = Line(dot_D.get_center(), dot_C.get_center(), color=YELLOW)
        line_DB = Line(dot_D.get_center(), dot_B.get_center(), color=YELLOW)
        step4_text = Tex("Step 4: Bisect angle BDC twice to find E on BC", font_size=36).to_edge(DOWN)
        self.play(Write(step4_text))
        self.play(Create(line_DC, line_DB))
        
        # First bisection
        arc_radius = 0.5
        circle_D1 = Circle(radius=arc_radius, color=ORANGE).move_to(dot_D.get_center())
        dot_Q1 = Dot([0,d_y-arc_radius,0], color=RED)
        t = arc_radius / np.sqrt(radius**2 + d_y**2)
        P1_x = -radius * t
        P1_y = d_y * (1 - t)
        dot_P1 = Dot([P1_x, P1_y, 0], color=RED)
        self.play(Create(circle_D1), FadeIn(dot_P1, dot_Q1))
        
        arc_P1_radius = 0.5
        arc_P1 = Circle(radius=arc_P1_radius, color=ORANGE).move_to(dot_P1.get_center())
        arc_Q1 = Circle(radius=arc_P1_radius, color=ORANGE).move_to(dot_Q1.get_center())
        self.play(Create(arc_P1, arc_Q1))
        
        # Approximate intersection for R1
        P1 = dot_P1.get_center()
        Q1 = dot_Q1.get_center()
        d = np.linalg.norm(P1 - Q1)
        a = (arc_P1_radius**2 - arc_P1_radius**2 + d**2) / (2 * d)
        h = np.sqrt(arc_P1_radius**2 - a**2)
        center = Q1 + a / d * (P1 - Q1)
        direction = np.array([P1[1] - Q1[1], Q1[0] - P1[0], 0]) / np.linalg.norm([P1[1] - Q1[1], Q1[0] - P1[0], 0])
        R1 = center + h * direction
        dot_R1 = Dot(R1, color=ORANGE)
        line_DR1 = Line(dot_D.get_center(), dot_R1.get_center(), color=ORANGE)
        self.play(FadeIn(dot_R1), Create(line_DR1))
        
        # Second bisection
        circle_D2 = Circle(radius=arc_radius, color=ORANGE).move_to(dot_D.get_center())
        dot_Q2 = Dot([0,d_y-arc_radius,0], color=RED)
        D = dot_D.get_center()
        R1_vec = dot_R1.get_center()
        direction_DR1 = (R1_vec - D) / np.linalg.norm(R1_vec - D)
        P2 = D + arc_radius * direction_DR1
        dot_P2 = Dot(P2, color=RED)
        self.play(Create(circle_D2), FadeIn(dot_P2, dot_Q2))
        
        arc_P2 = Circle(radius=arc_P1_radius, color=ORANGE).move_to(dot_P2.get_center())
        arc_Q2 = Circle(radius=arc_P1_radius, color=ORANGE).move_to(dot_Q2.get_center())
        self.play(Create(arc_P2, arc_Q2))
        
        P2_vec = dot_P2.get_center()
        Q2 = dot_Q2.get_center()
        d2 = np.linalg.norm(P2_vec - Q2)
        a2 = (arc_P1_radius**2 - arc_P1_radius**2 + d2**2) / (2 * d2)
        h2 = np.sqrt(arc_P1_radius**2 - a2**2)
        center2 = Q2 + a2 / d2 * (P2_vec - Q2)
        direction2 = np.array([P2_vec[1] - Q2[1], Q2[0] - P2_vec[0], 0]) / np.linalg.norm([P2_vec[1] - Q2[1], Q2[0] - P2_vec[0], 0])
        R2 = center2 + h2 * direction2
        dot_R2 = Dot(R2, color=ORANGE)
        line_DR2 = Line(dot_D.get_center(), dot_R2.get_center(), color=ORANGE)
        self.play(FadeIn(dot_R2), Create(line_DR2))
        
        # Find E
        t_E = -d_y / (R2[1] - d_y)
        E_x = t_E * R2[0]
        dot_E = Dot([E_x, 0, 0], color=WHITE)
        label_E = Tex("E").next_to(dot_E, DOWN)
        self.play(FadeIn(dot_E), Write(label_E))
        self.wait(1)
        self.play(FadeOut(step4_text, circle_D1, arc_P1, arc_Q1, dot_P1, dot_Q1, dot_R1, line_DR1, circle_D2, arc_P2, arc_Q2, dot_P2, dot_Q2, dot_R2, line_DR2))

        # Step 5: Find point H on AC where angle EDH = 45 degrees
        line_DE = Line(dot_D.get_center(), dot_E.get_center(), color=YELLOW)
        step5_text = Tex("Step 5: Find H on AC with angle EDH = 45°", font_size=36).to_edge(DOWN)
        self.play(Write(step5_text))
        self.play(Create(line_DE))
        
        DE_vec = dot_E.get_center() - D
        DE_angle = np.arctan2(DE_vec[1], DE_vec[0])
        angle_45 = DE_angle + PI / 4
        ray_length = 6
        ray_end = D + ray_length * np.array([np.cos(angle_45), np.sin(angle_45), 0])
        ray_DH = Line(D, ray_end, color=ORANGE)
        self.play(Create(ray_DH))
        
        t_H = -d_y / np.sin(angle_45)
        H_x = t_H * np.cos(angle_45)
        if 0 < H_x < radius:
            dot_H = Dot([H_x, 0, 0], color=WHITE)
            label_H = Tex("H").next_to(dot_H, DOWN)
            self.play(FadeIn(dot_H), Write(label_H))
        self.wait(1)
        self.play(FadeOut(step5_text, line_DE, ray_DH))

        # Step 6: Circle with diameter BH
        dot_X = Dot((dot_B.get_center() + dot_H.get_center()) / 2, color=WHITE)
        label_X = Tex("X").next_to(dot_X, UP)
        circle_BH = Circle(radius=np.linalg.norm(dot_B.get_center() - dot_X.get_center()), arc_center=dot_X.get_center(), color=PURPLE)
        step6_text = Tex("Step 6: Draw circle with diameter BH, find center X", font_size=36).to_edge(DOWN)
        self.play(Write(step6_text))
        self.play(FadeIn(dot_X), Write(label_X), Create(circle_BH))
        self.wait(1)
        self.play(FadeOut(step6_text))

        # Step 7: Find point K
        line_CD_extended = Line([0,d_y,0], [0,radius*2,0], color=GREEN)
        step7_text = Tex("Step 7: Extend CD, find intersection K", font_size=36).to_edge(DOWN)
        self.play(Write(step7_text))
        self.play(Create(line_CD_extended))
        
        X = dot_X.get_center()
        r = np.linalg.norm(dot_B.get_center() - X)
        if X[0]**2 < r**2:
            K_y = X[1] + np.sqrt(r**2 - X[0]**2)
            dot_K = Dot([0, K_y, 0], color=WHITE)
            label_K = Tex("K").next_to(dot_K, RIGHT)
            self.play(FadeIn(dot_K), Write(label_K))
        self.wait(1)
        self.play(FadeOut(step7_text, line_CD_extended))

        # Step 8: Circle with center E, radius EK
        EK = np.linalg.norm(dot_K.get_center() - dot_E.get_center())
        circle_E = Circle(radius=EK, arc_center=dot_E.get_center(), color=PURPLE)
        step8_text = Tex("Step 8: Draw circle with center E, radius EK", font_size=36).to_edge(DOWN)
        self.play(Write(step8_text))
        self.play(Create(circle_E))
        
        Ex = dot_E.get_center()[0]
        x1 = Ex + EK
        x2 = Ex - EK
        if x2 > -radius:
            dot_Y = Dot([x2,0,0], color=WHITE)
            label_Y = Tex("Y").next_to(dot_Y, DOWN)
            self.play(FadeIn(dot_Y), Write(label_Y))
        if 0 < x1 < radius:
            dot_Z = Dot([x1,0,0], color=WHITE)
            label_Z = Tex("Z").next_to(dot_Z, DOWN)
            self.play(FadeIn(dot_Z), Write(label_Z))
        self.wait(1)
        self.play(FadeOut(step8_text, circle_E))

        # Step 9: Perpendiculars from Y and Z
        Yx = dot_Y.get_center()[0]
        line_Y_perp = Line([Yx, -radius, 0], [Yx, radius, 0], color=ORANGE)
        Zx = dot_Z.get_center()[0]
        line_Z_perp = Line([Zx, -radius, 0], [Zx, radius, 0], color=ORANGE)
        step9_text = Tex("Step 9: Draw perpendiculars from Y and Z to find P, P'", font_size=36).to_edge(DOWN)
        self.play(Write(step9_text))
        self.play(Create(line_Y_perp, line_Z_perp))
        
        P_y = np.sqrt(radius**2 - Yx**2)
        dot_P = Dot([Yx, P_y, 0], color=WHITE)
        label_P = Tex("P").next_to(dot_P, UP)
        P_prime_y = np.sqrt(radius**2 - Zx**2)
        dot_P_prime = Dot([Zx, P_prime_y, 0], color=WHITE)
        label_P_prime = Tex("P'").next_to(dot_P_prime, UP)
        self.play(FadeIn(dot_P, dot_P_prime), Write(label_P, label_P_prime))
        self.wait(1)
        self.play(FadeOut(step9_text, line_Y_perp, line_Z_perp))

        # Step 10: Bisect angle PCP'
        line_CP = Line(dot_C.get_center(), dot_P.get_center(), color=YELLOW)
        line_CP_prime = Line(dot_C.get_center(), dot_P_prime.get_center(), color=YELLOW)
        step10_text = Tex("Step 10: Bisect angle PCP' to find P''", font_size=36).to_edge(DOWN)
        self.play(Write(step10_text))
        self.play(Create(line_CP, line_CP_prime))
        
        arc_C_radius = 2.0
        circle_C = Circle(radius=arc_C_radius, color=ORANGE).move_to(dot_C.get_center())
        t_S = arc_C_radius / np.sqrt(Yx**2 + P_y**2)
        S_x = t_S * Yx
        S_y = t_S * P_y
        dot_S = Dot([S_x, S_y, 0], color=RED)
        t_T = arc_C_radius / np.sqrt(Zx**2 + P_prime_y**2)
        T_x = t_T * Zx
        T_y = t_T * P_prime_y
        dot_T = Dot([T_x, T_y, 0], color=RED)
        self.play(Create(circle_C), FadeIn(dot_S, dot_T))
        
        arc_S = Circle(radius=1.0, color=ORANGE).move_to(dot_S.get_center())
        arc_T = Circle(radius=1.0, color=ORANGE).move_to(dot_T.get_center())
        self.play(Create(arc_S, arc_T))
        
        S = dot_S.get_center()
        T = dot_T.get_center()
        d_U = np.linalg.norm(S - T)
        a_U = (1.0**2 - 1.0**2 + d_U**2) / (2 * d_U)
        h_U = np.sqrt(1.0**2 - a_U**2)
        center_U = T + a_U / d_U * (S - T)
        direction_U = np.array([S[1] - T[1], T[0] - S[0], 0]) / np.linalg.norm([S[1] - T[1], T[0] - S[0], 0])
        U = center_U + h_U * direction_U
        dot_U = Dot(U, color=ORANGE)
        self.play(FadeIn(dot_U))
        
        line_CU = Line(dot_C.get_center(), U, color=ORANGE)
        self.play(Create(line_CU))
        
        t_P_double_prime = radius / np.sqrt(U[0]**2 + U[1]**2)
        P_double_prime_x = t_P_double_prime * U[0]
        P_double_prime_y = t_P_double_prime * U[1]
        dot_P_double_prime = Dot([P_double_prime_x, P_double_prime_y, 0], color=WHITE)
        label_P_double_prime = Tex("P''").next_to(dot_P_double_prime, UP)
        self.play(FadeIn(dot_P_double_prime), Write(label_P_double_prime))
        self.wait(1)
        self.play(FadeOut(step10_text, line_CP, line_CP_prime, circle_C, dot_S, dot_T, arc_S, arc_T, dot_U, line_CU))

        # Step 11: Complete the heptadecagon
        step11_text = Tex("Step 11: Mark vertices using distance PP'", font_size=36).to_edge(DOWN)
        self.play(Write(step11_text))
        P = dot_P.get_center()
        P_prime = dot_P_prime.get_center()
        dist_PP_prime = np.linalg.norm(P - P_prime)
        theta = 2 * np.arcsin(dist_PP_prime / (2 * radius))
        vertices = []
        for i in range(17):
            angle = i * (2 * PI / 17)
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            vertices.append(Dot([x, y, 0], color=WHITE))
        lines = []
        for i in range(17):
            lines.append(Line(vertices[i].get_center(), vertices[(i+1)%17].get_center(), color=WHITE))
        self.play(*[FadeIn(v) for v in vertices], *[Create(l) for l in lines])
        self.wait(2)
        self.play(FadeOut(step11_text))

        # Final note
        note = Tex("Regular heptadecagon constructed!", font_size=36).to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
