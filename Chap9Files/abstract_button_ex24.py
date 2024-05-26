from abc import ABC

class Button(ABC):
    def __init__(self, width, height, content, color):
        self.__width = width
        self.__height = height
        self.__content = content
        self.__color = color

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_content(self):
        return self.__content

    def set_content(self, content):
        self.__content = content

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color= color


    def __str__(self):
        return f'Width:  {self.__width}, Height: {self.__height}, Content: {self.__content} , color: {self.__color}'

    def on_click(self):
        pass


class FormButton(Button):
    def __init__(self, width, height, content, color, shadow):
        super().__init__(width, height, content, color)
        self.__shadow = shadow

    def get_shadow(self):
        return self.__shadow

    def set_shadow(self, shadow):
        self.__shadow = shadow

    def on_click(self):
        return 'Form Submitted'

    def __str__(self):
        return f'{super().__str__()} Shadow: {self.__shadow}'


class AnimateButton(Button):
    def __init__(self, width, height, content, color, animation_type, duration, delay):
        super().__init__(width, height, content, color)
        self.__animation_type = animation_type
        self.__animation_duration = duration
        self.__animation_delay = delay


    def get_animation_type(self):
        return self.__animation_type

    def set_animation_type(self, animation_type):
        self.__animation_type = animation_type

    def get__animation_duration(self):
        return self.__animation_duration

    def set_animation_duration(self, animation_duration):
        self.__animation_duration = animation_duration

    def get_animation_delay(self):
        return self.__animation_delay

    def set_animation_delay(self, animation_delay):
        self.__animation_delay = animation_delay

    def on_click(self):
        return f'Animation {self.__animation_type} starts at {self.__animation_delay} milli seconds and runs for \
{self.__animation_duration} millie seconds'

    def __str__(self):
        return f'{super().__str__()} Animation type: {self.__animation_type}, Animation duration: \
{self.__animation_duration} Animation delay: {self.__animation_delay}'


fb = FormButton(100, 20, "Submit", "blue", 10)
ab = AnimateButton(100, 20, "Animate", "Green","zoom in",  200, 50)
print(fb)
print(ab)

print(fb.on_click())
print(ab.on_click())

