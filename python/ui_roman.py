from helper import text_centered, UiBase

class UiRoman(UiBase):
    """Roman units style UI"""

    def __init__(self, display):
        """Initialise the UI and load the background image

            display - The display"""

        self.image = "images/back-roman.jpg"
        super().__init__(display)

        self.fg = self.display.create_pen(200, 180, 160)
        self.display.set_font('serif')
        self.display.set_thickness(2)

    def draw(self, distance):
        """Draw the UI

            distance - The distance instance"""
        self.drawBackground()
        self.display.set_pen(self.fg)

        # Display the distance in digitus
        text = "{distance:0.1f}".format(distance=distance.getDigitus())
        self.display.text(text, 155, 85, 200, 0.7)

        # Display the distance in pedes
        text = "{distance:0.1f}".format(distance=distance.getPedes())
        self.display.text(text, 155, 115, 200, 0.7)

        # Display the distance in cubitum
        text = "{distance:0.1f}".format(distance=distance.getCubitum())
        self.display.text(text, 155, 145, 200, 0.7)

        # Display the distance in gradus
        text = "{distance:0.2f}".format(distance=distance.getGradus())
        self.display.text(text, 155, 175, 200, 0.7)

        # Update the display
        self.display.update()
