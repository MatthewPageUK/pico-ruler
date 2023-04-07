from helper import text_centered, UiBase

class UiDefault(UiBase):
    """Default UI"""

    def __init__(self, display):
        """Initialise the UI and load the background image

            display - The display"""

        self.image = "images/back.jpg"
        super().__init__(display)

        self.bg = self.display.create_pen(90, 25, 70)
        self.fg = self.display.create_pen(50, 255, 50)

    def draw(self, distance):
        """Draw the UI

            distance - The distance instance"""
        self.drawBackground()

        self.display.set_pen(self.fg)

        # Display the distance in cm
        text = "{distance:0.2f}".format(distance=distance.getCm())
        text_centered(self.display, text, 90, 3)

        # Display the distance in inches
        text = "{distance:0.2f}".format(distance=distance.getInches())
        text_centered(self.display, text, 133, 3)

        # Update the display
        self.display.update()
