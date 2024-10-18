class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message



class Car:
    model = True
    __vin = True
    def __init__(self, model, vin, __numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = __numbers

        if not self.__is_valid_vin(vin):
            raise IncorrectVinNumber(message=True)
        if not self.__is_valid_numbers(__numbers):
            raise IncorrectCarNumber(message=True)



    def __is_valid_vin(self, vin_number):
        self.vin_number = vin_number
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(message='Некорректный тип vin номера')
        elif vin_number not in range(1000000, 9999999):
            raise IncorrectVinNumber(message='Неверный диапозон vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        self.numbers = numbers
        if not isinstance(numbers, str):
            raise IncorrectCarNumber(message='Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumber(message='Неверная длина номера')
        else:
            return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')