from manim import *
class DisplayVyakran(Scene):
    def construct(self):

        alankar_defination = Text(text="""
                                  अलंकार का परिभाषा (Definition of Alankar):
                                  
								"अलंकार" शब्द संस्कृत में "सजाने-सवारने" का अर्थ होता है।
								इसका मतलब है कि अलंकार के माध्यम से कविता या भाषा को रमणीय और अद्वितीय बनाने का प्रयास किया जाता है। 
								अलंकार का उपयोग 
                                  	कविता,
                                    प्रोस,
                                	और भाषा 
                                में भावनाओं और विचारों को अधिक प्रभावशाली बनाने के लिए किया जाता है।
								""", font="Nirmala UI")
        
        
        alankar_defination.scale_to_fit_height(config.frame_height)
        alankar_defination.scale_to_fit_width(config.frame_width)
        self.play(Create(alankar_defination),run_time=5)
        self.play(Uncreate(alankar_defination),run_time=3)
        
        text=Text("अलंकार", font="Nirmala UI").move_to(UP*3)
        type1=Text("शब्दालंकार", font="Nirmala UI").move_to(LEFT*3)
        type2=Text("अर्थालंकार", font="Nirmala UI").move_to(RIGHT*3)
        
        self.play(Create(text),run_time=2)
        a1 = Arrow(text, type1, color=YELLOW)
        self.play(GrowArrow(a1),run_time=1)
        
        self.play(Create(type1),run_time=5)
        a2 = Arrow(text, type2, color=YELLOW)
        self.play(GrowArrow(a2),run_time=1)
        self.play(Create(type2),run_time=2)
        
        
