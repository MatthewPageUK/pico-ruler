from helper import text_centered, UiBase

class UiTape(UiBase):
    """Tape style UI - experminental"""

    def __init__(self, display):
        """Initialise the UI and load the background image

            display - The display"""

        self.image = "images/tape.jpg"
        super().__init__(display)

        self.fg = self.display.create_pen(90, 25, 70)
        self.bg = self.display.create_pen(255, 255, 255)
        self.display.set_font('sans')
        self.display.set_thickness(2)

    def draw(self, distance):
        """Draw the UI

            distance - The distance instance"""

        # Clear the screen
        self.display.set_pen(self.bg)
        self.display.clear()

        # Draw the tape background with offset
        self.drawBackground(int(distance.getCm() * -45) + 25, 100)

        # Draw the pointer
        self.display.set_pen(self.fg)
        self.display.triangle(120, 120, 100, 100, 140, 100)

        text = "{distance:0.2f}cm".format(distance=distance.getCm())
        text_centered(self.display, text, 180, 0.5)

        # Update the display
        self.display.update()
