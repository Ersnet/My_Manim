'''
本视频使用了 @一碗星空咕 的MyTrianglePro类
详细源码请见他的gitee主页:
https://gitee.com/a-starry-sky/manim-video-source-code/blob/master/nine_point.py
'''


from manimlib import *
import numpy as np


def ArcLen(angle, radius):
    arclength = (angle*PI*radius)/180
    return arclength



class Introduce1(Scene):
    def construct(self):
        text1 = TexText("三角函数的产生和发展与天文学有密切联系")
        self.play(FadeIn(text1))
        self.wait(1)
        
        text2 = TexText(r"2世纪时希腊天文学家\\托勒密系统地编制出一张弦表\\将它收录在他所著的《天文学大成》一书中")
        self.play(Write(text2), FadeOut(text1, shift=DOWN))
        self.wait(1)

        text3 = TexText(r"""
                        他把半径为60的圆中\\
                        度数是$\theta $的弧所对的弦长制成了表\\
                        其中$\theta $从$\left (  \frac{1}{2} \right ) ^{\circ}$到$180^{\circ}$每隔$\left (  \frac{1}{2} \right ) ^{\circ}$依次取值
                        """)
        self.play(Write(text3), FadeOut(text2, shift=DOWN))

        cir = Circle(radius=2, arc_center=DOWN)
        dot_O = Dot(DOWN)
        tri = MyTrianglePro(np.array([1.5,0.31,0]), np.array([1.5,-2.31,0]), np.array([0,-1,0]))
        h = tri.get_heights()
        text_group = VGroup(
                    Tex("r").shift(np.array([0.5,-0.3,0])),
                    Tex("l").shift(np.array([1.7,-1,0])),
                    Tex(r"\theta").shift(np.array([0.8,-0.8,0])),
                    Tex("l", "=", "2r", r"\sin", "{", r"\theta", "\over", "2", "}").to_edge(RIGHT).shift(DOWN),
                    Tex(r"\sin \frac{\theta }{2} = \frac{l}{2r} ").to_edge(RIGHT).shift(DOWN*2.5)
        )
        arc = Arc(angle=81*DEGREES, start_angle=-41*DEGREES, arc_center=DOWN, radius=0.5).set_color(GREEN)
        self.play(ShowCreation(cir), ShowCreation(dot_O), text3.animate.move_to(np.array([0,2.5,0])),run_time=1.5)
        self.play(ShowCreation(tri))
        self.play(ShowCreation(h[2]))
        self.play(Write(text_group[0:3]), ShowCreation(arc))
        self.play(
            TransformMatchingShapes(text_group[0].copy(), text_group[3][2]),
            TransformMatchingShapes(text_group[1].copy(), text_group[3][0]),
            TransformMatchingShapes(text_group[2].copy(), text_group[3][4]),
            *[Write(text_group[3][i]) for i in range(0,7) if i !=0 and i !=2 and i !=4  ]
        )
        self.play(TransformMatchingShapes(text_group[3].copy(), text_group[4]))
        self.wait(1)
        
        all_objects = VGroup(text3, tri, arc, text_group, h[2], cir, dot_O,)
        self.play(FadeOut(all_objects))

class Introduce2(Scene):
    def construct(self):
        text1 = TexText(r"古希腊文化传播到古印度后\\公元5世纪末的数学家阿耶波多提出\\用弧对应的弦长的一半来对应半弧的正弦").to_edge(UP)
        self.play(Write(text1))
        self.wait(1)

        obj = VGroup(
                Circle(radius=2, arc_center=DOWN),
                Dot(DOWN),
                MyTrianglePro(np.array([1.51,0.31,0]), np.array([1.51,-1,0]), np.array([0,-1,0])),
                Arc(angle=41*DEGREES, start_angle=0*DEGREES, arc_center=DOWN, radius=0.5).set_color(GREEN),
                Elbow().shift(np.array([1.51,-1,0])).rotate(angle=PI/2, about_point=np.array([1.51,-1,0])).set_color(YELLOW)
        )
        text_group = VGroup(
                    Tex("r").shift(np.array([0.5,-0.3,0])),
                    Tex(r"\frac{l}{2} ", font_size=36).shift(np.array([1.7,-0.5,0])),
                    Tex(r"\theta").shift(np.array([0.7,-0.7,0])),
                    Tex(r"\frac{l}{2} = r \sin\theta  ").to_edge(RIGHT).shift(DOWN),
                    Tex(r"\sin\theta   = \frac{l}{2r} ").to_edge(RIGHT).shift(DOWN*2.5)
        )
        self.play(FadeIn(obj), FadeIn(text_group))
        self.wait(1)
        self.play(FadeOut(obj), FadeOut(text_group), FadeOut(text1))
        
        text2 = TexText(r"这个做法被后来的古印度数学家使用\\基本和现代的正弦定义一致了")
        self.play(Write(text2))
        self.wait(1)

        text3 = TexText(r"随着人们对数学研究的不断深入\\余弦，正切等三角函数都被引入到数的计算中")
        self.play(FadeOut(text2, shift=DOWN), Write(text3))
        self.wait(1)

        text4 = TexText(r"那么接下来让我们看看这些\\三角函数的图像和其相关定理吧")
        note = TexText(" *这里仅介绍正弦，余弦，正切这三类三角函数QAQ ", font_size=24).next_to(text4, DOWN*0.5).set_color(GREY_C)
        self.play(FadeOut(text3, shift=DOWN), Write(text4))
        self.play(FadeIn(note, shift=UP))
        self.wait(1)
        self.play(FadeOut(text4), FadeOut(note))
        
class tan(Scene):
    def construct(self):
        t = ValueTracker(0)
        t1 = ValueTracker(0)
        frame = self.camera.frame

        axe = Axes(height=2,width=2,x_range=(0, 2),y_range=(0, 2)).shift(np.array([-4,1,0]))
        cir = Circle(radius=2).shift(axe.c2p(0,0))
        tanLine = TangentLine(cir,alpha=0,length=20)
        e = Elbow().shift(axe.c2p(2,0)).rotate(angle=PI/2,axis=OUT,about_point=axe.c2p(2,0)).set_color(YELLOW)
        
        line = axe.get_graph(function=lambda x : 0,color=TEAL_B,x_range=(-5,2)).add_updater(lambda obj:obj.become(axe.get_graph(function=lambda x : t.get_value()*x,color=TEAL_B,x_range=(-5,2))))
        dot_p = Dot(axe.c2p(2,0)).add_updater(lambda obj:obj.move_to(axe.c2p(2,t.get_value()*2))).set_color(TEAL_B)
        dot_q = Dot().add_updater(lambda obj:obj.move_to(axe.c2p(np.arctan(t.get_value()*2)+4,t.get_value()*2))).set_color(GREEN_B)                  # 偷了个懒，直接反函数求了
        dot_q2 = Dot().add_updater(lambda obj:obj.move_to(axe.c2p(np.arctan(t.get_value()*2)+4+PI,t.get_value()*2))).set_color(MAROON_B)
        dot_q3 = Dot().add_updater(lambda obj:obj.move_to(axe.c2p(np.arctan(t.get_value()*2)+4+PI*2,t.get_value()*2))).set_color(GOLD_B)
        path = TracedPath(dot_q.get_center,stroke_color=GREEN_B,stroke_width=2)
        path2 = TracedPath(dot_q2.get_center,stroke_color=MAROON_B,stroke_width=2)
        path3 = TracedPath(dot_q3.get_center,stroke_color=GOLD_B,stroke_width=2)
        dline = DashedLine().add_updater(lambda obj:obj.become(DashedLine(start=axe.c2p(2,t.get_value()*2),end=axe.c2p(np.arctan(t.get_value()*2)+4,t.get_value()*2))))
        dline2 = DashedLine().add_updater(lambda obj:obj.become(DashedLine(start=axe.c2p(np.arctan(t.get_value()*2)+4,t.get_value()*2),end=axe.c2p(np.arctan(t.get_value()*2)+4+PI,t.get_value()*2))))
        dline3 = DashedLine().add_updater(lambda obj:obj.become(DashedLine(start=axe.c2p(np.arctan(t.get_value()*2)+4+PI,t.get_value()*2),end=axe.c2p(np.arctan(t.get_value()*2)+4+PI*2,t.get_value()*2))))
        frame.add_updater(lambda obj:obj.move_to(np.array([np.arctan(t.get_value()*2),t.get_value()*2,0])).set_width(14))
        
        g = VGroup(dline,dline2,dline3)
        self.play(ShowCreation(axe))
        self.play(ShowCreation(cir))
        self.play(ShowCreation(line),ShowCreation(tanLine))
        self.play(ShowCreation(e),ShowCreation(g))
        self.play(ShowCreation(dot_p),ShowCreation(dot_q),ShowCreation(dot_q2),ShowCreation(dot_q3))
    
        self.add(line,dline,path,frame,dline2,path2,path3,dline3,dot_p,dot_q,dot_q2,dot_q3)
        self.play(t.set_value,5,run_time=7,rate_func=there_and_back)

        line.clear_updaters()
        dot_p.clear_updaters()
        dot_q.clear_updaters()
        dot_q2.clear_updaters()
        dot_q3.clear_updaters()
        dline.clear_updaters()    # 不清除容易出bug
        dline2.clear_updaters()
        dline3.clear_updaters()
        frame.clear_updaters()
        line.add_updater(lambda obj:obj.become(axe.get_graph(function=lambda x : t1.get_value()*x,color=TEAL_B,x_range=(-5,2))))
        dot_p.add_updater(lambda obj:obj.move_to(axe.c2p(2,t1.get_value()*2)))
        dot_q.add_updater(lambda obj:obj.move_to(axe.c2p(np.arctan(t1.get_value()*2)+4,t1.get_value()*2))).set_color(GREEN_B)    # 偷个懒，直接反正切函数（
        dot_q2.add_updater(lambda obj:obj.move_to(axe.c2p(np.arctan(t1.get_value()*2)+4+PI,t1.get_value()*2))).set_color(MAROON_B)
        dot_q3.add_updater(lambda obj:obj.move_to(axe.c2p(np.arctan(t1.get_value()*2)+4+PI*2,t1.get_value()*2))).set_color(GOLD_B)
        frame.add_updater(lambda obj:obj.move_to(np.array([np.arctan(t1.get_value()*2),t1.get_value()*2,0])).set_width(14))
        dline.add_updater(lambda obj:obj.become(DashedLine(start=axe.c2p(2,t1.get_value()*2),end=axe.c2p(np.arctan(t1.get_value()*2)+4,t1.get_value()*2))))
        dline2.add_updater(lambda obj:obj.become(DashedLine(start=axe.c2p(np.arctan(t1.get_value()*2)+4,t1.get_value()*2),end=axe.c2p(np.arctan(t1.get_value()*2)+4+PI,t1.get_value()*2))))
        dline3.add_updater(lambda obj:obj.become(DashedLine(start=axe.c2p(np.arctan(t1.get_value()*2)+4+PI,t1.get_value()*2),end=axe.c2p(np.arctan(t1.get_value()*2)+4+PI*2,t1.get_value()*2))))
        
        self.add(line,frame,dline,dline2,dline3,dot_p,dot_q,dot_q3,dot_q2)
        self.play(t1.set_value,-5,run_time=7,rate_func=there_and_back)
        self.wait(1)
        frame.clear_updaters()
        line.clear_updaters()
        dot_p.clear_updaters()
        dot_q.clear_updaters()
        dot_q2.clear_updaters()
        dot_q3.clear_updaters()
        dline.clear_updaters()    
        dline2.clear_updaters()
        dline3.clear_updaters()
        group = VGroup(cir,e,path,path2,path3,dot_p,dot_q,dot_q2,dot_q3,dline,axe,dline2,dline3,tanLine,line)
        self.play(FadeOut(group))

class sin(Scene):
    def construct(self):
        t = ValueTracker(0)

        axe = Axes(height=4,width=4,x_range=(-2, 2),y_range=(-2, 2)).shift(np.array([-4,0,0]))
        cir = Circle(radius=2).shift(axe.c2p(0,0))
        dot_P = Dot(axe.c2p(2,0)).set_color(YELLOW).add_updater(lambda obj:obj.move_to(axe.c2p(2*np.cos(t.get_value()),2*np.sin(t.get_value()))))
        line_OP = Line(axe.c2p(0,0,),axe.c2p(2,0)).add_updater(lambda obj:obj.put_start_and_end_on(axe.c2p(0,0),axe.c2p(2*np.cos(t.get_value()),2*np.sin(t.get_value()))))
        vline = Line(axe.c2p(2,0),axe.c2p(2,0)).add_updater(lambda obj:obj.put_start_and_end_on(axe.c2p(2*np.cos(t.get_value()),0),axe.c2p(2*np.cos(t.get_value()),2*np.sin(t.get_value()))))
        arc = Arc(arc_center=axe.c2p(0,0),radius=0.5,angle=1*DEGREES,stroke_color=YELLOW).add_updater(lambda obj:obj.become(Arc(arc_center=axe.c2p(0,0),radius=0.5,angle=t.get_value()%TAU,stroke_color=YELLOW)))
        dot_Q = Dot(axe.c2p(2,0)).add_updater(lambda obj:obj.move_to(axe.c2p(ArcLen(t.get_value(),2)*20+2,2*np.sin(t.get_value())))).set_color(TEAL_B)   # 这里把弧长放大了
        path = TracedPath(dot_Q.get_center,stroke_color=TEAL_B,stroke_width=2)
        line_PQ = DashedLine(axe.c2p(2,0)).add_updater(lambda obj:obj.become(DashedLine(axe.c2p(2*np.cos(t.get_value()),2*np.sin(t.get_value())),axe.c2p(ArcLen(t.get_value(),2)*20+2,2*np.sin(t.get_value())))))
        
        self.play(ShowCreation(cir),ShowCreation(axe),ShowCreation(arc))
        self.play(ShowCreation(line_OP),ShowCreation(vline),ShowCreation(line_PQ))
        self.play(FadeIn(dot_P),FadeIn(dot_Q))
        self.add(line_OP,dot_P,vline,arc,line_PQ,dot_Q,path)
        self.play(t.set_value, TAU*2, run_time=6, rate_func=linear)
        self.wait(1)
        group = VGroup(line_OP,dot_P,vline,arc,line_PQ,dot_Q,path,axe,cir)
        self.play(FadeOut(group))

class cos(Scene):
    def construct(self):
        t = ValueTracker(0)

        axe = Axes(height=4,width=4,x_range=(-2, 2),y_range=(-2, 2)).shift(np.array([-4,0,0]))
        cir = Circle(radius=2).shift(axe.c2p(0,0))
        dot_P = Dot(axe.c2p(2,0)).set_color(YELLOW).add_updater(lambda obj:obj.move_to(axe.c2p(2*np.cos(t.get_value()),2*np.sin(t.get_value()))))
        line_OP = DashedLine(axe.c2p(0,0,),axe.c2p(2,0)).add_updater(lambda obj:obj.become(DashedLine(axe.c2p(0,0),axe.c2p(2*np.cos(t.get_value()),2*np.sin(t.get_value())),color=YELLOW))).set_color(YELLOW)
        vline = DashedLine(axe.c2p(2,0)).add_updater(lambda obj:obj.become(DashedLine(start=axe.c2p(2*np.cos(t.get_value()),0),end=axe.c2p(2*np.cos(t.get_value()),2*np.sin(t.get_value())),color=YELLOW))).set_color(YELLOW)
        slash = axe.get_graph(function=lambda x : x,color=GREEN_B,x_range=(-5,5))
        dot_M = Dot(axe.c2p(2,2)).add_updater(lambda obj:obj.move_to(axe.c2p(2*np.cos(t.get_value()),2*np.cos(t.get_value())))).set_color(GREEN_B)
        vlineM = Line(axe.c2p(2,2),axe.c2p(2,0)).add_updater(lambda obj:obj.put_start_and_end_on(axe.c2p(2*np.cos(t.get_value()),0),axe.c2p(2*np.cos(t.get_value()),2*np.cos(t.get_value())))).set_color(GREEN_B)
        dot_Q = Dot(axe.c2p(2,2)).add_updater(lambda obj:obj.move_to(axe.c2p(ArcLen(t.get_value(),2)*20+2,2*np.cos(t.get_value())))).set_color(TEAL_C)
        path = TracedPath(dot_Q.get_center,stroke_color=TEAL_C,stroke_width=2)
        line_MQ = DashedLine(axe.c2p(2,2)).add_updater(lambda obj:obj.become(DashedLine(axe.c2p(2*np.cos(t.get_value()),2*np.cos(t.get_value())),axe.c2p(ArcLen(t.get_value(),2)*20+2,2*np.cos(t.get_value())))))
        arc = Arc(arc_center=axe.c2p(0,0),radius=0.5,angle=1*DEGREES,stroke_color=YELLOW).add_updater(lambda obj:obj.become(Arc(arc_center=axe.c2p(0,0),radius=0.5,angle=t.get_value()%TAU,stroke_color=YELLOW)))

        self.play(ShowCreation(cir),ShowCreation(axe),ShowCreation(arc))
        self.play(ShowCreation(line_OP),ShowCreation(slash),ShowCreation(vline),ShowCreation(vlineM),ShowCreation(line_MQ))
        self.play(FadeIn(dot_P),FadeIn(dot_M),FadeIn(dot_Q))
        self.add(line_OP,vline,vlineM,line_MQ,dot_P,dot_M,dot_Q,path,arc)
        self.play(t.set_value, TAU*2, run_time=7, rate_func=linear)
        self.wait(1)
        group = VGroup(line_OP,vline,vlineM,line_MQ,dot_P,dot_M,dot_Q,path,arc,axe,cir,slash)
        self.play(FadeOut(group))

class sinTh(Scene):
    def construct(self):
        tex_color = {"{h}": YELLOW, "{a}": GREEN_C, "{b}": MAROON_A, "{h'}": YELLOW, "{c}": GOLD_A}

        tri = MyTrianglePro(np.array([-2,-1,0]),np.array([2,-1,0]),np.array([1,2,0]), color=BLUE, fill_opacity=0.5)
        dot_A = Tex("A").next_to(np.array([-2,-1,0]), DL*0.5)
        dot_B = Tex("B").next_to(np.array([2,-1,0]), DR*0.5)
        dot_C = Tex("C").next_to(np.array([1,2,0]), UP*0.5)
        group = VGroup(dot_A, dot_B, dot_C)
        self.play(ShowCreation(tri))
        self.play(Write(group))
        
        h = tri.get_heights()
        elbow = Elbow().shift(np.array([1,-1,0])).set_color(YELLOW)
        text_abc = VGroup(
                    Tex("h").next_to(h[2], LEFT).set_color(YELLOW),
                    Tex("a").shift(np.array([1.9,0.7,0])).set_color(GREEN_C), 
                    Tex("b").shift(np.array([-0.9,0.7,0])).set_color(MAROON_A), 
                    Tex("c").shift(np.array([0,-1.4,0])).set_color(GOLD_A)
        )
        self.play(ShowCreation(h[2]))
        self.play(FadeIn(elbow), FadeIn(text_abc[0]))
        self.play(*[ClockwiseTransform(group[i].copy(), text_abc[i+1]) for i in range(0,3)],run_time=2)
        
        text_theorem = VGroup(
                        Tex(r"\sin A = ", "{", "{h}", r" \over ", "{b}", "}").set_color_by_tex_to_color_map(tex_color).shift(np.array([-2,-3,0])),
                        Tex(r"\sin B = ", "{", "{h}", r" \over ", "{a}", "}").set_color_by_tex_to_color_map(tex_color).shift(np.array([2,-3,0]))
        )
        self.play(
            TransformFromCopy(text_abc[0], text_theorem[0][1]), 
            TransformFromCopy(text_abc[2], text_theorem[0][3]),
            *[Write(text_theorem[0][i]) for i in range(0,4) if i !=1 and i !=3  ],
            TransformFromCopy(text_abc[0], text_theorem[1][1]), 
            TransformFromCopy(text_abc[1], text_theorem[1][3]),
            *[Write(text_theorem[1][i]) for i in range(0,4) if i !=1 and i !=3  ])
        self.wait(0.5)
        text_theorem_transform1 = VGroup(
                                Tex("{h}", r" = \sin A \cdot  ", "{b}").set_color_by_tex_to_color_map(tex_color).shift(np.array([-2,-3,0])),
                                Tex("{h}", r" = \sin B \cdot ", "{a}").set_color_by_tex_to_color_map(tex_color).shift(np.array([2,-3,0]))
        )
        self.play(FadeTransformPieces(text_theorem[0], text_theorem_transform1[0]), FadeTransformPieces(text_theorem[1], text_theorem_transform1[1]))
        self.wait(0.5)
        
        text_theorem_transform2 = Tex(r"\sin A \cdot  ", "{b}", "=", "\sin B \cdot  ", "{a}").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0]))
        self.play(
            FadeOut(text_theorem_transform1[0][0]), 
            FadeOut(text_theorem_transform1[1][0]),
            FadeTransformPieces(text_theorem_transform1[0][1:], text_theorem_transform2[0:2]),
            FadeTransformPieces(text_theorem_transform1[1][1:], text_theorem_transform2[3:]),
            Write(text_theorem_transform2[2]))
        self.wait(0.5)
        
        text_theorem_transform3 = Tex("{", "{b}", r" \over \sin B}", "=", "{", "{a}", r" \over \sin A}").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0]))
        self.play(
                *[FadeOut(text_theorem_transform2[i]) for i in range(0,5) if i !=2 and i !=4  ],
                ReplacementTransform(text_theorem_transform2[2], text_theorem_transform3[0]),
                ReplacementTransform(text_theorem_transform2[4], text_theorem_transform3[3]),
                *[Write(text_theorem_transform3[i]) for i in range(0,5) if i !=0 and i !=3  ]
        )
        self.play(text_theorem_transform3.animate.shift(UP*5.5+LEFT*5),run_time=1.5)
        self.wait(0.5)
        
        h2 = Tex(" h' ").next_to(h[2], LEFT).set_color(YELLOW)
        elbow2 = Elbow().shift(tri.get_drop_feet()[0]).set_color(YELLOW).rotate(108*DEGREES, about_point=tri.get_drop_feet()[0])
        self.play(FadeOut(h[2]), FadeIn(h[0]), ClockwiseTransform(elbow, elbow2), ReplacementTransform(text_abc[0], h2))
        text_theorem2 = VGroup(
                        Tex(r"\sin C = ", "{", "{h'}", r" \over ", "{b}", "}").set_color_by_tex_to_color_map(tex_color).shift(np.array([-2,-3,0])),
                        Tex(r"\sin B = ", "{", "{h'}", r" \over ", "{c}", "}").set_color_by_tex_to_color_map(tex_color).shift(np.array([2,-3,0])))
        self.play(
            TransformFromCopy(h2, text_theorem2[0][1]), 
            TransformFromCopy(text_abc[2], text_theorem2[0][3]),
            *[Write(text_theorem2[0][i]) for i in range(0,4) if i !=1 and i !=3  ],
            TransformFromCopy(h2, text_theorem2[1][1]), 
            TransformFromCopy(text_abc[3], text_theorem2[1][3]),
            *[Write(text_theorem2[1][i]) for i in range(0,4) if i !=1 and i !=3  ])
        
        self.wait(0.5)
        text_theorem_transform4 = Tex("{", "{b}", r" \over \sin B}", "=", "{", "{c}", r" \over \sin C}").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0]))
        self.play(
            *[FadeOut(text_theorem2[0][i]) for i in range(0,4) if i !=0 and i !=3  ],
            *[FadeOut(text_theorem2[1][i]) for i in range(0,4) if i !=0 and i !=3  ],
            ReplacementTransform(text_theorem2[0][0], text_theorem_transform4[4]),
            ReplacementTransform(text_theorem2[1][0], text_theorem_transform4[1]),
            ReplacementTransform(text_theorem2[0][3], text_theorem_transform4[0]),
            ReplacementTransform(text_theorem2[1][3], text_theorem_transform4[3]),
            Write(text_theorem_transform4[2])
            )
        self.wait(0.5)
        
        self.play(ShowCreationThenDestructionAround(text_theorem_transform4[0:2]),ShowCreationThenDestructionAround(text_theorem_transform3[0:2]))
        text_theorem_transform5= Tex("=", "{", "{a}", r" \over \sin A}").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0])).next_to(text_theorem_transform4[4], RIGHT*0.5)
        text_theorem_transform5.shift(UP*0.25)
        self.play(FadeOut(text_theorem_transform3[0:3]), ReplacementTransform(text_theorem_transform3[3:5], text_theorem_transform5))
        
        circle = tri.get_circumcircle()
        tri_transform = MyTrianglePro(np.array([-2,-1,0]),np.array([2,-1,0]),np.array([2,1,0]), color=BLUE, fill_opacity=0.5)
        dot_c = Tex(" C' ").next_to(np.array([2,1,0]), UR*0.5)
        elbow3 = Elbow().shift(np.array([2,-1,0])).rotate(angle=PI/2, about_point=np.array([2,-1,0])).set_color(RED)
        text_theorem3 = Tex(r"\sin C = \sin C' = ", "{", "{c}", r" \over 2r}").shift(np.array([4.5,0.3,0])).set_color_by_tex_to_color_map(tex_color)
        self.play(ShowCreation(circle))
        self.play(TransformFromCopy(tri, tri_transform), TransformFromCopy(dot_C, dot_c))
        self.add(h2, elbow2, h[0])
        self.play(FadeIn(elbow3))
        self.play(Write(text_theorem3))
        self.wait(0.5)
        
        text_theorem4 = TexText("正弦定理：").next_to(text_theorem_transform4[1], LEFT*0.5)
        text_theorem4.shift(UP*0.25)
        text_theorem5 = Tex("=2r").next_to(text_theorem_transform5, RIGHT*0.5)
        self.play(Write(text_theorem4), FadeOut(text_theorem3[0]), ReplacementTransform(text_theorem3[1:], text_theorem5))
        self.wait(2)

class cosTh(Scene):
    def construct(self):
        tex_color = {"{h}": YELLOW, "{a}": GREEN_C, "{b}": MAROON_A, "{h'}": YELLOW, "{c}": GOLD_A}

        tri = MyTrianglePro(np.array([-2,-1,0]),np.array([2,-1,0]),np.array([1,2,0]), color=BLUE, fill_opacity=0.5)
        dot_A = Tex("A").next_to(np.array([-2,-1,0]), DL*0.5)
        dot_B = Tex("B").next_to(np.array([2,-1,0]), DR*0.5)
        dot_C = Tex("C").next_to(np.array([1,2,0]), UP*0.5)
        group = VGroup(dot_A, dot_B, dot_C)
        self.play(ShowCreation(tri))
        self.play(Write(group))

        h = tri.get_heights()
        elbow = Elbow().shift(np.array([1,-1,0])).set_color(YELLOW)
        text_abc = VGroup(
                    Tex("h").next_to(h[2], LEFT).set_color(YELLOW),
                    Tex("a").shift(np.array([1.9,0.7,0])).set_color(GREEN_C), 
                    Tex("b").shift(np.array([-0.9,0.7,0])).set_color(MAROON_A), 
                    Tex("c").shift(np.array([0,-1.4,0])).set_color(GOLD_A)
        )
        self.play(ShowCreation(h[2]))
        self.play(ShowCreation(elbow), FadeIn(text_abc[0]))
        self.play(*[ReplacementTransform(group[i].copy(), text_abc[i+1]) for i in range(0,3)],run_time=2)

        t = ValueTracker(1)
        tri.add_updater(lambda obj: obj.become(MyTrianglePro(np.array([-2,-1,0]),np.array([2,-1,0]),np.array([t.get_value(),2,0]), color=BLUE, fill_opacity=0.5)))
        h[2].add_updater(lambda obj: obj.become(tri.get_heights()[2]))
        elbow.add_updater(lambda obj: obj.become(Elbow().shift(np.array([t.get_value(),-1,0])).set_color(YELLOW)))
        text_abc[0].add_updater(lambda obj: obj.next_to(h[2],LEFT))
        text_abc[1].add_updater(lambda obj: obj.move_to(np.array([t.get_value()+0.9,0.7,0])))
        text_abc[2].add_updater(lambda obj: obj.move_to(np.array([t.get_value()-1.9,0.7,0])))
        dot_C.add_updater(lambda obj: obj.next_to(np.array([t.get_value(),2,0]), UP*0.5))
        line1 = Line(stroke_width=7).set_color(MAROON_C).add_updater(lambda obj: obj.put_start_and_end_on(np.array([2,-1,0]),np.array([t.get_value(),-1,0])))
        line2 = Line(stroke_width=7).set_color(RED_D).add_updater(lambda obj: obj.put_start_and_end_on(np.array([-2,-1,0]),np.array([t.get_value(),-1,0])))
        brace1 = BraceLabel(line1,"x", UP).add_updater(lambda obj: obj.become(BraceLabel(line1,"x", UP).set_color(MAROON_C))).set_color(MAROON_C)
        brace2 = BraceLabel(line1,"c-x", UP).add_updater(lambda obj: obj.become(BraceLabel(line2,"c-x", UP).set_color(RED_D))).set_color(RED_D)
        
        self.play(ShowCreation(line1), ShowCreation(line2))
        self.play(ShowCreation(brace1), ShowCreation(brace2))
        self.add(text_abc[1], text_abc[2], tri, h[2], elbow, text_abc[0], dot_C, line1, line2, brace1, brace2)
        self.play(t.set_value, -2, run_time=4, rate_func=there_and_back)

        text_theorem = Tex(r"\cos B = ", r"{x \over ", "{a}").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0]))
        self.play(Write(text_theorem[:2]), ReplacementTransform(text_abc[1].copy(), text_theorem[2]))
        self.wait(0.5)
        self.play(text_theorem.animate.shift(UP*5.5+LEFT*5),run_time=1.5)
        
        text_theorem1 = Tex(r"{h}", r" ^{2} ", "= ", "{b}", r" ^{2} -", "(", "{c}", "-", "{x}", ") ^{2} ").set_color_by_tex_to_color_map(tex_color).shift(np.array([-2,-3,0]))
        text_theorem2 = Tex(r"{h}", r" ^{2} ", "= ", "{a}", r" ^{2} - {x} ^{2}").set_color_by_tex_to_color_map(tex_color).shift(np.array([2,-3,0]))
        text_theorem3 = Tex("{b}", r" ^{2} -", "(", "{c}", "-", "{x}", ") ^{2} ", "=", "{a}", r" ^{2} - {x} ^{2}").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0]))
        text_theorem4 = Tex("{b}", r" ^{2} - ", "(", "{c}", r" ^{2} - 2", "{c}", r"x + x^{2}  ) ", "=", "{a}", r" ^{2} - {x} ^{2}").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0]))
        text_theorem5 = Tex("{b}", r" ^{2} - ", "(", "{c}", r" ^{2} - 2", "{c}", r"x ) ", "=", "{a}", r" ^{2}").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0]))
        text_theorem6 = Tex("2", "{c}", "x = ", "{a} ", r"^{2} + ", "{c}", " ^{2} - ", "{b} ", "^{2}").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0]))
        text_theorem7 = Tex("x = ", "{", "{a} ", r"^{2} + ", "{c}", " ^{2} - ", "{b} ", "^{2}", r"\over", "2", "{c}", "}" ).set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0]))
        text_theorem8 = Tex(r"\cos B = ", "{", "{a} ", r"^{2} + ", "{c}", " ^{2} - ", "{b} ", "^{2}", r"\over", "2", "{c}", "{a}",  "}" ).set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0]))
        text_theorem9 = Tex("{b}", r"^{2}", " = ", "{a} ", r"^{2} + ", "{c}", " ^{2} - ", "2", "{c}", "{a}", r"\cos B"   ).set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0]))
        text_theorem10 = Tex("{a}", r"^{2}", " = ", "{b} ", r"^{2} + ", "{c}", " ^{2} - ", "2", "{c}", "{b}", r"\cos A"   ).set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-2.5,0]))
        text_theorem11 = Tex("{c}", r"^{2}", " = ", "{a} ", r"^{2} + ", "{b}", " ^{2} - ", "2", "{b}", "{a}", r"\cos C"   ).set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3.5,0]))
        text = TexText("余弦定理：").next_to(text_theorem9, LEFT*0.5)
        self.play(
            *[Write(text_theorem1[i]) for i in range(0,10) if i !=0 and i !=3 and i !=6],
            *[Write(text_theorem2[i]) for i in range(0,5) if i !=0 and i !=3],
            ReplacementTransform(text_abc[0].copy(), text_theorem1[0]),
            ReplacementTransform(text_abc[2].copy(), text_theorem1[3]),
            ReplacementTransform(text_abc[3].copy(), text_theorem1[6]),
            ReplacementTransform(text_abc[0].copy(), text_theorem2[0]),
            ReplacementTransform(text_abc[1].copy(), text_theorem2[3])
            )
        self.wait(0.5)
        self.play(ShowCreationThenDestructionAround(text_theorem1[0:2]), ShowCreationThenDestructionAround(text_theorem2[0:2]))
        self.play(
            FadeOut(text_theorem1[0:3]), 
            FadeOut(text_theorem2[0:3]),
            FadeTransformPieces(text_theorem1[3:], text_theorem3[0:7]),
            FadeTransformPieces(text_theorem2[3:], text_theorem3[8:]),
            Write(text_theorem3[7]))
        self.wait(0.5)
        self.play(
            TransformMatchingTex(text_theorem3[0:2], text_theorem4[0:2]),
            TransformMatchingTex(text_theorem3[7:10], text_theorem4[7:10]),
            FadeOut(text_theorem3[2:7]),
            FadeIn(text_theorem4[2:7]))
        self.wait(0.5)
        self.play(Indicate(text_theorem4[6][2:4]), Indicate(text_theorem4[9][2:]))
        self.play(FadeOut(text_theorem4), FadeIn(text_theorem5))
        self.wait(0.5)
        self.play(TransformMatchingShapes(text_theorem5, text_theorem6))
        self.wait(0.5)
        self.play(TransformMatchingShapes(text_theorem6, text_theorem7))
        self.wait(0.5)
        self.play(CyclicReplace(text_theorem, text_theorem7))
        self.play(Indicate(text_theorem[1][0]), Indicate(text_theorem7))
        self.play(TransformMatchingTex(text_theorem, text_theorem8), TransformMatchingTex(text_theorem7, text_theorem8))
        self.play(TransformMatchingTex(text_theorem8, text_theorem9), Write(text), FadeIn(text_theorem10, shift=DOWN), FadeIn(text_theorem11, shift=UP))
        self.wait(2)

class tanTh(Scene):
    def construct(self):
        tex_color = {"{h}": YELLOW, "{a}": GREEN_C, "{b}": MAROON_A, "{h'}": YELLOW, "{c}": GOLD_A, r"{\alpha}": BLUE_E, r"{\beta}": TEAL_E}

        tri = MyTrianglePro(np.array([-2,-1,0]),np.array([2,-1,0]),np.array([1,2,0]), color=BLUE, fill_opacity=0.5)
        dot_A = Tex("A").next_to(np.array([-2,-1,0]), DL*0.5)
        dot_B = Tex("B").next_to(np.array([2,-1,0]), DR*0.5)
        dot_C = Tex("C").next_to(np.array([1,2,0]), UP*0.5)
        group = VGroup(dot_A, dot_B, dot_C)
        self.play(ShowCreation(tri))
        self.play(Write(group))

        h = tri.get_heights()
        elbow = Elbow().shift(np.array([1,-1,0])).set_color(YELLOW)
        text_abc = VGroup(
                    Tex("h").next_to(h[2], LEFT).set_color(YELLOW),
                    Tex("a").shift(np.array([1.9,0.7,0])).set_color(GREEN_C), 
                    Tex("b").shift(np.array([-0.9,0.7,0])).set_color(MAROON_A), 
                    Tex("c").shift(np.array([0,-1.4,0])).set_color(GOLD_A)
        )
        self.play(ShowCreation(h[2]))
        self.play(ShowCreation(elbow), FadeIn(text_abc[0]))
        self.play(*[CounterclockwiseTransform(group[i].copy(), text_abc[i+1]) for i in range(0,3)],run_time=2)

        text_theorem_group = VGroup(
                    Tex("{", "{b}", r" \over \sin B}", "=", "{", "{a}", r" \over \sin A}", "=2r").set_color_by_tex_to_color_map(tex_color).shift(np.array([1,-3,0])),
                    Tex("{b}", "= 2r", r"\sin B").set_color_by_tex_to_color_map(tex_color).shift(np.array([-2,-3,0])),
                    Tex("{a}", "= 2r"," \sin A").set_color_by_tex_to_color_map(tex_color).shift(np.array([2,-3,0])),
                    Tex("{a}", "-", "{b}", r"= 2r", r"\sin A", "-", r"2r", r"\sin B").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0])),
                    Tex("{","{a}", "-", "{b}", r"= 2r", r"\sin A", "-", r"2r", r"\sin B", "}", r"\over","{","{a}", "+", "{b}", r"= 2r", r"\sin A", "+", r"2r", r"\sin B", "}").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0])),
                    Tex("{", "{a}", "-", "{b}", r"\over", " {a}", " +", "{b}" ,"}", "=", r" { \sin A -\sin B\over \sin A + \sin B }").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0])),
                    TexText("正弦の和差化积公式：", font_size=28).to_corner(UR).shift(LEFT),
                    Tex(r"\sin ", r"{\alpha}", r" + \sin ", r"{\beta}", " = ", r"2 \sin", "{", r"{\alpha}", " + ", r"{\beta}", r" \over 2", "}", r" \cos", "{", r"{\alpha}", " -", r" {\beta}", r" \over 2", "}" ,font_size=28).set_color_by_tex_to_color_map(tex_color).to_corner(UR).shift(DOWN*0.5),
                    Tex(r"\sin ", r"{\alpha}", r" - \sin ", r"{\beta}", " = ", r"2 \cos", "{", r"{\alpha}", " + ", r"{\beta}", r" \over 2", "}", r" \sin", "{", r"{\alpha}", " -", r" {\beta}", r" \over 2", "}" ,font_size=28).set_color_by_tex_to_color_map(tex_color).to_corner(UR).shift(DOWN*1.5),
                    Tex("{", "{a}", " -", " {b}", " \over ", "{a}", " + ", "{b}", "}", r" = \frac{2\cos \frac{A+B}{2} }{2\sin \frac{A+B}{2} } \cdot \frac{\sin \frac{A-B}{2} }{\cos \frac{A-B}{2} }").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0])),
                    Tex("{", "{a}", " -", " {b}", " \over ", "{a}", " + ", "{b}", "}", r"=\frac{\tan \frac{A-B}{2} }{\tan \frac{A+B}{2} } ").set_color_by_tex_to_color_map(tex_color).shift(np.array([0,-3,0])),
        )
        text1 = TexText("由正弦定理得：").next_to(text_theorem_group[0], LEFT*0.5)
        text2 = TexText("正切定理：").next_to(text_theorem_group[10], LEFT*0.5)
        
        self.play(
            ReplacementTransform(text_abc[1].copy(), text_theorem_group[0][3]),
            ReplacementTransform(text_abc[2].copy(), text_theorem_group[0][0]),
            *[Write(text_theorem_group[0][i]) for i in range(0,6) if i !=0 and i !=3  ],
            FadeIn(text1)
            )
        self.wait(0.5)
        
        self.play(
            FadeOut(text1),
            ReplacementTransform(text_theorem_group[0][:2], text_theorem_group[1][0::2]),
            ReplacementTransform(text_theorem_group[0][3:5], text_theorem_group[2][0::2]),
            FadeOut(text_theorem_group[0][2]), FadeOut(text_theorem_group[0][5:]),
            Write(text_theorem_group[1][1]), Write(text_theorem_group[2][1])
        )
        self.wait(0.5)
        
        self.play(text_theorem_group[1].animate.shift(RIGHT*2+UP*0.5), text_theorem_group[2].animate.shift(LEFT*2+DOWN*0.5))
        self.play(text_theorem_group[1:3].animate.shift(UP*5.5+LEFT*5),run_time=1.5)
        self.wait(0.5)

        self.play(ReplacementTransform(text_theorem_group[2][0].copy(), text_theorem_group[3][0]))
        self.play(Write(text_theorem_group[3][1]))
        self.play(ReplacementTransform(text_theorem_group[1][0].copy(), text_theorem_group[3][2]))
            
        self.play(
            ReplacementTransform(text_theorem_group[1][1:].copy(), text_theorem_group[3][6:]),
            ReplacementTransform(text_theorem_group[2][1:].copy(), text_theorem_group[3][3:5]),
            Write(text_theorem_group[3][5]))
        self.wait(0.5)
        
        self.play(FadeTransformPieces(text_theorem_group[3], text_theorem_group[4][:8]), FadeIn(text_theorem_group[4][8:], shift=UP))
        self.play(TransformMatchingShapes(text_theorem_group[4], text_theorem_group[5]))
        self.play(FadeIn(text_theorem_group[6], shift=DOWN*3), FadeIn(text_theorem_group[7], shift=DOWN*2), FadeIn(text_theorem_group[8], shift=DOWN))
        
        self.wait(0.5)
        self.play(
            ShowCreationThenDestructionAround(text_theorem_group[6:9]), 
            Indicate(text_theorem_group[5][8]),
            ReplacementTransform(text_theorem_group[5][0:7], text_theorem_group[9][0:7]),
            FadeOut(text_theorem_group[5][7:]),
            FadeIn(text_theorem_group[9][7:])
        )
        self.wait(1)
        self.play(TransformMatchingShapes(text_theorem_group[9], text_theorem_group[10]), Write(text2))
        self.wait(2)
