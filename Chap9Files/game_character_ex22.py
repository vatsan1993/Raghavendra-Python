class GameCharacter:
    def __init__(self, name, hp, base_attack):
        self.__name = name
        self.__hp = hp
        self.__base_attack = base_attack

    def take_damage(self, opponent_attack):
        if opponent_attack <= self.__hp:
            self.__hp -= opponent_attack
        else:
            self.__hp = 0

    def get_hp(self):
        return self.__hp

    def get_base_attack(self):
        return self.__base_attack

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_hp(self, hp):
        self.__hp = hp

    def set_base_attack(self, base_attack):
        self.__base_attack = base_attack

    def __str__(self):
        return f'name: {self.__name}, HP: {self.__hp}, Base_Attack: {self.__base_attack}'


class Player(GameCharacter):
    def __init__(self, name, hp, base_attack, bonus_attack):
        super().__init__(name, hp, base_attack)
        self.__bonus_attack = bonus_attack

    def take_damage(self, opponent_attack):
        # overriding parent method
        super().take_damage(opponent_attack * 0.8)

    def get_bonus_attack(self):
        return self.__bonus_attack

    def set_bonus_attack(self, bonus_attack):
        self.__bonus_attack = bonus_attack

    def __str__(self):
        return super().__str__() + f", Bonus Attack: {self.__bonus_attack}"


player = Player("Thor", 120, 30, 5)
enemy = GameCharacter("Ragnorok", 100, 20)
print(player)
print(enemy)
round = 1
while(player.get_hp() != 0 and enemy.get_hp() !=0 ):
    enemy.take_damage(player.get_base_attack() + player.get_bonus_attack())
    player.take_damage(enemy.get_base_attack())

    print(f"\nRound: {round}")
    print(player)
    print(enemy)
    round += 1

if(player.get_hp() > 0):
    print(f'{player.get_name()} won the game ')
else:
    print(f'{enemy.get_name()} won the game ')


