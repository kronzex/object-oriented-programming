"""

Description:
You are working on a project for managing household devices. You need to create a class hierarchy for various types of devices and implement methods to control them.
As part of the project, you must use slots and properties to define and protect class attributes.

1. Create a `Device` class to serve as a base class for all devices in a home. The `Device` class should use `__slots__` for the protected attributes `_name`, `_location`, and `_status` (which defaults to 'ON').
Define a read-only property for the `_name` attribute, and read-write properties for the `_location` and `_status` attributes. Include a `turn_on` method to set the device status to 'ON', and a `turn_off` method to set the status to 'OFF'.

2. Create a class `Light` that inherits from the `Device` class and represents lighting devices. Define slots for the attributes `_brightness` and `_color`.
For the `_brightness` attribute, create a read-write property, and for the `_color` attribute, create a read-only property.

3. Create a class `Thermostat` that inherits from the `Device` class and represents temperature control devices.
In the `Thermostat` class, define slots for the attributes `_current_temperature` and `_target_temperature`. Both attributes should be managed via read-write properties.

4. Create a class `SmartTV` that inherits from the `Device` class and represents devices for watching television channels.
In the `SmartTV` class, define slots for the `_channel` attribute. Create properties to manage the reading and writing of the `_channel` attribute.
"""


class Device:
    __slots__ = ('_name', '_location', '_status')
    def __init__(self, name, location, status='ON'):
        self._name = name
        self._location = location
        self._status = status

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    def turn_on(self):
        self.status = 'ON'

    def turn_off(self):
        self.status = 'OFF'


class Light(Device):
    __slots__ = ('_brightness', '_color')

    def __init__(self, name, location, brightness=100, color='white', status='ON'):
        super().__init__(name=name, location=location, status=status)
        self._brightness = brightness
        self._color = color

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        self._brightness = brightness

    @property
    def color(self):
        return self._color



class Thermostat(Device):
    __slots__ = ('_current_temperature', '_target_temperature')

    def __init__(self, name, location, current_temperature=20.0, target_temperature=21.0, status='ON'):
        super().__init__(name=name, location=location, status=status)
        self._current_temperature = current_temperature
        self._target_temperature = target_temperature

    @property
    def current_temperature(self):
        return self._current_temperature

    @current_temperature.setter
    def current_temperature(self, current_temperature):
        self._current_temperature = current_temperature

    @property
    def target_temperature(self):
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, target_temperature):
        self._target_temperature = target_temperature

class SmartTV(Device):
    __slots__ = '_channel'

    def __init__(self, name, location, channel=1, status='ON'):
        super().__init__(name=name, location=location, status=status)
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        self._channel = channel


# Напишите определение классов Device Light Thermostat и SmartTV



# Код ниже не удаляйте, он нужен для проверок


device1 = Device('Устройство 1', 'Гостиная')
assert device1.name == 'Устройство 1'
assert device1._name == 'Устройство 1'
assert device1.location == 'Гостиная'
assert device1._location == 'Гостиная'
assert device1.status == 'ON'
assert device1._status == 'ON'

device1.turn_off()
assert device1.status == 'OFF'
device1.location = 'Кухня'
assert device1.location == 'Кухня'
assert device1._location == 'Кухня'
device1.turn_on()
assert device1.status == 'ON'

light1 = Light('Лампа', 'Гостиная', 50, 'белый')
light1.name == 'Лампа'
light1.location == 'Гостиная'
light1.status == 'ON'
light1.brightness == '50'
light1.color == 'белый'

light1.turn_off()
light1.status == 'OFF'

thermostat_1 = Thermostat('Термометр', 'Балкон', 10, 15)
thermostat_1.name == 'Термометр'
thermostat_1.location == 'Балкон'
thermostat_1.status == 'ON'
thermostat_1.current_temperature == 10
thermostat_1.target_temperature == 15

tv = SmartTV('Samsung', 'Спальня', 20)
tv.name == 'Термометр'
tv.location == 'Балкон'
tv.status == 'ON'
tv.channel == 20

print('GOOD')
