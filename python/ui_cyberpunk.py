from helper import text_centered, UiBase

class UiCyberpunk(UiBase):
    """Cyber style UI"""

    def __init__(self, display):
        """Initialise the UI and load the background image

            display - The display"""

        self.image = "images/back-cyber.jpg"
        super().__init__(display)

        self.bg = self.display.create_pen(90, 25, 70)
        self.fg = self.display.create_pen(180, 90, 180)
        self.display.set_font('sans')
        self.display.set_thickness(2)

    def draw(self, distance):
        """Draw the UI

            distance - The distance instance"""
        self.drawBackground()

        # Get the distance as a binary string
        distanceB = bin(int(distance.getCm()))

        # Get the distance as a hex string
        distanceH = hex(int(distance.getMm()))

        self.display.set_pen(self.white)

        text = "{distanceB}".format(distanceB=distanceB)
        self.display.text(text, 15, 85, 200, 0.5)
        text = "{distanceH}".format(distanceH=distanceH)
        self.display.text(text, 15, 105, 200, 0.5)

        text = "{distance:0.1f}mm".format(distance=distance.getMm())
        self.display.text(text, 155, 105, 200, 0.5)

        self.display.set_pen(self.fg)
        self.display.circle(self.midx, (230 - int(distance.getCm() * 1.3)), int((230 - int(distance.getCm() * 2)) / 7) )

        # Update the display
        self.display.update()
