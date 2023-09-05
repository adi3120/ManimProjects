from manim import *

class ShabdaTypes(Scene):
    def construct(self):
        # Create central node
        shabda = Text("शब्दालंकार", font="Nirmala UI").move_to(UP * 3)

        # Create leaf nodes
        anupras = Text("अनुप्रास अलंकार", font="Nirmala UI", font_size=30)
        yamak = Text("यमक अलंकार", font="Nirmala UI", font_size=30)
        slesh = Text("श्लेष अलंकार", font="Nirmala UI", font_size=30)

        # Position leaf nodes relative to the central node
        leaf_nodes = VGroup(anupras, yamak, slesh)
        leaf_nodes.set_x(0).arrange(buff=1.5)
        leaf_nodes.next_to(shabda, DOWN, buff=2)

        # Create lines pointing from central node to leaf nodes
        lines = VGroup()
        for leaf_node in leaf_nodes:
            line = Line(shabda.get_bottom(), leaf_node.get_top(), color=YELLOW)
            lines.add(line)

        # Add all elements to the scene
        self.play(Write(shabda), run_time=2)
        self.play(Create(lines), run_time=2)
        self.play(Write(leaf_nodes), run_time=3)
        self.wait(5)
