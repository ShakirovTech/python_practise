class Device:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}, Price: {self.get_price()}'

    def get_price(self):
        return self.price


class PhysicalDevice(Device):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        if not isinstance(weight, int):
            raise TypeError('Weight must be an integer')
        self.weight = weight

    def get_price(self):
        return super().get_price() + (self.weight * 300)

    def __str__(self):
        return super().__str__() + f', Weight: {self.weight}'


class ItDevice(Device):
    def __init__(self, name, price, mb):
        super().__init__(name, price)
        if not isinstance(mb, int):
            raise TypeError('MB must be an integer')
        self.mb = mb

    def __str__(self):
        return super().__str__() + f', MB: {self.mb}'


phone = Device('Phone', 300)
phone2 = PhysicalDevice('Phone2', 500, 2)
print(phone)
print(phone2)
phone3 = ItDevice('Phone3', 500, 2048)
print(phone3)