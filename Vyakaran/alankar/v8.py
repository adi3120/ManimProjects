from manim import *

def insert_newlines(text, n):
    words = text.split()
    lines = []
    line = []
    for word in words:
        line.append(word)
        if len(line) == n:
            lines.append(' '.join(line))
            line = []
    if line:
        lines.append(' '.join(line))
    return '\n'.join(lines)

class Upma(Scene):
    def construct(self):
        
        anupras=Text("उपमा अलंकार",font="Nirmala UI").move_to(UP*3)
        
        heading=MarkupText(f'<b><span underline="single" fgcolor="{BLUE}">परिभाषा</span></b>',line_spacing=1,font_size=25,font="Nirmala UI").next_to(anupras,DOWN)

        defination="""उपमा का सामान्य अर्थ है – समानता या मिलता-जुलता रूप दिखाना। \nजब किन्ही दो वस्तुओं के गुण, आकृति, स्वभाव आदि में समानता दिखाई जाए या दो भिन्न वस्तुओं कि तुलना कि जाए, तब वहां उपमा अलंकर होता है। """
        defination=insert_newlines(defination,7)
        defination=Text(defination,line_spacing=1,font_size=25,font="Nirmala UI").next_to(heading,DOWN)

        udahran=MarkupText(f'<b><span underline="single" fgcolor="{GREEN}">उदाहरण</span></b>',line_spacing=1,font_size=25,font="Nirmala UI").next_to(defination,DOWN)
        example=MarkupText(f'हरि पद कोमल कमल।',line_spacing=1,font_size=25,font="Nirmala UI").next_to(udahran,DOWN*2)
        
        self.play(Write(anupras),run_time=1)
        self.wait(3)
        self.play(Write(heading),run_time=1)
        self.wait(3)
        self.play(Write(defination),run_time=3)
        self.wait(3)
        self.play(Write(udahran),run_time=1)
        self.wait(3)
        self.play(Write(example),run_time=3)
        self.wait(3)
        