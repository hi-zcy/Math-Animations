from manim import *

class ARCIntro(ThreeDScene):
    def construct(self):
        # 配置
        self.camera.background_color = "#1e1e1e"
        logo_blue = "#3498db"
        logo_purple = "#9b59b6"
        
        # 创建代码背景
        code_background = Rectangle(
            width=14, height=8, 
            fill_color="#2c3e50", 
            fill_opacity=0.8, 
            stroke_color="#34495e",
            stroke_width=2
        )
        
        # 创建动态代码
        code_lines = [
            "def create_art():",
            "    particles = []",
            "    for i in range(1000):",
            "        p = Particle()",
            "        p.color = gradient(HSV)",
            "        p.apply_force(vector_field)",
            "        particles.append(p)",
            "    return particles",
            "",
            "class AlgorithmicArt:",
            "    def __init__(self, complexity):",
            "        self.fractals = generate_fractals(complexity)",
            "        self.transform()",
            "",
            "render(AlgorithmicArt(11))"
        ]
        
        # 修正：使用code_string参数代替code
        code = Code(
            code_string="\n".join(code_lines),  # 修正这里
            tab_width=4,
            insert_line_no=False,
            style="monokai",
            font="Monospace",
            language="python",
            line_spacing=0.5,
            font_size=16,
        ).scale(0.7)
        
        # 初始动画 - 代码显示
        self.play(DrawBorderThenFill(code_background))
        self.play(Write(code), run_time=3)
        self.wait(1)
        
        # 代码转化为几何形状
        self.play(
            code.animate.scale(0.7).to_edge(LEFT, buff=1),
            code_background.animate.scale(0.7).to_edge(LEFT, buff=1)
        )
        
        # 创建3D几何体
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=2)
        
        # 创建旋转的几何体
        cube = Cube(side_length=2, fill_color=logo_blue, 
                   fill_opacity=0.8, stroke_color=WHITE)
        sphere = Sphere(radius=1.2, resolution=(24,24), 
                       fill_color=logo_purple, fill_opacity=0.9)
        torus = Torus(major_radius=1.5, minor_radius=0.5, 
                     fill_color="#e74c3c", fill_opacity=0.7)
        
        # 几何体组
        geometric_group = VGroup(cube, sphere, torus).arrange(RIGHT, buff=2).shift(RIGHT*3)
        
        # 几何体动画
        self.play(
            FadeIn(cube),
            Rotate(cube, axis=UP, angle=TAU, run_time=3, rate_func=smooth)
        )
        self.play(
            FadeIn(sphere),
            Rotate(sphere, axis=RIGHT, angle=TAU, run_time=3, rate_func=smooth)
        )
        self.play(
            FadeIn(torus),
            Rotate(torus, axis=OUT, angle=TAU, run_time=3, rate_func=smooth)
        )
        self.wait(0.5)
        
        # 连接代码和几何的线条
        connecting_lines = VGroup()
        for i in range(8):
            start = code.get_corner(UR) + [0, -i*0.2, 0]
            end = cube.get_left() + [0, 0.5 - i*0.1, 0]
            line = Line(start, end, stroke_width=2, stroke_color=BLUE)
            connecting_lines.add(line)
        
        self.play(
            Create(connecting_lines),
            run_time=2
        )
        self.wait(1)
        
        # 创建ARC文字
        arc_text = Text("ARC", font="Arial Rounded MT Bold", 
                        weight=BOLD, gradient=(logo_blue, logo_purple))
        arc_text.scale(3)
        
        subtitle = Text("Art of Coding", font="Arial", 
                        color=WHITE, font_size=36)
        subtitle.next_to(arc_text, DOWN, buff=0.5)
        
        # 文字动画
        self.play(
            FadeOut(connecting_lines),
            FadeOut(geometric_group),
            FadeOut(code),
            FadeOut(code_background),
            FadeIn(arc_text, shift=UP),
            Write(subtitle),
            run_time=2
        )
        
        # 文字特效
        self.play(
            arc_text.animate.scale(1.2),
            subtitle.animate.scale(1.1),
            run_time=1.5,
            rate_func=there_and_back
        )
        
        # 最终光效
        glow = VGroup()
        colors = [logo_blue, logo_purple, "#e74c3c", "#2ecc71"]
        for i in range(20):
            circle = Circle(radius=0.5 + i*0.2, 
                          stroke_width=0.5 + i*0.1,
                          stroke_opacity=1.0 - i*0.05)
            circle.set_stroke(color=random.choice(colors), width=circle.stroke_width)
            glow.add(circle)
        
        glow.move_to(arc_text)
        self.play(
            LaggedStart(
                *[Create(g) for g in glow],
                lag_ratio=0.1
            ),
            run_time=3
        )
        
        # 渐变消失
        self.play(
            FadeOut(glow),
            FadeOut(arc_text),
            FadeOut(subtitle),
            run_time=2
        )
        
        self.wait(2)