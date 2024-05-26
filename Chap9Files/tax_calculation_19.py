class Asset:
    def __init__(self, name, cost, base_tax_rate):
        self.__name = name
        self.__cost = cost
        self.__base_tax_rate = base_tax_rate
    def get_name(self):
        return self.__name

    def get_cost(self):
        return  self.__cost

    def tax_calculation(self):
        return self.__cost * self.__base_tax_rate / 100

    def __str__(self):
        return  f'Asset Name: {self.__name} Cost: {self.__cost}'

class Liability:
    def __init__(self, name, cost, depreciation_rate):
        self.__name = name
        self.__cost = cost
        self.__depreciation_rate = depreciation_rate

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost

    def get_depreciation(self):
        return self.__depreciation_rate
    def depreciation_calc(self):
        return self.__cost  * self.__depreciation_rate /100

    def __str__(self):
        return f'Asset Name: {self.__name} Cost: {self.__cost}'


class Land(Asset):
    def __init__(self, cost, base_tax_rate, fixed_rate):
        super().__init__('Land', cost, base_tax_rate )
        self.__fixed_rate = fixed_rate

    def tax_calculation(self):
        return super().tax_calculation() + super().tax_calculation()/5 + self.__fixed_rate

class Gold(Asset):
    def __init__(self, cost, base_tax_rate, extra_interest):
        super().__init__('Gold', cost, base_tax_rate)
        self.__extra_interest = extra_interest

    def tax_calculation(self):
        if self.get_cost() > 10000:
            return super().tax_calculation() + self.__extra_interest
        else:
            return 0


class Car(Liability):
    def __init__(self, cost, depreciation):
        super().__init__('Car', cost, depreciation)

    def depreciation_calc(self):
        return super().depreciation_calc() + 500


class Laptop(Liability):
    def __init__(self, cost, depreciation):
        super().__init__('Car', cost, depreciation)

    def depreciation_calc(self):
        return super().depreciation_calc()  + self.get_depreciation() * 10/100


class InvalidArgumentException(Exception):
    def __init__(self, message):
        super().__init__(message)



class Tax_Calculation:
    def __init__(self, cost):
        self.__income = Asset("Income", cost, 5)
        self.__assets = []
        self.__liabilities = []

    def add_asset(self, asset):
        if isinstance(asset, Asset):
            self.__assets.append(asset)
        else:
            raise InvalidArgumentException("You need to provide a Asset class object")

    def add_liability(self, liability):
        if isinstance(liability, Liability):
            self.__liabilities.append(liability)
        else:
            raise InvalidArgumentException("You need to provide a Liability class object")

    def calculate_total_tax(self):

        base_tax = self.__income.tax_calculation()

        for asset in self.__assets:
            base_tax += asset.tax_calculation()

        for liability in self.__liabilities:
            base_tax -= liability.depreciation_calc()

        return base_tax


income = 100000
land = Land(30000, 20, 200)



gold1 = Gold(11000, 10, 100)

gold2 = Gold(12000, 10, 100)
gold3 = Gold(5000, 10, 100)
print(land.tax_calculation())
print(gold1.tax_calculation())
print(gold2.tax_calculation())
print(gold3.tax_calculation())
print()

car = Car(70000, 15)
laptop = Laptop(1000, 20)
print(car.depreciation_calc())
print(laptop.depreciation_calc())



tax_calculator = Tax_Calculation(income)
tax_calculator.add_asset(gold1)
tax_calculator.add_asset(gold2)
tax_calculator.add_asset(gold3)

tax_calculator.add_liability(car)
tax_calculator.add_liability(laptop)

print(tax_calculator.calculate_total_tax())
