import math
from helper import text_centered, UiBase

class UiDial(UiBase):
    """Dirty dial UI"""

    def __init__(self, display):
        """Initialise the UI and load the background image

            display - The display"""

        self.image = "images/back-dial.jpg"
        super().__init__(display)

        self.bg = self.display.create_pen(90, 25, 70)
        self.fg = self.display.create_pen(180, 180, 180)

    def draw(self, distance):
        """Draw the UI

            distance - The distance instance"""
        self.drawBackground()

        self.display.set_font('sans')
        self.display.set_thickness(2)

        text = "{distance:0.0f}mm".format(distance=distance.getMm())
        text_centered(self.display, text, 93, 0.7)

        self.drawHand(int(distance.getCm()), 85)

        # Update the display
        self.display.update()


    def drawHand(self, value, distance, intervals = 100):
        """Draw a hand on the clock face
        value: The hand position
        distance: The distance from the centre
        intervals: The number of intervals"""

        self.display.set_pen(self.black)

        # Calculate the position of the hand
        angle = math.pi * 2 * (value / intervals) - math.pi / 2
        x = int(self.midx + math.cos(angle) * distance)
        y = int(self.midy + math.sin(angle) * distance)

        # Draw the hand
        self.display.line(self.midx, self.midy, x, y, 2)

        # Draw lots of little hands ... messy but it works - try a triangle instead
        angle = ( math.pi * 2 * (value / intervals) - math.pi / 2 ) - math.pi / 2
        x1 = int(self.midx + math.cos(angle) * 2)
        y1 = int(self.midy + math.sin(angle) * 2)
        self.display.line(x1, y1, x, y, 2)

        angle = ( math.pi * 2 * (value / intervals) - math.pi / 2 ) + math.pi / 2
        x2 = int(self.midx + math.cos(angle) * 2)
        y2 = int(self.midy + math.sin(angle) * 2)
        self.display.line(x2, y2, x, y, 2)

        angle = ( math.pi * 2 * (value / intervals) - math.pi / 2 ) - math.pi / 2
        x1 = int(self.midx + math.cos(angle) * 4)
        y1 = int(self.midy + math.sin(angle) * 4)
        self.display.line(x1, y1, x, y, 2)

        angle = ( math.pi * 2 * (value / intervals) - math.pi / 2 ) + math.pi / 2
        x2 = int(self.midx + math.cos(angle) * 4)
        y2 = int(self.midy + math.sin(angle) * 4)
        self.display.line(x2, y2, x, y, 2)
