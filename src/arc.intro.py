from manim import *

class ARCIntro(Scene):
    def construct(self):
        # 第一部分：艺术元素 - 动态几何艺术
        colors = [BLUE, GREEN, YELLOW, RED]
        circles = VGroup()
        for i in range(12):
            circle = Circle(radius=0.5 + i*0.1, color=colors[i % 4], fill_opacity=0.1)
            circle.rotate(i * PI / 6)
            circles.add(circle)
        
        self.play(LaggedStart(
            *[Create(c) for c in circles],
            lag_ratio=0.1,
            run_time=2
        ))
        self.play(
            circles.animate.rotate(PI*2),
            run_time=3,
            rate_func=linear
        )
        self.play(FadeOut(circles))

        # 第二部分：现实生活 - 城市剪影
        buildings = VGroup()
        heights = [2, 2.5, 1.8, 3, 2.2, 1.5]
        for i, h in enumerate(heights):
            building = Rectangle(
                height=h, width=0.8, 
                fill_color=GREY_B, fill_opacity=1,
                stroke_width=0
            ).shift(RIGHT*(i - len(heights)/2))
            buildings.add(building)
        
        ground = Line(LEFT*5, RIGHT*5, color=GREEN).shift(DOWN*2)
        sun = Circle(radius=0.8, color=YELLOW, fill_opacity=1).shift(UP*1 + LEFT*3)
        
        self.play(
            DrawBorderThenFill(buildings),
            Create(ground),
            run_time=2
        )
        self.play(GrowFromCenter(sun))
        self.play(
            sun.animate.shift(RIGHT*6),
            run_time=3
        )
        self.play(FadeOut(Group(buildings, ground, sun)))

        # 第三部分：编程元素 - 代码动画
        code_str = '''def create_art():
    pattern = generate_fractal()
    render(pattern)

# Real-world connection
simulate_physics(artwork)

# Creative coding
apply_neural_style()'''
        
        code = Code(
            code=code_str,
            tab_width=4,
            background="rectangle",
            language="Python",
            font="Monospace",
            style="monokai"
        ).scale(0.7)
        
        self.play(Write(code), run_time=3)
        self.play(code.animate.shift(UP*1.5), run_time=1.5)
        
        # 第四部分：ARC标志组合（纯Manim图形）
        arc_text = Text("ARC", font="Sans Serif", weight=BOLD, gradient=(BLUE, GREEN, YELLOW))
        arc_text.scale(2)
        
        # 创建纯图形图标
        icons = VGroup()
        
        # 艺术图标：调色板（圆形+矩形）
        palette = VGroup(
            Circle(radius=0.4, color=WHITE, fill_opacity=1),
            Rectangle(width=0.3, height=0.6, fill_opacity=1, color=WHITE)
                .next_to(Circle().get_center(), RIGHT, buff=0)
        )
        # 添加颜料点
        paint_colors = [RED, BLUE, GREEN, YELLOW]
        for i, color in enumerate(paint_colors):
            dot = Dot(radius=0.15, color=color, fill_opacity=1)
            angle = i * PI/2
            dot.move_to(palette[0].get_center() + 0.25 * np.array([np.cos(angle), np.sin(angle), 0]))
            palette.add(dot)
        art_icon = palette.scale(0.8).next_to(arc_text, UP, buff=1)
        
        # 现实生活图标：地球（圆形+经纬线）
        earth = VGroup(
            Circle(radius=0.5, color=BLUE, fill_opacity=0.8),
            Arc(radius=0.5, angle=PI, color=GREEN).rotate(PI/2),
            Arc(radius=0.5, angle=PI, color=GREEN)
        )
        life_icon = earth.scale(0.8).next_to(arc_text, RIGHT, buff=1)
        
        # 编程图标：代码符号（两个尖括号）
        code_icon = VGroup(
            Polygon([-0.4,0,0], [0,-0.4,0], [0,0.4,0], color=PURPLE),
            Polygon([0.4,0,0], [0,-0.4,0], [0,0.4,0], color=PURPLE).flip(RIGHT)
        ).scale(0.8).next_to(arc_text, LEFT, buff=1)
        
        icons.add(art_icon, life_icon, code_icon)
        
        # 最终动画
        self.play(
            Transform(code, arc_text),
            FadeIn(icons)
        )
        
        # 添加动态旋转效果
        self.play(
            icons.animate.rotate(2*PI, about_point=arc_text.get_center()),
            run_time=4,
            rate_func=linear
        )
        
        subtitle = Text("Art · Real life · Coding", font_size=36).next_to(arc_text, DOWN)
        self.play(Write(subtitle))
        self.wait(2)
        
        # 结束动画：图标融合到文字中
        self.play(
            art_icon.animate.move_to(arc_text[0].get_center()),
            life_icon.animate.move_to(arc_text[1].get_center()),
            code_icon.animate.move_to(arc_text[2].get_center()),
            run_time=2
        )
        
        # 文字放大效果
        self.play(
            arc_text.animate.scale(1.5),
            FadeOut(subtitle),
            run_time=1.5
        )
        self.wait(2)