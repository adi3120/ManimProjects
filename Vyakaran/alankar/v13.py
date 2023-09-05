from manim import *
config = config.copy()
config.background_color = WHITE
config["background_color"] = WHITE

class AlankarTypes(Scene):
    def construct(self):
        text=Text("अलंकार के भेद", font="Nirmala UI").move_to(UP*3)
        
        leaf_nodes=VGroup(
        	Text("शब्दालंकार", font="Nirmala UI",font_size=25),
        	Text("अर्थालंकार", font="Nirmala UI",font_size=25)
		)
        leaf_nodes.set_x(0).arrange(buff=4)
        leaf_nodes.next_to(text, DOWN, buff=1)
        
		# Create lines pointing from central node to leaf nodes
        lines1 = VGroup()
        for leaf_node in leaf_nodes:
            line = Line(text.get_bottom(), leaf_node.get_top(), color=YELLOW)
            lines1.add(line)
        self.play(Write(text), run_time=2)
        self.play(Create(lines1), run_time=2)
        self.play(Write(leaf_nodes), run_time=3)
        
        shabda = leaf_nodes[0]
        artha = leaf_nodes[1]

        # Create leaf nodes
        anupras = Text("अनुप्रास \nअलंकार", font="Nirmala UI", font_size=20,line_spacing=1)
        yamak = Text("यमक \nअलंकार", font="Nirmala UI", font_size=20,line_spacing=1)
        slesh = Text("श्लेष \nअलंकार", font="Nirmala UI", font_size=20,line_spacing=1)

        # Position leaf nodes relative to the central node
        leaf_nodes = VGroup(anupras, yamak, slesh)
        leaf_nodes.set_x(0).arrange(buff=0.3)
        leaf_nodes.next_to(shabda, DOWN, buff=1)

        # Create lines pointing from central node to leaf nodes
        lines = VGroup()
        for leaf_node in leaf_nodes:
            line = Line(shabda.get_bottom(), leaf_node.get_top(), color=BLUE)
            lines.add(line)
        

        # Add all elements to the scene
        self.play(Create(lines), run_time=2)
        self.play(Write(leaf_nodes), run_time=3)
        

        # Create leaf nodes
        leaf_nodes = VGroup(
            Text("उपमा \nअलंकार", font="Nirmala UI", font_size=20,line_spacing=1),
            Text("रूपक \nअलंकार", font="Nirmala UI", font_size=20,line_spacing=1),
            Text("उत्प्रेक्षा \nअलंकार", font="Nirmala UI", font_size=20,line_spacing=1),
            Text("अतिश्योक्ति \nअलंकार", font="Nirmala UI", font_size=20,line_spacing=1),
            Text("मानवीकरण \nअलंकार", font="Nirmala UI", font_size=20,line_spacing=1)
        )

        # Position leaf nodes relative to the central node
        leaf_nodes.set_x(0).arrange(buff=0.5)
        leaf_nodes.next_to(artha, DOWN, buff=2)

        # Create lines pointing from central node to leaf nodes
        lines = VGroup()
        for leaf_node in leaf_nodes:
            line = Line(artha.get_bottom(), leaf_node.get_top(), color=RED)
            lines.add(line)

        # Add all elements to the scene
        self.play(Create(lines), run_time=2)
        self.play(Write(leaf_nodes), run_time=3)
        self.wait(5)

        
		
        

