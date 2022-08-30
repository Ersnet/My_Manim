from manimlib import *
import random


class demo1(Scene):
    def construct(self):
        pos = [UP, DOWN, LEFT, RIGHT, UR, UL, DR, DL]
        cir1 = Circle(radius=2, color=BLUE)
        tex1 = MTex("{n}={50}", tex_to_color_map={"{n}": BLUE_D, "{50}": RED}).shift(UP*3)
        
        self.play(SpinInFromNothing(cir1), Write(tex1))
        
        def love(n, p):
            dot_group = VGroup()
            for i in np.arange(0, TAU, TAU/n):
                dot = SmallDot(np.array([2*np.cos(i)+p, 2*np.sin(i), 0])).set_color(RED).scale(0.5)
                dot_group.add(dot)
        
            line_group = VGroup()
            for i in range(len(dot_group)):
                if 2*i+1 < len(dot_group):
                    line = Line(dot_group[i].get_center(), dot_group[2*i+1].get_center(), stroke_width=0.8).set_color(RED)
                    line_group.add(line)
                else:
                    line = Line(dot_group[i].get_center(), dot_group[(2*i+1)%(len(dot_group))].get_center(), stroke_width=0.8).set_color(RED)
                    line_group.add(line)
            return dot_group, line_group
        
        dot_group1, line_group1 = love(50, 0)
        dot_group2, line_group2 = love(114, -4.5)
        dot_group3, line_group3 = love(520, 4.5)
        cir2 = Circle(radius=2, color=BLUE).shift(np.array([-4.5, 0, 0]))
        cir3 = Circle(radius=2, color=BLUE).shift(np.array([4.5, 0, 0]))
        tex2 = MTex("{n}={114}", tex_to_color_map={"{n}": BLUE_D, "{114}": RED}).shift(UP*3 + LEFT*4.5)
        tex3 = MTex("{n}={520}", tex_to_color_map={"{n}": BLUE_D, "{520}": RED}).shift(UP*3 + RIGHT*4.5)
        
        self.play(LaggedStart(*[FadeIn(i, shift=random.choice(pos)*2) for i in dot_group1]), run_time=5)
        self.play(LaggedStart(*[FadeIn(i, shift=random.choice(pos)*2) for i in line_group1]), run_time=5)
        self.play(LaggedStart(*[
            ReplacementTransform(cir1.copy(), cir2), 
            ReplacementTransform(line_group1.copy(), line_group2), 
            ReplacementTransform(dot_group1.copy(), dot_group2), 
            ReplacementTransform(cir1.copy(), cir3), 
            ReplacementTransform(line_group1.copy(), line_group3), 
            ReplacementTransform(dot_group1.copy(), dot_group3),
            FadeTransformPieces(tex1.copy(), tex2), 
            FadeTransformPieces(tex1.copy(), tex3),
        ]))
        self.wait(1)
        

class demo2(Scene):
    def construct(self):
        cir = Circle(radius=2, color=BLUE)
        dot_O = SmallDot(cir.get_center())
        dot_P = SmallDot(np.array([1, 1, 0]))

        self.play(LaggedStart(*[Write(cir), FadeIn(dot_O), FadeIn(dot_P)]))

        line_group = VGroup()
        for i in np.arange(0, TAU, TAU/100):
            line = Line(dot_P.get_center(), np.array([2*np.cos(i), 2*np.sin(i), 0]), stroke_width=0.8).set_color(RED)
            line_group.add(line)
        
        self.play(*[GrowFromCenter(i) for i in line_group])
        self.play(LaggedStart(*[i.animate.rotate(angle=PI/2, about_point=i.get_center()) for i in line_group]))
        self.wait(0.5)

class demo3(Scene):
    def t_func1(self, t):
            a, b = 3, 3
            return np.array([
            a * np.cos(t) / t,
            b * np.sin(t) / t,
            0
        ])
    
    def construct(self):
        def fib(n):
            fibs = [1, 1]
            for i in range(2, n):
                fibs.append(fibs[-1] + fibs[-2])
            return fibs

        fibs = fib(7)
        frame = self.camera.frame

        s1 = Square(side_length=fibs[0]*0.4).set_color(BLUE_D)
        s2 = Square(side_length=fibs[1]*0.4).shift(np.array([0, 0.4, 0])).set_color(TEAL_D)
        s3 = Square(side_length=fibs[2]*0.4).shift(np.array([0.6, 0.2, 0])).set_color(GREEN_D)
        s4 = Square(side_length=fibs[3]*0.4).shift(np.array([0.4, 1.2, 0])).set_color(YELLOW_D)
        s5 = Square(side_length=fibs[4]*0.4).shift(np.array([-1.2, 0.8, 0])).set_color(GOLD_D)
        s6 = Square(side_length=fibs[5]*0.4).shift(np.array([-0.6, -1.8, 0])).set_color(RED_D)
        s7 = Square(side_length=fibs[6]*0.4).shift(np.array([3.6, -0.8, 0])).set_color(PURPLE_D)
        
        a1 = Arc(radius=fibs[0]*0.4, start_angle=-PI, arc_center=np.array([0.2, 0.2, 0])).set_color(MAROON_D)
        a2 = Arc(radius=fibs[1]*0.4, start_angle=PI/2, arc_center=np.array([0.2, 0.2, 0])).set_color(MAROON_D)
        a3 = Arc(radius=fibs[2]*0.4, start_angle=-PI/2, arc_center=np.array([0.2, 0.6, 0])).set_color(MAROON_D)
        a4 = Arc(radius=fibs[3]*0.4, start_angle=0, arc_center=np.array([-0.2, 0.6, 0])).set_color(MAROON_D)
        a5 = Arc(radius=fibs[4]*0.4, start_angle=PI/2, arc_center=np.array([-0.2, -0.2, 0])).set_color(MAROON_D)
        a6 = Arc(radius=fibs[5]*0.4, start_angle=-PI, arc_center=np.array([1, -0.2, 0])).set_color(MAROON_D)
        a7 = Arc(radius=fibs[6]*0.4, start_angle=-PI/2, arc_center=np.array([1, 1.8, 0])).set_color(MAROON_D)
        
        s_g = VGroup(s1, s2, s3, s4, s5, s6, s7).shift(LEFT*1.5 + UP*0.5)
        a_g = VGroup(a1, a2, a3, a4, a5, a6, a7).shift(LEFT*1.5 + UP*0.5)
        
        self.play(LaggedStart(*[GrowFromCenter(i) for i in s_g]))
        self.play(LaggedStart(*[FadeIn(i, shift=UP*2) for i in a_g]))
        self.play(LaggedStart(*[FadeOut(i, shift=UP*2) for i in s_g]))

        curve1 = ParametricCurve(self.t_func1, t_range=[0.1, 100, 0.05], color=MAROON_D)
        curve2 = FunctionGraph(lambda x: np.sin(x), color=MAROON_D)
        curve3 = FunctionGraph(lambda x: np.sin(2*x)+np.cos(x), color=MAROON_D)
        curve4 = FunctionGraph(lambda x: np.sin(2*x)+np.cos(x)+np.cos(3*x), color=MAROON_D)
        curve5 = FunctionGraph(lambda x: np.sin(2*x)+np.cos(x)+np.cos(3*x)+np.tan(x), color=MAROON_D)

        self.play(FadeTransform(a_g, curve1))
        self.play(
            curve1.animate.set_stroke(width=0.3),       
            frame.animate.rotate(PI / 2).set_width(2),
        )
        self.play(FadeTransform(curve1, curve2), frame.animate.to_default_state())
        self.play(FadeTransform(curve2, curve3))
        self.play(FadeTransform(curve3, curve4))
        self.play(FadeTransform(curve4, curve5))

class demo4(Scene):
    def construct(self):
        def get_distance_between_two_points(pos1, pos2):
            x1 = pos1.get_center()[0]
            y1 = pos1.get_center()[1]
            x2 = pos2.get_center()[0]
            y2 = pos2.get_center()[1]
            return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

        cir1 = Circle(radius=1, color=BLUE)
        dot_p = Dot(np.array([0, 1, 0]))
        self.play(SpinInFromNothing(cir1))

        dot_group = VGroup()
        for i in np.arange(0, TAU, TAU/36):
            dot = SmallDot(np.array([np.cos(i), np.sin(i), 0]))
            dot_group.add(dot)
        
        cir_group = VGroup()
        for i in dot_group:
            cir = Circle(radius=get_distance_between_two_points(dot_p, i)).shift(i.get_center())
            cir_group.add(cir)

        self.play(LaggedStart(*[GrowFromCenter(i) for i in cir_group]))
        self.wait(0.5)

class demo5(Scene):
    def construct(self):
        text1 = Text("数 学 de 美", font="IPix", font_size=120).shift(UP*0.5)
        text2 = Text("the beauty of mathematics", font="IPix").shift(DOWN)
        text3 = Text("By Ersnet.", font="IPix").to_corner(DR)

        self.play(LaggedStart(*[FadeIn(i) for i in text1], *[FadeIn(i) for i in text2]), run_time=3)
        self.play(LaggedStart(*[FadeIn(i, shift=UP) for i in text3]), run_time=2)
        self.wait(2)

class demo6(Scene):
    def construct(self):
        value = ValueTracker()
        func = FunctionGraph(lambda x: (x**2)**(1/3)+.9*np.sqrt(abs(8-x*x))*np.sin(
            value.get_value()*x), x_range=[-np.sqrt(8), np.sqrt(8), 0.001]).set_color(RED)
        
        self.play(ShowCreation(VGroup(func)))
        
        func.add_updater(lambda M: M.become(FunctionGraph(lambda x: (x**2)**(1/3) + 0.9*np.sqrt(abs(8-x**2)) * np.sin(value.get_value()*x), x_range=[-np.sqrt(8), np.sqrt(8), 0.01]).set_color(RED)))
        self.add(func, value)
        self.play(value.animate.set_value(20), run_time=3)

class demo7(Scene):
    def construct(self):
        t = ValueTracker()

        cir1 = Circle(radius=1.5, color=WHITE).shift(UP*1.5 + RIGHT*1.5)
        cir2 = Circle(radius=1.5, color=WHITE).shift(LEFT*2 + DOWN*2)
        self.add(cir1, cir2)

        dot_p = Dot(color=ORANGE).add_updater(lambda d: d.move_to(np.array([1.5*np.cos(7*t.get_value())+1.5, 1.5*np.sin(7*t.get_value())+1.5, 0])))
        dot_q = Dot(color=ORANGE).add_updater(lambda d: d.move_to(np.array([1.5*np.cos(3*t.get_value())-2, 1.5*np.sin(3*t.get_value())-2, 0])))
        line_p = Line(UP*8, DOWN*8, stroke_width=3).add_updater(lambda l: l.move_to(np.array([1.5*np.cos(7*t.get_value())+1.5, 1.5*np.sin(7*t.get_value())+1.5, 0])))
        line_q = Line(LEFT*10, RIGHT*10, stroke_width=3).add_updater(lambda l: l.move_to(np.array([1.5*np.cos(3*t.get_value())-2, 1.5*np.sin(3*t.get_value())-2, 0])))
        dot_t = Dot(color=BLUE).add_updater(lambda d: d.move_to(line_intersection(line_p.get_start_and_end(), line_q.get_start_and_end())))
        path = TracedPath(dot_t.get_center, stroke_color=BLUE, stroke_width=5)

        self.add(line_p, line_q, dot_p, dot_q, dot_t, path)
        self.play(t.animate.set_value(TAU), run_time=5)

class demo8(Scene):
    def construct(self):
        t = ValueTracker()

        P0 = Dot(np.array([ -3, -1.5, 0]))
        P1 = Dot(np.array([  0,  1.5, 0]))
        P2 = Dot(np.array([1.5, -1.5, 0]))

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)  

        Q0 = Dot().add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot().add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        
        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        
        B = Dot(color=ORANGE).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        path = TracedPath(B.get_center, stroke_width=5, stroke_color=ORANGE)

        self.add(P0_P1, P1_P2, Q0_Q1, P0, P1, P2, Q0, Q1, B, path)
        self.play(t.animate.set_value(1), run_time=3)

class demo9(Scene):
    def construct(self):
        t = ValueTracker()

        P0 = Dot(np.array([-3.6, -1.5, 0]))
        P1 = Dot(np.array([-4.2,  1.5, 0]))
        P2 = Dot(np.array([   0,  1.5, 0]))
        P3 = Dot(np.array([   2, -1.5, 0]))
        P4 = Dot(np.array([   3,  0.5, 0]))

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P3_P4 = Line(P3, P4)

        Q0 = Dot().add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot().add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot().add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q3 = Dot().add_updater(lambda m: m.move_to((P4.get_center() - P3.get_center()) * t.get_value() + P3.get_center()))
        
        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q2_Q3 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2.get_center(), Q3.get_center()))
        
        R0 = Dot().add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot().add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R2 = Dot().add_updater(lambda m: m.move_to((Q3.get_center() - Q2.get_center()) * t.get_value() + Q2.get_center()))
        
        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center()))
        R1_R2 = Line().add_updater(lambda m: m.put_start_and_end_on(R1.get_center(), R2.get_center()))
        
        S0 = Dot().add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        S1 = Dot().add_updater(lambda m: m.move_to((R2.get_center() - R1.get_center()) * t.get_value() + R1.get_center()))
        
        S0_S1 = Line().add_updater(lambda m: m.put_start_and_end_on(S0.get_center(), S1.get_center()))
        B = Dot(color=ORANGE).add_updater(lambda m: m.move_to((S1.get_center() - S0.get_center()) * t.get_value() + S0.get_center()))
        path = TracedPath(B.get_center, stroke_width=5, stroke_color=ORANGE)

        self.add(P0_P1, P1_P2, P2_P3, P3_P4, Q0_Q1, Q1_Q2, Q2_Q3, R0_R1, R1_R2, S0_S1, P0, P1, P2, P3, P4, Q0, Q1, Q2, Q3, R0, R1, R2, S0, S1, B, path)
        self.play(t.animate.set_value(1), run_time=3)

class demo10(Scene):
    def construct(self):
        pos = [UP, DOWN, LEFT, RIGHT, UR, UL, DR, DL]
        axes = Axes(x_range=[0, 1, 0.05], y_range=[0, 1, 0.05])

        curve_group1 = VGroup()
        for i in range(1, 31):
            curve1 = axes.get_graph(lambda x: x**(1/i), x_range=[0, 1])
            curve2 = axes.get_graph(lambda x: x**(i), x_range=[0, 1])
            curve_group1.add(curve1, curve2)
        
        curve_group1.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE)

        self.play(LaggedStart(*[ShowCreation(i) for i in curve_group1]))
        self.play(*[FadeOut(i, shift=random.choice(pos)*2) for i in curve_group1])

class demo11(Scene):
    def construct(self):
        axes = Axes(x_range=[-1, 10], y_range=[0, 5], height=5, width=11).shift(RIGHT + UP*2)
        cir = Circle(color=WHITE).shift(axes.coords_to_point(-1, 0))
        curve = axes.get_graph(lambda x: np.sin(x), color=YELLOW, x_range=[0, 10])
        
        dot_group1 = VGroup()
        for i in np.arange(0, TAU, TAU/100):
            dot1 = SmallDot(axes.coords_to_point(np.cos(i)-1, np.sin(i))).scale(0.5).set_color(YELLOW)
            dot_group1.add(dot1)
        
        dot_group2 = VGroup()
        for i in np.arange(0, TAU, TAU/100):
            dot2 = SmallDot(axes.coords_to_point(i, np.sin(i))).scale(0.5).set_color(YELLOW)
            dot_group2.add(dot2)
        
        dot_group3 = VGroup()
        for i in np.arange(TAU, 10, TAU/100):
            dot3 = SmallDot(axes.coords_to_point(i, np.sin(i))).scale(0.5).set_color(YELLOW)
            dot_group3.add(dot3)
        
        self.add(cir, axes, dot_group1)
        self.play(*[ReplacementTransform(i, n) for i, n in zip(dot_group1, dot_group2)])
        self.play(ReplacementTransform(dot_group2.copy(), dot_group3), run_time=0.5)
        self.play(ShowCreation(curve))

class demo12(Scene):
    def construct(self):
        text1 = Text("欧拉恒等式", font="IPix", font_size=120).shift(UP*0.5)
        tex1 = MTex(r"e^{i \pi } +1 =0", font_size=56).shift(DOWN)
        self.play(FadeIn(text1), FadeIn(tex1), run_time=0.5)

class demo13(Scene):
    def construct(self):
        text1 = Text("傅里叶级数", font_size=120, font="IPix").shift(UP*0.5)
        tex1 = MTex(r"x(t)=\sum_{n=-\infty}^{\infty} C_{n} e^{j n 2 \pi f t}", font_size=56).shift(DOWN)
        self.play(FadeIn(text1), FadeIn(tex1), run_time=0.5)

class demo14(Scene):
    def construct(self):
        text1 = Text("笛卡尔心形线", font_size=120, font="IPix").shift(UP*0.5)
        tex1 = MTex(r"r = a (1- \sin \theta )", font_size=56).shift(DOWN)
        self.play(FadeIn(text1), FadeIn(tex1), run_time=0.5)

class demo15(Scene):
    def construct(self):
        text1 = Text("黎曼函数", font_size=120, font="IPix").shift(UP*0.5)
        tex1 = MTex(r"\xi(s)=\frac{1}{2} s(s-1) \pi^{-s / 2} \Gamma\left(\frac{s}{2}\right) \zeta(s)", font_size=56).shift(DOWN)
        self.play(FadeIn(text1), FadeIn(tex1), run_time=0.5)

class demo16(Scene):
    def construct(self):
        axes = Axes()
        curve = axes.get_graph(lambda x: 0.3*(x**2), color=YELLOW)
        

        def get_tangent(a, b, step):
            curve_group = VGroup()
            for n in np.arange(-5, 5, step):
                k = 2*a*n + b
                y1 = a*(n**2)
                curve = axes.get_graph(lambda x: k*x - k*(n) + y1, color=BLUE_B)
                curve_group.add(curve)
            return curve_group

        def get_point_of_tangency(a, b, step):
            dot_group = VGroup()
            for n in np.arange(-5, 5, step):
                dot = SmallDot(axes.coords_to_point(n, a*(n**2) + b*n), color=BLUE_B)
                dot_group.add(dot)
            return dot_group
        
        dot_g1 = get_point_of_tangency(0.3, 0, 0.2)
        line_g1 = get_tangent(0.3, 0, 0.2)
        self.add(axes, curve, dot_g1)
        self.play(*[ReplacementTransform(i, n) for i, n in zip(dot_g1, line_g1)])

class demo17(Scene):
    def construct(self):
        axis1 = NumberLine().shift(UP*2)
        axis2 = NumberLine().shift(DOWN*2)
        self.add(axis1, axis2)

        line_group = VGroup()
        for i in np.arange(-8, 8, 0.1):
            line1 = Line(axis1.number_to_point(i), axis2.number_to_point(0.3*(i**2)), stroke_width=0.8, color=RED_D)
            line2 = Line(axis2.number_to_point(i), axis1.number_to_point(-0.3*(i**2)), stroke_width=0.8, color=BLUE_D)
            line_group.add(line1, line2)
        
        self.play(LaggedStart(*[ShowCreation(i) for i in line_group]), run_time=5)

class demo18(Scene):
    def construct(self):
        axis1 = NumberLine().shift(UP*2)
        axis2 = NumberLine().shift(DOWN*2)
        self.add(axis1, axis2)

        line_group = VGroup()
        for i in np.arange(-8, 8, 0.05):
            line1 = Line(axis1.number_to_point(i), axis2.number_to_point(np.sin(i) + np.cos(i)), stroke_width=0.8)
            line2 = Line(axis2.number_to_point(i), axis1.number_to_point(np.sin(i) + np.cos(i)), stroke_width=0.8)
            line_group.add(line1, line2)
        
        line_group.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE)
        self.play(LaggedStart(*[ShowCreation(i) for i in line_group]), run_time=5)


class demo19(Scene):
    def construct(self):
        c_grid = ComplexPlane()
        c_grid.prepare_for_nonlinear_transform()
        c_grid.set_stroke(BLUE_E, 1)
        
        self.add(c_grid)
        self.play(
            c_grid.animate.apply_complex_function(lambda z: z**3),
            run_time=3,
        )

class demo20(Scene):
    def construct(self):
        axes = Axes()
        s = StreamLines(lambda x, y: (np.sin(x) * 0.7 + np.cos(y) * 0.5, y * 0.7 - x * 0.5), axes)
        asl = AnimatedStreamLines(s)

        self.add(asl)
        self.wait(3)

class demo21(Scene):
    def construct(self):
        text1 = Text("费马大定理", font_size=120, font="IPix").shift(UP*0.5)
        tex1 = MTex("x^{n}+y^{n}=z^{n}", font_size=56).shift(DOWN)
        self.play(FadeIn(text1), FadeIn(tex1), run_time=0.5)

class demo22(Scene):
    def construct(self):
        text1 = Text("牛顿莱布尼茨公式", font_size=120, font="IPix").shift(UP*0.5)
        tex1 = MTex("\int_{a}^{b} f(x) \mathrm{d} x=F(b)-F(a)", font_size=56).shift(DOWN)
        self.play(FadeIn(text1), FadeIn(tex1), run_time=0.5)

class demo23(Scene):
    def construct(self):
        text1 = Text("勾股定理", font_size=120, font="IPix").shift(UP*0.5)
        tex1 = MTex("a^{2}+b^{2}=c^{2}", font_size=56).shift(DOWN)
        self.play(FadeIn(text1), FadeIn(tex1), run_time=0.5)

class demo24(Scene):
    def construct(self):
        text1 = Text("万恶之源()", font_size=120, font="IPix").shift(UP*0.5)
        tex1 = MTex("1+1=2", font_size=56).shift(DOWN)
        self.play(FadeIn(text1), FadeIn(tex1), run_time=0.5)

class demo25(Scene):
    def construct(self):
        text1 = Text("数 学 de 美", font_size=120, font="IPix").shift(UP*0.5)
        text2 = Text("the beauty of mathematics", font="IPix").shift(DOWN)
        self.play(FadeIn(text1), FadeIn(text2), run_time=2)

class end(Scene):
    def construct(self):
        t = TexText("@E{r}{s}net", tex_to_color_map={"{r}": "#0088FF", "{s}": "#B46F00"}, font_size=100)
        self.play(FadeIn(t), run_time=2)






        

        
        
        
        