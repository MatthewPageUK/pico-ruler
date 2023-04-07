from helper import UiBase

class UiFlip(UiBase):
    """Flip style UI"""

    def __init__(self, display):
        """Initialise the UI and load the background image

            display - The display"""

        self.image = "images/back-flip.jpg"
        super().__init__(display)

        self.display.set_font('sans')
        self.display.set_thickness(3)

    def draw(self, distance):
        """Draw the UI

            distance - The distance instance"""
        self.drawBackground()

        self.display.set_pen(self.white)

        text = "{distance:04d}".format(distance=int(distance.getCm()))

        self.display.text(text[0], 27, 121, 200, 1.25)

        try:
            self.display.text(text[1], 82, 121, 200, 1.25)
        except:
            pass

        try:
            self.display.text(text[2], 138, 121, 200, 1.25)
        except:
            pass

        try:
            self.display.text(text[3], 193, 121, 200, 1.25)
        except:
            pass

        self.display.set_pen(self.black)
        self.display.line(25, 120, 50, 120, 3)
        self.display.line(81, 120, 106, 120, 3)
        self.display.line(137, 120, 162, 120, 3)
        self.display.line(194, 120, 219, 120, 3)

        # Update the display
        self.display.update()
