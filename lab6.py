class Building:
    className = 'Building'
    objectsCount = 0

    def __init__(self, area, cost, residents):
        self._area = area
        self._cost = cost
        self._residents = residents
        Building.objectsCount = Building.objectsCount + 1

    def total_cost(self):
        return self._area * self._cost

    def ratio(self):
        if self._residents > 0:
            return self._cost / self._residents
        return 0

    def info(self):
        print(f'Тип: {self.className}')
        print(f'Площадь: {self._area} кв.м')
        print(f'Стоимость за 1 кв.м: {self._cost} руб.')
        print(f'Количество проживающих: {self._residents}')

class Country_house(Building):
    className = 'Деревенский дом'

    def __init__(self, area, cost, residents, garden_area):
        super().__init__(area, cost, residents)
        self._garden_area = garden_area

    def info(self):
        super().info()
        print(f'Площадь участка: {self._garden_area} кв.м')

    def ratio(self):
        if self._residents > 0:
            return self.total_cost() / self._residents
        else: 0

    def __add__ (self, other):
            if isinstance(other, Country_house):
                new_area = self._area + other._area
                new_cost = (self.total_cost() + other.total_cost()) / new_area
                new_residents = self._residents + other._residents
                new_garden_area = self._garden_area + other._garden_area
                return Country_house(new_area, new_cost, new_residents, new_garden_area)
            return NotImplemented
    
class Apartment(Building):
    className = 'Городской дом'

    def __init__(self, area, cost, residents, number):
        super().__init__(area, cost, residents)
        self._number = number

    def info(self):
        super().info()
        print(f'Колличество квартир: {self._number}')

    def ratio(self):
        if self._residents > 0:
            return self.total_cost() / self._residents
        else: 0
    
    def __add__(self, other):
        if isinstance(other, Apartment):
            new_area = self._area + other._area
            new_cost = (self.total_cost() + other.total_cost()) / new_area
            new_residents = self._residents + other._residents
            new_number = self._number + other._number
            return Apartment(new_area, new_cost, new_residents, new_number)
        return NotImplemented

# for example

country = Country_house(100, 20000, 5, 40)
country.info()
print(f'Общая стоимость: {country.total_cost()}')
print(f'Соотношение стоимости к количеству проживающих: {country.ratio()}')

print("\n")

apart = Apartment(500, 20000, 20, 10)
apart.info()
print(f'Общая стоимость: {apart.total_cost()}')
print(f'Соотношение стоимости к количеству проживающих: {apart.ratio()}')

country1 = Country_house(100, 20000, 5, 40)
country2 = Country_house(100, 10000, 5, 40)

print('\n')

country3 = country1 + country2
print(f'Общая площадь: {country3._area}')
print(f'Общая стоимость: {country3._cost}')
print(f'Общее количество проживающих: {country3._residents}')
print(f'Общая площадб сада: {country3._garden_area}')

print('\n')

apart1 = Apartment(500, 20000, 20, 10)
apart2 = Apartment(600, 30000, 10, 30)

apart3 = apart1 + apart2
print(f'Общая площадь: {apart3._area}')
print(f'Общая стоимость: {apart3._cost}')
print(f'Общее количество проживающих: {apart3._residents}')
print(f'Общая площадб сада: {apart3._number}')