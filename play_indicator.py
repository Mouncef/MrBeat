from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget


class PlayIndicatorButton(ToggleButton):
    pass


class PlayIndicatorLights(Image):
    pass



class PlayIndicatorWidget(BoxLayout):
    nb_steps = 0
    buttons = []
    lights = []
    left_align = NumericProperty(0)

    def set_current_step_index(self, index):
        if index >= len(self.lights):
            return

        for i in range(0, len(self.lights)):
            light = self.lights[i]
            if i == index:
                # button.state = 'down'
                light.source = 'assets/images/indicator_light_on.png'
            else:
                # button.state = 'normal'
                light.source = 'assets/images/indicator_light_off.png'

    def set_nb_steps(self, nb_steps):
        if not nb_steps == self.nb_steps:
            self.lights = []
            self.clear_widgets()

            dummy_widget = Widget()
            dummy_widget.size_hint_x = None
            dummy_widget.width = self.left_align
            self.add_widget(dummy_widget)

            for i in range(0, nb_steps):
                light = PlayIndicatorLights()
                light.source =  'assets/images/indicator_light_off.png'

                # button.disabled = True
                # button.background_color = (0.5, 0.5, 1.0, 1.0)
                # button.background_disabled_down = ''
                # button.background_disabled_normal = ''
                # if i == 0:
                #     button.state = "down"
                self.lights.append(light)
                self.add_widget(light)

            self.nb_steps = nb_steps