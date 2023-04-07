from helper import UiBase

class UiHomer(UiBase):
    """Homer Simpson UI"""

    def __init__(self, display):
        """Initialise the UI and load the background image

            display - The display"""

        self.image = "images/back-homer.jpg"
        super().__init__(display)

        self.bg = self.display.create_pen(90, 25, 70)
        self.fg = self.display.create_pen(180, 180, 180)

    def draw(self, distance):
        """Draw the UI

            distance - The distance instance"""
        self.drawBackground()

        self.display.set_pen(self.fg)
        self.display.set_font('sans')
        self.display.set_thickness(2)

        if (distance.getCm() < 4):
            # Too close
            text = "D'oh!"
        else:
            # Display the distance in cm
            text = "{distance:0.0f}cm".format(distance=distance.getCm())

        self.display.text(text, 120, 90, 200, 0.8)

        # Update the display
        self.display.update()