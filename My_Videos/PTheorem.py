from manimlib import *
import random

pos = [UP, DOWN, LEFT, RIGHT, UR, UL, DR, DL]

# 查索引用：
def debugTeX(self, texm, scale_factor=0.6, text_color=RED):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="SimSun").scale(scale_factor).set_color(text_color)
        tex_id.move_to(j)
        self.add(tex_id)


def get_all_pos(pos1, pos2):  # 只写了适合视频效果的情况
    a, b, c, d = pos1[0], pos1[1], pos2[0], pos2[1]

    if b < d and a > c:
        x_len, y_len = d - b, a - c
        e, f, g, h = a + x_len, b + y_len, c + x_len, d + y_len
        pos3, pos4 = np.array([e, f, 0]), np.array([g, h, 0])
        return pos3, pos4

    elif b < d and a < c:
        x_len, y_len = d - b, c - a
        e, f, g, h = a - x_len, b + y_len, c - x_len, d + y_len
        pos3, pos4 = np.array([e, f, 0]), np.array([g, h, 0])
        return pos3, pos4

def get_area(pos1, pos2):
            a, b, c, d = pos1[0], pos1[1], pos2[0], pos2[1]
            area = (c - a)**2 + (d - b)**2
            return area


class chapter_01(Scene):
    def construct(self):
        tri = Polygon(np.array([-1, 0, 0]), np.array([-1, 1, 0]), np.array([2, 0, 0]))
        elbow = Elbow(color=YELLOW).shift(np.array([-1, 0, 0]))
        s1 = Polygon(np.array([-1, 0, 0]), np.array([-1, 1, 0]), np.array([-2, 1, 0]), np.array([-2, 0, 0]), color=TEAL, fill_opacity=0.6)
        s2 = Polygon(np.array([2, 0, 0]), np.array([-1, 1, 0]), np.array([0, 4, 0]), np.array([3, 3, 0]), color=BLUE, fill_opacity=0.6)
        s3 = Polygon(np.array([-1, 0, 0]), np.array([2, 0, 0]), np.array([2, -3, 0]), np.array([-1, -3, 0]), color=RED, fill_opacity=0.6)
        s4 = Square(side_length=10**0.5, color=BLUE, fill_opacity=0.6).shift(np.array([4.5, 0, 0]))

        self.play(ShowCreation(tri))
        self.play(FadeIn(elbow))
        self.wait(0.5)
        self.play(LaggedStart(FadeIn(s1, shift=LEFT), FadeIn(s2, shift=DR), FadeIn(s3, shift=DOWN)))
        self.wait(0.5)
        self.play(LaggedStart(
                s1.animate.move_to(np.array([-5, 0, 0])), 
                s3.animate.move_to(np.array([-1, 0, 0])), 
                ReplacementTransform(s2, s4), 
                FadeOut(tri), FadeOut(elbow)
        ))

        tex1 = MTex("+").shift(np.array([-3.5, 0, 0]))
        tex2 = MTex("=").shift(np.array([1.75, 0, 0]))
        
        self.play(LaggedStart(Write(tex1, shift=UP), Write(tex2, shift=UP)))
        self.wait(1)
        
class chapter_02(Scene):
    def construct(self):
        pos = [UP, DOWN, LEFT, RIGHT, UR, UL, DR, DL]

        text1 = Text("定义：a，b为三角形较短两边，c为最长边", font="LXGW WenKai", t2c={"定义": YELLOW, "a": TEAL_D, "b": BLUE_D, "c": LIGHT_BROWN}).shift(UP*2)
        text2 = Text("所以：a²+b²=c²", font="LXGW WenKai", t2c={"所以": YELLOW, "a": TEAL_D, "b": BLUE_D, "c": LIGHT_BROWN}).next_to(text1, DOWN*4, aligned_edge=LEFT)
        text3 = Tex(r"\Longleftrightarrow ").next_to(text2, RIGHT*0.5)
        text4 = Text("∠C=90°（∠C为c的对角）", font="LXGW WenKai", t2c={"C": DARK_BROWN, "c": LIGHT_BROWN}).next_to(text3, RIGHT*0.5)
        text5 = Text("那么：a²+b²>c²", font="LXGW WenKai", t2c={"那么": YELLOW, "a": TEAL_D, "b": BLUE_D, "c": LIGHT_BROWN}).next_to(text2, DOWN*4, aligned_edge=LEFT)
        text6 = Tex(r"\Longleftrightarrow ").next_to(text5, RIGHT*0.5)
        text7 = Text("∠C<90° ？？？", font="LXGW WenKai", t2c={"C": DARK_BROWN}).next_to(text6, RIGHT*0.5)
        text8 = Text("a²+b²<c²", font="LXGW WenKai", t2c={"a": TEAL_D, "b": BLUE_D, "c": LIGHT_BROWN}).next_to(text5[3], DOWN*4, aligned_edge=LEFT)
        text9 = Tex(r"\Longleftrightarrow ").next_to(text8, RIGHT*0.5)
        text10 = Text("∠C>90° ？？？", font="LXGW WenKai", t2c={"C": DARK_BROWN}).next_to(text9, RIGHT*0.5)

        self.play(Write(text1))
        self.play(LaggedStart(
            *[FadeIn(text2[i], shift=random.choice(pos)*2) for i in range(len(text2)) if i != 3 and i != 6 and i != 9], 
            FadeIn(text3, shift=random.choice(pos)*2), 
            *[FadeIn(text4[:10][i], shift=random.choice(pos)*2) for i in range(len(text4[:10]))],
            *[FadeIn(text4[11:][i], shift=random.choice(pos)*2) for i in range(len(text4[11:]))],
            ReplacementTransform(text1[3].copy(), text2[3]), 
            ReplacementTransform(text1[5].copy(), text2[6]), 
            ReplacementTransform(text1[15].copy(), text2[9]), 
            ReplacementTransform(text1[15].copy(), text4[10])
        ))
        self.wait(2)

        self.play(LaggedStart(
            *[FadeIn(text5[i], shift=random.choice(pos)*2) for i in range(len(text5)) if i != 3 and i != 6 and i != 9], 
            FadeIn(text6, shift=random.choice(pos)*2), 
            *[FadeIn(text7[:][i], shift=random.choice(pos)*2) for i in range(len(text7[:]))],
            ReplacementTransform(text1[3].copy(), text5[3]), 
            ReplacementTransform(text1[5].copy(), text5[6]), 
            ReplacementTransform(text1[15].copy(), text5[9]), 
            *[FadeIn(text8[i], shift=random.choice(pos)*2) for i in range(len(text8)) if i != 0 and i != 3 and i != 6],
            FadeIn(text9, shift=random.choice(pos)*2), 
            *[FadeIn(text10[:][i], shift=random.choice(pos)*2) for i in range(len(text10[:]))],
            ReplacementTransform(text1[3].copy(), text8[0]), 
            ReplacementTransform(text1[5].copy(), text8[3]), 
            ReplacementTransform(text1[15].copy(), text8[6]), 
        ))
        self.wait(2)


class chapter_03(Scene):
    def construct(self):

        t = ValueTracker(1.5)

        tri = Polygon(np.array([1*1.5, 0, 0]), np.array([-1*1.5, 0, 0]), np.array([0, 1*1.5, 0])).add_updater(lambda tri: tri.become(Polygon(np.array([1*1.5, 0, 0]), np.array([-1*1.5, 0, 0]), np.array([1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0]))))
        elbow = Elbow(color=YELLOW).shift(np.array([1.5*np.cos(1.5), 1.5*np.sin(1.5), 0])).rotate(angle=-135*DEGREES, about_point=np.array([1.5*np.cos(1.5), 1.5*np.sin(1.5), 0]))

        def ani1(obj):
            pos3, pos4 = get_all_pos([-1*1.5, 0, 0], [1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0])
            obj.become(Polygon(np.array([-1*1.5, 0, 0]), np.array([1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0]), pos4, pos3, color=TEAL, fill_opacity=0.6))

        def ani2(obj):
            pos3, pos4 = get_all_pos([1*1.5, 0, 0], [1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0])
            obj.become(Polygon(np.array([1*1.5, 0, 0]), np.array([1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0]), pos4, pos3, color=BLUE, fill_opacity=0.6))
        
        s1 = Polygon(np.array([-1*1.5, 0, 0]), np.array([0, 1*1.5, 0]), np.array([-1*1.5, 2*1.5, 0]), np.array([-2*1.5, 1*1.5, 0]), color=TEAL, fill_opacity=0.6).add_updater(ani1)
        s2 = Polygon(np.array([1*1.5, 0, 0]), np.array([0, 1*1.5, 0]), np.array([1*1.5, 2*1.5, 0]), np.array([2*1.5, 1*1.5, 0]), color=BLUE, fill_opacity=0.6).add_updater(ani2)
        s3 = Polygon(np.array([1*1.5, 0, 0]), np.array([-1*1.5, 0, 0]), np.array([-1*1.5, -2*1.5, 0]), np.array([1*1.5, -2*1.5, 0]), color=RED, fill_opacity=0.6)
        
        a1 = MTex(r"\cdot {s_{1}}=", tex_to_color_map={"{s_{1}}": TEAL}).shift(LEFT*5.5 + UP*2)
        a2 = MTex(r"\cdot {s_{2}}=", tex_to_color_map={"{s_{2}}": BLUE}).next_to(a1, DOWN*6)
        a3 = MTex(r"\cdot {s_{3}}=", tex_to_color_map={"{s_{3}}": RED}).next_to(a2, DOWN*6)
        a = MTex("{s_{1}}+{s_{2}}={s_{3}}", tex_to_color_map={"{s_{1}}": TEAL, "{s_{2}}": BLUE, "{s_{3}}": RED}).next_to(a2, RIGHT*35)

        num1 = DecimalNumber().next_to(a1, RIGHT*0.8, aligned_edge=DOWN).set_color(TEAL).add_updater(lambda n: n.set_value(get_area(s1.get_vertices()[0], s1.get_vertices()[1])))
        num2 = DecimalNumber().next_to(a2, RIGHT*0.8, aligned_edge=DOWN).set_color(BLUE).add_updater(lambda n: n.set_value(get_area(s2.get_vertices()[0], s2.get_vertices()[1])))
        num3 = DecimalNumber(9).next_to(a3, RIGHT*0.8, aligned_edge=DOWN).set_color(RED)
        
        self.play(ShowCreation(tri))
        self.play(ShowCreationThenFadeOut(elbow))
        self.add(tri)
        self.play(t.animate.set_value(PI-0.1), run_time=2, rate_func=there_and_back)
        self.play(t.animate.set_value(0.1))
        self.play(LaggedStart(ShowCreation(s1), ShowCreation(s2), ShowCreation(s3)))
        self.add(s1, s2, num1, num2, num3, a1, a2, a3)
        self.play(t.animate.set_value(PI-0.1), run_time=5, rate_func=there_and_back)
        self.play(LaggedStart(
            ReplacementTransform(a1[1:3].copy(), a[0:2]), 
            ReplacementTransform(a2[1:3].copy(), a[3:5]), 
            ReplacementTransform(a3[1:3].copy(), a[6:]),
        ))
        self.play(Write(a[2]), Write(a[5]))
        self.wait(2)
        
class chapter_04(Scene):
    def construct(self):
        t = ValueTracker(1.5)

        tri = Polygon(np.array([1.5, 0, 0]), np.array([-1.5, 0, 0]), np.array([0, 1.5, 0]))

        s1 = Polygon(np.array([1.5, 0, 0]), np.array([0, 1.5, 0]), np.array([1.5, 3, 0]), np.array([3, 1.5, 0]), color=BLUE, fill_opacity=0.6)
        s2 = Polygon(np.array([-1.5, 0, 0]), np.array([0, 1.5, 0]), np.array([-1.5, 3, 0]), np.array([-3, 1.5, 0]), color=TEAL, fill_opacity=0.6)
        s3 = Polygon(np.array([-1.5, 0, 0]), np.array([1.5, 0, 0]), np.array([1.5, -3, 0]), np.array([-1.5, -3, 0]), color=RED, fill_opacity=0.6)
        d_l = DashedLine(np.array([0, 1.5, 0]), np.array([0, -3, 0]))

        tri1 = Polygon(np.array([-1.5, 0, 0]), np.array([-3, 1.5, 0]), np.array([1.5, 0, 0]), color=YELLOW, fill_opacity=0.4)
        tri2 = Polygon(np.array([-1.5, 0, 0]), np.array([0, 1.5, 0]), np.array([-1.5, -3, 0]), color=YELLOW, fill_opacity=0.4)

        tri3 = Polygon(np.array([-1.5, 0, 0]), np.array([-3, 1.5, 0]), np.array([0, 1.5, 0]), color=YELLOW, fill_opacity=0.4)
        tri4 = Polygon(np.array([-1.5, 0, 0]), np.array([0, 0, 0]), np.array([-1.5, -3, 0]), color=YELLOW, fill_opacity=0.4)
        
        tri5 = Polygon(np.array([-1.5, 3, 0]), np.array([-3, 1.5, 0]), np.array([0, 1.5, 0]), color=YELLOW, fill_opacity=0.4)
        tri6 = Polygon(np.array([0, 0, 0]), np.array([0, -3, 0]), np.array([-1.5, -3, 0]), color=YELLOW, fill_opacity=0.4)

        s4 = Polygon(np.array([-5, 0.5, 0]), np.array([-3.5, 2, 0]), np.array([-5, 3.5, 0]), np.array([-6.5, 2, 0]), color=YELLOW, fill_opacity=0.4)
        s5 = Polygon(np.array([-5.75, -0.5, 0]), np.array([-4.25, -0.5, 0]), np.array([-4.25, -3.5, 0]), np.array([-5.75, -3.5, 0]), color=YELLOW, fill_opacity=0.4)

        s6 = Polygon(np.array([5, 0.5, 0]), np.array([3.5, 2, 0]), np.array([5, 3.5, 0]), np.array([6.5, 2, 0]), color=YELLOW, fill_opacity=0.4).shift(LEFT*3.5+DOWN*0.5)
        s7 = Polygon(np.array([5.75, -0.5, 0]), np.array([4.25, -0.5, 0]), np.array([4.25, -3.5, 0]), np.array([5.75, -3.5, 0]), color=YELLOW, fill_opacity=0.4).shift(LEFT*4.25+UP*0.5)
        
        tex1 = MTex("=").rotate(90*DEGREES).shift(LEFT*5)
        tex2 = MTex("=").rotate(90*DEGREES).shift(RIGHT*5)

        self.play(ShowCreation(tri))
        self.play(LaggedStart(FadeIn(s1), FadeIn(s2), FadeIn(s3)))
        self.play(ShowCreation(d_l))
        self.play(ShowCreation(tri1))
        self.play(ReplacementTransform(tri1.copy(), tri2))
        self.wait(0.25)
        self.play(LaggedStart(ReplacementTransform(tri1, tri3), ReplacementTransform(tri2, tri4)))
        self.play(LaggedStart(ReplacementTransform(tri3.copy(), tri5), ReplacementTransform(tri4.copy(), tri6)))
        self.play(LaggedStart(VGroup(tri3, tri5).animate.shift(LEFT*3.5+UP*0.5), VGroup(tri4, tri6).animate.shift(LEFT*4.25+DOWN*0.5)))
        self.play(LaggedStart(FadeOut(VGroup(tri3, tri5)), FadeIn(s4), FadeOut(VGroup(tri4, tri6)), FadeIn(s5)))
        self.play(Write(tex1))
        self.play(LaggedStart(FadeIn(s6), FadeIn(s7)))
        self.play(LaggedStart(s6.animate.shift(RIGHT*3.5+UP*0.5), s7.animate.shift(RIGHT*4.25+DOWN*0.5), Write(tex2)))
        
        def tri_anim(obj):
            obj.become(Polygon(np.array([1*1.5, 0, 0]), np.array([-1*1.5, 0, 0]), np.array([1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0])))
        
        def l_anim(obj):
            obj.become(DashedLine(np.array([1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0]), np.array([1.5*np.cos(t.get_value()), -3, 0])))

        def s2_anim(obj):
            pos3, pos4 = get_all_pos([-1*1.5, 0, 0], [1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0])
            obj.become(Polygon(np.array([-1*1.5, 0, 0]), np.array([1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0]), pos4, pos3, color=TEAL, fill_opacity=0.6))

        def s4_anim(obj):
            pos3, pos4 = get_all_pos([-1*1.5-3.5, 0+0.5, 0], [1.5*np.cos(t.get_value())-3.5, 1.5*np.sin(t.get_value())+0.5, 0])
            obj.become(Polygon(np.array([-1*1.5-3.5, 0+0.5, 0]), np.array([1.5*np.cos(t.get_value())-3.5, 1.5*np.sin(t.get_value())+0.5, 0]), pos4, pos3, color=YELLOW, fill_opacity=0.6))
        
        def s5_anim(obj):
            obj.become(Polygon(np.array([-5.75, -0.5, 0]), np.array([1.5*np.cos(t.get_value())-4.25, -0.5, 0]), np.array([1.5*np.cos(t.get_value())-4.25, -3.5, 0]), np.array([-5.75, -3.5, 0]), color=YELLOW, fill_opacity=0.4))
        
        def s1_anim(obj):
            pos3, pos4 = get_all_pos([1*1.5, 0, 0], [1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0])
            obj.become(Polygon(np.array([1*1.5, 0, 0]), np.array([1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0]), pos4, pos3, color=BLUE, fill_opacity=0.6))
        
        def s6_anim(obj):
            pos3, pos4 = get_all_pos([1*1.5+3.5, 0+0.5, 0], [1.5*np.cos(t.get_value())+3.5, 1.5*np.sin(t.get_value())+0.5, 0])
            obj.become(Polygon(np.array([1*1.5+3.5, 0+0.5, 0]), np.array([1.5*np.cos(t.get_value())+3.5, 1.5*np.sin(t.get_value())+0.5, 0]), pos4, pos3, color=YELLOW, fill_opacity=0.6))
        
        def s7_anim(obj):
            obj.become(Polygon(np.array([5.75, -0.5, 0]), np.array([1.5*np.cos(t.get_value())+4.25, -0.5, 0]), np.array([1.5*np.cos(t.get_value())+4.25, -3.5, 0]), np.array([5.75, -3.5, 0]), color=YELLOW, fill_opacity=0.4))
        
        tri.add_updater(tri_anim)
        d_l.add_updater(l_anim)
        s2.add_updater(s2_anim)
        s4.add_updater(s4_anim)
        s5.add_updater(s5_anim)
        s1.add_updater(s1_anim)
        s6.add_updater(s6_anim)
        s7.add_updater(s7_anim)
        
        self.add(tri, s2, s4, s3, d_l, s1, s6, s7, s5)
        self.play(t.animate.set_value(PI-0.001), run_time=6, rate_func=there_and_back)
        self.play(LaggedStart(Uncreate(tex1), Uncreate(s4), Uncreate(d_l), Uncreate(s6), Uncreate(s7), Uncreate(tex2), Uncreate(s5)))

        tex3 = MTex("s_{1}").set_color(BLUE).shift(s1.get_center())
        tex4 = MTex("s_{2}").set_color(TEAL).shift(s2.get_center())
        tex5 = MTex("s_{3}").set_color(RED).shift(s3.get_center())
        tex6 = MTex("{s_{1}}+{s_{2}}={s_{3}}", tex_to_color_map={"{s_{1}}": BLUE, "{s_{2}}": TEAL, "{s_{3}}": RED}).to_edge(DOWN)

        self.play(LaggedStart(Write(tex3), Write(tex4), Write(tex5)))
        self.play(LaggedStart(
            ReplacementTransform(tex3.copy(), tex6[0:2]), 
            ReplacementTransform(tex4.copy(), tex6[3:5]), 
            ReplacementTransform(tex5.copy(), tex6[6:]),
        ))
        self.play(Write(tex6[2]), Write(tex6[5]))
        self.wait(0.5)
        
        t1 = MTex("a").shift(np.array([-0.75, 0.75, 0])).set_color(TEAL)
        t2 = MTex("b").shift(np.array([0.75, 0.75, 0])).set_color(BLUE)
        t3 = MTex("c").shift(np.array([0, 0, 0])).set_color(RED)
        t_group = VGroup(t1, t2, t3)
        t4 = MTex(r"{a}^{2}+{b}^{2}={c}^{2} \Longleftrightarrow \angle C=90^{\circ }", tex_to_color_map={"{b}": BLUE, "{a}": TEAL, "{c}": RED}).to_edge(DOWN)
            

        self.play(LaggedStart(*[FadeIn(i, shift=random.choice(pos)**2) for i in t_group]))
        self.play(LaggedStart(
            ReplacementTransform(t1, t4[0]), 
            ReplacementTransform(t2, t4[3]), 
            ReplacementTransform(t3, t4[6]), 
            FadeOut(tex6), 
            *[Write(t4[i]) for i in range(len(t4))  if i != 0 and i != 3 and i != 6]
        ))
        self.wait(2)

class chapter_05(Scene):
    def construct(self):

        t = ValueTracker(0)
        n = ValueTracker(1)

        tri = Polygon(np.array([1.5, 0, 0]), np.array([-1.5, 0, 0]), np.array([-0.5, 1, 0]))
        arc = Arc(arc_center=np.array([-0.5, 1, 0]), radius=0.3, angle=108*DEGREES, start_angle=-135*DEGREES, color=YELLOW)

        s1 = Polygon(np.array([-1.5, 0, 0]), np.array([-0.5, 1, 0]), np.array([-1.5, 2, 0]), np.array([-2.5, 1, 0]), color=TEAL, fill_opacity=0.6)
        s2 = Polygon(np.array([1.5, 0, 0]), np.array([-0.5, 1, 0]), np.array([0.5, 3, 0]), np.array([2.5, 2, 0]), color=BLUE, fill_opacity=0.6)
        s3 = Polygon(np.array([1*1.5, 0, 0]), np.array([-1*1.5, 0, 0]), np.array([-1*1.5, -2*1.5, 0]), np.array([1*1.5, -2*1.5, 0]), color=RED, fill_opacity=0.6)
        
        def tri_anim(obj):
            obj.become( Polygon(np.array([1.5, 0, 0]), np.array([-1.5, 0, 0]), np.array([-0.5+t.get_value(), n.get_value(), 0])))
        
        def s1_anim(obj):
            pos3, pos4 = get_all_pos([-1.5, 0, 0], [-0.5+t.get_value(), n.get_value(), 0])
            obj.become(Polygon(np.array([-1.5, 0, 0]), np.array([-0.5+t.get_value(), n.get_value(), 0]), pos4, pos3, color=TEAL, fill_opacity=0.6))

        def s2_anim(obj):
            pos3, pos4 = get_all_pos([1.5, 0, 0], [-0.5+t.get_value(), n.get_value(), 0])
            obj.become(Polygon(np.array([1.5, 0, 0]), np.array([-0.5+t.get_value(), n.get_value(), 0]), pos4, pos3, color=BLUE, fill_opacity=0.6))

        a1 = MTex(r"\cdot {s_{1}}=", tex_to_color_map={"{s_{1}}": TEAL}).shift(LEFT*5.5 + UP*2)
        a2 = MTex(r"\cdot {s_{2}}=", tex_to_color_map={"{s_{2}}": BLUE}).next_to(a1, DOWN*6)
        a3 = MTex(r"\cdot {s_{3}}=", tex_to_color_map={"{s_{3}}": RED}).next_to(a2, DOWN*6)
        a = MTex("{s_{1}}+{s_{2}}<{s_{3}}", tex_to_color_map={"{s_{1}}": TEAL, "{s_{2}}": BLUE, "{s_{3}}": RED}).next_to(a2, RIGHT*35)
        tex1 = MTex(r"\angle {C}>90^{\circ }", tex_to_color_map={"{C}": DARK_BROWN}).next_to(a, DOWN)

        num1 = DecimalNumber().next_to(a1, RIGHT*0.8, aligned_edge=DOWN).set_color(TEAL).add_updater(lambda n: n.set_value(get_area(s1.get_vertices()[0], s1.get_vertices()[1])))
        num2 = DecimalNumber().next_to(a2, RIGHT*0.8, aligned_edge=DOWN).set_color(BLUE).add_updater(lambda n: n.set_value(get_area(s2.get_vertices()[0], s2.get_vertices()[1])))
        num3 = DecimalNumber(9).next_to(a3, RIGHT*0.8, aligned_edge=DOWN).set_color(RED)
        
        self.play(ShowCreation(tri))
        self.play(ShowCreationThenFadeOut(arc))
        self.play(LaggedStart(ShowCreation(s1), ShowCreation(s2), ShowCreation(s3)))

        tri.add_updater(tri_anim)
        s1.add_updater(s1_anim)
        s2.add_updater(s2_anim)

        self.add(tri, s1, s2, s3, a1, a2, a3, num1, num2, num3)
        self.play(t.animate.set_value(1.499999), run_time=3, rate_func=there_and_back)
        self.play(t.animate.set_value(-0.499999), run_time=2, rate_func=there_and_back)
        self.play(LaggedStart(
            ReplacementTransform(a1[1:3].copy(), a[0:2]), 
            ReplacementTransform(a2[1:3].copy(), a[3:5]), 
            ReplacementTransform(a3[1:3].copy(), a[6:]),
        ))
        self.play(Write(a[2]), Write(a[5]))
        self.play(Write(tex1))
        self.play(n.animate.set_value(3.8), run_time=5)

        a4 = MTex("{s_{1}}+{s_{2}}>{s_{3}}", tex_to_color_map={"{s_{1}}": TEAL, "{s_{2}}": BLUE, "{s_{3}}": RED}).next_to(a2, RIGHT*35)
        tex2 = MTex(r"\angle {C}<90^{\circ }", tex_to_color_map={"{C}": DARK_BROWN}).next_to(a4, DOWN)

        self.play(FadeTransformPieces(a, a4), FadeTransformPieces(tex1, tex2))
        self.wait(2)

class chapter_06(Scene):
    def construct(self):
        t = ValueTracker(0)
        n = ValueTracker(1)

        tri = Polygon(np.array([1.5, 0, 0]), np.array([-1.5, 0, 0]), np.array([-0.5, 1, 0]))

        s1 = Polygon(np.array([-1.5, 0, 0]), np.array([-0.5, 1, 0]), np.array([-1.5, 2, 0]), np.array([-2.5, 1, 0]), color=TEAL, fill_opacity=0.6)
        s2 = Polygon(np.array([1.5, 0, 0]), np.array([-0.5, 1, 0]), np.array([0.5, 3, 0]), np.array([2.5, 2, 0]), color=BLUE, fill_opacity=0.6)
        s3 = Polygon(np.array([1*1.5, 0, 0]), np.array([-1*1.5, 0, 0]), np.array([-1*1.5, -2*1.5, 0]), np.array([1*1.5, -2*1.5, 0]), color=RED, fill_opacity=0.6)
        
        d_l = DashedLine(np.array([-0.5, 1, 0]), np.array([-0.5, -3, 0]))

        tri1 = Polygon(np.array([-1.5, 0, 0]), np.array([-2.5, 1, 0]), np.array([1.5, 0, 0]), color=YELLOW, fill_opacity=0.4)
        tri2 = Polygon(np.array([-1.5, 0, 0]), np.array([-0.5, 1, 0]), np.array([-1.5, -3, 0]), color=YELLOW, fill_opacity=0.4)

        tri3 = Polygon(np.array([-1.5, 0, 0]), np.array([-2.5, 1, 0]), np.array([-0.5, 1, 0]), color=ORANGE, fill_opacity=0.4)
        tri4 = Polygon(np.array([-1.5, 0, 0]), np.array([-0.5, 0, 0]), np.array([-1.5, -3, 0]), color=YELLOW, fill_opacity=0.4)

        group = VGroup(tri, s1, s2, s3, d_l, tri2, tri4)
        background1 = BackgroundRectangle(group, BLACK, opacity=0.8)
        tex1 = MTex("<").shift(LEFT*0.5 + UP*0.5)

        tri5 = Polygon(np.array([-1.5, 2, 0]), np.array([-2.5, 1, 0]), np.array([-0.5, 1, 0]), color=ORANGE, fill_opacity=0.4)
        tri6 = Polygon(np.array([-0.5, -3, 0]), np.array([-0.5, 0, 0]), np.array([-1.5, -3, 0]), color=YELLOW, fill_opacity=0.4)

        s4 = Polygon(np.array([-1.5, 0, 0]), np.array([-0.5, 1, 0]), np.array([-1.5, 2, 0]), np.array([-2.5, 1, 0]), color=ORANGE, fill_opacity=0.4)
        s5 = Polygon(np.array([-1.5, 0, 0]), np.array([-0.5, 0, 0]), np.array([-0.5, -3, 0]), np.array([-1.5, -3, 0]), color=YELLOW, fill_opacity=0.4)
        tex2 = MTex("<").rotate(-90*DEGREES).shift(LEFT*5)

        s6 = Polygon(np.array([1.5, 0, 0]), np.array([-0.5, 1, 0]), np.array([0.5, 3, 0]), np.array([2.5, 2, 0]), color=ORANGE, fill_opacity=0.4)
        s7 = Polygon(np.array([1.5, 0, 0]), np.array([-0.5, 0, 0]), np.array([-0.5, -3, 0]), np.array([1.5, -3, 0]), color=YELLOW, fill_opacity=0.4)
        tex3 = MTex("<").rotate(-90*DEGREES).shift(RIGHT*5)

        self.play(ShowCreation(tri))
        self.play(LaggedStart(FadeIn(s1), FadeIn(s2), FadeIn(s3)))
        self.play(ShowCreation(d_l))
        self.play(ShowCreation(tri1))
        self.play(ReplacementTransform(tri1.copy(), tri2))
        self.wait(0.25)
        self.play(ReplacementTransform(tri2, tri4))
        self.play(FadeIn(tri3))
        self.play(LaggedStart(FadeIn(background1), tri1.animate.rotate(45*DEGREES, about_point=np.array([-1.5, 0, 0])).shift(RIGHT*3), tri3.animate.rotate(45*DEGREES, about_point=np.array([-1.5, 0, 0]))))
        self.wait(0.5)
        self.play(Write(tex1))
        self.wait(0.5)
        self.play(LaggedStart(FadeOut(background1), FadeOut(tex1), FadeOut(tri1), tri3.animate.rotate(-45*DEGREES, about_point=np.array([-1.5, 0, 0]))))
        self.play(LaggedStart(ReplacementTransform(tri3.copy(), tri5), ReplacementTransform(tri4.copy(), tri6)))
        self.play(LaggedStart(FadeOut(VGroup(tri3, tri5)), FadeIn(s4), FadeOut(VGroup(tri4, tri6)), FadeIn(s5)))
        self.play(LaggedStart(s4.animate.shift(LEFT*3.5+UP*0.5), s5.animate.shift(LEFT*4+DOWN*0.5), Write(tex2)))
        self.wait(0.5)
        self.play(LaggedStart(FadeIn(s6), FadeIn(s7)))
        self.play(LaggedStart(s6.animate.shift(RIGHT*3.5+UP*0.5), s7.animate.shift(RIGHT*4+DOWN*0.5), Write(tex3)))

        def tri_anim(obj):
            obj.become(Polygon(np.array([1.5, 0, 0]), np.array([-1.5, 0, 0]), np.array([-0.5+t.get_value(), n.get_value(), 0])))
        
        def l_anim(obj):
            obj.become(DashedLine(np.array([-0.5+t.get_value(), n.get_value(), 0]), np.array([-0.5+t.get_value(), -3, 0])))

        def s2_anim(obj):
            pos3, pos4 = get_all_pos([1.5, 0, 0], [-0.5+t.get_value(), n.get_value(), 0])
            obj.become(Polygon(np.array([1.5, 0, 0]), np.array([-0.5+t.get_value(), n.get_value(), 0]), pos4, pos3, color=BLUE, fill_opacity=0.6))

        def s4_anim(obj):
            pos3, pos4 = get_all_pos([-1.5-3.5, 0+0.5, 0], [-0.5+t.get_value()-3.5, n.get_value()+0.5, 0])
            obj.become(Polygon(np.array([-1.5-3.5, 0+0.5, 0]), np.array([-0.5+t.get_value()-3.5, n.get_value()+0.5, 0]), pos4, pos3, color=ORANGE, fill_opacity=0.4))
        
        def s5_anim(obj):
            obj.become(Polygon(np.array([-1.5-4, 0-0.5, 0]), np.array([-0.5+t.get_value()-4, 0-0.5, 0]), np.array([-0.5+t.get_value()-4, -3-0.5, 0]), np.array([-1.5-4, -3-0.5, 0]), color=YELLOW, fill_opacity=0.4))
        
        def s1_anim(obj):
            pos3, pos4 = get_all_pos([-1.5, 0, 0], [-0.5+t.get_value(), n.get_value(), 0])
            obj.become(Polygon(np.array([-1.5, 0, 0]), np.array([-0.5+t.get_value(), n.get_value(), 0]), pos4, pos3, color=TEAL, fill_opacity=0.6))
        
        def s6_anim(obj):
            pos3, pos4 = get_all_pos([1.5+3.5, 0+0.5, 0], [-0.5+t.get_value()+3.5, n.get_value()+0.5, 0])
            obj.become(Polygon(np.array([1.5+3.5, 0+0.5, 0]), np.array([-0.5+t.get_value()+3.5, n.get_value()+0.5, 0]), pos4, pos3, color=ORANGE, fill_opacity=0.4))
        
        def s7_anim(obj):
            obj.become(Polygon(np.array([1.5+4, 0-0.5, 0]),  np.array([-0.5+t.get_value()+4, 0-0.5, 0]), np.array([-0.5+t.get_value()+4, -3-0.5, 0]), np.array([1.5+4, -3-0.5, 0]), color=YELLOW, fill_opacity=0.4))
        
        def tex2_anim(obj):
            if n.get_value() < 1.145:
                obj.become(MTex("<").rotate(-90*DEGREES).shift(LEFT*5))
            else:
                obj.become(MTex("<").rotate(90*DEGREES).shift(LEFT*5))
        
        def tex3_anim(obj):
            if n.get_value() < 1.145:
                obj.become(MTex("<").rotate(-90*DEGREES).shift(RIGHT*5))
            else:
                obj.become(MTex("<").rotate(90*DEGREES).shift(RIGHT*5))

        tri.add_updater(tri_anim)
        d_l.add_updater(l_anim)
        s2.add_updater(s2_anim)
        s4.add_updater(s4_anim)
        s5.add_updater(s5_anim)
        s1.add_updater(s1_anim)
        s6.add_updater(s6_anim)
        s7.add_updater(s7_anim)
        tex2.add_updater(tex2_anim)
        tex3.add_updater(tex3_anim)

        self.add(tri, s2, s4, s3, d_l, s1, s6, s7, s5, tex2, tex3)
        self.play(t.animate.set_value(1.499999), run_time=3, rate_func=there_and_back)
        self.play(t.animate.set_value(-0.499999), run_time=2, rate_func=there_and_back)
        self.play(n.animate.set_value(3.8), run_time=5, rate_func=there_and_back)

        g = VGroup(tri, s2, s4, s3, d_l, s1, s6, s7, s5, tex2, tex3)
        background2 = BackgroundRectangle(g, BLACK, opacity=0.8)
        tex4 = Text("a²+b²=c²⇔∠C=90° \n\na²+b²>c²⇔∠C<90° \n\na²+b²<c²⇔∠C>90°", font="LXGW WenKai", t2c={"a": TEAL_D, "b": BLUE_D, "c": LIGHT_BROWN, "C": DARK_BROWN})

        self.play(LaggedStart(FadeIn(background2), *[FadeIn(i, shift=random.choice(pos)*3) for i in tex4]))
        self.wait(2)

        
        c_g = VGroup()
        for x in np.arange(1, 14, 0.1):
            cir = Circle(radius=x, stroke_color=BLACK, fill_color=BLACK, fill_opacity=1)
            c_g.add(cir)

        self.play(LaggedStart(*[ShowCreation(i) for i in c_g]))

        text = TexText("@E{r}{s}net", tex_to_color_map={"{r}": "#0088FF", "{s}": "#B46F00"}, font_size=100)
        
        self.play(FadeIn(text), run_time=2)
        self.wait(2)
        



        
        




        
        


