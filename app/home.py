import kivy

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.label import Label

from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior

# Set window size (e.g., 1080x1920 for a 1080p phone)
Window.size = (360, 640)  # Dimensions in dp, portrait orientation.
font="assets/fonts/DMSans-VariableFont_opsz,wght.ttf"

class HomeApp(App):
    def build(self):
        # Create a ScrollView
        scroll_view = ScrollView(size_hint=(1, 1))

        # Create a BoxLayout to hold the content
        content_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=(10, 20, 10, 10), spacing=30)
        content_layout.bind(minimum_height=content_layout.setter('height'))

        hatch_img = Image(source="assets/images/hatch.png", size_hint_y=None, height=180)
        content_layout.add_widget(hatch_img)

        set_alarm_btn = Button(
            text='Set Alarm',
            font_name=font,
            font_size=25,
            size_hint=(None, None),
            size=(330, 60),
            background_color=(1, 0, 0, 0.25),
            border=(10, 10, 10, 10)
            )
        content_layout.add_widget(set_alarm_btn)

        alarm_layout = BoxLayout(orientation='vertical', spacing=5)
        alarm_label = Label(text="Alarms",
                            font_name=font,
                            font_size=22,
                            size_hint_x=None,
                            width=75
                            )
        alarm_layout.add_widget(alarm_label)

        # Create a divider using a Widget with specific height and color
        divider = Widget(size_hint=(None, None), size=(10,10))
        divider.canvas.add(Color(0, 0, 0, 1))  # Set color to black
        divider.canvas.add(Line(rectangle=(0, 0, 330, 1),
                                pos_x=100
                                ))  # Draw a horizontal line
        alarm_layout.add_widget(divider)

        content_layout.add_widget(alarm_layout)

        # Add the content layout to the ScrollView
        scroll_view.add_widget(content_layout)

        # Apply the gradient to the background (canvas)
        with scroll_view.canvas.before:
            # Create the gradient effect from color #FFAD48 to #BB54E7
            num_rectangles = 100  # Number of rectangles for the gradient
            rect_height = 640 / num_rectangles  # Height of each rectangle
            for i in range(num_rectangles):
                # Interpolate between the start and end colors
                ratio = i / float(num_rectangles)
                r = (1 - ratio) * 1 + ratio * 0.733
                g = (1 - ratio) * 0.678 + ratio * 0.329
                b = (1 - ratio) * 0.282 + ratio * 0.906
                a = 1  # Full opacity for the gradient

                # Set the color and draw each rectangle
                Color(r, g, b, a)
                self.rect = Rectangle(size=(360, 640), pos=(0, i * rect_height))

        return scroll_view


if __name__ == "__main__":
    HomeApp().run()
