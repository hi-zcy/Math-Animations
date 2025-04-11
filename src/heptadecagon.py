# RegularHeptadecagonConstruction
# To run this:
# 1. Make sure you have Manim installed (pip install manim)
# 2. Save this code as e.g., heptadecagon_construction.py
# 3. Run from the terminal: manim -pql heptadecagon_construction.py RegularHeptadecagonConstruction

try:
    from manim import *
except ImportError:
    try:
        from manimlib import *
    except ImportError:
        from manimgl import *

class RegularHeptadecagonConstruction(Scene):
    def construct(self):
        # 配置场景
        config["frame_rate"] = 30
        self.camera.set_zoom(1.5)
        
        # 步骤1：画圆O和两条互相垂直的直径AB和CD
        circle = Circle(radius=2, color="#000000")
        center = Dot(point=circle.get_center(), color="#000000")
        horizontal_diameter = Line(circle.get_left(), circle.get_right(), color="#000000")
        vertical_diameter = Line(circle.get_bottom(), circle.get_top(), color="#000000")
        
        # 添加标签
        label_O = Text("O", color="#000000").next_to(center, direction=DOWN, buff=0.2)
        label_A = Text("A", color="#000000").next_to(circle.get_right(), direction=RIGHT, buff=0.2)
        label_B = Text("B", color="#000000").next_to(circle.get_left(), direction=LEFT, buff=0.2)
        label_C = Text("C", color="#000000").next_to(circle.get_top(), direction=UP, buff=0.2)
        label_D = Text("D", color="#000000").next_to(circle.get_bottom(), direction=DOWN, buff=0.2)
        
        # 组合对象
        step1 = VGroup(
            circle, center, horizontal_diameter, vertical_diameter,
            label_O, label_A, label_B, label_C, label_D
        )
        
        # 显示步骤1
        self.play(FadeIn(step1))
        self.wait(2)
        
        # 步骤2：在OA上作点E，使OE = 1/4 AO，连接CE
        point_O = circle.get_center()
        point_A = circle.get_right()
        point_E = Dot(
            point=point_O + (point_A - point_O) * 0.25,
            color="#FF0000"
        )
        line_CE = Line(
            circle.get_top(), point_E.get_center(),
            color="#FF0000"
        )
        
        # 添加标签
        label_E = Text("E", color="#FF0000").next_to(point_E, direction=RIGHT, buff=0.2)
        
        # 显示步骤2
        self.play(FadeIn(point_E), FadeIn(line_CE), FadeIn(label_E))
        self.wait(2)
        
        # 步骤3：作∠CEB的平分线EF
        point_C = circle.get_top()
        point_E = point_E.get_center()
        point_B = circle.get_left()
        
        # 计算角度
        angle_CEB = Angle(
            Line(point_E, point_C), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#00FF00"
        )
        
        # 计算角平分线
        angle_half = angle_CEB.get_value() / 2
        direction = Line(point_E, point_C).get_unit_vector()
        point_F = Dot(
            point=point_E + direction * 2,
            color="#00FF00"
        )
        line_EF = Line(point_E, point_F.get_center(), color="#00FF00")
        
        # 添加标签
        label_F = Text("F", color="#00FF00").next_to(point_F, direction=UP, buff=0.2)
        
        # 显示步骤3
        self.play(FadeIn(angle_CEB), FadeIn(line_EF), FadeIn(point_F), FadeIn(label_F))
        self.wait(2)
        
        # 步骤4：作∠FEB的平分线EG
        point_F = point_F.get_center()
        
        # 计算角度
        angle_FEB = Angle(
            Line(point_E, point_F), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#0000FF"
        )
        
        # 计算角平分线
        angle_half = angle_FEB.get_value() / 2
        direction = Line(point_E, point_F).get_unit_vector()
        point_G = Dot(
            point=point_E + direction * 2,
            color="#0000FF"
        )
        line_EG = Line(point_E, point_G.get_center(), color="#0000FF")
        
        # 添加标签
        label_G = Text("G", color="#0000FF").next_to(point_G, direction=UP, buff=0.2)
        
        # 显示步骤4
        self.play(FadeIn(angle_FEB), FadeIn(line_EG), FadeIn(point_G), FadeIn(label_G))
        self.wait(2)
        
        # 步骤5：作∠GEB的平分线GH
        point_G = point_G.get_center()
        
        # 计算角度
        angle_GEB = Angle(
            Line(point_E, point_G), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#FF00FF"
        )
        
        # 计算角平分线
        angle_half = angle_GEB.get_value() / 2
        direction = Line(point_E, point_G).get_unit_vector()
        point_H = Dot(
            point=point_E + direction * 2,
            color="#FF00FF"
        )
        line_EH = Line(point_E, point_H.get_center(), color="#FF00FF")
        
        # 添加标签
        label_H = Text("H", color="#FF00FF").next_to(point_H, direction=UP, buff=0.2)
        
        # 显示步骤5
        self.play(FadeIn(angle_GEB), FadeIn(line_EH), FadeIn(point_H), FadeIn(label_H))
        self.wait(2)
        
        # 步骤6：作∠HEB的平分线HI
        point_H = point_H.get_center()
        
        # 计算角度
        angle_HEB = Angle(
            Line(point_E, point_H), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#00FFFF"
        )
        
        # 计算角平分线
        angle_half = angle_HEB.get_value() / 2
        direction = Line(point_E, point_H).get_unit_vector()
        point_I = Dot(
            point=point_E + direction * 2,
            color="#00FFFF"
        )
        line_EI = Line(point_E, point_I.get_center(), color="#00FFFF")
        
        # 添加标签
        label_I = Text("I", color="#00FFFF").next_to(point_I, direction=UP, buff=0.2)
        
        # 显示步骤6
        self.play(FadeIn(angle_HEB), FadeIn(line_EI), FadeIn(point_I), FadeIn(label_I))
        self.wait(2)
        
        # 步骤7：作∠IEB的平分线IJ
        point_I = point_I.get_center()
        
        # 计算角度
        angle_IEB = Angle(
            Line(point_E, point_I), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#FFA500"
        )
        
        # 计算角平分线
        angle_half = angle_IEB.get_value() / 2
        direction = Line(point_E, point_I).get_unit_vector()
        point_J = Dot(
            point=point_E + direction * 2,
            color="#FFA500"
        )
        line_EJ = Line(point_E, point_J.get_center(), color="#FFA500")
        
        # 添加标签
        label_J = Text("J", color="#FFA500").next_to(point_J, direction=UP, buff=0.2)
        
        # 显示步骤7
        self.play(FadeIn(angle_IEB), FadeIn(line_EJ), FadeIn(point_J), FadeIn(label_J))
        self.wait(2)
        
        # 步骤8：作∠JEB的平分线JK
        point_J = point_J.get_center()
        
        # 计算角度
        angle_JEB = Angle(
            Line(point_E, point_J), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#008000"
        )
        
        # 计算角平分线
        angle_half = angle_JEB.get_value() / 2
        direction = Line(point_E, point_J).get_unit_vector()
        point_K = Dot(
            point=point_E + direction * 2,
            color="#008000"
        )
        line_EK = Line(point_E, point_K.get_center(), color="#008000")
        
        # 添加标签
        label_K = Text("K", color="#008000").next_to(point_K, direction=UP, buff=0.2)
        
        # 显示步骤8
        self.play(FadeIn(angle_JEB), FadeIn(line_EK), FadeIn(point_K), FadeIn(label_K))
        self.wait(2)
        
        # 步骤9：作∠KEB的平分线KL
        point_K = point_K.get_center()
        
        # 计算角度
        angle_KEB = Angle(
            Line(point_E, point_K), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#800080"
        )
        
        # 计算角平分线
        angle_half = angle_KEB.get_value() / 2
        direction = Line(point_E, point_K).get_unit_vector()
        point_L = Dot(
            point=point_E + direction * 2,
            color="#800080"
        )
        line_EL = Line(point_E, point_L.get_center(), color="#800080")
        
        # 添加标签
        label_L = Text("L", color="#800080").next_to(point_L, direction=UP, buff=0.2)
        
        # 显示步骤9
        self.play(FadeIn(angle_KEB), FadeIn(line_EL), FadeIn(point_L), FadeIn(label_L))
        self.wait(2)
        
        # 步骤10：作∠LEB的平分线LM
        point_L = point_L.get_center()
        
        # 计算角度
        angle_LEB = Angle(
            Line(point_E, point_L), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#000080"
        )
        
        # 计算角平分线
        angle_half = angle_LEB.get_value() / 2
        direction = Line(point_E, point_L).get_unit_vector()
        point_M = Dot(
            point=point_E + direction * 2,
            color="#000080"
        )
        line_EM = Line(point_E, point_M.get_center(), color="#000080")
        
        # 添加标签
        label_M = Text("M", color="#000080").next_to(point_M, direction=UP, buff=0.2)
        
        # 显示步骤10
        self.play(FadeIn(angle_LEB), FadeIn(line_EM), FadeIn(point_M), FadeIn(label_M))
        self.wait(2)
        
        # 步骤11：作∠MEB的平分线MN
        point_M = point_M.get_center()
        
        # 计算角度
        angle_MEB = Angle(
            Line(point_E, point_M), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#800000"
        )
        
        # 计算角平分线
        angle_half = angle_MEB.get_value() / 2
        direction = Line(point_E, point_M).get_unit_vector()
        point_N = Dot(
            point=point_E + direction * 2,
            color="#800000"
        )
        line_EN = Line(point_E, point_N.get_center(), color="#800000")
        
        # 添加标签
        label_N = Text("N", color="#800000").next_to(point_N, direction=UP, buff=0.2)
        
        # 显示步骤11
        self.play(FadeIn(angle_MEB), FadeIn(line_EN), FadeIn(point_N), FadeIn(label_N))
        self.wait(2)
        
        # 步骤12：作∠NEB的平分线NO
        point_N = point_N.get_center()
        
        # 计算角度
        angle_NEB = Angle(
            Line(point_E, point_N), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#008080"
        )
        
        # 计算角平分线
        angle_half = angle_NEB.get_value() / 2
        direction = Line(point_E, point_N).get_unit_vector()
        point_O = Dot(
            point=point_E + direction * 2,
            color="#008080"
        )
        line_EO = Line(point_E, point_O.get_center(), color="#008080")
        
        # 添加标签
        label_O_step12 = Text("O", color="#008080").next_to(point_O, direction=UP, buff=0.2)
        
        # 显示步骤12
        self.play(FadeIn(angle_NEB), FadeIn(line_EO), FadeIn(point_O), FadeIn(label_O_step12))
        self.wait(2)
        
        # 步骤13：作∠OEB的平分线OP
        point_O = point_O.get_center()
        
        # 计算角度
        angle_OEB = Angle(
            Line(point_E, point_O), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#808000"
        )
        
        # 计算角平分线
        angle_half = angle_OEB.get_value() / 2
        direction = Line(point_E, point_O).get_unit_vector()
        point_P = Dot(
            point=point_E + direction * 2,
            color="#808000"
        )
        line_EP = Line(point_E, point_P.get_center(), color="#808000")
        
        # 添加标签
        label_P = Text("P", color="#808000").next_to(point_P, direction=UP, buff=0.2)
        
        # 显示步骤13
        self.play(FadeIn(angle_OEB), FadeIn(line_EP), FadeIn(point_P), FadeIn(label_P))
        self.wait(2)
        
        # 步骤14：作∠PEB的平分线PQ
        point_P = point_P.get_center()
        
        # 计算角度
        angle_PEB = Angle(
            Line(point_E, point_P), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#0000FF"
        )
        
        # 计算角平分线
        angle_half = angle_PEB.get_value() / 2
        direction = Line(point_E, point_P).get_unit_vector()
        point_Q = Dot(
            point=point_E + direction * 2,
            color="#0000FF"
        )
        line_EQ = Line(point_E, point_Q.get_center(), color="#0000FF")
        
        # 添加标签
        label_Q = Text("Q", color="#0000FF").next_to(point_Q, direction=UP, buff=0.2)
        
        # 显示步骤14
        self.play(FadeIn(angle_PEB), FadeIn(line_EQ), FadeIn(point_Q), FadeIn(label_Q))
        self.wait(2)
        
        # 步骤15：作∠QEB的平分线QR
        point_Q = point_Q.get_center()
        
        # 计算角度
        angle_QEB = Angle(
            Line(point_E, point_Q), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#FF0000"
        )
        
        # 计算角平分线
        angle_half = angle_QEB.get_value() / 2
        direction = Line(point_E, point_Q).get_unit_vector()
        point_R = Dot(
            point=point_E + direction * 2,
            color="#FF0000"
        )
        line_ER = Line(point_E, point_R.get_center(), color="#FF0000")
        
        # 添加标签
        label_R = Text("R", color="#FF0000").next_to(point_R, direction=UP, buff=0.2)
        
        # 显示步骤15
        self.play(FadeIn(angle_QEB), FadeIn(line_ER), FadeIn(point_R), FadeIn(label_R))
        self.wait(2)
        
        # 步骤16：作∠REB的平分线RS
        point_R = point_R.get_center()
        
        # 计算角度
        angle_REB = Angle(
            Line(point_E, point_R), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#00FF00"
        )
        
        # 计算角平分线
        angle_half = angle_REB.get_value() / 2
        direction = Line(point_E, point_R).get_unit_vector()
        point_S = Dot(
            point=point_E + direction * 2,
            color="#00FF00"
        )
        line_ES = Line(point_E, point_S.get_center(), color="#00FF00")
        
        # 添加标签
        label_S = Text("S", color="#00FF00").next_to(point_S, direction=UP, buff=0.2)
        
        # 显示步骤16
        self.play(FadeIn(angle_REB), FadeIn(line_ES), FadeIn(point_S), FadeIn(label_S))
        self.wait(2)
        
        # 步骤17：作∠SEB的平分线ST
        point_S = point_S.get_center()
        
        # 计算角度
        angle_SEB = Angle(
            Line(point_E, point_S), Line(point_E, point_B),
            vertex=point_E, radius=0.5, color="#FF00FF"
        )
        
        # 计算角平分线
        angle_half = angle_SEB.get_value() / 2
        direction = Line(point_E, point_S).get_unit_vector()
        point_T = Dot(
            point=point_E + direction * 2,
            color="#FF00FF"
        )
        line_ET = Line(point_E, point_T.get_center(), color="#FF00FF")
        
        # 添加标签
        label_T = Text("T", color="#FF00FF").next_to(point_T, direction=UP, buff=0.2)
        
        # 显示步骤17
        self.play(FadeIn(angle_SEB), FadeIn(line_ET), FadeIn(point_T), FadeIn(label_T))
        self.wait(2)
