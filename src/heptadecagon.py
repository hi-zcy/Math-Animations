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
    
import math
import numpy as np

class HeptadecagonConstruction(Scene):
    def construct(self):
        # Title and introduction
        title = Text("Construction of a Regular Heptadecagon", font_size=36)
        subtitle = Text("Gauss's Compass-and-Straightedge Construction", font_size=24)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Construction begins
        construction_title = Text("Step-by-Step Construction of 17-gon", font_size=32)
        self.play(Write(construction_title))
        self.play(construction_title.animate.to_edge(UP))
        
        # Initialize all elements we'll reuse
        O = Dot(ORIGIN, color=WHITE)
        O_label = Tex("O", font_size=24).next_to(O, DL, buff=0.1)
        circle = Circle(radius=3, color=BLUE)
        V = Dot(circle.point_at_angle(0), color=RED)
        V_label = Tex("V", font_size=24).next_to(V, RIGHT, buff=0.1)
        
        # Step 1: Draw main circle and points O, V
        step_text = Text("1. Draw main circle with center O and vertex V", font_size=24, color=YELLOW)
        step_text.to_edge(DOWN)
        
        self.play(Write(step_text))
        self.play(Create(circle), Create(O), Write(O_label))
        self.play(Create(V), Write(V_label))
        self.wait(2)
        
        # Step 2: Find point A perpendicular to OV
        new_step = Text("2. Find point A where OA ⊥ OV", font_size=24, color=YELLOW)
        new_step.to_edge(DOWN)
        
        A = Dot(circle.point_at_angle(PI/2), color=GREEN)
        A_label = Tex("A", font_size=24).next_to(A, UP, buff=0.1)
        OA = Line(O.get_center(), A.get_center(), color=YELLOW)
        
        self.play(Transform(step_text, new_step))
        self.play(Create(A), Write(A_label), Create(OA))
        self.wait(2)
        
        # Step 3: Find point B on OA such that OB = 1/4 OA
        new_step = Text("3. Find B where OB = 1/4 OA", font_size=24, color=YELLOW)
        new_step.to_edge(DOWN)
        
        B_pos = OA.point_from_proportion(0.25)
        B = Dot(B_pos, color=PINK)
        B_label = Tex("B", font_size=24).next_to(B, LEFT, buff=0.1)
        OB = Line(O.get_center(), B.get_center(), color=PINK)
        
        self.play(Transform(step_text, new_step))
        self.play(Create(B), Write(B_label), Create(OB))
        self.wait(2)
        
        # Step 4: Find point C on OV such that ∠OBC = 1/4 ∠OBV
        new_step = Text("4. Find C on OV where ∠OBC = 1/4 ∠OBV", font_size=24, color=YELLOW)
        new_step.to_edge(DOWN)
        
        angle_OBV = PI/2
        target_angle = angle_OBV / 4
        OB_length = np.linalg.norm(B.get_center() - O.get_center())
        C_y = OB_length * math.tan(target_angle)
        C_pos = [0, C_y, 0]
        C = Dot(C_pos, color=ORANGE)
        C_label = Tex("C", font_size=24).next_to(C, RIGHT, buff=0.1)
        OV_line = Line(O.get_center(), V.get_center())
        BC = Line(B.get_center(), C.get_center(), color=ORANGE)
        
        angle_arc = Angle(OB, BC, radius=0.5, other_angle=False, color=GREEN)
        angle_label = MathTex(r"\frac{\theta}{4}", font_size=20).move_to(
            Angle(OB, BC, radius=0.7, other_angle=False).point_from_proportion(0.5)
        )
        
        self.play(Transform(step_text, new_step))
        self.play(Create(C), Write(C_label), Create(BC))
        self.play(Create(angle_arc), Write(angle_label))
        self.wait(3)
        
        # Step 5: Find point D on OV extended such that ∠DBC = π/4
        new_step = Text("5. Find D on OV extended where ∠DBC = 45°", font_size=24, color=YELLOW)
        new_step.to_edge(DOWN)
        
        # Calculate D position using trigonometry
        CB_vec = B.get_center() - C.get_center()
        CB_angle = math.atan2(CB_vec[1], CB_vec[0])
        BD_angle = CB_angle - PI/4  # 45 degrees clockwise from CB
        slope_BD = math.tan(BD_angle)
        
        # Find intersection of BD with OV line (x=0)
        if abs(slope_BD) > 1e-6:
            x_D = 0
            y_D = B.get_center()[1] + slope_BD * (x_D - B.get_center()[0])
            D_pos = [x_D, y_D, 0]
        else:
            D_pos = [0, B.get_center()[1], 0]
        
        D = Dot(D_pos, color=PURPLE)
        D_label = Tex("D", font_size=24).next_to(D, RIGHT, buff=0.1)
        BD = DashedLine(B.get_center(), D_pos, color=PURPLE)
        
        # Right angle marker
        right_angle = RightAngle(
            BC, BD, length=0.4, quadrant=(-1,1), color=YELLOW
        )
        
        self.play(Transform(step_text, new_step))
        self.play(Create(D), Write(D_label), Create(BD))
        self.play(Create(right_angle))
        self.wait(3)
        
        # Step 6: Draw circle on DV and find point E
        new_step = Text("6. Draw circle with diameter DV, find intersection E with OA", font_size=24, color=YELLOW)
        new_step.to_edge(DOWN)
        
        DV_midpoint = (D.get_center() + V.get_center()) / 2
        DV_length = np.linalg.norm(D.get_center() - V.get_center())
        DV_circle = Circle(radius=DV_length/2, color=GREEN)
        DV_circle.move_to(DV_midpoint)
        
        # Find intersection E with OA
        E_pos = line_circle_intersection(OA, DV_circle)[0]
        E = Dot(E_pos, color=TEAL)
        E_label = Tex("E", font_size=24).next_to(E, LEFT, buff=0.1)
        
        self.play(Transform(step_text, new_step))
        self.play(Create(DV_circle))
        self.play(Create(E), Write(E_label))
        self.wait(2)
        
        # Step 7: Draw circle centered at C through E, find F and G
        new_step = Text("7. Draw circle centered at C through E, find F and G on OV", font_size=24, color=YELLOW)
        new_step.to_edge(DOWN)
        
        CE_radius = np.linalg.norm(E_pos - C.get_center())
        CE_circle = Circle(radius=CE_radius, color=ORANGE)
        CE_circle.move_to(C.get_center())
        
        # Find intersections with OV
        OV_infinite = Line(O.get_center(), O.get_center() + DOWN * 5)
        F_pos, G_pos = line_circle_intersection(OV_infinite, CE_circle)
        F = Dot(F_pos, color=MAROON)
        F_label = Tex("F", font_size=24).next_to(F, LEFT, buff=0.1)
        G = Dot(G_pos, color=MAROON)
        G_label = Tex("G", font_size=24).next_to(G, LEFT, buff=0.1)
        
        self.play(Transform(step_text, new_step))
        self.play(Create(CE_circle))
        self.play(Create(F), Write(F_label), Create(G), Write(G_label))
        self.wait(2)
        
        # Step 8: Find vertices V3 and V5
        new_step = Text("8. Erect perpendiculars at F and G to find vertices V3 and V5", font_size=24, color=YELLOW)
        new_step.to_edge(DOWN)
        
        # Perpendicular lines
        perp_F = Line(F_pos, [F_pos[0], circle.radius, 0], color=RED)
        perp_G = Line(G_pos, [G_pos[0], circle.radius, 0], color=RED)
        
        # Find intersections with main circle
        V3_pos = circle.point_at_angle(math.asin(F_pos[0]/circle.radius))
        V5_pos = circle.point_at_angle(math.asin(G_pos[0]/circle.radius))
        V3 = Dot(V3_pos, color=GOLD)
        V5 = Dot(V5_pos, color=GOLD)
        V3_label = Tex("V_3", font_size=24).next_to(V3, UR, buff=0.1)
        V5_label = Tex("V_5", font_size=24).next_to(V5, DR, buff=0.1)
        
        self.play(Transform(step_text, new_step))
        self.play(Create(perp_F), Create(perp_G))
        self.play(Create(V3), Write(V3_label), Create(V5), Write(V5_label))
        self.wait(3)
        
        # Final step: Complete the heptadecagon
        new_step = Text("9. Remaining vertices found by angle bisection", font_size=24, color=YELLOW)
        new_step.to_edge(DOWN)
        
        self.play(Transform(step_text, new_step))
        
        # Calculate all 17 vertices
        angle_V = 0
        angle_V3 = math.asin(F_pos[0]/circle.radius)
        angle_V5 = math.asin(G_pos[0]/circle.radius)
        
        vertices = []
        vertex_angles = []
        
        # Add known vertices
        vertex_angles.extend([angle_V, angle_V3, angle_V5])
        
        # Calculate remaining vertices by angle bisection
        vertex_angles.append((angle_V3 + angle_V5)/2)  # V4
        vertex_angles.append((angle_V + angle_V3)/2)   # V1
        vertex_angles.append((angle_V + vertex_angles[-1])/2)  # V2
        vertex_angles.append((angle_V5 + 2*PI)/2)      # V6 (wrap around)
        
        # Complete the set through symmetry
        for i in range(7, 17):
            if i % 2 == 1:  # Odd vertices
                base_idx = (i-3)//2
                new_angle = (vertex_angles[base_idx] + vertex_angles[base_idx+2])/2
            else:            # Even vertices
                base_idx = (i-4)//2
                new_angle = (vertex_angles[base_idx] + vertex_angles[base_idx+3])/2
            vertex_angles.append(new_angle)
        
        # Sort and remove duplicates
        vertex_angles = sorted(list(set(vertex_angles)))
        
        # Create all vertex dots
        for i, angle in enumerate(vertex_angles):
            pos = circle.point_at_angle(angle)
            v = Dot(pos, color=GOLD)
            if i in [0, 3, 5]:
                continue  # Already created
            vertices.append(v)
        
        # Draw the complete heptadecagon
        heptadecagon = Polygon(*[circle.point_at_angle(a) for a in vertex_angles], color=WHITE)
        
        self.play(Create(heptadecagon))
        self.play(LaggedStart(*[Create(v) for v in vertices], lag_ratio=0.1))
        self.wait(3)
        
        # Final message
        final_text = Text("Regular 17-gon Construction Complete!", font_size=36)
        self.play(FadeOut(step_text))
        self.play(Write(final_text))
        self.wait(3)
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])

def line_circle_intersection(line, circle):
    """Find intersection points between a line and circle"""
    # Line equation: p = p0 + t * d
    p0 = line.get_start()
    d = line.get_unit_vector()
    
    # Circle equation: |p - c|^2 = r^2
    c = circle.get_center()
    r = circle.radius
    
    # Solve quadratic equation
    delta_p = p0 - c
    a = np.dot(d, d)
    b = 2 * np.dot(d, delta_p)
    c_val = np.dot(delta_p, delta_p) - r**2
    
    discriminant = b**2 - 4*a*c_val
    if discriminant < 0:
        return []  # No intersection
    
    t1 = (-b + math.sqrt(discriminant)) / (2*a)
    t2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    return [p0 + t1 * d, p0 + t2 * d]