import jpegdec

def text_centered(display, text, ypos, size):
    """Display text centered on the screen
        display - The display
        text - The text to display
        ypos - The y position to display the text
        size - The size of the text"""
    display.text(
        text,
        int((display.get_bounds()[0] - display.measure_text(text, size)) / 2),
        ypos,
        display.get_bounds()[0],
        size)

class Distance:
    """Class for distance conversions
        distance - distance in CM
    """
    def __init__(self, distance):
        self.distance = distance

    def getCm(self) -> float:
        return self.distance

    def getMm(self) -> float:
        return self.distance * 10

    def getInches(self) -> float:
        return self.distance / 2.54

    def getFeetAndInches(self) -> str:
        inches = self.distance / 2.54
        feet = int(inches / 12)
        inches = round(inches - (feet * 12))
        return "{feet}ft {inches}in".format(feet=feet, inches=inches)

    # Roman units
    def getDigitus(self) -> float:
        return self.distance / 1.85

    def getPedes(self) -> float:
        return self.distance / 29.6

    def getCubitum(self) -> float:
        return self.distance / 44.4

    def getGradus(self) -> float:
        return self.distance / 74


class UiBase:
    """Default UI Base"""
    image = None
    j = None
    width = 0
    height = 0
    midx = 0
    midy = 0

    def __init__(self, display):
        """Initialise the UI and load the background image

            display - The display"""
        self.display = display

        self.width = display.get_bounds()[0]     # Screen width
        self.height = display.get_bounds()[1]    # Screen height
        self.midx = int(self.width / 2)          # Middle of the screen
        self.midy = int(self.height / 2)         # Middle of the screen

        if self.image is not None:
            try:
                self.j = jpegdec.JPEG(self.display)
                self.j.open_file(self.image)
            except:
                exit()

        self.black = self.display.create_pen(0, 0, 0)
        self.white = self.display.create_pen(255, 255, 255)

    def drawBackground(self, x=0, y=0):
        """Draw the background JPG"""
        if self.j is not None:
            self.j.decode(x, y, jpegdec.JPEG_SCALE_FULL, dither=True)