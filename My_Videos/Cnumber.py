from manimlib import *
import random



# 查索引用：
def debugTeX(self, texm, scale_factor=0.6, text_color=RED):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="SimSun").scale(scale_factor).set_color(text_color)
        tex_id.move_to(j)
        self.add(tex_id)

def R(pos, color):
    re = Rectangle(height=0.5, width=1).shift(np.array(pos)).set_color(color)
    l1 = Line(np.array([re.get_edge_center(LEFT)[0]-0.5, re.get_edge_center(LEFT)[1], 0]), re.get_edge_center(LEFT))
    l2 = Line(np.array([re.get_edge_center(RIGHT)[0]+0.5, re.get_edge_center(RIGHT)[1], 0]), re.get_edge_center(RIGHT))
    return VGroup(re, l1, l2)


class ErsFadeInFromRandom(LaggedStart):
    CONFIG = {
        "directions":[DL, DOWN, DR, RIGHT, UR, UP, UL, LEFT],
        "magnitude":0.5,
        "lag_ratio":0
    }
    def __init__(self, text , **kwargs):
        digest_config(self, kwargs)
        super().__init__(
            *[FadeInFromPoint(obj,point=random.choice(self.directions)*self.magnitude)
                for obj in text],
            **kwargs
        )


class chapter_01(Scene):
    def construct(self):
        tex_color = {r"$n$": BLUE_B, r"$m_{1}$": TEAL_A, r"$m_{2}$": TEAL_B, r"$m_{3}$": TEAL_C, r"$m_{n} $": TEAL_D, r"$N$": BLUE_D}
        
        title = Title("分类加法计数原理", stroke_color=BLACK)
        self.wait(10)
        self.play(Write(title))

        definition1 = TexText(r"完成某件事有", r"$n$", r"类办法，在第一类中\\有", r"$m_{1}$", "种不同的方法，第二类中有", r"$m_{2}$", r"种不同的方法，\\则完成这件事共有", r"$N$", "$=$", r"$m_{1}$", " $+$", r"$m_{2}$", "$+$", r"$m_{3}$",r"$ +\cdots +$", r"$m_{n} $", "种不同的方法").set_color_by_tex_to_color_map(tex_color)
        self.play(Write(definition1))
        self.wait(16)
        self.play(LaggedStart(*[FadeOut(i) for i in definition1[:7]], *[FadeOut(i) for i in definition1[16:]], definition1[7:16].animate.shift(UP*2.5+LEFT*4)))

        tex1 = MTex(r"""{N} = \left\{\begin{matrix} \quad {m_{1}}
                            & \\ \quad {m_{2}}
                            & \\ \quad {m_{3}} 
                            & \\ \quad \vdots 
                            & \\ \quad \vdots 
                            & \\ \quad {m_{n}}
                            &
                            \end{matrix}\right.""", tex_to_color_map={"{m_{1}}": TEAL_A, "{m_{2}}": TEAL_B, "{m_{3}}": TEAL_C, "{m_{n}}": TEAL_D, "{N}": BLUE_D}).shift(np.array([-4.5, -1, 0]))
        self.play(LaggedStart(*[
            ReplacementTransform(definition1[9].copy(), tex1[2:4], path_arc=-PI), 
            ReplacementTransform(definition1[11].copy(), tex1[4:6], path_arc=-PI), 
            ReplacementTransform(definition1[13].copy(), tex1[6:8], path_arc=-PI), 
            ReplacementTransform(definition1[15].copy(), tex1[9:11], path_arc=-PI)]), 
            *[ Write(tex1[:2]), Write(tex1[8:9])], run_time=2.5)
        self.wait(5)
        
        r1 = R([3, 1, 0], TEAL_A)
        r2 = R([3, 0, 0], TEAL_B)
        r3 = R([3, -1, 0], TEAL_C)
        r4 = R([3, -3, 0], TEAL_C)
        tex2 = Tex(r"\vdots").shift(np.array([3, -2, 0]))
        self.play(LaggedStart(*[FadeTransform(tex1[2:4].copy(), r1), FadeTransform(tex1[4:6].copy(), r2), FadeTransform(tex1[6:8].copy(), r3), FadeTransform(tex1[9:11].copy(), r4), FadeTransform(tex1[8].copy(), tex2)]), run_time=1.5)
        
        l1 = Line(np.array([2, -3.7, 0]), np.array([2, 1, 0]))
        l2 = Line(np.array([4, -3.7, 0]), np.array([4, 1, 0]))
        l3 = Line(np.array([4, -3.7, 0]), np.array([3.5, -3.7, 0]))
        l4 = Line(np.array([2, -3.7, 0]), np.array([2.5, -3.7, 0]))
        u = Tex("220V").shift(np.array([3, -3.7, 0])).scale(0.5)
        d1 = Dot(np.array([2, -3.7, 0])).set_color(YELLOW)
        d2 = Dot(np.array([2, -3, 0])).set_color(YELLOW)
        d3 = Dot(np.array([2, -1, 0])).set_color(YELLOW)
        d4 = Dot(np.array([2, 0, 0])).set_color(YELLOW)
        p1 = TracedPath(d1.get_center, stroke_color=YELLOW, stroke_width=4)
        p2 = TracedPath(d2.get_center, stroke_color=YELLOW, stroke_width=4)
        p3 = TracedPath(d3.get_center, stroke_color=YELLOW, stroke_width=4)
        p4 = TracedPath(d4.get_center, stroke_color=YELLOW, stroke_width=4)


        self.play(LaggedStart(*[GrowFromCenter(l1), GrowFromCenter(l2), GrowFromCenter(l3), GrowFromCenter(l4), FadeIn(u)]))
        self.play(FadeIn(d1))
        self.add(p1, p2, p3, p4)
        self.play(MoveAlongPath(d1, l1))
        self.play(d1.animate.shift(RIGHT*2))
        self.play(d1.animate.shift(DOWN*(l2.get_length())))
        self.play(LaggedStart(*[
            ReplacementTransform(d1.copy(), d2), 
            ReplacementTransform(d1.copy(), d2), 
            ReplacementTransform(d1.copy(), d3), 
            ReplacementTransform(d1.copy(), d4)
        ]))
        self.play(LaggedStart(*[d2.animate.shift(RIGHT*2), d3.animate.shift(RIGHT*2), d4.animate.shift(RIGHT*2)]))
        self.play(LaggedStart(*[d2.animate.move_to(np.array([4, -3.7, 0])), d3.animate.move_to(np.array([4, -3.7, 0])), d4.animate.move_to(np.array([4, -3.7, 0]))]))

        tex3 = MTex("{N}=", tex_to_color_map={"{N}": BLUE_D}).shift(LEFT)
        tex4 = MTex("1").next_to(tex3, RIGHT*0.8).set_color(YELLOW)
        tex5 = MTex("2").next_to(tex3, RIGHT*0.8).set_color(YELLOW)
        tex6 = MTex("3").next_to(tex3, RIGHT*0.8).set_color(YELLOW)

        self.play(Write(tex3))
        self.play(FadeTransform(p1.copy(), tex4))
        self.play(FadeTransform(p4.copy(), tex5), FadeOut(tex4))
        self.play(FadeTransform(p3.copy(), tex6), FadeOut(tex5))
        self.play(FadeOut(tex6))

        ani_g = []
        num_g = VGroup()
        for i in range(4, 114514, 1000):
            num = MTex(f"{i}").next_to(tex3, RIGHT*0.8).set_color(YELLOW)
            tex = MTex(f"{i}").next_to(tex3, RIGHT*0.8).set_color(YELLOW).scale(0.00001)
            transform = FadeTransform(p3.copy(), tex)
            ani_g.append(transform)
            num_g.add(num)
        self.play(LaggedStart(*[FadeIn(i, rate_func=there_and_back) for i in num_g]), LaggedStart(*[a for a in ani_g]))

        tex7 = MTex("n").set_color(TEAL_D).next_to(tex3, RIGHT*0.8)
        self.play(FadeTransform(p2.copy(), tex7))
        
        s_g = VGroup()
        for x in range(-8, 8):
            for y in range(-5, 5):
                s = Square(side_length=1, stroke_color=BLACK, fill_color=BLACK, fill_opacity=1).shift(np.array([x, y, 0]))
                s_g.add(s)
        self.play(*[FadeIn(i) for i in s_g])


class chapter_02(Scene):
    def construct(self):
        title = Title("分步乘法计数原理", stroke_color=BLACK)
        self.play(Write(title))

        definition1 = TexText("完成某件事有", "$n$", r"个步骤， 在第一个步骤中\\有", "$m_{1}$", "种不同的方法， 在第二个步骤中有", "$m_{2}$", r"种不同的方法\\则完成这件事共有", "$N$", "$=$", "$m_{1}$", r"$ \cdot $", "$m_{2}$", r" $ \cdot \ \dots \ \cdot $", "$m_{n}$", "种不同的方法").set_color_by_tex_to_color_map({"$n$": BLUE_B, "$m_{1}$": TEAL_A, "$m_{2}$": TEAL_B, "$m_{n}$": TEAL_D, "$N$": BLUE_D})
        self.wait(3)
        self.play(Write(definition1))
        self.wait(19)
        self.play(LaggedStart(*[FadeOut(i) for i in definition1[:7]], *[FadeOut(i) for i in definition1[14:]], definition1[7:14].animate.shift(UP*2.5+LEFT*4)))
        
        r1 = R([-2, 0, 0], TEAL_B)
        r2 = R([-2, -1, 0], TEAL_B)
        r3 = R([-2, -2, 0], TEAL_B)
        r4 = R([0.5, 1, 0], TEAL_C)
        r5 = R([0.5, 0, 0], TEAL_C)
        r6 = R([0.5, -1, 0], TEAL_C)
        r7 = R([0.5, -2, 0], TEAL_C)
        r8 = R([0.5, -3, 0], TEAL_C)
        l1 = Line(np.array([-3, 0, 0]), np.array([-3, -2, 0]))
        l2 = Line(np.array([-1, 0, 0]), np.array([-1, -2, 0]))
        l3 = Line(np.array([-0.5, 1, 0]), np.array([-0.5, -3, 0]))
        l4 = Line(np.array([1.5, 1, 0]), np.array([1.5, -3, 0]))
        l5 = Line(np.array([-1, -1, 0]), np.array([-0.5, -1, 0]))
        l6 = Line(np.array([-4, -1, 0]), np.array([-3, -1, 0]))
        l7 = Line(np.array([2.5, -1, 0]), np.array([1.5, -1, 0]))
        l8 = Line(np.array([-4, -1, 0]), np.array([-4, -3.5, 0]))
        l9 = Line(np.array([2.5, -1, 0]), np.array([2.5, -3.5, 0]))
        l10 = Line(np.array([-4, -3.5, 0]), np.array([-1.25, -3.5, 0]))
        l11 = Line(np.array([2.5, -3.5, 0]), np.array([0.25, -3.5, 0]))
        u = Tex("220V").shift(np.array([-0.5, -3.5, 0])).scale(0.5)
        r_g1 = VGroup(r1, r2, r3, r4, r5, r6, r7, r8)
        l_g1 = VGroup(l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11)

        self.play(LaggedStart(*[ErsFadeInFromRandom(i) for i in r_g1]), LaggedStart(*[SpinInFromNothing(i) for i in l_g1]), FadeIn(u))

        d1 = Dot(np.array([-3, -1, 0])).set_color(YELLOW)
        d2 = Dot(np.array([-0.5, 0, 0])).set_color(YELLOW)
        d3 = Dot(np.array([-0.5, 1, 0])).set_color(YELLOW)
        d4 = Dot(np.array([-0.5, -2, 0])).set_color(YELLOW)
        d5 = Dot(np.array([-0.5, -3, 0])).set_color(YELLOW)
        p1 = TracedPath(d1.get_center, stroke_color=YELLOW, stroke_width=4)
        p2 = TracedPath(d2.get_center, stroke_color=YELLOW, stroke_width=4)
        p3 = TracedPath(d3.get_center, stroke_color=YELLOW, stroke_width=4)
        p4 = TracedPath(d4.get_center, stroke_color=YELLOW, stroke_width=4)
        p5 = TracedPath(d5.get_center, stroke_color=YELLOW, stroke_width=4)

        self.play(FadeIn(d1))
        self.add(p1, p2, p3, p4, p5)
        self.play(d1.animate.shift(UP))
        self.play(d1.animate.shift(RIGHT*2))
        self.play(d1.animate.shift(DOWN))
        self.play(d1.animate.shift(RIGHT*0.5))
        self.play(LaggedStart(*[
            ReplacementTransform(d1.copy(), d2),  
            ReplacementTransform(d1.copy(), d3), 
            ReplacementTransform(d1.copy(), d4),
            ReplacementTransform(d1.copy(), d5)
        ]))
        self.play(LaggedStart(*[d1.animate.shift(RIGHT*2), d2.animate.shift(RIGHT*2), d3.animate.shift(RIGHT*2), d4.animate.shift(RIGHT*2), d5.animate.shift(RIGHT*2)]))
        self.play(LaggedStart(*[d2.animate.move_to(np.array([1.5, -1, 0])), d3.animate.move_to(np.array([1.5, -1, 0])), d4.animate.move_to(np.array([1.5, -1, 0])), d5.animate.move_to(np.array([1.5, -1, 0]))]))

        d6 = Dot(np.array([-3, -1, 0])).set_color(YELLOW)
        d7 = Dot(np.array([-3, -2, 0])).set_color(YELLOW)
        d8 = Dot(np.array([-0.5, 0, 0])).set_color(YELLOW)
        d9 = Dot(np.array([-0.5, 1, 0])).set_color(YELLOW)
        d10 = Dot(np.array([-0.5, -2, 0])).set_color(YELLOW)
        d11 = Dot(np.array([-0.5, -3, 0])).set_color(YELLOW)
        p6 = TracedPath(d6.get_center, stroke_color=YELLOW, stroke_width=4)
        p7 = TracedPath(d7.get_center, stroke_color=YELLOW, stroke_width=4)

        self.play(LaggedStart(*[FadeIn(d6, shift=UP), FadeIn(d7, shift=UP)]))
        self.add(p6, p7)
        self.play(LaggedStart(*[d6.animate.shift(RIGHT*2), d7.animate.shift(RIGHT*2)]))
        self.play(d7.animate.shift(UP))
        self.play(LaggedStart(*[d6.animate.shift(RIGHT*0.5), d7.animate.shift(RIGHT*0.5)]))
        self.play(LaggedStart(*[
            ReplacementTransform(d6.copy(), d8),  
            ReplacementTransform(d6.copy(), d9), 
            ReplacementTransform(d6.copy(), d10),
            ReplacementTransform(d6.copy(), d11),
            ReplacementTransform(d7.copy(), d8),  
            ReplacementTransform(d7.copy(), d9), 
            ReplacementTransform(d7.copy(), d10),
            ReplacementTransform(d7.copy(), d11),
        ]))
        self.play(LaggedStart(*[d8.animate.shift(RIGHT*2), d9.animate.shift(RIGHT*2), d10.animate.shift(RIGHT*2), d11.animate.shift(RIGHT*2), d6.animate.shift(RIGHT*2), d7.animate.shift(RIGHT*2)]))
        self.play(LaggedStart(*[d8.animate.move_to(np.array([1.5, -1, 0])), d9.animate.move_to(np.array([1.5, -1, 0])), d10.animate.move_to(np.array([1.5, -1, 0])), d11.animate.move_to(np.array([1.5, -1, 0])), d6.animate.move_to(np.array([1.5, -1, 0])), d7.animate.move_to(np.array([1.5, -1, 0]))]))
        self.wait(4)
        self.play(ShowPassingFlashAround(definition1[7:14]))
        s_g = VGroup()
        for x in range(-8, 8):
            for y in range(-5, 5):
                s = Square(side_length=1, stroke_color=BLACK, fill_color=BLACK, fill_opacity=1).shift(np.array([x, y, 0]))
                s_g.add(s)
        self.play(*[FadeIn(i) for i in s_g])


class chapter_03(Scene):
    def construct(self):
        cir1 = Circle(color=WHITE).shift(LEFT*2.5 + UP*2)
        cir2 = Circle(color=WHITE).shift(RIGHT*2.5 + UP*2)
        arrow1 = Line(start=np.array([-1.3, 2, 0]), end=np.array([1.3, 2, 0])).add_tip()
        arrow2 = CurvedArrow(start_point=np.array([-1.3, 2.5, 0]), end_point=np.array([1.3, 2.5, 0]), angle=-PI/3)
        arrow3 = CurvedArrow(start_point=np.array([-1.3, 1.5, 0]), end_point=np.array([1.3, 1.5, 0]), angle=PI/3)
        t_A = TexText("A").shift(cir1.get_center()).set_color(TEAL_D)
        t_B = TexText("B").shift(cir2.get_center()).set_color(BLUE_D)
        text1 = TexText("第$1$种方法", font_size=28).next_to(arrow2, UP)
        text2 = TexText("第$2$种方法", font_size=28).next_to(arrow1, UP*0.3)
        text3 = TexText("第$m$种方法", font_size=28).next_to(arrow3, DOWN)
        group1 = VGroup(cir1, cir2, arrow1, arrow2, arrow3, t_A, t_B, text1, text2, text3)
        group1_copy = group1.copy()

        self.wait(10)
        self.play(LaggedStart(*[FadeIn(cir1), FadeIn(t_A, shift=UP), FadeIn(cir2), FadeIn(t_B, shift=UP)]), run_time=1.5)
        self.play(LaggedStart(*[GrowArrow(arrow2), FadeIn(text1, shift=UP), GrowArrow(arrow1), FadeIn(text2, shift=UP), GrowArrow(arrow3), FadeIn(text3, shift=UP)]))
        self.wait(7)
        self.play(group1_copy.animate.move_to(LEFT*2 + DOWN*1.8))

        cir3 = Circle(color=WHITE).shift(RIGHT*5 + DOWN*1.8)
        t_C = TexText("C").shift(cir3.get_center()).set_color(PURPLE_D)
        arrow4 = CurvedArrow(start_point=np.array([1.7, -1.4, 0]), end_point=np.array([3.8, -1.4, 0]), angle=-PI/3)
        arrow5 = CurvedArrow(start_point=np.array([1.7, -1.9, 0]), end_point=np.array([3.8, -1.9, 0]), angle=PI/3)
        text4 = TexText("第$1$种方法", font_size=28).next_to(arrow4, UP)
        text5 = TexText("第$n$种方法", font_size=28).next_to(arrow5, DOWN)
        group2 = VGroup(cir3, t_C, arrow4, arrow5, text4, text5)

        self.play(LaggedStart(*[FadeIn(cir3), FadeIn(t_C, shift=UP)]))
        self.play(LaggedStart(*[GrowArrow(arrow4), FadeIn(text4, shift=UP), GrowArrow(arrow5), FadeIn(text5, shift=UP)]))
        self.wait(7)

        tex1 = TexText(r"分类加法:", "$N$", "$=$", "$m$").shift(UP*2).set_color_by_tex_to_color_map({"$N$": BLUE_D, "$m$": YELLOW})
        tex1_0= TexText(r"*这里将$m_{1}, m_{2} \dots m_{n}$种方法设作仅含有一种方法了", font_size=24, color=GREY).next_to(tex1, DOWN*0.8)
        background1 = BackgroundRectangle(group1, BLACK, opacity=0.8)
        tex2 = TexText(r"分步乘法:", "$N$", "$=$", "$m$", "$n$").shift(DOWN*1.8).set_color_by_tex_to_color_map({"$N$": BLUE_D, "$m$": YELLOW, "$n$": RED})
        background2 = BackgroundRectangle(group1_copy, BLACK, opacity=0.8)
        background3 = BackgroundRectangle(group2, BLACK, opacity=0.8)

        self.play(FadeIn(background1), Write(tex1), FadeIn(tex1_0, shift=UP))
        self.wait(5)
        self.play(FadeIn(background2), FadeIn(background3), Write(tex2))
        self.wait(4)
        s_g = VGroup()
        for x in range(-8, 8):
            for y in range(-5, 5):
                s = Square(side_length=1, stroke_color=BLACK, fill_color=BLACK, fill_opacity=1).shift(np.array([x, y, 0]))
                s_g.add(s)
        self.play(*[FadeIn(i) for i in s_g])


class chapter_04(Scene):
    def construct(self):
        title1 = Title("排列", stroke_color=BLACK)
        title2 = Title("组合", stroke_color=BLACK)
        definition1 = TexText("从给定个数为", "$n$", "的不同元素中\\\\取出指定个数为", "$m$", "(", "$m$", "$\\le$", "$n$", ")", "的元素进行排序").set_color_by_tex_to_color_map({"$n$": BLUE_D, "$m$": TEAL_D})
        definition2 = TexText("从给定个数为", "$n$", "的不同元素中\\\\取出指定个数为", "$m$", "(", "$m$", "$\\le$", "$n$", ")", "的元素不进行排序").set_color_by_tex_to_color_map({"$n$": BLUE_D, "$m$": TEAL_D})
        
        self.wait(9)
        self.play(Write(title1))
        self.play(Write(definition1))
        self.wait(6)
        self.play(definition1[9][3:].animate.set_color(YELLOW))
        self.wait(3)
        self.play(LaggedStart(*[FadeTransform(title1, title2), FadeTransform(definition1, definition2)]))
        self.wait(6)
        self.play(definition2[9][3:].animate.set_color(YELLOW))
        self.wait(8)
        self.play(FadeOut(definition2), FadeOut(title2))

        text1 = TexText("•", "组合", "相当于是", "选择", "的结果").set_color_by_tex_to_color_map({"组合": BLUE_D, "选择": YELLOW}).shift(UP + LEFT*0.5)
        text2 = TexText("•", "排列", "相当于是", "选择", "后再", "排序", "的结果").next_to(text1, DOWN*3, aligned_edge=LEFT).set_color_by_tex_to_color_map({"排列": TEAL_D, "选择": YELLOW, "排序": RED})
        self.play(LaggedStart(*[Write(text1), Write(text2)]))

        text3 = TexText("组合", "数").set_color_by_tex_to_color_map({"组合": BLUE_D}).shift(RIGHT*4 + UP*2)
        text4 = TexText("排列", "数").set_color_by_tex_to_color_map({"排列": TEAL_D}).shift(LEFT*4 + UP*2)
        definition3 = TexText("从给定个数为", "$n$", "的\\\\不同元素中取出指定\\\\个数为", "$m$", "(", "$m$", "$\\le$", "$n$", ")", "的\\\\元素所有排列的个数").set_color_by_tex_to_color_map({"$n$": BLUE_D, "$m$": TEAL_D}).next_to(text4, DOWN*2)
        definition4 = TexText("从给定个数为", "$n$", "的\\\\不同元素中取出指定\\\\个数为", "$m$", "(", "$m$", "$\\le$", "$n$", ")", "的\\\\元素所有组合的个数").set_color_by_tex_to_color_map({"$n$": BLUE_D, "$m$": TEAL_D}).next_to(text3, DOWN*2)
        line = DashedLine(UP*5, DOWN*5)

        self.wait(3)
        self.play(LaggedStart(*[ReplacementTransform(text2[1], text4[0]), FadeIn(text4[1], shift=RIGHT), FadeOut(text2[0]), FadeOut(text2[2:])]), LaggedStart(*[ReplacementTransform(text1[1], text3[0]), FadeIn(text3[1], shift=LEFT), FadeOut(text1[0]), FadeOut(text1[2:])]), ShowCreation(line))
        self.wait(2)
        self.play(LaggedStart(*[Write(definition3), Write(definition4)]))

        text5 = TexText("记作：", color=GREY).next_to(definition3, DOWN*2, aligned_edge=LEFT)
        text6 = TexText("记作：", color=GREY).next_to(definition4, DOWN*2, aligned_edge=LEFT)
        tex1 = MTex("A^{{m}}_{{n}}", tex_to_color_map={"{m}": TEAL_D, "{n}": BLUE_D}).next_to(text5, RIGHT)
        tex2 = MTex("C^{{m}}_{{n}}", tex_to_color_map={"{m}": TEAL_D, "{n}": BLUE_D}).next_to(text6, RIGHT)
        
        self.wait(4)
        self.play(Write(text5), Write(text6), 
            LaggedStart(*[FadeIn(tex1[0], shift=UP*3), FadeIn(tex2[0], shift=UP*3)]), 
            LaggedStart(*[
                ReplacementTransform(definition3[1].copy(), tex1[2]), 
                ReplacementTransform(definition4[1].copy(), tex2[2]), 
                ReplacementTransform(definition3[3].copy(), tex1[1]), 
                ReplacementTransform(definition4[3].copy(), tex2[1]),
            ]))
        s_g = VGroup()
        for x in range(-8, 8):
            for y in range(-5, 5):
                s = Square(side_length=1, stroke_color=BLACK, fill_color=BLACK, fill_opacity=1).shift(np.array([x, y, 0]))
                s_g.add(s)
        self.play(LaggedStart(*[FadeIn(i) for i in s_g]))


class chapter_05(Scene):
    def construct(self):
        text1 = Tex(r"a \quad b \quad c \quad d \quad e").shift(UP*2.5)
        list1 = ["a", "b", "c", "d", "e"]
        t_g = VGroup()
        for i, x in zip(list1, range(-2, 3)):
            for n, y in zip(list1, range(-3, 2)):
                if i != n:
                    t = Tex(i + n).shift(np.array([x, y, 0]))
                    t_g.add(t)
        t_g.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        background = BackgroundRectangle(t_g, BLACK, opacity=0.8)
        tex1 = Tex(r"4 \times 5 = 20", color=YELLOW).shift(t_g.get_center()).scale(2)

        self.wait(4)
        self.play(Write(text1))
        self.wait(5)
        self.play(LaggedStart(*[FadeIn(i, shift=UP) for i in t_g]), run_time=2)
        self.play(FadeIn(background), Write(tex1), ShowCreationThenFadeAround(t_g))
        self.play(FadeOut(background), FadeOut(tex1))

        ani_g = []
        pos = [UP, DOWN]
        for i in t_g:
            for n in i[0]:
                ani = FadeOut(n, shift=random.choice(pos))
                ani_g.append(ani)
        self.play(LaggedStart(*[i for i in ani_g]))
        
        text2 = Tex(r"a\\b\\c\\d\\e").shift(LEFT*0.3)
        text3 = Tex(r"( \quad , \quad )").set_color(YELLOW)

        self.play(ReplacementTransform(text1, text2))
        self.play(Write(text3))
        self.play(text2.animate.shift(UP*1.5), rate_func=there_and_back, run_time=2)
        self.play(text2.animate.shift(DOWN*1.5), rate_func=there_and_back, run_time=2)

        text4 = Tex(r"a\\b\\ \ \\d\\e").shift(RIGHT*0.3)
        text5 = Tex("c").shift(LEFT*0.3)
        tex2 = Tex("N", "=", "5(5-1)").shift(DOWN).set_color_by_tex_to_color_map({"N": BLUE_D, "5(5-1)": YELLOW}).scale(0.8)
        tex3 = Tex("N", "=", "5 \\times 4").shift(DOWN).set_color_by_tex_to_color_map({"N": BLUE_D, "5 \\times 4": YELLOW}).scale(0.8)
        tex4 = MTex("A^{{2}}_{{5}}={20}", tex_to_color_map={"{2}": TEAL_D, "{5}": BLUE_D, "{20}": YELLOW}).shift(DOWN).scale(0.8)
        tex5 = Tex(r"( \  a \ , \ c \  )").shift(DOWN*2)
        tex6 = Tex("=").shift(DOWN).rotate(PI/2)
        tex7 = MTex(r"C^{{2}}_{{5}}={A^{{2}}_{{5}} \over 2} = {10}", tex_to_color_map={"{2}": TEAL_D, "{5}": BLUE_D, "{10}": YELLOW}).shift(DOWN*3)

        self.play(FadeIn(text5), FadeTransform(text2, text4))
        self.play(text4.animate.shift(UP*1.5), rate_func=there_and_back, run_time=2)
        self.play(text4.animate.shift(DOWN*1.5))
        self.play(FadeOut(text4[0][1:]))
        self.play(FadeIn(tex2, shift=DOWN))
        self.play(FadeTransform(tex2, tex3))
        self.play(FadeTransformPieces(tex3, tex4))
        self.wait(16)
        self.play(FadeOut(tex4))
        
        self.play(LaggedStart(*[FadeTransform(text3[0][0].copy(), tex5[0][0]), FadeTransform(text3[0][2].copy(), tex5[0][4]), FadeTransform(text3[0][1].copy(), tex5[0][2]), FadeTransform(text5.copy(), tex5[0][3]), FadeTransform(text4[0][0].copy(), tex5[0][1]), FadeIn(tex6)]))
        self.wait(7)
        self.play(FadeIn(tex7, shift=DOWN))
        self.wait(2)
        s_g = VGroup()
        for x in range(-8, 8):
            for y in range(-5, 5):
                s = Square(side_length=1, stroke_color=BLACK, fill_color=BLACK, fill_opacity=1).shift(np.array([x, y, 0]))
                s_g.add(s)
        self.play(*[FadeIn(i) for i in s_g])


class chapter_06(Scene):
    def construct(self):
        tex1 = Tex(r"a \quad b \quad c \quad d \quad e").shift(UP*2.5)
        tex2 = Tex(r"a\\b\\c\\d\\e").shift(LEFT*0.8)
        tex3 = Tex(r"( \quad , \quad , \quad )").set_color(YELLOW)
        tex4 = Tex(r"a\\b\\ \ \\d\\e")
        tex5 = Tex("c").shift(LEFT*0.8)
        tex6 = Tex(r"\ \\b\\ \ \\d\\e").shift(RIGHT*0.8 + DOWN*1.1)
        tex7 = Tex("a")
        tex8 = Tex("d").shift(RIGHT*0.8)
        tex9 = MTex(r"A^{{3}}_{{5}}={5 \times 4 \times 3}", tex_to_color_map={"{3}": TEAL_D, "{5}": BLUE_D, r"{5 \times 4 \times 3}": YELLOW}).shift(DOWN).scale(0.8)
        tex10 = MTex("A^{{3}}_{{5}}={60}", tex_to_color_map={"{3}": TEAL_D, "{5}": BLUE_D, "{60}": YELLOW}).shift(DOWN).scale(0.8)

        self.wait(7)
        self.play(FadeIn(tex1), Write(tex3))
        self.play(ReplacementTransform(tex1, tex2))
        self.play(tex2.animate.shift(DOWN*1.5), rate_func=there_and_back, run_time=2)
        self.play(tex2.animate.shift(UP*1.5), rate_func=there_and_back, run_time=2)
        self.play(FadeIn(tex5), FadeTransform(tex2, tex4))
        self.play(tex4.animate.shift(DOWN*1.5))
        self.play(FadeIn(tex7), FadeTransform(tex4, tex6))
        self.play(tex6.animate.shift(UP*1.5))
        self.play(FadeOut(tex6), FadeIn(tex8))
        self.play(Write(tex9))
        self.wait(1)
        self.play(TransformMatchingMTex(tex9, tex10))
        self.wait(9)
        self.play(CyclicReplace(tex5, tex7))
        self.play(CyclicReplace(tex7, tex8))
        self.play(CyclicReplace(tex7, tex5))
        self.play(CyclicReplace(tex7, tex8))

        tex11 = MTex(r"C^{{3}}_{{5}}={A^{{3}}_{{5}} \over A^{{3}}_{{3}}}", tex_to_color_map={"{3}": TEAL_D, "{5}": BLUE_D}).shift(DOWN*2).scale(0.8)
        tex12 = MTex(r"={3 \times 2 \times 1}", tex_to_color_map={r"{3 \times 2 \times 1}": YELLOW}).scale(0.5).next_to(tex11[6:], RIGHT*0.8)
        tex13 = MTex(r"C^{{3}}_{{5}}={A^{{3}}_{{5}} \over {3 \times 2 \times 1}} = {10}", tex_to_color_map={r"{3 \times 2 \times 1}": YELLOW, "{3}": TEAL_D, "{5}": BLUE_D, "{10}": YELLOW}).shift(DOWN*2).scale(0.8)

        self.wait(12)
        self.play(FadeIn(tex11, shift=DOWN))
        self.wait(9)
        self.play(ShowCreationThenFadeAround(tex11[6:]), FadeIn(tex12, shift=RIGHT))
        self.play(TransformMatchingMTex(tex11, tex13), FadeOut(tex12))
        self.wait(2)
        s_g = VGroup()
        for x in range(-8, 8):
            for y in range(-5, 5):
                s = Square(side_length=1, stroke_color=BLACK, fill_color=BLACK, fill_opacity=1).shift(np.array([x, y, 0]))
                s_g.add(s)
        self.play(*[FadeIn(i) for i in s_g])


class chapter_07(Scene):
    def construct(self):
        definition1 = TexText("一个正整数的阶乘是所有小于等于该数正整数的积")
        tex1 = MTex(r"{n}!=1 \times 2 \times 3 \times \dots \times ({n}-1) \times {n}", tex_to_color_map={"n": BLUE_D}).shift(DOWN)
        tex2 = MTex(r"{n}!=({n}-1)!{n}", tex_to_color_map={"n": BLUE_D}).shift(DOWN)

        self.wait(10)
        self.play(Write(definition1))
        self.wait(7)
        self.play(Write(tex1))
        self.wait(4)
        self.play(TransformMatchingShapes(tex1, tex2))
        self.play(FadeOut(definition1), FadeOut(tex2))
        self.wait(13)

        tex3 = MTex(r"A^{{m}}_{{n}}={n}({n}-1)({n}-2) \dots ({n}-{m}+1)", tex_to_color_map={"{m}": TEAL_D, "{n}": BLUE_D}, font_size=36).shift(UP*2 + LEFT)
        tex4 = MTex(r"=\frac{{n}({n}-1)({n}-2) \dots({n}-{m}+1)({n}-{m})({n}-{m}-1) \dots  \times 1}{({n}-{m})({n}-{m}-1) \dots  \times 1}", tex_to_color_map={"{m}": TEAL_D, "{n}": BLUE_D}, font_size=36).next_to(tex3[3], DOWN*1.5, aligned_edge=LEFT)
        tex5 = MTex(r"=\frac{{n} !}{({n}-{m}) !}", tex_to_color_map={"{m}": TEAL_D, "{n}": BLUE_D}, font_size=36).next_to(tex4[0], DOWN*1.5, aligned_edge=LEFT)

        self.play(Write(tex3[0:4]))
        self.play(FadeIn(tex3[4], shift=DOWN))
        self.wait(3)
        self.play(FadeIn(tex3[5:8], shift=DOWN))
        self.wait(2)
        self.play(FadeIn(tex3[8:10], shift=DOWN))
        self.wait(2)
        self.play(FadeIn(tex3[10:], shift=DOWN))
        self.wait(9)
        
        self.play(LaggedStart(*[FadeTransformPieces(tex3[4:].copy(), tex4[1:11]), 
                *[Write(i) for i in tex4[11:]], 
                Write(tex4[0])]), run_time=2
        )
        self.play(FadeTransform(tex4.copy(), tex5))
        self.wait(26)

        tex6 = MTex(r"C^{m}_{n} = {A^{m}_{n} \over A^{m}_{m}}", tex_to_color_map={"{m}": TEAL_D, "{n}": BLUE_D}, font_size=36).next_to(tex3, DOWN*9, aligned_edge=LEFT)
        tex7 = MTex(r"=\frac{{n}({n}-1)({n}-2) \dots({n}-{m}+1)}{{m} !}", tex_to_color_map={"{m}": TEAL_D, "{n}": BLUE_D}, font_size=36).next_to(tex6[3], DOWN*2, aligned_edge=LEFT)
        tex8 = MTex(r"=\frac{{n} !}{{m} !({n}-{m}) !}", tex_to_color_map={"{m}": TEAL_D, "{n}": BLUE_D}, font_size=36).next_to(tex7, DOWN*1.5, aligned_edge=LEFT)
        
        self.play(Write(tex6))
        self.play(FadeIn(tex7, shift=DOWN))
        self.play(FadeTransform(tex7.copy(), tex8))
        self.wait(4)

        pos = [UP, DOWN, LEFT, RIGHT, UR, UL, DR, DL]
        self.play(
            *[FadeOut(i, shift=random.choice(pos)*3) for i in tex3], 
            *[FadeOut(i, shift=random.choice(pos)*3) for i in tex4], 
            *[FadeOut(i, shift=random.choice(pos)*3) for i in tex5], 
            *[FadeOut(i, shift=random.choice(pos)*3) for i in tex6], 
            *[FadeOut(i, shift=random.choice(pos)*3) for i in tex7], 
            *[FadeOut(i, shift=random.choice(pos)*3) for i in tex8], run_time=3
        )
        t = TexText("@E{r}{s}net", tex_to_color_map={"{r}": "#0088FF", "{s}": "#B46F00"}, font_size=100)
        self.play(FadeIn(t), run_time=2)
        


        
        

        
        