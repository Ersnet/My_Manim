from manimlib import *
import random


# 查索引用：
def debugTeX(self, texm, scale_factor=0.6, text_color=RED):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="SimSun").scale(scale_factor).set_color(text_color)
        tex_id.move_to(j)
        self.add(tex_id)

class chapter_01(Scene):
    def construct(self):
        t1 = ValueTracker(0.001)
        t2 = ValueTracker(1)
        t3 = ValueTracker(0.001)
        tex_color = {"{k}": RED_A, "{f(x)}": YELLOW}
        position = [UP, DOWN, LEFT, RIGHT, UR, UL, DR, DL]
        
        axes = Axes(x_range=(0, 5), y_range=(0, 5), height=5, width=5).shift(np.array([-3, 0, 0]))
        x_y = axes.get_axis_labels()
        curve1 = axes.get_graph(lambda x: x, color=YELLOW).add_updater(lambda obj: obj.become(axes.get_graph(lambda x: x, x_range=[0, t1.get_value()], color=YELLOW)))
        l1_h = axes.get_h_line_to_graph(0.001, curve1).add_updater(lambda obj: obj.become(axes.get_h_line_to_graph(t1.get_value(), curve1)))
        l1_v = axes.get_v_line_to_graph(0.001, curve1).add_updater(lambda obj: obj.become(axes.get_v_line_to_graph(t1.get_value(), curve1)))
        tex1 = MTex(r"{f(x)}={k}x({k}\ne 0)", tex_to_color_map=tex_color).shift(UP*2+RIGHT*3)

        self.play(LaggedStart(*[Write(axes), FadeIn(x_y)]))
        self.add(l1_h, l1_v, curve1)
        self.play(t1.set_value, 4, rate_func=linear)
        self.play(Uncreate(l1_h), Uncreate(l1_v))
        self.play(Write(tex1))
        self.wait(2)

        curve1.clear_updaters()
        curve1.add_updater(lambda obj: obj.become(axes.get_graph(lambda x: t2.get_value()*x, x_range=[0, 4], color=YELLOW)))
        axis = NumberLine(x_range=[1, 4], include_numbers=True).shift(np.array([4, -2.4, 0]))
        triangle = Triangle(fill_opacity=1, color=YELLOW).scale(0.1).rotate(PI).add_updater(lambda obj: obj.move_to(np.array([2.5+t2.get_value()-1, -2.1, 0])))
        tex2 = MTex("{k}=", tex_to_color_map=tex_color).add_updater(lambda obj: obj.next_to(triangle, UP))
        num = DecimalNumber(1).add_updater(lambda obj: obj.set_value(t2.get_value()).next_to(tex2, RIGHT*0.5))

        self.play(FadeIn(axis, shift=UP))
        self.add(triangle, num, tex2)
        self.play(t2.set_value, 4, run_time=5.5, rate_func=there_and_back)
        self.wait(2.8)

        curve1.clear_updaters()
        triangle.clear_updaters()
        num.clear_updaters()
        tex2.clear_updaters()
        self.play(LaggedStart(*[FadeOut(i, shift=DOWN) for i in tex1]), LaggedStart(*[FadeOut(num, shift=DOWN), FadeOut(tex2, shift=DOWN), FadeOut(triangle, shift=DOWN*2), FadeOut(axis, shift=DOWN*3)]), run_time=2)

        curve2 = axes.get_graph(lambda x: 5*x, x_range=[0, 4], color=RED_A)
        y1 = axes.get_graph_label(curve1, "y_{1}=x")
        y2 = axes.get_graph_label(curve2, "y_{2}=5x")
        k1 = Tex("k_{1}", color=YELLOW).shift(RIGHT*2+UP*2)
        k2 = Tex("k_{2}", color=RED_A).shift(RIGHT*4+UP*2)
        tex3 = Tex("<").next_to(k1, RIGHT*2.5)
        self.play(ShowCreation(curve2))
        self.play(LaggedStart(*[Write(y1), Write(y2)]))
        self.wait(3)
        self.play(LaggedStart(*[GrowFromCenter(k1), GrowFromCenter(k2)]))
        self.play(Write(tex3))
        self.wait(2)
        self.play(LaggedStart(*[FadeOut(k1), FadeOut(k2), FadeOut(tex3), FadeOut(y1), FadeOut(y2), FadeOut(curve1), FadeOut(curve2)]))
        
        def get_tangent(a, b, step):
            curve_group = VGroup()
            for n in np.arange(0, 4, step):
                k = 2*a*n + b
                y1 = a*(n**2)
                curve = axes.get_graph(lambda x: k*x - k*(n) + y1, color=BLUE_B)
                curve_group.add(curve)
            return curve_group
        
        def get_point_of_tangency(a, b, step):
            dot_group = VGroup()
            for n in np.arange(0, 4, step):
                dot = SmallDot(axes.coords_to_point(n, a*(n**2) + b*n), color=BLUE_B)
                dot_group.add(dot)
            return dot_group

        def get_x_dots(step):
            dot_group = VGroup()
            for n in np.arange(0, 4, step):
                dot = SmallDot(axes.coords_to_point(n, 0), color=TEAL)
                dot_group.add(dot)
            return dot_group
        
        curve3 = axes.get_graph(lambda x: 0.3*(x**2), x_range=[0, 4], color=YELLOW).add_updater(lambda obj: obj.become(axes.get_graph(lambda x: 0.3*(x**2), x_range=[0, t3.get_value()], color=YELLOW)))
        l2_h = axes.get_h_line_to_graph(0.001, curve3).add_updater(lambda obj: obj.become(axes.get_h_line_to_graph(t3.get_value(), curve3)))
        l2_v = axes.get_v_line_to_graph(0.001, curve3).add_updater(lambda obj: obj.become(axes.get_v_line_to_graph(t3.get_value(), curve3)))
        self.add(curve3, l2_h, l2_v)
        self.play(t3.set_value, 4, run_time=2, rate_func=linear)
        self.play(Uncreate(l2_h), Uncreate(l2_v))
        self.wait(2)
        curve3.clear_updaters()

        dot_g1 = get_x_dots(0.5)
        dot_g2 = get_point_of_tangency(0.3, 0, 0.5)
        tangent_g1 = get_tangent(0.3, 0, 0.5)
        tangent_g2 = get_tangent(0.3, 0, 0.2)
        tangent_g3 = get_tangent(0.3, 0, 0.1)
        tangent_g4 = get_tangent(0.3, 0, 0.08)
        self.play(LaggedStart(*[FadeIn(i, shift=DOWN*n) for i, n in zip(dot_g1, np.arange(0, 4, 0.5))]))
        self.play(LaggedStart(*[ReplacementTransform(a, b) for a, b in zip(dot_g1, dot_g2)]))
        self.play(LaggedStart(*[ReplacementTransform(c, d) for c, d in zip(dot_g2, tangent_g1)]))
        self.wait(4.5)
        self.play(ReplacementTransform(tangent_g1, tangent_g2))
        self.play(ReplacementTransform(tangent_g2, tangent_g3))
        self.play(ReplacementTransform(tangent_g3, tangent_g4))
        self.wait(0.5)
        self.play(LaggedStart(*[FadeOut(i, shift=random.choice(position)*3) for i in tangent_g4]))
        self.play(FadeOut(curve3), FadeOut(axes), FadeOut(x_y))

class chapter_02(Scene):
    def construct(self):
        tex_color = {"{x_{1}}": TEAL_B, "{x_{2}}": TEAL_C, "{y_{1}}": BLUE_B, "{y_{2}}": BLUE_C, "{k}": RED_A}

        axes = Axes(x_range=(0, 5), y_range=(0, 5), height=5, width=5).shift(np.array([-3, 0, 0]))
        x_y = axes.get_axis_labels()
        curve = axes.get_graph(lambda x: 0.53*x + 0.5, x_range=[0, 4], color=YELLOW)
        self.wait(6)
        self.play(LaggedStart(*[Write(axes), FadeIn(x_y)]))
        self.play(ShowCreation(curve))
        self.wait(1.5)
        d1 = Dot(axes.coords_to_point(0.7, 0.53*0.7+0.5), color=TEAL_B)
        d2 = Dot(axes.coords_to_point(2.1, 0.53*2.1+0.5), color=TEAL_C)
        tex1 = MTex("({x_{1}}, {y_{1}})", tex_to_color_map=tex_color).next_to(d1, RIGHT*0.5)
        tex2 = MTex("({x_{2}}, {y_{2}})", tex_to_color_map=tex_color).next_to(d2, RIGHT*0.5)
        tex3 = MTex("{y_{1}} = {k} {x_{1}} + b ", tex_to_color_map=tex_color).shift(RIGHT*3.5+UP*2)
        tex4 = MTex("{y_{2}} = {k} {x_{2}} + b ", tex_to_color_map=tex_color).next_to(tex3, DOWN*0.8, aligned_edge=LEFT)
        tex5 = MTex("{y_{1}} - {y_{2}} = {k} {x_{1}} - {k} {x_{2}} + b - b", tex_to_color_map=tex_color).next_to(tex4, DOWN*0.8)

        self.play(LaggedStart(*[FadeIn(d1, shift=UP), FadeIn(d2, shift=UP*1.5)]))
        self.wait(1)
        self.play(LaggedStart(*[FadeIn(tex1, shift=UP), FadeIn(tex2, shift=UP*1.5)]))
        self.wait(4)
        self.play(LaggedStart(*[
            ReplacementTransform(tex1[1:3].copy(), tex3[4:6]), 
            ReplacementTransform(tex1[4:6].copy(), tex3[0:2]),
            ReplacementTransform(tex2[1:3].copy(), tex4[4:6]),
            ReplacementTransform(tex2[4:6].copy(), tex4[0:2])]),
            *[Write(tex3[i]) for i in range(len(tex3)) if i != 4 and i != 5 and i != 0 and i != 1], 
            *[Write(tex4[i]) for i in range(len(tex4)) if i != 4 and i != 5 and i != 0 and i != 1],
            )
        self.wait(1)
        self.play(LaggedStart(*[
            ReplacementTransform(tex3[0:2], tex5[0:2], path_arc=PI), 
            ReplacementTransform(tex4[0:2], tex5[3:5], path_arc=PI)]), 
            Write(tex5[2])
        )
        self.play(Write(tex5[5]))
        self.play(LaggedStart(*[
            ReplacementTransform(tex3[3:6], tex5[6:9], path_arc=PI), 
            ReplacementTransform(tex4[3:6], tex5[10:13], path_arc=PI), 
            ReplacementTransform(tex3[6][1], tex5[13][1], path_arc=PI),
            ReplacementTransform(tex4[6][1], tex5[13][3], path_arc=PI)]),
            *[Write(tex5[9]), Write(tex5[13][0]), Write(tex5[13][2])], 
            *[FadeOut(tex3[2]), FadeOut(tex3[6][0]), FadeOut(tex4[2]), FadeOut(tex4[6][0])]
    )
        
        tex6 = MTex("{y_{1}} - {y_{2}} = {k} ( {x_{1}} -  {x_{2}} )", tex_to_color_map=tex_color).shift(tex5.get_center())
        tex7 = MTex("{{y_{1}} - {y_{2}} \over {x_{1}} -  {x_{2}}}  = {k}", tex_to_color_map=tex_color).shift(tex5.get_center())
        tex8 = MTex(" {k} = {{y_{1}} - {y_{2}} \over {x_{1}} -  {x_{2}}} ", tex_to_color_map=tex_color).shift(tex5.get_center())
        self.play(TransformMatchingMTex(tex5, tex6))
        self.play(TransformMatchingMTex(tex6, tex7))
        self.play(TransformMatchingMTex(tex7, tex8))
        self.play(ShowCreationThenDestructionAround(tex8))
        self.wait(19)

        self.play(LaggedStart(*[FadeOut(tex8), FadeOut(axes), FadeOut(curve), FadeOut(d1), FadeOut(d2), FadeOut(tex1), FadeOut(tex2), FadeOut(x_y)]))

class chapter_03(Scene):
    def construct(self):
        tex_color1 = {r"$ \Delta x $": TEAL_D, "$x_{0}$": BLUE_D, "$x$": GOLD_E, "$y$": YELLOW, r"$ \Delta y$": PURPLE_C}
        tex_color2 = {
            "{x}": GOLD_E, 
            r"{\Delta x}": TEAL_D, 
            "{x_{0}}": BLUE_D, 
            r"\Delta y": PURPLE_C, 
            "{x_{1}}": TEAL_B, 
            "{x_{2}}": TEAL_C, 
            "{y_{1}}": BLUE_B, 
            "{y_{2}}": BLUE_C, 
            "{k}": RED_A
        }

        definition = TexText(
        "假设函数", "$y$", "$=f$", "(", "$x$", r")在\\点", 
        "$x_{0}$", r"处的邻域内有定义\\当自变量", 
        "$x$", "在", "$x_{0}$", "处取得增量", r"$ \Delta x $\\", 
        "相应的函数取得增量", r"$ \Delta y$ ", "如果", r"$ \Delta y \over  \Delta x $", "在", r"$ \Delta x $", r"$\rightarrow 0  $\\", 
        r"时的极限存在", "那么称函数", "$y$", "$=f$", "(", "$x$", ")  在点  ", "$x_{0}$ ", "处可导"
    ).set_color_by_tex_to_color_map(tex_color1)
        definition[16][0:2].set_color(PURPLE_C)
        definition[16][3:].set_color(TEAL_D)
        tex1 = MTex(r"f^{\prime}({x})=\lim _{{\Delta x} \rightarrow 0} {f({x_{0}}+{\Delta x})-f({x_{0}}) \over {\Delta x}}", tex_to_color_map=tex_color2)
        tex2 = MTex(r"f^{\prime}({x})=\lim _{{\Delta x} \rightarrow 0} {{\Delta y} \over {\Delta x}}", tex_to_color_map=tex_color2)
        callout = MTex(r"{\Delta y}\\ \Uparrow ", tex_to_color_map=tex_color2).next_to(tex1[7:15].get_center(), UP*2.5)
        tex3 = MTex(" {k} = {{y_{1}} - {y_{2}} \over {x_{1}} -  {x_{2}}} ", tex_to_color_map=tex_color2).to_corner(UL)
        tex4 = MTex("{k} ={{\Delta y} \over {\Delta x}}", tex_to_color_map=tex_color2).to_corner(UL)

        self.play(Write(definition), run_time=2.5)
        self.wait(29)
        self.play(TransformMatchingShapes(definition, tex1), run_time=1.5)
        self.wait(7)
        self.play(tex1[:7].animate.set_fill(opacity=0.3), tex1[16:].animate.set_fill(opacity=0.3))
        self.wait(4)
        self.play(Write(callout))
        self.play(
            ReplacementTransform(callout[0], tex2[7]), 
            FadeOut(tex1[7:16]), 
            *[FadeOut(tex1[i]) for i in range(len(tex2)) if i != 7 and i != 8 and i != 9 and i != 10 and i != 11 and i != 12 and i != 13 and i != 14 and i != 15],
            *[Write(tex2[i]) for i in range(len(tex2)) if i != 7], 
            FadeOut(callout[1]), run_time=1.5
        )
        self.wait(6)
        self.play(FadeIn(tex3))
        self.play(FadeOut(tex3[2:]))
        self.play(FadeIn(tex4[2:]), ReplacementTransform(tex3[:2], tex4[:2]))
        self.play(Indicate(tex4[2:]), Indicate(tex2[7:]))
        self.play(tex4[:2].animate.next_to(tex2, LEFT*0.5), FadeOut(tex4[2:]))
        self.wait(5)
        self.play(FadeOut(tex4[:2]), FadeOut(tex2))


class chapter_04(Scene):
    def construct(self):
        frame = self.camera.frame
        tex_color = {"{x_{1}}": TEAL_B, "{x_{2}}": TEAL_C, "{y_{1}}": BLUE_B, "{y_{2}}": BLUE_C, "{k}": RED_A}
        tex_color2 = {
            "{x}": GOLD_E, 
            r"{\Delta x}": TEAL_D, 
            "{x_{0}}": BLUE_D, 
            r"\Delta y": PURPLE_C,  
            "{k}": RED_A
        }

        axes = Axes(x_range=(0, 5), y_range=(0, 5), height=5, width=5).shift(np.array([-3, 0, 0]))
        x_y = axes.get_axis_labels()
        curve = axes.get_graph(lambda x: 0.3*(x**2), x_range=[0, 4], color=BLUE)
        fx = axes.get_graph_label(curve, "f(x)=0.3x^{2}")

        self.play(LaggedStart(*[Write(axes), FadeIn(x_y)]))
        self.play(ShowCreation(curve))
        self.wait(2)
        self.play(Write(fx))
        self.wait(4)

        d1 = Dot(axes.coords_to_point(1, 0.3))
        d1_pos = MTex("({1}, {0.3})", tex_to_color_map={"{1}": TEAL_B, "{0.3}": BLUE_B}).next_to(d1, LEFT*0.5)
        d2 = Dot(axes.coords_to_point(3, 2.7))
        d2_pos = MTex("({3}, {2.7})", tex_to_color_map={"{3}": TEAL_B, "{2.7}": BLUE_B}).next_to(d2, LEFT*0.5)
        
        tangent_l = axes.get_graph(lambda x: (2*1*0.3)*x - (2*1*0.3)*1 + 0.3*(1**2))
        tangent_l_copy = DashedVMobject(tangent_l.copy())
        l1 = axes.get_graph(lambda x: 1.2*x - 0.9)
        l1_copy = DashedVMobject(l1.copy())
        tex1 = MTex(r" {k} = {{y_{1}} - {y_{2}} \over {x_{1}} -  {x_{2}}} ", tex_to_color_map=tex_color).shift(UP*2 + RIGHT*5)
        tex2 = MTex(r"{k_{1}} = {{{0.3} - {2.7}} \over {{1} - {3}} }", tex_to_color_map={"{1}": TEAL_B, "{0.3}": BLUE_B, "{3}": TEAL_B, "{2.7}": BLUE_B, "{k_{1}}": RED_B}).next_to(tex1, DOWN*0.8)
        tex3 = MTex(r"{k_{1}} = {1.2}", tex_to_color_map={"{k_{1}}": RED_B, "{1.2}": GOLD}).next_to(tex1, DOWN, aligned_edge=LEFT)
        
        self.play(LaggedStart(*[FadeIn(d1), FadeIn(d1_pos, shift=UP)]))
        self.play(GrowFromCenter(tangent_l))
        self.wait(10)
        self.play(LaggedStart(*[FadeIn(d2), FadeIn(d2_pos, shift=UP)]))
        self.play(Write(tex1))
        self.play(Write(tex2))
        self.play(TransformMatchingShapes(tex2, tex3))
        self.play(LaggedStart(*[ReplacementTransform(tangent_l, l1), FadeIn(tangent_l_copy)]))
        self.wait(11)

        def get_line(pos):
            n_pos = axes.point_to_coords(pos)
            k = (n_pos[1] - 0.3*(1**2)) / (n_pos[0] - 1)
            b = 0.3 - 1*k
            return lambda x: k*x + b
    
        t = ValueTracker(3)
        d3 = d2.copy().set_color(ORANGE).add_updater(lambda obj: obj.move_to(axes.coords_to_point(t.get_value(), 0.3*(t.get_value()**2))))
        l2 = axes.get_graph(get_line(d3.get_center()), color=GREEN_D).add_updater(lambda obj: obj.become(axes.get_graph(get_line(d3.get_center()), color=GREEN_D)))
        l3 = Line(color=YELLOW).add_updater(lambda obj: obj.put_start_and_end_on(d1.get_center(), np.array([d3.get_center()[0], d1.get_center()[1], 0])))
        l4 = Line(color=ORANGE).add_updater(lambda obj: obj.put_start_and_end_on(d3.get_center(), np.array([d3.get_center()[0], d1.get_center()[1], 0])))
        brace1 = Brace(l3, direction=DOWN*2).add_updater(lambda obj: obj.become(Brace(l3, direction=DOWN*2).set_color(YELLOW))).set_color(YELLOW)
        tex4 = MTex(r"{\Delta x}", tex_to_color_map={r"{\Delta x}": TEAL_D}).add_updater(lambda obj: obj.next_to(brace1, DOWN*0.8))
        brace2 = Brace(l4, direction=RIGHT*2).add_updater(lambda obj: obj.become(Brace(l4, direction=RIGHT*2).set_color(ORANGE))).set_color(ORANGE)
        tex5 = MTex(r"{\Delta y}", tex_to_color_map={r"{\Delta y}": PURPLE_C}).add_updater(lambda obj: obj.next_to(brace2, RIGHT*0.8))

        self.play(frame.animate.shift(LEFT*2 + DOWN).set_width(10), LaggedStart(*[FadeOut(l1), FadeIn(l1_copy)]), LaggedStart(*[ShowCreation(l2), ShowCreation(l3), ShowCreation(l4), ShowCreation(brace1), ShowCreation(brace2), ShowCreation(tex4), ShowCreation(tex5)]), run_time=2)
        self.add(l2, l3, l4, d3, d1, brace1, brace2, tex4, tex5)
        self.play(t.animate.set_value(1.00000001), run_time=6)
        self.play(t.animate.set_value(3), run_time=5)
        self.play(frame.animate.to_default_state())

        tex6 = MTex(r"{k}=\lim_{{\Delta x} \to 0} {0.3({x}+ {\Delta x})^{2} - 0.3{x}^2 \over {\Delta x}}", tex_to_color_map=tex_color2, font_size=36).next_to(tex3, DOWN)
        tex7 = MTex(r"{k}=\lim_{{\Delta x} \to 0} 0.3{\Delta x}+0.6{x}", tex_to_color_map=tex_color2, font_size=36).next_to(tex3, DOWN)
        tex8 = MTex("{k}=0.6", tex_to_color_map=tex_color2, font_size=36).next_to(tex7, DOWN)
        tex9 = MTex(r"{\Delta x} \ne 0", tex_to_color_map=tex_color2, font_size=36).next_to(tex8, DOWN)
        self.play(Write(tex6))
        self.play(TransformMatchingShapes(tex6, tex7))
        self.wait(10)
        self.play(Write(tex8))
        self.play(Write(tex9))
        self.wait(12)
        

        s_g = VGroup()
        for x in range(-8, 8):
            for y in range(-5, 5):
                s = Square(side_length=1, stroke_color=BLACK, fill_color=BLACK, fill_opacity=1).shift(np.array([x, y, 0]))
                s_g.add(s)
        self.play(*[FadeIn(i) for i in s_g])

class end(Scene):
    def construct(self):
        t = TexText("@E{r}{s}net", tex_to_color_map={"{r}": "#0088FF", "{s}": "#B46F00"}, font_size=100)
        self.play(FadeIn(t), run_time=2)


