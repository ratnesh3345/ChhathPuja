from manim import *
from manim.utils.color import *

class ChhathPujaScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFD1DC"
        self.animate_water()
        self.wait(1)
        self.add_banana_trees()
        self.wait(1)
        self.add_devotees()
        self.animate_sun()
        greeting = Text("Happy Chhath Puja!", font_size=48, color=BLACK).to_edge(UP*4)
        self.play(Write(greeting), run_time = 3)
        self.wait(2)

    def add_banana_trees(self):
        banana_tree1 = self.create_banana_tree()
        banana_tree1.move_to(DOWN * 0.5 + RIGHT * 5.5)
        self.add(banana_tree1)
        banana_tree2 = self.create_banana_tree()
        banana_tree2.move_to(DOWN * 0.5 + LEFT * 5.5)
        self.add(banana_tree2)

    def create_banana_tree(self):
        # Trunk
        trunk = Rectangle(width=0.15, height=1, color="#8B4513").set_fill("#8B4513", opacity=0.3)
        trunk.move_to(DOWN * 1)

        # Large banana leaves
        leaves = VGroup()
        for angle in [60, 30, -30, -60]:
            leaf = Ellipse(width=1.2, height=0.4, color=GREEN, fill_opacity=1).set_fill(GREEN, opacity=0.8)
            leaf.rotate(angle * DEGREES)
            leaf.next_to(trunk, UP, buff=0.1)
            leaves.add(leaf)

        # Group trunk and leaves
        banana_tree = VGroup(trunk, leaves)
        return banana_tree
    def animate_sun(self):
        sun = Circle(radius=1, color=YELLOW, fill_opacity=1).set_fill(YELLOW)
        sun.move_to(3*DOWN)
        self.play(sun.animate.move_to(3*UP), run_time = 5, rate_func = smooth)


    def animate_water(self):
        river = Rectangle(width=config.frame_width, height=3, color=BLUE, fill_opacity=0.6 )
        river.move_to(2.5*DOWN)
        self.add(river)
    def add_devotees(self):
        devotee = self.create_devotee()  # Create devotee figure
        devotee.move_to(DOWN * 1.5 + RIGHT * 4)  # Position the devotee
        self.add(devotee)
        hand_movement = devotee.animate.shift(UP * 0.1).shift(DOWN * 0.1)
        self.play(hand_movement, rate_func=there_and_back, run_time=2)

        devotee2 = self.create_devotee()  # Create devotee figure
        devotee2.move_to(DOWN * 1.5 + LEFT * 4)  # Position the devotee
        self.add(devotee2)
        hand_movement = devotee2.animate.shift(UP * 0.1).shift(DOWN * 0.1)
        self.play(hand_movement, rate_func=there_and_back, run_time=2)

    def create_devotee(self):
        # Body
        body = Rectangle(width=0.3, height=1.2, color=ORANGE).set_fill(ORANGE, opacity=1)  # Body

        # Head
        head = Circle(radius=0.3, color="#f1c27d").set_fill("#f1c27d", opacity=1)

        # Position the head above the body and rotate it
        head.move_to(body.get_top() + UP * 0.15)
        head.rotate(90 * DEGREES)  # Rotate head slightly to face northwest

        # Eyes
        left_eye = Circle(radius=0.05, color=BLACK).move_to(head.get_center() + LEFT * 0.1 + UP * 0.1)  # Left eye
        right_eye = Circle(radius=0.05, color=BLACK).move_to(head.get_center() + RIGHT * 0.1 + UP * 0.1)  # Right eye

        smile = Arc(radius=0.1, angle=PI / 4, color=BLACK).move_to(head.get_center() + DOWN * 0.05)
        smile.flip(LEFT)
        left_arm = Line(start=body.get_left() + LEFT * 0.1, end=body.get_top() + UP * 0.1, color="#f1c27d")
        right_arm = Line(start=body.get_right() + RIGHT * 0.1, end=body.get_top() + UP * 0.1, color="#f1c27d")

        devotee_figure = VGroup(body, head, left_arm, right_arm, left_eye, right_eye, smile)


        return devotee_figure
