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
        # 设置场景参数
        self.camera.background_color = WHITE
        self.camera.frame_center = ORIGIN
        self.camera.frame_height = 10
        
        # 第一步：绘制基本构造
        self.add_title("第一步：基本构造")
        
        # 1. 作直径AP
        self.ap = Line(LEFT*2, RIGHT*2, color=BLUE)
        self.add(self.ap)
        self.wait(1)
        
        # 2. 作半径OB垂直于OP
        self.op = Line(ORIGIN, RIGHT*2, color=BLUE)
        self.add(self.op)
        
        self.ob = Line(ORIGIN, UP*2, color=BLUE)
        self.add(self.ob)
        self.wait(1)
        
        # 3. 在半径OB上取点C，使得OC为1/4 OB的长度
        point_c = Dot(UP*0.5, color=RED)
        self.add(point_c)
        
        label_c = Text("C", color=BLACK).next_to(point_c, UP*0.2)
        self.add(label_c)
        self.wait(1)
        
        # 4. 作CE与OP形成特定角度
        point_e = Dot(RIGHT*1.5, color=RED)
        self.add(point_e)
        
        label_e = Text("E", color=BLACK).next_to(point_e, RIGHT*0.2)
        self.add(label_e)
        
        ce = Line(point_c, point_e, color=RED)
        self.add(ce)
        self.wait(2)
        
        # 第二步：角度平分
        self.add_title("第二步：角度平分")
        
        # 5. 作∠CEB的平分线EF
        # 计算角平分线
        vector_ce = point_e - point_c
        vector_be = point_e - DOWN*2
        
        # 计算角平分线方向
        direction = normalize(vector_ce) + normalize(vector_be)
        direction = normalize(direction)
        
        # 从E点出发，沿着方向延伸
        point_f = Dot(point_e + direction*3, color=RED)
        self.add(point_f)
        
        label_f = Text("F", color=BLACK).next_to(point_f, direction*1.5)
        self.add(label_f)
        
        ef = Line(point_e, point_f, color=RED)
        self.add(ef)
        self.wait(2)
        
        # 6. 作∠FEB的平分线EG
        # 计算角平分线
        vector_ef = point_f - point_e
        vector_be = point_e - DOWN*2
        
        # 计算角平分线方向
        direction = normalize(vector_ef) + normalize(vector_be)
        direction = normalize(direction)
        
        # 从E点出发，沿着方向延伸
        point_g = Dot(point_e + direction*3, color=RED)
        self.add(point_g)
        
        label_g = Text("G", color=BLACK).next_to(point_g, direction*1.5)
        self.add(label_g)
        
        eg = Line(point_e, point_g, color=RED)
        self.add,eg)
        self.wait(2)
        
        # 第三步：构建辅助线
        self.add_title("第三步：构建辅助线")
        
        # 7. 作AE的中点M
        point_a = Dot(LEFT*2, color=RED)
        self.add(point_a)
        
        label_a = Text("A", color=BLACK).next_to(point_a, LEFT*0.2)
        self.add(label_a)
        
        ae = Line(point_a, point_e, color=RED)
        self.add(ae)
        
        point_m = Dot(midpoint(point_a, point_e), color=RED)
        self.add(point_m)
        
        label_m = Text("M", color=BLACK).next_to(point_m, RIGHT*0.2 + DOWN*0.2)
        self.add(label_m)
        self.wait(2)
        
        # 8. 以M为圆心作一个圆
        circle_m = Circle(radius=distance(point_m, point_a), color=RED).move_to(point_m)
        self.add(circle_m)
        self.wait(2)
        
        # 第四步：确定顶点
        self.add_title("第四步：确定顶点")
        
        # 9. 通过与圆的交点确定正17边形的顶点
        # 这里使用正17边形类来展示结果
        regular_17 = RegularPolygon(17, radius=2, color=GREEN)
        self.add(regular_17)
        self.wait(2)
        
        # 10. 依次连接各顶点，形成正17边形
        self.play(ShowCreation(regular_17))
        self.wait(3)
        
    def add_title(self, text):
        # 添加标题动画
        title = Text(text, font_size=24).to_edge(UP)
        self.play(FadeIn(title))
        self.wait(1)
        self.remove(title)
