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
        
        anupras=Text("रूपक अलंकार ",font="Nirmala UI").move_to(UP*3)
        
        heading=MarkupText(f'<b><span underline="single" fgcolor="{BLUE}">परिभाषा</span></b>',line_spacing=1,font_size=25,font="Nirmala UI").next_to(anupras,DOWN)

        defination="""जब गुण की अत्यंत समानता के कारण उपमेय को ही उपमान बता दिया जाए यानी उपमेय ओर उपमान में अभिन्नता दर्शायी जाए तब वह रूपक अलंकार कहलाता है। """
        defination=insert_newlines(defination,7)
        defination=Text(defination,line_spacing=1,font_size=25,font="Nirmala UI").next_to(heading,DOWN)

        udahran=MarkupText(f'<b><span underline="single" fgcolor="{GREEN}">उदाहरण</span></b>',line_spacing=1,font_size=25,font="Nirmala UI").next_to(defination,DOWN)
        example=MarkupText(f'गोपी पद-पंकज पावन कि रज जामे सिर भीजे।',line_spacing=1,font_size=25,font="Nirmala UI").next_to(udahran,DOWN*2)
        
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
        