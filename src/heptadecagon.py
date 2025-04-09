# HeptadecagonConstruction
# To run this:
# 1. Make sure you have Manim installed (pip install manim)
# 2. Save this code as e.g., heptadecagon_construction.py
# 3. Run from the terminal: manim -pql heptadecagon_construction.py HeptadecagonConstruction

try:
    from manim import *
except ImportError:
    from manimlib import *
import numpy as np

# Helper function to simulate compass arc for bisection
def compass_arc_between(point1, point2, center, radius_scale=0.6, angle=-PI/3, **kwargs):
    """Creates a small arc simulating a compass swing from point1 towards point2"""
    start_vec = point1 - center
    end_vec = point2 - center
    mid_angle = (angle_of_vector(start_vec) + angle_of_vector(end_vec)) / 2
    # Adjust radius slightly to make arcs intersect clearly if needed
    radius = np.linalg.norm(start_vec) * radius_scale
    # Ensure radius is not zero
    if radius < 0.01:
        radius = 0.5
    return Arc(radius=radius, start_angle=angle_of_vector(start_vec), angle=angle, arc_center=point1, **kwargs)

class HeptadecagonConstruction(Scene):
    def construct(self):
        # Configuration
        R = 3.0  # Radius of the main circle
        O = ORIGIN
        circle_color = BLUE
        construction_color = YELLOW
        point_color = RED
        final_polygon_color = GREEN

        # --- Introduction ---
        title = Text("Constructing a Regular 17-gon (Heptadecagon)", t2c={"17-gon": GREEN, "Heptadecagon": GREEN})
        subtitle = Text("A Compass and Straightedge Feat", font_size=36).next_to(title, DOWN)
        gauss_text = Text("Gauss proved this possible in 1796", font_size=28).next_to(subtitle, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(FadeIn(gauss_text, shift=UP))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(gauss_text))
        self.wait(0.5)

        # --- Setup ---
        center_dot = Dot(O, color=point_color)
        O_label = MathTex("O").next_to(center_dot, DOWN + LEFT, buff=0.1)
        main_circle = Circle(radius=R, color=circle_color).move_to(O)

        self.play(Create(center_dot), Write(O_label))
        self.play(Create(main_circle))
        self.wait(0.5)

        # Define key points on the circle
        P0_coord = R * RIGHT
        A_coord = R * UP
        A_prime_coord = R * DOWN

        P0 = Dot(P0_coord, color=point_color)
        P0_label = MathTex("P_0").next_to(P0, RIGHT, buff=0.1)
        A = Dot(A_coord, color=point_color)
        A_label = MathTex("A").next_to(A, UP, buff=0.1)
        A_prime = Dot(A_prime_coord, color=point_color)
        # A_prime_label = MathTex("A'").next_to(A_prime, DOWN, buff=0.1) # Label if needed

        horiz_diameter = Line(R * LEFT, R * RIGHT, color=GRAY)
        vert_diameter = Line(R * DOWN, R * UP, color=GRAY)

        self.play(Create(horiz_diameter), Create(vert_diameter))
        self.play(FadeIn(P0), Write(P0_label), FadeIn(A), Write(A_label), FadeIn(A_prime))
        setup_text = Text("Start with Circle(O, R), Diameter P₀P₈, Diameter AA'", font_size=24).to_edge(UP)
        self.play(Write(setup_text))
        self.wait(2)
        self.play(FadeOut(setup_text))

        # Store objects for later use/fading
        base_elements = VGroup(center_dot, O_label, main_circle, horiz_diameter, vert_diameter, P0, P0_label, A, A_label, A_prime)

        # --- Step 1: Construct Point J ---
        step1_text = Text("1. Mark J on OA' such that OJ = ¼ OA' = R/4", font_size=24).to_edge(UP)
        self.play(Write(step1_text))

        J_coord = O + R/4 * DOWN
        J = Dot(J_coord, color=point_color)
        J_label = MathTex("J").next_to(J, LEFT, buff=0.1)

        # Visualize division (optional, can be complex)
        # Instead, just mark the point
        temp_line_OJ = Line(O, J_coord, color=construction_color, stroke_width=2)
        self.play(Create(temp_line_OJ))
        self.play(FadeIn(J), Write(J_label))
        self.play(FadeOut(temp_line_OJ))
        self.wait(2)
        self.play(FadeOut(step1_text))

        # --- Step 2: Construct Point E ---
        step2_text = Text("2. Construct E on OP₀ such that ∠OJE = ¼ ∠OJP₀", font_size=24).to_edge(UP)
        self.play(Write(step2_text))

        # Calculate coordinates for accuracy (based on the known result of the construction)
        # The construction leads to points related to cos(2k*pi/17).
        # E's x-coordinate is R * (cos(2pi/17) + cos(8pi/17)) / 2
        # This is derived from the algebraic theory, Richmond's construction finds it geometrically.
        theta = 2 * PI / 17
        # We need E such that tan(angle OJE) = OE / OJ = OE / (R/4)
        # Angle OJP0: vector JO = (0, R/4), vector JP0 = (R, R/4)
        # Angle is arctan(R / (R/4)) = arctan(4) with vertical axis.
        # Or use atan2(R, R/4) for angle with horizontal axis going through J
        vec_JP0 = P0_coord - J_coord
        angle_OJP0_rad = np.arctan2(vec_JP0[1], vec_JP0[0]) - np.arctan2(-1, 0) # Angle relative to neg y-axis (OJ)
        angle_OJP0_rad = angle_of_vector(vec_JP0) - angle_of_vector(DOWN) # Correct angle relative to OJ vector
        angle_OJP0_rad = np.arccos(np.dot(DOWN, vec_JP0) / (np.linalg.norm(DOWN) * np.linalg.norm(vec_JP0)))


        target_angle_OJE = angle_OJP0_rad / 4

        # Calculate E coordinate: OE = OJ * tan(target_angle_OJE) = (R/4) * tan(target_angle_OJE)
        E_coord_x = (R / 4.0) * np.tan(target_angle_OJE)
        E_coord = E_coord_x * RIGHT
        E = Dot(E_coord, color=point_color)
        E_label = MathTex("E").next_to(E, DOWN, buff=0.1)

        # Animate the geometric steps (simplified visualization)
        line_JP0 = Line(J_coord, P0_coord, color=construction_color)
        self.play(Create(line_JP0))

        # Show angle OJP0
        # Angle() needs 3 points or (line1, line2)
        line_JO = Line(J_coord, O, color=GRAY) # Use original vertical line part
        angle_OJP0_obj = Angle(line_JP0, line_JO, radius=0.5, other_angle=False, color=YELLOW)
        OJP0_label = MathTex("\\angle OJP_0", font_size=20).move_to(
            Angle(line_JP0, line_JO, radius=0.5+0.2).point_from_proportion(0.5)
        )
        self.play(Create(angle_OJP0_obj), Write(OJP0_label))
        self.wait(1)

        # Simulate bisections (just show the resulting line JE)
        bisect_text = Text("Bisect ∠OJP₀ twice", font_size=20).next_to(step2_text, DOWN)
        self.play(Write(bisect_text))
        # First bisection (visual cue)
        temp_bisector1 = Line(J_coord, J_coord + rotate_vector(vec_JP0/np.linalg.norm(vec_JP0), -angle_OJP0_rad * 3/4) * R*0.6, color=WHITE, stroke_width=1, stroke_opacity=0.5)
        # Second bisection (visual cue)
        temp_bisector2 = Line(J_coord, J_coord + rotate_vector(vec_JP0/np.linalg.norm(vec_JP0), -angle_OJP0_rad * 7/8) * R*0.7, color=WHITE, stroke_width=1, stroke_opacity=0.5)

        line_JE = Line(J_coord, E_coord, color=construction_color)
        angle_OJE_obj = Angle(line_JE, line_JO, radius=0.4, other_angle=False, color=GREEN)
        OJE_label = MathTex("\\angle OJE", font_size=20).move_to(
             Angle(line_JE, line_JO, radius=0.4+0.2).point_from_proportion(0.5)
        )

        self.play(Create(temp_bisector1))
        self.wait(0.5)
        self.play(Create(temp_bisector2))
        self.wait(0.5)
        self.play(ReplacementTransform(temp_bisector2, line_JE), FadeOut(temp_bisector1)) # Show final line
        self.play(FadeOut(angle_OJP0_obj), FadeOut(OJP0_label), FadeOut(line_JP0))
        self.play(FadeIn(E), Write(E_label), Create(angle_OJE_obj), Write(OJE_label))
        self.wait(2)
        self.play(FadeOut(step2_text), FadeOut(bisect_text), FadeOut(angle_OJE_obj), FadeOut(OJE_label))


        # --- Step 3: Construct Point F ---
        step3_text = Text("3. Construct F on OP₀ such that ∠FJE = 45°", font_size=24).to_edge(UP)
        self.play(Write(step3_text))

        # Calculate F coordinate
        # Angle FJE = 45 degrees = PI/4 radians
        # F lies on horizontal axis (line OP0)
        # Vector JE = E_coord - J_coord = (E_coord_x, R/4)
        # We need vector JF = (F_coord_x - 0, 0 - (-R/4)) = (F_coord_x, R/4)
        # Angle between JE and JF should be 45 deg. Use dot product or rotation.
        # Rotate JE vector by -45 deg around J to get direction of JF
        vec_JE = E_coord - J_coord
        rotated_vec = rotate_vector(vec_JE, -PI/4)
        # Line through J with direction rotated_vec: J + t * rotated_vec
        # Intersection with horizontal axis (y=0): J[1] + t * rotated_vec[1] = 0 => t = -J[1] / rotated_vec[1]
        t = -J_coord[1] / rotated_vec[1]
        F_coord = J_coord + t * rotated_vec
        F = Dot(F_coord, color=point_color)
        F_label = MathTex("F").next_to(F, DOWN, buff=0.1)

        # Animate construction (e.g., bisect 90 deg angle at J)
        # Simpler: Show the angle directly
        line_JF = Line(J_coord, F_coord, color=construction_color)
        angle_FJE_obj = Angle(line_JF, line_JE, radius=0.6, other_angle=True, color=GREEN) # other_angle=True might be needed depending on order
        # Check angle direction, might need -PI/4 for Angle()
        angle_FJE_obj = Angle.from_three_points(F_coord, J_coord, E_coord, radius=0.6, color=GREEN) # Ensure correct vertex order

        FJE_label = MathTex("45^\\circ", font_size=20).move_to(
            Angle.from_three_points(F_coord, J_coord, E_coord, radius=0.6+0.2).point_from_proportion(0.5)
        )

        self.play(Create(line_JF))
        self.play(FadeIn(F), Write(F_label))
        self.play(Create(angle_FJE_obj), Write(FJE_label))
        self.wait(2)
        self.play(FadeOut(step3_text), FadeOut(angle_FJE_obj), FadeOut(FJE_label))
        self.play(FadeOut(line_JE), FadeOut(line_JF)) # Clean up intermediate lines


        # --- Step 4: Construct Point K ---
        step4_text = Text("4. Draw circle with diameter FP₀. Mark intersection K on OA.", font_size=24).to_edge(UP)
        self.play(Write(step4_text))

        # Midpoint M of FP0
        M_coord = (F_coord + P0_coord) / 2
        M = Dot(M_coord, color=ORANGE)
        M_label = MathTex("M").next_to(M, DOWN, buff=0.1)

        # Radius of circle M is half the distance FP0
        radius_M = np.linalg.norm(P0_coord - F_coord) / 2
        circle_M = Circle(radius=radius_M, color=ORANGE).move_to(M_coord)

        self.play(FadeIn(M), Write(M_label))
        self.play(Create(circle_M))
        self.wait(1)

        # Find intersection K. Circle M: (x-Mx)^2 + (y-My)^2 = rM^2. OA is y-axis (x=0).
        # (0-Mx)^2 + (y-My)^2 = rM^2 => y = My +/- sqrt(rM^2 - Mx^2)
        # Since My=0 (M is on horizontal axis), y = +/- sqrt(rM^2 - Mx^2)
        # K is the upper intersection (positive y).
        K_coord_y = np.sqrt(radius_M**2 - M_coord[0]**2)
        K_coord = K_coord_y * UP
        K = Dot(K_coord, color=point_color)
        K_label = MathTex("K").next_to(K, LEFT, buff=0.1)

        self.play(FadeIn(K), Write(K_label), Indicate(K))
        self.wait(2)
        self.play(FadeOut(step4_text))
        # Keep circle_M for context briefly


        # --- Step 5: Construct Points N₃ and N₅ ---
        step5_text = Text("5. Draw circle(E, EK). Mark intersections N₃, N₅ on OP₀.", font_size=24).to_edge(UP)
        self.play(Write(step5_text))

        radius_N = np.linalg.norm(K_coord - E_coord)
        circle_N = Circle(radius=radius_N, color=PURPLE).move_to(E_coord)

        # Show radius EK
        line_EK = DashedLine(E_coord, K_coord, color=PURPLE)
        self.play(Create(line_EK))
        self.play(Create(circle_N))
        self.wait(1)
        self.play(FadeOut(line_EK))

        # Find intersections N3, N5. Circle N: (x-Ex)^2 + (y-Ey)^2 = rN^2. OP0 is x-axis (y=0).
        # (x-Ex)^2 + (0-Ey)^2 = rN^2 => x = Ex +/- sqrt(rN^2 - Ey^2)
        # Since Ey=0 (E is on horizontal axis), x = Ex +/- sqrt(rN^2) = Ex +/- rN
        N3_coord_x = E_coord[0] - radius_N # N3 is closer to O
        N5_coord_x = E_coord[0] + radius_N # N5 is further from O
        N3_coord = N3_coord_x * RIGHT
        N5_coord = N5_coord_x * RIGHT

        N3 = Dot(N3_coord, color=point_color)
        N3_label = MathTex("N_3").next_to(N3, DOWN, buff=0.1)
        N5 = Dot(N5_coord, color=point_color)
        N5_label = MathTex("N_5").next_to(N5, DOWN, buff=0.1)

        self.play(FadeIn(N3), Write(N3_label), Indicate(N3))
        self.play(FadeIn(N5), Write(N5_label), Indicate(N5))
        self.wait(2)
        self.play(FadeOut(step5_text))
        # Keep circle_N briefly for context


        # --- Step 6: Construct Points P₃ and P₅ ---
        step6_text = Text("6. Draw perpendiculars from N₃, N₅ to main circle.", font_size=24).to_edge(UP)
        self.play(Write(step6_text))

        # P3 has x-coordinate = N3_coord_x. Find y using circle equation x^2+y^2=R^2
        P3_coord_y = np.sqrt(R**2 - N3_coord_x**2)
        P3_coord = N3_coord_x * RIGHT + P3_coord_y * UP
        P3 = Dot(P3_coord, color=GREEN)
        P3_label = MathTex("P_3").move_to(P3_coord + 0.2*normalize(P3_coord)) # Position label outside

        perp_N3 = DashedLine(N3_coord, P3_coord, color=construction_color)
        self.play(Create(perp_N3))
        self.play(FadeIn(P3), Write(P3_label))
        self.wait(1)

        # P5 has x-coordinate = N5_coord_x. Find y
        P5_coord_y = np.sqrt(R**2 - N5_coord_x**2)
        P5_coord = N5_coord_x * RIGHT + P5_coord_y * UP
        P5 = Dot(P5_coord, color=GREEN)
        P5_label = MathTex("P_5").move_to(P5_coord + 0.2*normalize(P5_coord)) # Position label outside

        perp_N5 = DashedLine(N5_coord, P5_coord, color=construction_color)
        self.play(Create(perp_N5))
        self.play(FadeIn(P5), Write(P5_label))
        self.wait(2)

        explain_P3P5 = MathTex("P_3, P_5 \\text{ are vertices 3 and 5}", font_size=20).next_to(step6_text, DOWN)
        self.play(Write(explain_P3P5))
        self.wait(2)
        self.play(FadeOut(step6_text), FadeOut(explain_P3P5))

        # Fade out construction circles M and N, and perpendiculars
        self.play(FadeOut(circle_M), FadeOut(M), FadeOut(M_label),
                  FadeOut(circle_N), FadeOut(perp_N3), FadeOut(perp_N5),
                  FadeOut(K), FadeOut(K_label), FadeOut(N3), FadeOut(N3_label),
                  FadeOut(N5), FadeOut(N5_label), FadeOut(E), FadeOut(E_label),
                  FadeOut(F), FadeOut(F_label), FadeOut(J), FadeOut(J_label))
        self.wait(0.5)


        # --- Step 7: Find P₁ via Arc Bisections ---
        step7_text = Text("7. Find P₁ by bisecting arcs P₃P₅ → P₄ → P₂ → P₁", font_size=24).to_edge(UP)
        self.play(Write(step7_text))

        # Bisect arc P3 P5 to get P4
        bisect_arc_text = Text("Bisect arc P₃P₅ → P₄", font_size=20, color=YELLOW).next_to(step7_text, DOWN)
        self.play(Write(bisect_arc_text))
        arc_P3P5 = ArcBetweenPoints(P3_coord, P5_coord, radius=R, color=YELLOW)
        self.play(Create(arc_P3P5))

        # Simulate compass arcs for bisection
        comp_arc1 = compass_arc_between(P3_coord, P5_coord, P3_coord, angle=-PI/2.5, color=WHITE, stroke_width=2)
        comp_arc2 = compass_arc_between(P5_coord, P3_coord, P5_coord, angle=PI/2.5, color=WHITE, stroke_width=2)
        self.play(Create(comp_arc1), Create(comp_arc2))

        # Calculate P4 coordinate (midpoint of arc P3P5)
        angle_P3 = angle_of_vector(P3_coord)
        angle_P5 = angle_of_vector(P5_coord)
        angle_P4 = (angle_P3 + angle_P5) / 2
        P4_coord = R * np.array([np.cos(angle_P4), np.sin(angle_P4), 0])
        P4 = Dot(P4_coord, color=GREEN)
        P4_label = MathTex("P_4").move_to(P4_coord + 0.2*normalize(P4_coord))

        # Bisector line (visual only)
        bisector_line_P3P5 = Line(O, P4_coord*1.1, color=WHITE, stroke_width=1, stroke_opacity=0.7)
        self.play(Create(bisector_line_P3P5))
        self.play(FadeIn(P4), Write(P4_label))
        self.play(FadeOut(comp_arc1), FadeOut(comp_arc2), FadeOut(arc_P3P5), FadeOut(bisector_line_P3P5))
        self.play(FadeOut(bisect_arc_text))
        self.wait(1)

        # Bisect arc P0 P4 to get P2
        bisect_arc_text = Text("Bisect arc P₀P₄ → P₂", font_size=20, color=YELLOW).next_to(step7_text, DOWN)
        self.play(Write(bisect_arc_text))
        arc_P0P4 = ArcBetweenPoints(P0_coord, P4_coord, radius=R, color=YELLOW)
        self.play(Create(arc_P0P4))
        comp_arc1 = compass_arc_between(P0_coord, P4_coord, P0_coord, angle=-PI/2.5, color=WHITE, stroke_width=2)
        comp_arc2 = compass_arc_between(P4_coord, P0_coord, P4_coord, angle=PI/2.5, color=WHITE, stroke_width=2)
        self.play(Create(comp_arc1), Create(comp_arc2))

        angle_P0 = angle_of_vector(P0_coord) # Should be 0
        angle_P2 = (angle_P0 + angle_P4) / 2
        P2_coord = R * np.array([np.cos(angle_P2), np.sin(angle_P2), 0])
        P2 = Dot(P2_coord, color=GREEN)
        P2_label = MathTex("P_2").move_to(P2_coord + 0.2*normalize(P2_coord))
        bisector_line_P0P4 = Line(O, P2_coord*1.1, color=WHITE, stroke_width=1, stroke_opacity=0.7)
        self.play(Create(bisector_line_P0P4))
        self.play(FadeIn(P2), Write(P2_label))
        self.play(FadeOut(comp_arc1), FadeOut(comp_arc2), FadeOut(arc_P0P4), FadeOut(bisector_line_P0P4))
        self.play(FadeOut(bisect_arc_text))
        self.wait(1)

        # Bisect arc P0 P2 to get P1
        bisect_arc_text = Text("Bisect arc P₀P₂ → P₁ (First Vertex!)", font_size=20, color=YELLOW).next_to(step7_text, DOWN)
        self.play(Write(bisect_arc_text))
        arc_P0P2 = ArcBetweenPoints(P0_coord, P2_coord, radius=R, color=YELLOW)
        self.play(Create(arc_P0P2))
        comp_arc1 = compass_arc_between(P0_coord, P2_coord, P0_coord, angle=-PI/2.5, color=WHITE, stroke_width=2)
        comp_arc2 = compass_arc_between(P2_coord, P0_coord, P2_coord, angle=PI/2.5, color=WHITE, stroke_width=2)
        self.play(Create(comp_arc1), Create(comp_arc2))

        angle_P1 = (angle_P0 + angle_P2) / 2 # This is 2*PI/17
        P1_coord = R * np.array([np.cos(angle_P1), np.sin(angle_P1), 0])
        P1 = Dot(P1_coord, color=RED) # Highlight P1
        P1_label = MathTex("P_1").move_to(P1_coord + 0.2*normalize(P1_coord))
        bisector_line_P0P2 = Line(O, P1_coord*1.1, color=WHITE, stroke_width=1, stroke_opacity=0.7)
        self.play(Create(bisector_line_P0P2))
        self.play(FadeIn(P1), Write(P1_label))
        self.play(FadeOut(comp_arc1), FadeOut(comp_arc2), FadeOut(arc_P0P2), FadeOut(bisector_line_P0P2))
        self.play(FadeOut(bisect_arc_text))
        self.wait(2)
        self.play(FadeOut(step7_text))


        # --- Step 8: Complete the 17-gon ---
        step8_text = Text("8. Use chord P₀P₁ to mark remaining vertices.", font_size=24).to_edge(UP)
        self.play(Write(step8_text))

        # Calculate chord length P0P1
        chord_len_P0P1 = np.linalg.norm(P1_coord - P0_coord)

        # Show setting the compass
        compass_base = P0.copy()
        compass_tip = P1.copy()
        compass_line = Line(compass_base.get_center(), compass_tip.get_center(), color=WHITE, stroke_width=2)
        self.play(Create(compass_line))
        self.wait(0.5)
        # Simulate picking up the compass
        self.play(compass_line.animate.shift(UP*0.5 + LEFT*0.5), compass_base.animate.shift(UP*0.5 + LEFT*0.5), compass_tip.animate.shift(UP*0.5 + LEFT*0.5))
        self.wait(0.5)
        # Place compass at P1
        self.play(compass_base.animate.move_to(P1_coord), compass_tip.animate.move_to(P1_coord + (P1_coord-P0_coord)), compass_line.animate.put_start_and_end_on(P1_coord, P1_coord + (P1_coord-P0_coord)))
        self.wait(0.5)

        # Mark remaining vertices using the angle step (2*PI/17)
        vertices_coords = [P0_coord]
        vertices_dots = VGroup(P0)
        # Keep existing dots P1, P2, P3, P4, P5
        existing_dots = {
            1: (P1, P1_label), 2: (P2, P2_label), 3: (P3, P3_label),
            4: (P4, P4_label), 5: (P5, P5_label)
        }

        all_vertices_coords = []
        all_vertices_dots = VGroup()
        all_vertices_labels = VGroup()

        for i in range(17):
            angle = i * (2 * PI / 17)
            coord = R * np.array([np.cos(angle), np.sin(angle), 0])
            all_vertices_coords.append(coord)
            if i == 0:
                dot = P0
                label = P0_label
            elif i in existing_dots:
                dot, label = existing_dots[i]
            else:
                dot = Dot(coord, color=GREEN)
                label = MathTex(f"P_{{{i}}}", font_size=18).move_to(coord + 0.2*normalize(coord))

            all_vertices_dots.add(dot)
            all_vertices_labels.add(label)

        # Animate marking points sequentially (simulated)
        anims = []
        temp_arcs = VGroup()
        for i in range(1, 17):
            start_point = all_vertices_coords[i-1]
            end_point = all_vertices_coords[i]
            # Simulate compass swing
            arc = Arc(radius=chord_len_P0P1, arc_center=start_point, start_angle=angle_of_vector(end_point-start_point)-PI/12, angle=PI/6, color=WHITE, stroke_width=1)
            temp_arcs.add(arc)
            # Only create new dots/labels
            if i not in existing_dots and i != 0:
                 anims.extend([Create(arc), FadeIn(all_vertices_dots[i]), Write(all_vertices_labels[i], run_time=0.2)])

        # Fade out compass visualizer
        self.play(FadeOut(compass_base), FadeOut(compass_tip), FadeOut(compass_line))
        # Play marking animations
        self.play(AnimationGroup(*anims, lag_ratio=0.1))
        self.wait(0.5)
        self.play(FadeOut(temp_arcs))

        # Connect vertices
        heptadecagon = Polygon(*all_vertices_coords, color=final_polygon_color, fill_opacity=0.3, stroke_width=3)
        connect_text = Text("Connect the vertices P₀, P₁, ..., P₁₆", font_size=20).next_to(step8_text, DOWN)
        self.play(Write(connect_text))
        self.play(Create(heptadecagon))
        self.wait(2)

        self.play(FadeOut(step8_text), FadeOut(connect_text))
        self.play(FadeOut(all_vertices_labels)) # Remove vertex labels for clarity

        # --- Conclusion ---
        final_title = Text("The Regular Heptadecagon", color=final_polygon_color).scale(1.2)
        final_subtitle = Text("Constructed with Compass and Straightedge", font_size=30).next_to(final_title, DOWN)

        # Fade out construction lines leaving just the polygon
        self.play(FadeOut(base_elements), FadeOut(A_prime), # Fade all initial setup
                #   FadeOut(all_vertices_dots), # Keep dots or fade them? Keep for now.
                  FadeOut(J), FadeOut(J_label), FadeOut(E), FadeOut(E_label), # Ensure all construction points are gone
                  FadeOut(F), FadeOut(F_label), FadeOut(K), FadeOut(K_label),
                  FadeOut(N3), FadeOut(N3_label), FadeOut(N5), FadeOut(N5_label))

        self.play(Write(final_title.to_edge(UP)))
        self.play(Write(final_subtitle))

        self.wait(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects]) # Fade everything out


