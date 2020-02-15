# coding:UTF-8
from manimlib.imports import *


class Intro(Scene):

    def construct(self):
        # 开头
        # 标题
        title = TextMobject("Minecraft粒子动画教程")
        title.scale(2)
        # 作者 带颜色
        author = TextMobject(
            "Author: Zoyn",
            tex_to_color_map={"Zoyn": BLUE}
        )
        author.scale(1.5)
        
        tools = TextMobject(
            "本教程使用Bukkit代码(Java)讲解",
            tex_to_color_map={"Bukkit":RED, "(Java)":RED}
        )
        tools2 = TextMobject(
            "本动画使用manim库制作",
            tex_to_color_map={"manim":RED}
        )
        tools.to_edge(DOWN)
        tools2.next_to(tools, DOWN)
        
        toolsGroup = VGroup(tools, tools2)
        toolsGroup.scale(0.7)
        
        # 做组
        group = VGroup(title, author)
        group.arrange(DOWN)
        self.play(
            Write(title),
            # 从上往下出现
            FadeInFrom(author, UP),
            ShowCreation(toolsGroup, run_time=2),
        )
        self.wait(3)
        
        # 清除所有内容
        self.clear()
        image = ImageMobject("sticker\高傲.jpg")
        image.move_to(UP * 3)
        image.scale(0.7)
        drama = Subtitle("讲道理，说实话，有一说一，平心而论", size=0.4)
        drama.move_to(UP * 2)
        drama2 = Subtitle(
            "这个视频的动画效果我写了很多天, 给个3连应该不过分吧",
            t2c={"3连":RED},
            size=0.4
        )
        drama2.next_to(drama, DOWN)
        self.add(drama, drama2, image)
        self.wait(5)
        
        drama3 = Subtitle(
            "我好像听到有人在说下次一定? 哇别啊,我莫某人跪在地上ball ball你们了!",
            t2c={"ball ball":GREEN},
            size=0.4
        )
        drama4 = Subtitle(
            "养家糊口, 不过分, 勤工俭学, 是不是",
            t2c={"不过分":YELLOW, "是不是":YELLOW},
            size=0.4
        )
        drama3.next_to(drama2, DOWN)
        drama4.next_to(drama3, DOWN)
        image = ImageMobject("sticker\哭狗.jpg")
        image.next_to(drama4, LEFT * 2 + DOWN / 20)
        image.scale(0.6)
        self.play(
            FadeInFrom(drama3, UP),
            FadeInFrom(drama4, UP),
            FadeInFrom(image, RIGHT),
        )
        self.wait(5)
        
        drama5 = Subtitle(
            "行了, *话说太多没有意思, 建议立即开始视频",
            t2c={"立即开始":ORANGE},
            size=0.4
        )
        drama5.next_to(drama4, DOWN)
        self.play(ShowCreation(drama5))
        image = ImageMobject("sticker\白嫖.jpg")
        image.next_to(drama5, DOWN)
        self.play(
            FadeInFrom(image, UP),
        )
        self.wait(3)
        
        self.clear()
        base = Subtitle("在X, Z轴上的画圆操作", size=0.6)
        content = Subtitle(
            "在教程开始之前, 先来学一个简单的数学知识吧~",
            t2c={"简单":GREEN},
            size=0.5
        )
        content.next_to(base, DOWN)
        self.play(
            Write(base, run_time=2),
            FadeInFrom(content, UP, run_time=2),
        )
         
        self.wait(3)

        
class Graph(GraphScene):             
    CONFIG = {
        "x_min":-5,
        "x_max": 5,
        "y_min":-5,
        "y_max": 5,
        "x_axis_width": 6.5,
        "y_axis_height": 6.5,
        "graph_origin": ORIGIN,
        "axes_color" : BLUE,
        "x_labeled_nums": range(-5, 6, 2)
    }

    def construct(self):
        self.setup_axes(animate=True)
            
        changeToMinecraftAxes = Subtitle("""
                                在MC当中，玩家在二维平面的移动影响的是X轴和Z轴
                                为了方便起见, 此处我们把Y轴更改为MC里的Z轴
            """,
            t2c={"二维平面":RED, "X轴": BLUE, "Y轴": BLUE, "Z轴": BLUE}
        )
        changeToMinecraftAxes.to_edge(DOWN)
        self.play(Write(changeToMinecraftAxes))
        self.wait(2)
          
        # # 更改y轴的名字为z轴 (模仿mc坐标系)
        z_label = TextMobject("$z$")
        # 移动至y轴label的位置
        z_label.move_to(self.y_axis_label_mob)
        # 变化
        self.play(Transform(self.y_axis_label_mob, z_label))
        self.y_axis.add(z_label)
        self.y_axis_label_mob = z_label
        self.wait()
          
        drawUnitCircleText = Subtitle("""
                                首先我们在这个坐标系上画一个单位圆
            """,
            t2c={"单位圆":RED, }
        )
        drawUnitCircleText.to_edge(DOWN)
        self.play(Transform(changeToMinecraftAxes, drawUnitCircleText))
          
        circle = Circle()
        circle.set_fill(RED, opacity=0.5)
        circle.set_width(1.3)
        circle.set_height(1.3)
        self.play(ShowCreation(circle))
        self.wait(2)
          
        drawLineText = Subtitle("""
                                然后我们选择一个角为30°的角画一条线
            """,
            t2c={"角为30°":RED, }
        )
        drawLineText.to_edge(DOWN)
        self.remove(changeToMinecraftAxes)
        self.play(Transform(drawUnitCircleText, drawLineText))
        self.wait(2)
          
        angle30Line = Line(start=ORIGIN, end=np.array((0.65, 0, 0)))
        angle30Line.set_color(YELLOW)
        angle30Line.rotate_about_origin(PI / 6)
         
        dot = Dot(np.array((0.6, 0.3, 0)))
        dot.set_height(0.15)
        dot.set_width(0.15)
        self.play(ShowCreation(angle30Line), ShowCreation(dot))
        self.wait(2)
          
        drawVerticalLineText = Subtitle("""
                                若我们以单位圆和黄线的交点P, 向下作垂线, 得到绿线
            """,
            t2c={"交点":RED, "绿线":GREEN}
        )
        drawVerticalLineText.to_edge(DOWN)
        self.remove(drawUnitCircleText)
        self.play(Transform(drawLineText, drawVerticalLineText))
        self.wait(2)
          
        angle90Line = Line(start=ORIGIN, end=np.array((0, 0.3, 0)))
        angle90Line.set_color(GREEN)
        angle90Line.move_to(np.array([0.6, 0.15, 0]))
        self.play(ShowCreation(angle90Line))
        self.wait(2)
         
        dotPointText = TexMobject("P(cos(\\frac{\pi}{6}), sin(\\frac{\pi}{6}))")
        dotPointText.next_to(dot, UP + RIGHT)
        dotPointText.scale(0.7)
        self.play(ShowCreation(dotPointText))
        self.wait()
         
        dotLocationText = Subtitle(
            "根据sin函数和cos函数的几何定义, 我们不难知道其坐标应该为P(cos(PI/6), sin(PI/6))，那么我们可以得到一个模型...",
            t2c={"sin函数和cos函数":GREEN, "P(cos(PI/6), sin(PI/6))":RED, }
        )
        dotLocationText.to_edge(DOWN)
        dotLocationText.scale(0.7)
        self.remove(drawLineText)
        self.play(
            Transform(drawVerticalLineText, dotLocationText),
        )
        self.wait(6)
         
        self.clear()
        
        dotLocationFormula = TexMobject(
            "sin(t) = ",  # 0
            "\\frac{z}{",  # 1
            "r",  # 2
            "},",  # 3
            "cos(t) = ",  # 4
            "\\frac{x}{",  # 5
            "r",  # 6
            "}"  # 7
        )
        formulaDesc = TextMobject(
            "(其中t为角的度数, r为斜边, 也就是单位圆的半径)",
            tex_to_color_map={"角的度数": BLUE, "r为斜边":BLUE, "半径":BLUE}
        )
        formulaDesc.next_to(dotLocationFormula, DOWN)
        self.play(
            Write(dotLocationFormula),
            ShowCreation(formulaDesc)
        )
        self.wait(3)
        
        formulaDesc2 = Subtitle(
            "因为单位圆的半径为1, 所以r等于1",
            t2c={"半径为1":GREEN}
        )
        formulaDesc2.to_edge(DOWN)
        self.play(
            Write(formulaDesc2),
        )
        self.wait(2)
        
        dotLocationFormula2 = TexMobject(
            "sin(t) = ",  # 0
            "\\frac{z}{",  # 1
            "1",  # 2
            "},",  # 3
            "cos(t) = ",  # 4
            "\\frac{x}{",  # 5
            "1",  # 6
            "}"  # 7
        )
        self.play(
            Transform(dotLocationFormula, dotLocationFormula2),
        )
        self.wait(2)
        
        formulaDesc3 = Subtitle("进而可以得到")
        formulaDesc3.to_edge(DOWN)
        dotLocationFormula3 = TexMobject(
            "sin(t) = z , cos(t) = x",
        )
        
        self.remove(dotLocationFormula)
        self.remove(formulaDesc)
        self.remove(formulaDesc2)
        self.play(
            Transform(dotLocationFormula2, dotLocationFormula3),
            Transform(formulaDesc2, formulaDesc3),
            FadeOut(formulaDesc)
        )
        self.wait(3)


class BukkitCodeIntro(Scene):

    def construct(self):
        resultLastPhase = Subtitle("那么在有了刚才的模型, 我们就可以总结出,", size=0.5,)
        resultLastPhase2 = Subtitle(
            "P点的横纵坐标都可以用函数cos和sin求出",
            t2c={"横纵坐标":BLUE, "cos":RED, "sin":RED},
            size=0.5,
        )
        resultLastPhase2.next_to(resultLastPhase, DOWN)
        resultGroup = VGroup(resultLastPhase, resultLastPhase2)
        resultGroup.move_to(ORIGIN + UP * 2)
        self.play(Write(resultGroup))
        self.wait(4)
        
        describe = Subtitle("刚才我们只用30°来举例, 而在实际代码当中我们可以用", size=0.5,)
        describe2 = Subtitle(
            "for循环将所有的角度都给进行遍历, 来获得对应的P点",
            t2c={"for循环":GREEN, "对应的P点":RED},
            size=0.5,
        )
        describe2.next_to(describe, DOWN)
        describeGroup = VGroup(describe, describe2)
        describeGroup.next_to(resultGroup, DOWN * 8)
        self.play(FadeInFrom(describeGroup, UP))
        self.wait(6)
        
        self.clear()
        tip = Subtitle("温馨提示", size=0.55,)
        tip.to_edge(UP)
        content = Subtitle(
            "以下内容你可能需要Java基础的相关知识",
            t2c={"可能": RED, "Java基础":BLUE}
        )
        content.next_to(tip, DOWN)
        self.play(
            Write(tip),
            ShowCreation(content)
        )
        self.wait(2)
        content2 = Subtitle(
            "不然的话可能就会......",
            t2c={"可能": ORANGE}
        )
        content2.next_to(content, DOWN)
        self.play(
            ShowCreation(content2)
        )
        self.wait(3)
        
        content3 = Subtitle("上图!", size=0.4,)
        content3.next_to(content2, DOWN * 3)
        image = ImageMobject("sticker\上图.jpg")
        image.scale(2)
        image.next_to(content3, DOWN)
        
        self.play(
            ShowCreation(content3),
            FadeInFrom(image, DOWN)
        )
        
        self.wait(3)
#         


class BukkitCode(Scene):

    def construct(self):
        changePhase = Subtitle("那么....接下来我们就可以去写代码了", size=0.5)
        self.play(Write(changePhase))
        self.wait(2)
        self.clear()
          
        title = TextMobject("首先我们来写段代码")
        title.to_edge(UP)
        self.play(ShowCreation(title))
        
        code = '''
        Location location = player.getLocation();
        for (int degree = 0; degree < 360; degree++) {
             
        }
        '''
        codeText = CodeText(code)
        frameBox = SurroundingRectangle(codeText, buff=SMALL_BUFF)
        frameBox.set_color(GRAY)
        self.play(ShowCreation(frameBox))
        self.play(Write(codeText))
        self.wait(2)
           
        subtitle = Subtitle(
            "在Bukkit当中, 我们可以通过getLocation()方法来获得\n        玩家脚底下的坐标, 我们用来当做我们的原点O",
            t2c={"Bukkit":ORANGE , "getLocation()方法":GREEN, "脚底下":RED}
        )
        subtitle.to_edge(DOWN)
        self.play(ShowCreation(subtitle))
        self.wait(3)
           
        subtitle2 = Subtitle(
            "在上方的代码, 我写了一个for循环,用于遍历0-360°的所有度数",
            t2c={"for循环":BLUE , "0-360°":GREEN}
        )
        subtitle2.to_edge(DOWN)
        self.play(
            Transform(subtitle, subtitle2)
        )
        self.wait(3)
           
        title2 = TextMobject("- Coding -")
        title2.to_edge(UP)
        self.clear()
        self.add(subtitle2)
        self.play(Transform(title, title2))
           
        code = '''
        Location location = player.getLocation();
        for (int degree = 0; degree < 360; degree++) {
            double radians = Math.toRadians(degree);
            double x = Math.cos(radians);
            double z = Math.sin(radians);
        }
        '''
        codeText = CodeText(code)
        frameBox = SurroundingRectangle(codeText, buff=SMALL_BUFF)
        frameBox.set_color(GRAY)
        self.play(ShowCreation(frameBox))
        self.play(Write(codeText))
        self.wait(2)
           
        subtitle3 = Subtitle(
            "我们将其扩展, 首先要将角度制转换至弧度制才可以使用\n                        Math类下的cos和sin方法",
            t2c={"角度制转换至弧度制":BLUE , "Math":RED}
        )
        subtitle3.to_edge(DOWN)
        self.play(
            Transform(subtitle2, subtitle3)
        )
        self.wait(5)
           
        subtitle4 = Subtitle(
            "这样我们便得到了X和Z的坐标",
            t2c={"X":GREEN , "Z":GREEN}
        )
        subtitle4.to_edge(DOWN)
        self.remove(subtitle2)
        self.play(
            Transform(subtitle3, subtitle4)
        )
        self.wait(4)
         
        self.clear()
        self.add(title2)
         
        code = '''
        Location location = player.getLocation();
        for (int degree = 0; degree < 360; degree++) {
            double radians = Math.toRadians(degree);
            double x = Math.cos(radians);
            double z = Math.sin(radians);
            
            location.add(x, 0D, z);
            // particle code 你生成粒子的代码
            location.subtract(x, 0D, z);
        }
        '''
        codeText = CodeText(code)
        frameBox = SurroundingRectangle(codeText, buff=SMALL_BUFF)
        frameBox.set_color(GRAY)
        self.play(ShowCreation(frameBox))
         
        desc = TextMobject(
            "particle code是指播放粒子的代码, \\\\你可以使用类库或者Bukkit方法:\\\\location.getWorld().spawnParticle(Particle.FLAME, location, 0)",
            tex_to_color_map={"播放粒子": RED, "类库": GREEN, "Bukkit": GREEN}
        )
        desc.move_to(UP * 2.3)
        desc.scale(0.5)
        self.play(Write(codeText), Write(desc))
        self.wait(4)
         
        subtitle5 = Subtitle(
            "我们添加了三行代码, 首先第一行, 我们是对原点O的location进行了\n                            一个增加的操作也就是P(0+x, 0+z)",
            t2c={"第一行":GREEN , "原点O的location":BLUE, "P(0+x, 0+z)":RED}
        )
        subtitle5.to_edge(DOWN)
        self.play(
            ShowCreation(subtitle5, run_time=3)
        )
        self.wait(5)
          
        subtitle6 = Subtitle(
            "那么经过了add操作的location, 我们便可以在这个新的location播放粒子",
            t2c={"add操作":GREEN , "新的location":BLUE}
        )
        subtitle6.to_edge(DOWN)
        self.remove(subtitle4)
        self.play(
            Transform(subtitle5, subtitle6, run_time=2)
        )
        self.wait(5)
          
        subtitle7 = Subtitle(
            "最后, 为了保证location的点还是原来的原点O\n                我们就需要对它进行减的操作",
            t2c={"location": RED, "原来的原点O": ORANGE, "减":BLUE}
        )
        subtitle7.to_edge(DOWN)
        self.remove(subtitle5)
        self.play(
            Transform(subtitle6, subtitle7, run_time=2)
        )
        self.wait(7)
        
        self.clear()
        image = ImageMobject("sticker\生病.jpg")
        image.to_edge(UP)
        self.add(image)
        subtitle8 = Subtitle(
            "什么?? 你们还没听懂?!"
        )
        subtitle8.next_to(image, DOWN)
        self.add(subtitle8)
        self.wait(2)
         
        subtitle9 = Subtitle(
            "我的天啊! 这么浅显易懂的东西都...",
            t2c={"浅显易懂": BLUE}
        )
        subtitle9.next_to(subtitle8, DOWN)
        self.play(FadeInFrom(subtitle9, UP))
        self.wait(2)
         
        subtitle10 = Subtitle(
            "算了, 没事我还有动画嘻嘻嘻嘻嘻嘻",
            t2c={"还有": ORANGE}
        )
        subtitle10.next_to(subtitle9, DOWN)
        image = ImageMobject("sticker\嘻嘻.jpg")
        image.next_to(subtitle10, DOWN)
        self.play(
            FadeInFrom(subtitle10, UP),
            FadeInFrom(image, UP)
        )
        self.wait(4)


class Minecraft(ThreeDScene):
    CONFIG = {
        "x_min":-5,
        "x_max": 5,
        "y_min":-5,
        "y_max": 5,
        "z_min":-5,
        "z_max": 5,
    }

    def construct(self):
        # 建立3D坐标系
        axes = ThreeDAxes()
        intro = Subtitle("现在我们就直接进入到MC坐标系内", size=0.5)
        
        zeroDot = Dot()
        zeroDot.scale(1.5)
        zeroDot.set_color(ORANGE)
        self.play(
            Write(intro)
        )
        self.wait(2)
        intro2 = Subtitle("MC坐标系 - 3D视图", size=0.5)
        intro2.to_corner(UL)
        self.play(
            Transform(intro, intro2),
            ShowCreation(axes),
            FadeIn(zeroDot)
        )
        # 移动摄像机朝向
        self.move_camera(phi=55 * DEGREES, theta=45 * DEGREES, run_time=4)
        
        self.wait()
        
        intro3 = Subtitle("MC坐标系 - 3D视图", size=0.5)
        self.add_fixed_in_frame_mobjects(intro3)
        intro3.to_corner(UL)
        
        self.remove(intro)
        self.play(
            FadeOut(intro2),
            FadeIn(intro3)
        )
        
        xLabel = TexMobject(
            "x",
            tex_to_color_map={"x": GREEN}
        ).scale(1.5)
        xLabel.move_to(RIGHT * 5.8)
        xLabel.rotate(-45 * DEGREES + PI, OUT)
        yLabel = TexMobject(
            "z",
            tex_to_color_map={"z": GREEN}
        ).scale(1.5)
        yLabel.move_to(UP * 5.8)
        yLabel.rotate(-45 * DEGREES + PI, OUT)
        zLabel = TexMobject(
            "y",
            tex_to_color_map={"y": GREEN}
        ).scale(1.5)
        zLabel.move_to(OUT * 3.8)
        zLabel.rotate(PI, OUT)
        zLabel.rotate(-PI / 2, RIGHT)
        self.play(
            FadeIn(xLabel),
            FadeIn(yLabel),
            FadeIn(zLabel)
        )
        self.wait()
        
        subtitle = Subtitle(
            "在我们之前的代码中我们用for循环遍历了0-360°\n    让我们在动画中看看这个循环都发生了什么",
            t2c={"之前的":RED, "循环遍历": BLUE, "这个循环": GREEN}
        )
        subtitle.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(subtitle)
        self.play(Write(subtitle))
        self.wait(3)
        self.play(FadeOut(subtitle))
        
        # 角度计数
        degree = Subtitle(
            "角度:",
            t2c={"角度:":GREEN},
            size=0.5,
        )
        degreeNum = DecimalNumber(0, num_decimal_places=0)
        # 字放置在左边
        degree.next_to(degreeNum, LEFT)
        # 用于计数角度ValueTracker
        time = ValueTracker(0)

        def numUpdater(num):
            center = num.get_center()
            num.set_value(time.get_value())
            num.move_to(ORIGIN)
            num.rotate(PI / 2, axis=RIGHT)
            num.rotate(PI / 2, axis=OUT)
            num.move_to(center)
 
        degreeNum.add_updater(numUpdater)
#         degreeNum.add_updater(lambda num:num.set_value(time.get_value()))
        angleGroup = VGroup(degree, degreeNum)
        angleGroup.move_to(UP * 2 + OUT / 2)
        angleGroup.rotate(PI / 2, axis=RIGHT)
        angleGroup.rotate(PI / 2, axis=OUT)
        # # 调试点
        testDot = Dot(np.array((1, 0, 0)))
        # 记得加上这行代码, 使其以帧视角来显示
        self.add(degreeNum)
        self.play(Write(degree))
        self.play(
            Rotate(testDot, PI / 6, run_time=3, about_point=ORIGIN),
            ApplyMethod(time.increment_value, 30.0, rate_func=smooth, run_time=3)
        )
        
        tip = TexMobject(
            "cos(\\frac{\pi}{6}) = \\frac{\sqrt{3}}{2}\\\\sin(\\frac{\pi}{6}) = \\frac{1}{2}"
        ).scale(0.8)
        tip.to_corner(UR)
        self.add_fixed_in_frame_mobjects(tip)
        self.play(Write(tip))
        self.wait()
        
        subtitle2 = Subtitle("1) location.add(x, 0D, z)")
        subtitle2.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(ShowCreation(subtitle2))
        self.wait(2)
        
        # 箭头
        arrow = Arrow(start=ORIGIN, end=np.array((np.cos(PI / 6), np.sin(PI / 6), 0)))
        self.play(
            GrowArrow(arrow),
            ApplyMethod(zeroDot.move_to, np.array((np.cos(PI / 6), np.sin(PI / 6), 0)))
        )
        self.wait()
        
        subtitle3 = Subtitle("2) 生成粒子")
        subtitle3.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(
            FadeOut(subtitle2, run_time=0.8),
            FadeIn(subtitle3, run_time=0.8)
        )
        self.wait()
        
        # 生成粒子
        angle30Dot = Dot(np.array((np.cos(PI / 6), np.sin(PI / 6), 0)))
        angle30Dot.set_color(RED)
        self.play(
            FadeIn(angle30Dot),
            FadeOut(arrow)
        )
        
        subtitle4 = Subtitle("3) location.subtract(x, 0D, z)")
        subtitle4.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(subtitle4)
        self.play(
            FadeOut(subtitle3, run_time=0.8),
            FadeIn(subtitle4, run_time=0.8)
        )
        self.wait()
        
        # 箭头
        arrow = Arrow(start=np.array((np.cos(PI / 6), np.sin(PI / 6), 0)), end=ORIGIN)
        self.play(
            GrowArrow(arrow),
            ApplyMethod(zeroDot.move_to, ORIGIN)
        )
        self.wait(2)
        
        self.play(
            FadeOut(arrow),
            FadeOut(tip),
            FadeOut(subtitle4, run_time=0.8),
            Rotate(testDot, PI / 6, run_time=3, about_point=ORIGIN),
            ApplyMethod(time.increment_value, 30.0, rate_func=smooth, run_time=3)
        )
        ####### 下面是60°时候的情况
        tip = TexMobject(
            "cos(\\frac{\pi}{3}) = \\frac{1}{2}\\\\sin(\\frac{\pi}{3}) = \\frac{\sqrt{3}}{2}"
        ).scale(0.8)
        tip.to_corner(UR)
        self.add_fixed_in_frame_mobjects(tip)
        self.play(Write(tip))
        self.wait()
        
        subtitle5 = Subtitle("1) location.add(x, 0D, z)")
        subtitle5.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(subtitle5)
        self.play(ShowCreation(subtitle5))
        self.wait(2)
        
        # 箭头
        arrow = Arrow(start=ORIGIN, end=np.array((np.cos(PI / 3), np.sin(PI / 3), 0)))
        self.play(
            GrowArrow(arrow),
            ApplyMethod(zeroDot.move_to, np.array((np.cos(PI / 3), np.sin(PI / 3), 0)))
        )
        self.wait()
        
        subtitle6 = Subtitle("2) 生成粒子")
        subtitle6.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(subtitle6)
        self.play(
            FadeOut(subtitle5, run_time=0.8),
            FadeIn(subtitle6, run_time=0.8)
        )
        self.wait()
        
        # 生成粒子
        angle60Dot = Dot(np.array((np.cos(PI / 3), np.sin(PI / 3), 0)))
        angle60Dot.set_color(RED)
        self.play(
            FadeIn(angle60Dot),
            FadeOut(arrow)
        )
        
        subtitle7 = Subtitle("3) location.subtract(x, 0D, z)")
        subtitle7.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(subtitle7)
        self.play(
            FadeOut(subtitle6, run_time=0.8),
            FadeIn(subtitle7, run_time=0.8)
        )
        self.wait()
        
        # 箭头
        arrow = Arrow(start=np.array((np.cos(PI / 3), np.sin(PI / 3), 0)), end=ORIGIN)
        self.play(
            GrowArrow(arrow),
            ApplyMethod(zeroDot.move_to, ORIGIN)
        )
        self.wait(2)
        
        subtitle8 = Subtitle("之后的角省略...")
        subtitle8.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(subtitle8)
        self.play(
            FadeOut(subtitle7, run_time=0.8),
            FadeIn(subtitle8, run_time=0.8)
        )
        self.wait(3)
        self.play(
            FadeOut(arrow),
            FadeOut(angle30Dot),
            FadeOut(angle60Dot),
            FadeOut(testDot),
            FadeOut(tip),
            FadeOut(degree),
            FadeOut(degreeNum),
            FadeOut(subtitle8)
        )
        self.wait(2)
        
        circle = Circle()
        self.play(ShowCreation(circle, run_time=2))
        self.wait(2)

class FormulaTransformation(Scene):

    def construct(self):
        intro = Subtitle(
            "                  在刚才的动画演示当中,\n我们已经知道了如何在MC中绘制一个单位圆",
            t2c={"动画演示":GREEN, "单位圆": RED},
            size=0.45
        )
        question = Subtitle(
            "可是问题是, 如果我们想扩大圆的半径应该怎么做呢?",
            t2c={"扩大圆的半径":BLUE},
            size=0.45
        )
        intro.move_to(ORIGIN + UP * 2)
        question.next_to(intro, DOWN * 2)
        self.play(
            Write(intro, run_time=2)
        )
        self.wait()
        
        self.play(
            FadeInFrom(question, UP, run_time=2)
        )
        self.wait()
        
        answer = Subtitle(
            "让我们来看看一组公式的变换",
            t2c={"公式":ORANGE},
            size=0.45
        )
        answer.next_to(question, DOWN * 2)
        self.play(
            FadeInFrom(answer, UP, run_time=2)
        )
        
        self.wait(2)
        
        self.clear()
        formula = TexMobject(
            "sin(t) = ",  # 0
            "\\frac{z}{",  # 1
            "r",  # 2
            "},",  # 3
            "cos(t) = ",  # 4
            "\\frac{x}{",  # 5
            "r",  # 6
            "}"  # 7
        )
        self.play(
            Write(formula),
        )
        self.wait(2)
        
        subtitle = Subtitle(
            "在之前的内容中, 我已经阐述了这组公式的由来, 现在让我们对它进行一个变换",
            t2c={"之前的":RED, "这组公式":GREEN, "变换":ORANGE}
        )
        subtitle.to_edge(DOWN)
        self.play(ShowCreation(subtitle, run_time=2))
        self.wait(2)
        self.play(FadeOut(subtitle))
        
        frameBox = SurroundingRectangle(formula[2])
        frameBox.set_stroke(GREEN, 5)
        
        frameBox2 = SurroundingRectangle(formula[6])
        frameBox2.set_stroke(GREEN, 5)
        self.play(
            ShowCreation(frameBox),
            ShowCreation(frameBox2)
        )
        self.wait(2)
        self.play(
            FadeOut(frameBox),
            FadeOut(frameBox2)
        )
         
        changedformula = TexMobject(
            "rsin(t) = z, rcos(t) = x",  # 0
        )
         
        self.play(
            Transform(formula, changedformula), run_time=2
        )
        
        subtitle = Subtitle(
            "在上方的公式中, 我们r的数值就是圆的半径, 那么反映到代码上应该是这样的",
            t2c={"r的数值":BLUE, "代码上":ORANGE, }
        )
        subtitle.to_edge(DOWN)
        self.play(ShowCreation(subtitle, run_time=2))
        self.wait()
        
        code = '''
        double radius = 设置的半径;
        Location location = player.getLocation();
        for (int degree = 0; degree < 360; degree++) {
            double radians = Math.toRadians(degree);
            double x = radius * Math.cos(radians);
            double z = radius * Math.sin(radians);
            
            location.add(x, 0D, z);
            // particle code
            location.subtract(x, 0D, z);
        }
        '''
        codeText = CodeText(code)
        frameBox = SurroundingRectangle(codeText, buff=SMALL_BUFF)
        frameBox.set_color(GRAY)
        self.play(
            FadeOut(formula, run_time=0.8),
            FadeOut(changedformula, run_time=0.8),
            ShowCreation(frameBox)
        )
         
        self.play(Write(codeText))
        self.wait(5)

        
class LastScene(Scene):

    def construct(self):
        epilogue = Subtitle(
            "              那么这就是本期视频的主要内容了\n如果你觉得这个视频很赞的话不妨给一个素质三连",
            t2c={"主要内容":BLUE, "视频":GREEN, "素质三连":ORANGE},
            size=0.4
        )
        epilogue.move_to(ORIGIN + UP * 1.5)
        
        image = ImageMobject("sticker\憨憨汤姆.jpg")
        image.move_to(UP * 3)
        image.scale(0.7)
        
        self.add(image)
        self.add(epilogue)
        self.wait(2)
        
        image = ImageMobject("sticker\三连.png")
        image.next_to(epilogue, DOWN)
        image.scale(0.4)
        self.play(FadeInFrom(image, DOWN))
        self.wait()
        desc = Subtitle("如果你还想有下一期的话不妨在评论区告诉我你们的感受\n                        (有没有下一期就看你们了)",
            t2c={"评论区":PINK, "下一期":GREEN, "看你们了":ORANGE},
        )
        desc.to_edge(DOWN)
        self.play(ShowCreation(desc, run_time=2))
        self.wait(3)
        
        self.clear()
        subtitle = Subtitle("动画或粒子代码我已放在简介内了嗷")
        self.play(FadeIn(subtitle))
        self.wait(3)
        self.play(FadeOut(subtitle))
        

class CodeText(Text):
    # Courier New:
    CONFIG = {
        "font": "宋体",
        "size": 0.35,
        "stroke_width": 0,
    }


class Subtitle(Text):
#     SourceHanSansCN-Regular
    CONFIG = {
        "font": "SourceHanSerifCN-Bold",
        "size": 0.35,
        "stroke_width": 0,
    }
