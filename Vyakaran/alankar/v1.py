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

class AlankarDefination(Scene):
    def construct(self):
        anupras=Text("अलंकार ",font="Nirmala UI").move_to(UP*3)
        
        heading=MarkupText(f'<b><span underline="single" fgcolor="{BLUE}">परिभाषा</span></b>',line_spacing=1,font_size=25,font="Nirmala UI").next_to(anupras,DOWN)

        defination="""अलंकर का शाब्दिक अर्थ होता है "आभूषण।" इसका मतलब है कि अलंकार के माध्यम से कविता या भाषा को रमणीय और अद्वितीय बनाने का प्रयास किया जाता है। अलंकार का उपयोग कविता,प्रोस,और भाषा में भावनाओं और विचारों को अधिक प्रभावशाली बनाने के लिए किया जाता है।"""
        defination=insert_newlines(defination,7)
        defination=Text(defination,line_spacing=1,font_size=25,font="Nirmala UI").next_to(heading,DOWN*2)

    
        self.play(Write(anupras),run_time=1)
        self.wait(3)
        self.play(Write(heading),run_time=1)
        self.wait(3)
        self.play(Write(defination),run_time=3)
        self.wait(3)
