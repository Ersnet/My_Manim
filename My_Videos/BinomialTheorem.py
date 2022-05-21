from manimlib import *
import random

lst = [1]
num = [[1]]

def PaTri(lst):
    l1 = [lst[i] + lst[i+1] for i in range(len(lst)-1)]    # 推导式
    l1.insert(len(l1), 1)
    l1.insert(0, 1)
    num.append(l1)
    if len(l1) <= 5:
        PaTri(l1)             # 递归
    else:
        pass
PaTri(lst)

def PaTriWrite():
    group_temp = []  # 建立临时列表
    for item, n in zip(num, range(5)):
        s = str(item)
        ns = "\\ ".join(s)     # 空格
        new_s = ns.strip("[]") .replace(",", "")
        text = Tex(f"{new_s}", font_size=72).shift(np.array([-4, -n+2, 0]))  # 数
        group_temp.append(text)
    return VGroup(*group_temp)  # 返回

def re_around(obj):
    re_around = Rectangle(height=obj[0].get_height()+0.25, width=obj[0].get_width()+0.5, fill_color=YELLOW, fill_opacity=0.3, stroke_width=0).shift(np.array(obj[0].get_center()))
    return re_around


class PaTrinumbers(Scene):
    def construct(self):
        direction = [UP, DOWN, LEFT, RIGHT, UR, UL, DR, DL]
        tex_color = {"{a}": BLUE_E, "{b}": TEAL_E}

        group = PaTriWrite()
        self.play(
            *[FadeIn(group[0][0][i], shift=random.choice(direction)*3) for i in range(len(group[0][0]))],
            *[FadeIn(group[1][0][i], shift=random.choice(direction)*3) for i in range(len(group[1][0]))],
            *[FadeIn(group[2][0][i], shift=random.choice(direction)*3) for i in range(len(group[2][0]))],
            *[FadeIn(group[3][0][i], shift=random.choice(direction)*3) for i in range(len(group[3][0]))],
            *[FadeIn(group[4][0][i], shift=random.choice(direction)*3) for i in range(len(group[4][0]))],
            run_time=2
        )

        tex1 = Tex("(", "{a}", "+", "{b}", ")^{4} = ", "1", "{a}", "^{4}+", "4", "{a}", "^{3}", "{b}", "+", "6", "{a}", "^{2}", "{b}", "^{2}  +", "4", "{a}", "{b}", "^{3}+", "1", "{b}", "^{4} ", font_size=41).set_color_by_tex_to_color_map(tex_color).next_to(group[4], RIGHT*3)
        tex2 = Tex("(", "{a}", "+", "{b}", ")^{3} = ", "1", "{a}", "^{3}+", "3", "{a}", "^{2}", "{b}", "+", "3", "{a}", "{b}", "^{2}+", "1", "{b}", "^{3}", font_size=41).set_color_by_tex_to_color_map(tex_color).next_to(tex1, UP*2, aligned_edge=LEFT)
        tex3 = Tex("(", "{a}", "+", "{b}", ")^{2} = ", "1", "{a}", "^{2}+", "2", "{a}", "{b}", "+", "1", "{b}", "^{2}", font_size=41).set_color_by_tex_to_color_map(tex_color).next_to(tex2, UP*2, aligned_edge=LEFT)
        tex4 = Tex("(", "{a}", "+", "{b}", ")^{1} = ", "1", "{a}", "+", "1", "{b} ", font_size=41).set_color_by_tex_to_color_map(tex_color).next_to(tex3, UP*2, aligned_edge=LEFT)
    
        self.play(
            ReplacementTransform(group[4][0][0].copy(), tex1[5], path_arc=-PI),
            ReplacementTransform(group[4][0][1].copy(), tex1[8], path_arc=-PI),
            ReplacementTransform(group[4][0][2].copy(), tex1[13], path_arc=-PI),
            ReplacementTransform(group[4][0][3].copy(), tex1[18], path_arc=-PI),
            ReplacementTransform(group[4][0][4].copy(), tex1[22], path_arc=-PI),
            *[Write(tex1[i]) for i in range(len(tex1)) if i != 5 and i !=8 and i !=13 and i !=18 and i !=22],
            
            ReplacementTransform(group[3][0][0].copy(), tex2[5], path_arc=-PI),
            ReplacementTransform(group[3][0][1].copy(), tex2[8], path_arc=-PI),
            ReplacementTransform(group[3][0][2].copy(), tex2[13], path_arc=-PI),
            ReplacementTransform(group[3][0][3].copy(), tex2[17], path_arc=-PI),
            *[Write(tex2[i]) for i in range(len(tex2)) if i != 5 and i !=8 and i !=13 and i !=17],
            
            ReplacementTransform(group[2][0][0].copy(), tex3[5], path_arc=-PI),
            ReplacementTransform(group[2][0][1].copy(), tex3[8], path_arc=-PI),
            ReplacementTransform(group[2][0][2].copy(), tex3[12], path_arc=-PI),
            *[Write(tex3[i]) for i in range(len(tex3)) if i != 5 and i !=8 and i !=12],

            ReplacementTransform(group[1][0][0].copy(), tex4[5], path_arc=-PI),
            ReplacementTransform(group[1][0][1].copy(), tex4[8], path_arc=-PI),
            *[Write(tex4[i]) for i in range(len(tex4)) if i != 5 and i !=8],
            run_time=2.5
        )
        self.wait(0.5)

        self.play(
            *[FadeOut(tex1[i], shift=DOWN) for i in range(len(tex1)) if i == 5 or i == 22],
            *[FadeOut(tex2[i], shift=DOWN) for i in range(len(tex2)) if i == 5 or i == 17],
            *[FadeOut(tex3[i], shift=DOWN) for i in range(len(tex3)) if i == 5 or i == 12],
            *[FadeOut(tex4[i], shift=DOWN) for i in range(len(tex4)) if i == 5 or i == 8],
            tex1[6:len(tex1)-3].animate.shift(LEFT*0.25),
            tex2[6:len(tex2)-3].animate.shift(LEFT*0.25),
            tex3[6:len(tex3)-3].animate.shift(LEFT*0.25),
            tex4[6:len(tex4)-2].animate.shift(LEFT*0.25),
            tex1[len(tex1)-2 :].animate.shift(LEFT*0.5),
            tex2[len(tex2)-2 :].animate.shift(LEFT*0.5),
            tex3[len(tex3)-2 :].animate.shift(LEFT*0.5),
            tex4[len(tex4)-1].animate.shift(LEFT*0.5)
        )
        self.wait(1)
        
        self.play(
            *[FadeOut(tex1[i], shift=random.choice(direction)*3) for i in range(len(tex1)) if i != 5 and i != 22],
            *[FadeOut(tex2[i], shift=random.choice(direction)*3) for i in range(len(tex2)) if i != 5 and i != 17],
            *[FadeOut(tex3[i], shift=random.choice(direction)*3) for i in range(len(tex3)) if i != 5 and i != 12],
            *[FadeOut(tex4[i], shift=random.choice(direction)*3) for i in range(len(tex4)) if i != 5 and i != 8],
            *[FadeOut(group[0][0][i], shift=random.choice(direction)*3) for i in range(len(group[0][0]))],
            *[FadeOut(group[1][0][i], shift=random.choice(direction)*3) for i in range(len(group[1][0]))],
            *[FadeOut(group[2][0][i], shift=random.choice(direction)*3) for i in range(len(group[2][0]))],
            *[FadeOut(group[3][0][i], shift=random.choice(direction)*3) for i in range(len(group[3][0]))],
            *[FadeOut(group[4][0][i], shift=random.choice(direction)*3) for i in range(len(group[4][0]))],
            run_time=2.5
        )

class PaTrinumbersWrite(Scene):
    def construct(self):
        group = PaTriWrite()
        text1 = Title("杨辉三角", stroke_color=BLACK)
        self.play(Write(text1), run_time=2)
       
        for n in range(4):
            if n == 0:           # if len(group[n][0]) == 1:
                self.play(Write(group[0][0][0]))
                self.play(
                    ReplacementTransform(group[0][0][0].copy(), group[1][0][0]),
                    ReplacementTransform(group[0][0][0].copy(), group[1][0][1]),
                )
            else:
                self.play(
                    ReplacementTransform(group[n][0][0].copy(), group[n+1][0][0]),
                    ReplacementTransform(group[n][0][len(group[n][0])-1].copy(), group[n+1][0][len(group[n+1][0])-1]),
                )
            self.play(
                *[FadeTransform(group[n][0][i].copy(), group[n+1][0][i+1].copy()) for i in range(len(group[n][0])-1)], 
                *[FadeTransform(group[n][0][i+1].copy(), group[n+1][0][i+1].copy()) for i in range(len(group[n][0])-1)],
                run_time=1.5
            )
        
        tex_dot1 = Tex(r"\cdots").next_to(group[4][0][0], DOWN*2.5).rotate(angle=PI/2)
        tex_dot2 = Tex(r"\cdots").next_to(group[4][0][4], DOWN*2.5).rotate(angle=PI/2)
        self.play(Write(tex_dot1), Write(tex_dot2))
        
        text_lst = BulletedList(
            "每行系数等于上一行的左右两系数之和", 
            "每一行均等于11的n-1次幂", "每一行中最小项为1", 
            "每一行各系数相加等于2的n-1次幂",
            "斐波那契数列",
            "二次项展开系数对应每行系数", 
            font_size=36, stroke_color=BLACK
        ).shift(np.array([3, -0.25, 0]))
        self.play(Write(text_lst[0]))

        re1 = re_around(group[0])
        re2 = re_around(group[1])
        re3 = re_around(group[2])
        re4 = re_around(group[3])
        re5 = re_around(group[4])
        num1 = Tex(r"11^{0}", font_size=24, color=YELLOW).next_to(re1, RIGHT*0.5)
        num2 = Tex(r"11^{1}", font_size=24, color=YELLOW).next_to(re2, RIGHT*0.5)
        num3 = Tex(r"11^{2}", font_size=24, color=YELLOW).next_to(re3, RIGHT*0.5)
        num4 = Tex(r"11^{3}", font_size=24, color=YELLOW).next_to(re4, RIGHT*0.5)
        num5 = Tex(r"11^{4}", font_size=24, color=YELLOW).next_to(re5, RIGHT*0.5)
        self.play(FadeIn(re1))
        self.play(ReplacementTransform(group[0][0].copy(), num1[0][0:2]), Write(num1[0][2:]))
        self.play(FadeTransform(re1, re2))
        self.play(
            ReplacementTransform(group[1][0][0].copy(), num2[0][0]), 
            ReplacementTransform(group[1][0][len(group[1][0])-1].copy(), num2[0][1]),
            Write(num2[0][2:])
        )
        self.play(FadeTransform(re2, re3))
        self.play(
            ReplacementTransform(group[2][0][0].copy(), num3[0][0]), 
            ReplacementTransform(group[2][0][len(group[2][0])-1].copy(), num3[0][1]),
            Write(num3[0][2:])
        )
        self.play(FadeTransform(re3, re4))
        self.play(
            ReplacementTransform(group[3][0][0].copy(), num4[0][0]), 
            ReplacementTransform(group[3][0][len(group[3][0])-1].copy(), num4[0][1]),
            Write(num4[0][2:])
        )
        self.play(FadeTransform(re4, re5))
        self.play(
            ReplacementTransform(group[4][0][0].copy(), num5[0][0]), 
            ReplacementTransform(group[4][0][len(group[4][0])-1].copy(), num5[0][1]),
            Write(num5[0][2:])
        )

        self.wait(0.5)
        self.play(FadeIn(text_lst[1], shift=DOWN))
        self.wait(0.5)
        self.play(LaggedStart(*[FadeOut(num1, shift=DOWN), FadeOut(num2, shift=DOWN), FadeOut(num3, shift=DOWN), FadeOut(num4, shift=DOWN), FadeOut(num5, shift=DOWN), FadeOut(re5)]))
        self.play(LaggedStart(*[Indicate(group[i][0][0]) for i in range(5)], lag_ratio=0.1), run_time=2)
        self.play(FadeIn(text_lst[2], shift=DOWN))
        self.wait(0.5)
        
        temp_add = []
        for n in range(1, 5):
            for i in range(len(group[n][0])-1):
                text_add = Tex("+").next_to(group[n][0][i], RIGHT)
                temp_add.append(text_add)
        group_add = VGroup(*temp_add)
        self.play(FadeIn(group_add, shift=UP*2))
        num6 = Tex(r"=2^{0}", font_size=24, color=BLUE_D).next_to(group[0][0], RIGHT*0.5)
        num7 = Tex(r"=2^{1}", font_size=24, color=BLUE_D).next_to(group[1][0], RIGHT*0.5)
        num8 = Tex(r"=2^{2}", font_size=24, color=BLUE_D).next_to(group[2][0], RIGHT*0.5)
        num9 = Tex(r"=2^{3}", font_size=24, color=BLUE_D).next_to(group[3][0], RIGHT*0.5)
        num10 = Tex(r"=2^{4}", font_size=24, color=BLUE_D).next_to(group[4][0], RIGHT*0.5)
        self.play(LaggedStart(*[FadeIn(num6, shift=DOWN*2), FadeIn(num7, shift=DOWN*2), FadeIn(num8, shift=DOWN*2), FadeIn(num9, shift=DOWN*2), FadeIn(num10, shift=DOWN*2)]))
        self.play(FadeIn(text_lst[3], shift=DOWN))
        self.wait(0.5)
        self.play(LaggedStart(*[FadeOut(num6, shift=DOWN), FadeOut(num7, shift=DOWN), FadeOut(num8, shift=DOWN), FadeOut(num9, shift=DOWN), FadeOut(num10, shift=DOWN), FadeOut(group_add)]))
        
        line1 = Line(np.array([-4.75, 1.6, 0]), np.array([-3, 2.75, 0])).set_color(RED_E)
        line2 = Line(np.array([-5, 0.75, 0]), np.array([-3.25, 1.9, 0]), ).set_color(RED_E)
        line3 = Line(group[2][0][0].get_center(), group[1][0][1].get_center()).set_color(RED_E)
        line4 = Line(group[3][0][0].get_center(), group[2][0][1].get_center()).set_color(RED_E)
        line5 = Line(group[4][0][0].get_center(), group[2][0][2].get_center()).set_color(RED_E)
        num11 = Tex("1").shift(line1.get_end()).rotate(22.5*DEGREES)
        num12 = Tex("1").shift(line2.get_end()).rotate(22.5*DEGREES)
        num13 = Tex("2").shift(line3.get_end()).rotate(22.5*DEGREES)
        num14 = Tex("3").shift(line4.get_end()).rotate(22.5*DEGREES)
        num15 = Tex("5").shift(line5.get_end()).rotate(22.5*DEGREES)
        tex_dot3 = Tex(r"\cdots").next_to(num15, DOWN*6).rotate(angle=PI/2)
        re_grey = BackgroundRectangle(group, BLACK, fill_opacity=0.6, stroke_opacity=0)
        
        self.play(FadeIn(re_grey))
        self.play(ShowCreation(line1), ShowCreation(line2), ShowCreation(line3), ShowCreation(line4), ShowCreation(line5))
        self.play(ReplacementTransform(line1.copy(), num11), ReplacementTransform(line2.copy(), num12), ReplacementTransform(line3.copy(), num13), ReplacementTransform(line4.copy(), num14), ReplacementTransform(line5.copy(), num15))
        self.play(num12.animate.align_to(num11, LEFT), num13.animate.align_to(num11, LEFT), num14.animate.align_to(num11, LEFT), num15.animate.align_to(num11, LEFT).shift(DOWN))
        self.play(Write(tex_dot3))
        self.wait(1)
        self.play(LaggedStart(*[FadeOut(line1, shift=DOWN), FadeOut(line2, shift=DOWN), FadeOut(line3, shift=DOWN), FadeOut(line4, shift=DOWN), FadeOut(line5, shift=DOWN), FadeOut(num11, shift=UP), FadeOut(num12, shift=UP), FadeOut(num13, shift=UP), FadeOut(num14, shift=UP), FadeOut(num15, shift=UP), FadeOut(tex_dot3, shift=UP)]))
        self.play(FadeOut(re_grey))

        self.play(FadeIn(text_lst[4], shift=DOWN))
        self.wait(1)
        self.play(FadeIn(text_lst[5], shift=DOWN))
        self.wait(0.5)
        
        re = Rectangle(height=8, width=15, fill_color=BLACK, stroke_color=BLACK, fill_opacity=1)
        self.play(FadeIn(re), run_time=3)

class Binomial1(Scene):
    def construct(self):
        tex_color = {"{r}": BLUE_E, "{n}": TEAL_E}
        
        tex1 = MTex(r"\sum_{{r}=0}^{n}C^{r}_{n}a^{{n}-{r}}  b^{r}", tex_to_color_map=tex_color).shift(np.array([2, 0, 0]))
        tex2 = MTex(r"C^{r}  _{n} ={{n}! \over {r}!({n}-{r})!}", tex_to_color_map=tex_color).to_edge(UP)
        tex3 = MTex(r"(a+b)^{n}=C_{n}^{0} a^{n}+C_{n}^{1} a^{{n}-1} b+\cdots+{C_{n}^{r}} a^{{n}-r} b^{r}+\cdots+C_{n}^{n} b^{n}", tex_to_color_map=tex_color)
        tex4 = MTex(r"C_{n}^{r} a^{n-r} b^{r}", tex_to_color_map=tex_color).shift(DOWN+RIGHT)
        tex5 = MTex(r"T_{{r}+1}=", tex_to_color_map=tex_color).next_to(tex4, LEFT*0.5)
        tex6 = MTex(r"C_{n}^{r}({r}=0,1,\cdots, {n})", tex_to_color_map=tex_color).shift(DOWN*2+RIGHT*1.5)

        text1 = TexText("二项式定理：").shift(np.array([-1, 0, 0]))
        text2 = TexText("将它展开").to_edge(DOWN)
        text3 = TexText("通项：").next_to(tex4, LEFT*0.5)
        text4 = TexText("二项式系数：").next_to(tex6, LEFT*0.5)

        self.play(Write(tex1), FadeIn(text1, shift=LEFT), run_time=1.5)
        self.play(ReplacementTransform(tex1[4:7].copy(), tex2[0:3]), Write(tex2[3:]), run_time=1.5)
        self.play(Write(text2))
        self.play(TransformMatchingMTex(tex1, tex3), text1.animate.shift(UP+RIGHT), FadeOut(text2))
        self.wait(1)

        self.play(ReplacementTransform(tex3[14:21].copy(), tex4[1:]), FadeIn(text3, shift=LEFT), Write(tex4[0]))
        self.wait(0.5)
        self.play(FadeOut(text3), FadeIn(tex5))
        self.play(FadeIn(text4, shift=DOWN), FadeIn(tex6, shift=UP))
        self.wait(1)
        re = Rectangle(height=8, width=15, fill_color=BLACK, stroke_color=BLACK, fill_opacity=1)
        self.play(FadeIn(re), run_time=3)

class Binomial2(Scene):
    def construct(self):
        tex_color = {"{r}": BLUE_E, "{n}": TEAL_E}

        title = Title("二项式系数的性质", stroke_color=BLACK)
        text1 = BulletedList("对称性", "单峰性", "相加和为2的n次幂", stroke_color=BLACK).shift(LEFT*4)
        text2 = TexText("故成立").to_edge(DOWN)
        
        tex1 = MTex(r"C_{n}^{r}=C_{n}^{{n}-{r}}", tex_to_color_map=tex_color).shift(UP)
        tex2 = MTex(r"C_{n}^{r}={{n} ! \over {r} !({n}-{r}) !}", tex_to_color_map=tex_color).next_to(tex1, DOWN, aligned_edge=LEFT)
        tex3 = MTex(r"C_{n}^{{n}-{r}}={{n} ! \over ({n}-{r}) !({n}-{n}+{r}) !}", tex_to_color_map=tex_color).next_to(tex2, DOWN, aligned_edge=LEFT)
        tex4 = MTex(r"C_{n}^{{n}-{r}}={{n} ! \over ({n}-{r}) !{r} !}", tex_to_color_map=tex_color).next_to(tex2, DOWN, aligned_edge=LEFT)


        self.play(Write(title), run_time=2)
        self.play(Write(text1[0]))
        self.play(Write(tex1), run_time=1.5)
        self.play(
            ReplacementTransform(tex1[0:3].copy(), tex2[0:3]), 
            ReplacementTransform(tex1[4:].copy(), tex3[1:5]),
            Write(tex2[3:]), Write(tex3[0]), Write(tex3[5:]), run_time=2
        )
        self.wait(1)
        self.play(TransformMatchingMTex(tex3, tex4), run_time=2)
        self.wait(0.5)
        self.play(Write(text2))
        self.play(LaggedStart(*[FadeOut(tex1, shift=LEFT), FadeOut(tex2, shift=RIGHT), FadeOut(tex4, shift=LEFT), FadeOut(text2, shift=DOWN)]))
        self.play(Write(text1[1]), run_time=1.5)

        text3 = TexText(r"当", r"${n}$", "为偶数时：").shift(UP*0.5).set_color_by_tex_to_color_map(tex_color)
        tex5 = MTex(r"C^{{{n} \over 2}} _{n} > C^{n} _{n}", tex_to_color_map=tex_color).next_to(text3, DOWN)
        text4 = TexText(r"当", r"${n}$", "为奇数时：").next_to(tex5, DOWN).set_color_by_tex_to_color_map(tex_color)
        tex6 = MTex(r"C^{{{n}-1 \over 2}} _{n} = C^{{{n}+1 \over 2}} _{n} > C^{n} _{n}", tex_to_color_map=tex_color).next_to(text4, DOWN)

        self.play(Write(text3))
        self.play(FadeIn(tex5, shift=DOWN))
        self.wait(0.5)
        self.play(Write(text4))
        self.play(FadeIn(tex6, shift=DOWN))
        self.wait(0.5)
        self.play(LaggedStart(*[FadeOut(tex5, shift=LEFT), FadeOut(tex6, shift=RIGHT), FadeOut(text3, shift=RIGHT), FadeOut(text4, shift=LEFT)]))
        self.play(Write(text1[2]), run_time=1.5)
        self.wait(0.5)

        tex7 = MTex(r"2^{n}=(1+1)^{n}", tex_to_color_map=tex_color)
        self.play(Write(tex7))
        tex8 = MTex(r"=\sum_{{r}=0}^{n} C_{n}^{p}=C_{n}^{0}+C_{n}^{1}+\cdots+C_{n}^{n}", tex_to_color_map=tex_color).next_to(tex7[2], DOWN,aligned_edge=LEFT)
        self.play(Write(tex8))
        self.wait(2)
        re = Rectangle(height=8, width=15, fill_color=BLACK, stroke_color=BLACK, fill_opacity=1)
        self.play(FadeIn(re), run_time=3)

class Final(Scene):
    def construct(self):
        t = ValueTracker(-8)
        group = PaTriWrite().shift(RIGHT*4)
        self.play(FadeIn(group), run_time=2)
        re_grey = BackgroundRectangle(group, BLACK, fill_opacity=0.4, stroke_opacity=0)
        self.play(FadeIn(re_grey), run_time=2)
        
        text1 = TexText("杨辉三角可以直接联系到二项式定理").to_edge(LEFT)
        text2 = TexText("其中许多性质基本等价于二项式定理").next_to(text1, DOWN*0.5, aligned_edge=LEFT)
        text3 = TexText("杨辉每一行的数字左右对称").next_to(text2, DOWN*0.5, aligned_edge=LEFT)
        text4 = TexText(r"即$C_{n}^{r}=C_{n}^{n-r}$").next_to(text3, DOWN*0.5, aligned_edge=LEFT)
        text5 = TexText("当n为偶数时，最中间那个数最大").next_to(text4, DOWN*0.5, aligned_edge=LEFT)
        text6 = TexText("当n为奇数时，最中间的两个数最大").next_to(text5, DOWN*0.5, aligned_edge=LEFT)
        text7 = TexText("即二项式系数性质中的单峰性").next_to(text6, DOWN*0.5, aligned_edge=LEFT)
        text8 = TexText("第n行的数字有n项，数字和为2的n-1次幂").next_to(text7, DOWN*0.5, aligned_edge=LEFT)
        text9 = TexText("杨辉三角每行系数对应二次项展开系数等等").next_to(text8, DOWN*0.5, aligned_edge=LEFT)
        text10 = TexText("杨辉三角它仍然受到世界上数学家们的重视").next_to(text9, DOWN*0.5, aligned_edge=LEFT)
        text11 = TexText("杨辉三角是中国古代数学的杰出研究成果之").next_to(text10, DOWN*0.5, aligned_edge=LEFT)
        text12 = TexText("它把二项式系数图形化").next_to(text11, DOWN*0.5, aligned_edge=LEFT)
        text13 = TexText("把组合数内在的一些代数性质直观地从图形中体现出来").next_to(text12, DOWN*0.5, aligned_edge=LEFT)
        text14 = TexText("是一种离散型的数与形的结合!").next_to(text13, DOWN*0.5, aligned_edge=LEFT)
        
        
        g = VGroup(text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14).scale(0.8).add_updater(lambda obj: obj.move_to(np.array([-2, t.get_value(), 0])))
        self.add(g)
        self.play(t.set_value, 7.5, rate_func=linear, run_time=25)
        self.play(FadeOut(re_grey))
        self.play(FadeOut(group))
        
class end(Scene):
    def construct(self):
        text = TexText("@E", "r", "s", "net", font_size=100).set_color_by_tex_to_color_map({"r": "#0088FF", "s": "#B46F00"})
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(text))
