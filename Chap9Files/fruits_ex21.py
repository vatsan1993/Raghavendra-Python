# Fruit , Mango, Alphano, Banana,type of banana(multi level inheritance )


class Fruit:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def __str__(self):
        return f'Name: {self.__name}, Color: {self.__color}'


class Mango(Fruit):
    def __init__(self, color, can_pickle):
        super().__init__("Mango", color)
        self.__can_pickle = can_pickle

    def get_can_pickle(self):
        return self.__can_pickle

    def set_can_pickle(self, can_pickle):
        self.__can_pickle = can_pickle

    def __str__(self):
        if self.__can_pickle:
            return super().__str__() + f', Can Pickle: Yes'
        return super().__str__() + f', Can Pickle: No'



class Alphonso(Mango):
    def __init__(self, sweetness_level):
        super().__init__("Gold", False)
        self.__sweetness_level = sweetness_level
        self.set_name("Alphonso")

    def get_sweetness_level(self):
        return self.__sweetness_level

    def set_sweetness_level(self, sweetness_level):
        self.__sweetness_level = sweetness_level

    def __str__(self):
        return super().__str__() + f', Sweetness Level: {self.__sweetness_level}'
    
class Jalalu(Mango):
    def __init__(self, sourness_level):
        super().__init__("green", True)
        self.__sourness_level = sourness_level
        self.set_name("Jalalu")

    def get_sourness_level(self):
        return self.__sourness_level

    def set_sourness_level(self, sourness_level):
        self.__sourness_level = sourness_level

    def __str__(self):
        return super().__str__() + f', Sourness Level: {self.__sourness_level}'


class Banana(Fruit):
    def __init__(self, color, can_make_chips):
        super().__init__("Banana",color)
        self.__can_make_chips = can_make_chips

    def get_can_make_chips(self):
        return self.__can_make_chips

    def set_can_make_chips(self, can_make_chips):
        self.__can_make_chips = can_make_chips

    def __str__(self):
        if self.__can_make_chips:
            return super().__str__() + ", Can make chips: Yes"
        return super().__str__() + ", Can make chips: No"


class KeralaBanana(Banana):
    def __init__(self, hardness):
        super().__init__("green", True)
        self.__hardness = hardness
        self.set_name("Kerala Banana")

    def get_hardness(self):
        return self.__hardness

    def set_hardness(self, hardness):
        self.__hardness = hardness

    def __str__(self):
        return super().__str__() + f", Hardness level: {self.__hardness}"


class RedBanana(Banana):
    def __init__(self, ripeness):
        super().__init__("red", False)
        self.__ripeness = ripeness
        self.set_name("Red Banana")

    def get_ripeness(self):
        return self.__ripeness

    def set_ripeness(self, ripeness):
        self.__ripeness= ripeness

    def __str__(self):
        return super().__str__() + f", Ripeness level: {self.__ripeness}"


aphonso = Alphonso(10)
jalalu = Jalalu(10)
kerala_banana = KeralaBanana(10)
red_banana = RedBanana(8)

print(aphonso)
print(jalalu)
print(kerala_banana)
print(red_banana)