from helper import text_centered, UiBase

class UiTrek(UiBase):
    """Star Trek style UI"""

    def __init__(self, display):
        """Initialise the UI and load the background image

            display - The display"""

        self.image = "images/back-trek.jpg"
        super().__init__(display)

        self.fg = self.display.create_pen(172, 169, 255)
        self.display.set_font('sans')
        self.display.set_thickness(3)

    def draw(self, distance):
        """Draw the UI

            distance - The distance instance"""
        self.drawBackground()
        self.display.set_pen(self.fg)
        text = "{distance:0.2f}cm".format(distance=distance.getCm())
        text_centered(self.display, text, 120, 1)

        # Update the display
        self.display.update()
