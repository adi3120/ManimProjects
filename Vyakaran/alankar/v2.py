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

class AlankarTypes(Scene):
    def construct(self):
        
        text=Text("अलंकार", font="Nirmala UI").move_to(UP*3)
        
        leaf_nodes=VGroup(
        	Text("शब्दालंकार", font="Nirmala UI",font_size=30),
        	Text("अर्थालंकार", font="Nirmala UI",font_size=30)
		)
        leaf_nodes.set_x(0).arrange(buff=2.5)
        leaf_nodes.next_to(text, DOWN, buff=1)
        
		# Create lines pointing from central node to leaf nodes
        lines1 = VGroup()
        for leaf_node in leaf_nodes:
            line = Line(text.get_bottom(), leaf_node.get_top(), color=YELLOW)
            lines1.add(line)
        
		
        deftype1="""शब्दालंकार वह अलंकार है जिसमें 'शब्दों' का प्रयोग विशेष रूप से किया जाता है ताकि कविता या भाषा में रमणीयता और छायाचित्रण बढ़ा दिया जा सके।"""
        deftype1=insert_newlines(deftype1,5)
        deftype1=Text(deftype1,font="Nirmala UI",line_spacing=1,font_size=20)
        leaves1=VGroup(
               deftype1,
		)
        leaves1.set_x(0).arrange(buff=0.5)
        leaves1.next_to(leaf_nodes[0], DOWN, buff=1)

        # Create lines pointing from central node to leaf nodes
        lines2 = VGroup()
        for leaf_node in leaves1:
            line = Line(leaf_nodes[0].get_bottom(), leaf_node.get_top(), color=YELLOW)
            lines2.add(line)
        
        
        deftype2="""अर्थालंकार वह अलंकार है जिसमें भाषा के 'अर्थों' को विशेष तरीके से प्रस्तुत किया जाता है ताकि उनका गहरा और विचारपूर्ण सांदर्भ बना सके।"""
        deftype2=insert_newlines(deftype2,5)
        deftype2=Text(deftype2,font="Nirmala UI",line_spacing=1,font_size=20)
        leaves2=VGroup(
               deftype2,
		)
        leaves2.set_x(0).arrange(buff=0.5)
        leaves2.next_to(leaf_nodes[1], DOWN, buff=1)

        # Create lines pointing from central node to leaf nodes
        lines3 = VGroup()
        for leaf_node in leaves2:
            line = Line(leaf_nodes[1].get_bottom(), leaf_node.get_top(), color=YELLOW)
            lines3.add(line)
        self.play(Write(text), run_time=2)
        self.play(Create(lines1), run_time=2)
        self.play(Write(leaf_nodes), run_time=3)
        self.play(Create(lines2), run_time=2)
        self.play(Write(leaves1), run_time=3)
        self.play(Create(lines3), run_time=2)
        self.play(Write(leaves2), run_time=3)
        self.wait(5)
        


