# HeptadecagonConstruction

from manim import *
import numpy as np

class HeptadecagonConstruction(Scene):
    def construct(self):
        # Title and historical context
        title = Tex(r"Regular Heptadecagon Construction", font_size=48)
        subtitle = Tex(r"Gauss (1796) Solved a 2000-Year-Old Problem", font_size=36)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), FadeIn(subtitle, shift=UP))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Gauss quote
        quote = Tex(r'"Mathematics is the queen of sciences, and number theory is the queen of mathematics."', font_size=32)
        author = Tex(r"- Carl Friedrich Gauss", font_size=28).next_to(quote, DOWN)
        self.play(Write(quote), Write(author))
        self.wait(2)
        self.play(FadeOut(quote), FadeOut(author))
        
        # Initialize circle and radius
        self.show_initial_construction()

        # Construct key points
        self.construct_key_points()

        # Locate vertices
        self.locate_vertices()

        # Complete the heptadecagon
        self.form_polygon()

    def show_initial_construction(self):
        # Create circle and vertical diameter
        circle = Circle(radius=3, color=WHITE)
        center = Dot(ORIGIN)
        label_o = Tex("O").next_to(center, DL, buff=0.1)
        
        # Vertical diameter OA and OB
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
        
        # Animate initial construction
        self.play(Create(circle), Create(center))
        self.play(Write(label_o))
        self.play(Create(line_OA), Create(line_OB), 
                 Write(label_A), Write(label_B))
        self.wait(1)
        
        # Save initial elements
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
        # Step 1: On OB, take OC = 1/4 OB
        O = self.center.get_center()
        B_point = self.B
        OB_vector = B_point - O
        OC_point = O + 0.25 * OB_vector
        dot_C = Dot(OC_point, color=YELLOW)
        label_C = Tex("C").next_to(dot_C, LEFT, buff=0.1)
        
        self.play(Create(dot_C), Write(label_C))
        self.wait(0.5)
        
        # Step 2: Construct ∠OCD = 1/4∠OCA
        A_point = self.A
        line_CA = Line(OC_point, A_point, color=PINK)
        
        # Create angle visualization
        angle_OCA = Angle(line_CA, self.line_OB, radius=0.4, other_angle=False, color=GREEN)
        angle_label = Tex(r"$\angle OCA$", font_size=20).next_to(angle_OCA, UR, buff=0.1)
        
        self.play(Create(line_CA), Create(angle_OCA), Write(angle_label))
        self.wait(1)
        
        # Calculate angle value manually
        vector_OB = self.line_OB.get_unit_vector()
        vector_CA = line_CA.get_unit_vector()
        angle_value = np.arccos(np.dot(vector_OB, vector_CA))
        
        # Construct 1/4 angle
        quarter_angle = angle_value * 0.25
        line_CD = Line(
            OC_point,
            OC_point + [np.cos(3*PI/2 + quarter_angle), np.sin(3*PI/2 + quarter_angle), 0],
            color=ORANGE
        )
        dot_D = Dot(line_CD.get_end(), color=RED)
        label_D = Tex("D").next_to(dot_D, DOWN, buff=0.1)
        
        self.play(Create(line_CD), Create(dot_D), Write(label_D))
        self.wait(1)
        
        # Step 3: On AO extension, create E such that ∠DCE=45°
        AO_extension = Line(O, O + (A_point - O)*1.5, color=BLUE_E)
        self.play(Create(AO_extension))
        
        # 45-degree angle construction
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
        
        # Save key points
        self.dot_C = dot_C
        self.label_C = label_C
        self.dot_D = dot_D
        self.label_D = label_D
        self.dot_E = dot_E
        self.label_E = label_E
        self.line_CE = line_CE

    def locate_vertices(self):
        # Step 4: Find midpoint M of AE
        A_point = self.A
        E_point = self.dot_E.get_center()
        M_point = (A_point + E_point)/2
        dot_M = Dot(M_point, color=YELLOW)
        label_M = Tex("M").next_to(dot_M, UR, buff=0.1)
        
        circle_M = Circle(radius=np.linalg.norm(A_point - M_point), color=TEAL).move_to(M_point)
        
        self.play(Create(dot_M), Write(label_M))
        self.play(Create(circle_M))
        self.wait(0.5)
        
        # Step 5: Circle M intersects OB at F
        O = self.center.get_center()
        B_point = self.B
        OB_line = Line(O, B_point)
        
        # Calculate intersection
        intersections = self.intersect_circle_line(circle_M, OB_line)
        F_point = intersections[1] if np.linalg.norm(intersections[0]-O) < np.linalg.norm(intersections[1]-O) else intersections[0]
        dot_F = Dot(F_point, color=ORANGE)
        label_F = Tex("F").next_to(dot_F, LEFT, buff=0.1)
        
        self.play(Create(dot_F), Write(label_F))
        self.wait(0.5)
        
        # Step 6: Circle with center D and radius DF
        D_point = self.dot_D.get_center()
        radius_DF = np.linalg.norm(F_point - D_point)
        circle_D = Circle(radius=radius_DF, color=LIGHT_BROWN).move_to(D_point)
        
        self.play(Create(circle_D))
        self.wait(0.5)
        
        # Step 7: Circle D intersects OA at G4 and G6
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
        
        # Save key points
        self.dot_M = dot_M
        self.label_M = label_M
        self.dot_F = dot_F
        self.label_F = label_F
        self.dot_G4 = dot_G4
        self.dot_G6 = dot_G6
        self.label_G4 = label_G4
        self.label_G6 = label_G6

    def form_polygon(self):
        # Step 8: Perpendiculars through G4, G6 give vertices P4, P6
        O = self.center.get_center()
        OA_line = self.line_OA
        
        # Create perpendiculars
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
        
        # Calculate intersections
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
        
        # Step 9: Use 1/2 arc P4P6 to find all vertices
        arc_P4P6 = ArcBetweenPoints(P4, P6, angle=-TAU/17, color=YELLOW)
        half_arc = arc_P4P6.copy().set_color(RED)
        half_arc.rotate(-TAU/(17*2), about_point=O)
        
        self.play(Create(arc_P4P6))
        self.play(Transform(arc_P4P6, half_arc))
        self.wait(1)
        
        # Generate all vertices
        all_vertices = []
        current_angle = np.arctan2(P4[1]-O[1], P4[0]-O[0])
        angle_step = TAU/17
        
        for i in range(17):
            angle = current_angle + i * angle_step
            vertex = circle.point_at_angle(angle)
            all_vertices.append(vertex)
        
        # Draw the heptadecagon
        polygon = Polygon(*all_vertices, color=MAROON_B, fill_opacity=0.2)
        self.play(Create(polygon), run_time=3)
        
        # Mathematical formula
        math_text = MathTex(
            r"\cos\frac{2\pi}{17} = \frac{-1 + \sqrt{17} + \sqrt{34-2\sqrt{17}} + 2\sqrt{17+3\sqrt{17} - \sqrt{34-2\sqrt{17}} - 2\sqrt{34+2\sqrt{17}}}}{16}",
            font_size=28
        ).to_edge(DOWN)
        
        self.play(Write(math_text))
        self.wait(3)
        
        # Gauss signature
        signature = Tex(r"- Carl Friedrich Gauss, 1796 -", font_size=24).to_edge(DOWN)
        self.play(Transform(math_text, signature))
        self.wait(2)

    def intersect_circle_line(self, circle, line):
        # Calculate circle-line intersections
        C = circle.get_center()
        r = circle.radius
        P = line.get_start()
        Q = line.get_end()
        
        # Line equation: L(t) = P + t*(Q-P)
        dx = Q[0] - P[0]
        dy = Q[1] - P[1]
        
        a = dx**2 + dy**2
        b = 2*(dx*(P[0]-C[0]) + dy*(P[1]-C[1]))
        c = (P[0]-C[0])**2 + (P[1]-C[1])**2 - r**2
        
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return []  # No intersection
        
        t1 = (-b + np.sqrt(discriminant)) / (2*a)
        t2 = (-b - np.sqrt(discriminant)) / (2*a)
        
        point1 = np.array([P[0] + t1*dx, P[1] + t1*dy, 0])
        point2 = np.array([P[0] + t2*dx, P[1] + t2*dy, 0])
        
        return [point1, point2]

# Run command: manim -pql GaussSeventeen.py GaussSeventeen