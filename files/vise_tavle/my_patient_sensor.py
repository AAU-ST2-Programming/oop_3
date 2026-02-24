from random import randint

class Sensor:
    def measure(self):
        hr = randint(0,240)
        return hr

class Patient:
    def __init__(self, id, age, hr = 0):
        self.id = id
        self.age = age
        self.hr = hr

    def update_heartrate(self, sensor:Sensor):
        new_hr = sensor.measure()
        self.hr = new_hr

    def __repr__(self):
        id = self.id
        hr = self.hr
        age = self.age
        return f"Patient({id=},{age=},{hr=})"


sensor = Sensor()
patient = Patient(id="Martin", age=38)

patient.update_heartrate(sensor)
print(patient)