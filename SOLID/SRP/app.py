from manim import *
import codecs
class DisplayTodoCode(Scene):
    def construct(self):
        # code=open("code.cpp").read()
        # rendered_code = Code(code=code,
		# 				background_stroke_width=1,
		# 				background_stroke_color=WHITE,
		# 				background="window",
		# 				language="cpp")
        # # rendered_code.scale_to_fit_height(config.frame_height)
        # self.play(Write(rendered_code))
        # code=codecs.open("matter.txt",encoding="utf-8").read()
        rendered_code = Text(text="""अद्भुत रस (Adbhuta Rasa) वह भावना रस है जो आश्चर्य, अद्वितीयता, और अद्वितीयता की भावनाओं को 
प्रकट करता है। यह रस व्यक्ति को चौंकाने, आकर्षित करने, और आश्चर्यमय घटनाओं के प्रति आकर्षित 
करता है। अद्भुत रस का उपयोग कहानियों, नृत्य, नाटक, और फिल्मों में अद्वितीय और अच्छे अनुभवों 
को प्रस्तुत करने के लिए किया जाता है।""", font="Nirmala UI")
        
		
        rendered_code.scale_to_fit_height(config.frame_height)
        rendered_code.scale_to_fit_width(config.frame_width)
        self.play(Write(rendered_code),run_time=10)