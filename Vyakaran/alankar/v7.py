from manim import *

class ArthaTypes(Scene):
    def construct(self):
        # Create central node
        artha = Text("अर्थालंकार", font="Nirmala UI").move_to(UP*3)

        # Create leaf nodes
        leaf_nodes = VGroup(
            Text("उपमा \nअलंकार", font="Nirmala UI", font_size=30,line_spacing=1),
            Text("रूपक \nअलंकार", font="Nirmala UI", font_size=30,line_spacing=1),
            Text("उत्प्रेक्षा \nअलंकार", font="Nirmala UI", font_size=30,line_spacing=1),
            Text("अतिश्योक्ति \nअलंकार", font="Nirmala UI", font_size=30,line_spacing=1),
            Text("मानवीकरण \nअलंकार", font="Nirmala UI", font_size=30,line_spacing=1)
        )
        # Position leaf nodes relative to the central node
        leaf_nodes.set_x(0).arrange(buff=0.5)
        leaf_nodes.next_to(artha, DOWN, buff=2)

        # Create lines pointing from central node to leaf nodes
        lines = VGroup()
        for leaf_node in leaf_nodes:
            line = Line(artha.get_bottom(), leaf_node.get_top(), color=YELLOW)
            lines.add(line)

        # Add all elements to the scene
        self.play(Write(artha), run_time=2)
        self.play(Create(lines), run_time=2)
        self.play(Write(leaf_nodes), run_time=3)
        self.wait(5)
