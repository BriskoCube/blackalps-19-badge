import machine 
import ssd1306
import framebuf


class Screen:

    blackalps_logo = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@8\x06\x02\x06\x9c\xfc\xf8\xf0\xe0\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@ \x1e\x01\x00\x00\x00\x00\x80\xf0\xff\xff\xff\xff\xff\xff\xff\xfe\xf0\xe0\xc0\x80\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xe0\xf0\xf8|~}|x\xf8\xf0\xf0\xf0\xf8\xfc~\x7f\x7f\x7f\x7f\x7f\xff\xff\xff\xff\xff\xff\xff\xff\x7f?\x7f\x7f\x7f~|\xfc\xf8\xf0\xe0\xe0\xc0\x80\x80\x00\x00\x00\x00\x00\x00\xc0\xf8\xfc\xfc<\x9c\x9c\x9c\x9c\xfc\xfc\xfcx\x00\xc0\xfc\xfc\xfc\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xf0\xfc|\xfc\xfc\xfc\xf0\x00\x00\xe0\xf8\xfc|\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x0c\x80\xf8\xfc\xfc\xbc\xc4\xe0\xe0\xf0x<\x1c\x0c\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xf0\xf8\xfc=\xfd\xfd\xfc\x00\x00\x00\x00\x80\xf0\xfc\xfd}\x05\x00\x00\x00\x00\x00\x00\xe0\xfc\xfd\xfd\x9d\x9c\x9c\x9c\xdc\xfc\xfc\xfc0\x00\xf0\xfc\xfc\xfc\x9c\x9c\x9c\x9c\x9c\x1c\x1c\x0c\x00\x00\x00`|\x7f\x7f\x7fssss{\x7f\x7f?\x0f`~\x7f\x7f\x7fpppp0\x00`p|\x7f\x7f\x7fsp0\x19\x7f\x7f\x7fp\x01\x1f??|xppp0\x10@|\x7f\x7f\x1f\x03\x03\x0f\x1f\x7f~xp@\x00\x00\x00\x00\x00\x00@px~\x7f\x7f\x7fqp0\x1f\x7f\x7f\x7f\x00@x\x7f\x7f\x7f{ppp0\x10\x00p\x7f\x7f?\x07\x03\x03\x03\x03\x03\x03\x03\x01\x00`pqsssss{\x7f\x7f\x1f\x00\x00\x00\x00')

    def __init__(self):
        self.i2c = machine.I2C(scl=machine.Pin(27), sda=machine.Pin(26))
        self.oled = ssd1306.SSD1306_I2C(128, 64, self.i2c, 0x3c)

    def clear(self):
        """
        Clear screen
        """
        self.oled.fill(0)
        self.oled.show()

    def textbox(self, lines, draw_screen = 1):
        """
        Draws text on the screen

        lines is a list containing the text lines
        Up to 5 lines can be displayed at once
        """
        self.oled.fill_rect(0,12,128,52,0)
        self.oled.rect(0,12,128,52,1)
        x = 13
        for line in lines[:5]:
            self.oled.text(line, 1, x)
            x = x+10
        if draw_screen:
            self.oled.show() 

    def show_logo(self):
        self.oled.fill(0)
        fb = framebuf.FrameBuffer(self.blackalps_logo, 128, 40, framebuf.MVLSB)
        self.oled.blit(fb, 0,0)
        self.oled.show()

    def text(self, text, x, y, invert=False):
        """
        Display text at position x, y

        invert allows to invert colors
        """
        l = len(text)
        self.oled.fill_rect(x-1, y-1, x+(8*l)+1, 10, invert)
        self.oled.text(text, x, y, not invert)
        self.oled.show()

    def draw_menu(self, items, position):
        """
        Draws a list of items, and highlights the position element
        """
        for i in range(len(items)):
            if i == position:
                self.text(items[i], 2, 14+(10*i), 1)
            else:
                self.text(items[i], 2, 14+(10*i), 0)
