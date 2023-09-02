class Elevator:
    def __init__(self, min_level=0, max_level=5):
        self._min_level = min_level
        self._max_level = max_level
        self._current_level = 0

    def get_min_level(self):
        return self._min_level

    def get_max_level(self):
        return self._max_level

    def set_min_level(self, level):
        self._min_level = level

    def set_max_level(self, level):
        self._max_level = level

    def get_current_level(self):
        return self._current_level

    def go_up(self):
        if self._current_level + 1 > self.max_level:
            print('You are in the last level. Cannot go up')
        else:
            self._current_level += 1
            print(f'You are currently at {self._current_level}')

    def go_down(self):
        if self._current_level - 1 < self.min_level:
            print('You are in the last level. Cannot go down')
        else:
            self._current_level -= 1
            print(f'You are currently at {self._current_level}')


min_floor = 0
max_floor = 6
lift = Elevator(min_floor, max_floor)


def menu():
    print('pick a floor')
    for floor_num in range(min_floor, max_floor + 1):
        print(floor_num, 'floor', floor_num, end='\t')
    print(':')


def get_user_choice():
    num = int(input())
    return num


def move(lift, floor_num):
    floor_difference = lift.get_current_level() - floor_num
    if floor_difference < 0:
        for i in range(floor_difference):
            print('going up')
            lift.go_up()
    elif floor_difference > 0:

        for i in range(floor_difference):
            print('going down')
            lift.go_down()
    else:
        print('Already in the same level.')


while True:
    menu()
    floor_num = get_user_choice()
    if floor_num < 0:
        print("bye")
        break
    move(lift, floor_num)
    print(lift.get_current_level())
