"""The following code will provide 3 different HTML when calling df_1, df_2, df_3 respectfully"""

import random
import pandas as pd
from faker import Faker



def generate_patient():
    """Generate a random patient with medical data."""
    
    fake = Faker(["da_DK"])
    # Generate BP (Systolic: 90-180, Diastolic: 60-110)
    systolic_bp = random.randint(90, 180)
    diastolic_bp = random.randint(60, 110)

    # Generate EF% (Ejection Fraction: 20% - 70%)
    ef = random.randint(20, 70)
    
    return {
        "Name": fake.name(),
        "DOB": fake.date_of_birth(),
        "Systolic_BP": systolic_bp,
        "Diastolic_BP": diastolic_bp,
        "EF_Percent": ef,
    }


def generate_person():
    """
    Generate a person with name, gender, height (cm), and weight (kg).
    """
    fake = Faker()
    gender = random.choice(["male", "female"])

    if gender == "male":
        name = fake.name_male()
        height_cm = random.gauss(178, 7)
        weight_kg = random.gauss(78, 10)

    else:
        name = fake.name_female()
        height_cm = random.gauss(165, 6)
        weight_kg = random.gauss(65, 8)

    # Clamp to reasonable ranges
    height_m = round(max(140, min(height_cm, 210)), 1) / 100.0
    weight_kg = round(max(40, min(weight_kg, 150)), 1)
    bmi = round(weight_kg / height_m / height_m,1)
    if random.randint(0, 99)>95:
        weight_kg = weight_kg + round(random.choice([random.gauss(10,1), random.gauss(-10,1)]),1)
    return {
        "name": name,
        "gender": gender,
        "height_m": height_m,
        "weight_kg": weight_kg,
        "bmi": bmi 
    }

def generate_patient_wide():
    """Generate a random patient with medical data."""
    fake = Faker(["da_DK"])
    
    return {
        "Name": fake.name(),
        "DOB": fake.date_of_birth(minimum_age=10),
        "Systolic_BP_1": random.randint(110, 180),
        "Diastolic_BP_1": random.randint(60, 110),
        "bt_date_1": fake.date_of_birth(maximum_age=8),
        "EF_Percent_1": random.randint(20, 70),
        "EF_date_1": fake.date_of_birth(maximum_age=8),
        "Systolic_BP_2": random.randint(110, 180),
        "Diastolic_BP_2": random.randint(60, 110),
        "bt_date_2": fake.date_of_birth(maximum_age=8),
        "EF_Percent_2": random.randint(20, 70),
        "EF_date_2": fake.date_of_birth(maximum_age=8),
    }


def generate_patients_df(n=10):
    """Generate a Pandas DataFrame of n patients."""
    patients = [generate_patient() for _ in range(n)]
    return pd.DataFrame(patients)


def generate_patients_wider_df(n=10):
    """Generate a Pandas DataFrame of n patients."""
    patients = [generate_patient_wide() for _ in range(n)]
    return pd.DataFrame(patients)




class GameUnit:
    """A class representing a military unit in an RTS game."""

    fake = Faker()
    UNIT_TYPES = ["Infantry", "Tank", "Aircraft", "Mech", "Artillery", "Naval"]

    def __init__(
        self, name, unit_type, normal_attack, max_health, ult_attack, current_health
    ):
        self.name = name
        self.unit_type = unit_type
        self.normal_attack = normal_attack
        self.max_health = max_health
        self.ult_attack = ult_attack
        self.current_health = current_health

    def to_dict(self):
        """Convert unit attributes to a dictionary."""
        return {
            "Unit Name": self.name,
            "Type": self.unit_type,
            "Normal Attack Power": self.normal_attack,
            "Max Health": self.max_health,
            "Ultimate Attack Power": self.ult_attack,
        }


def generate_units(n=10):
    """Generate a list of random game units."""
    units = []

    for _ in range(n):
        name = fake.word().capitalize() + " " + random.choice(GameUnit.UNIT_TYPES)
        unit_type = random.choice(GameUnit.UNIT_TYPES)

        # Assign stats based on unit type
        if unit_type == "Infantry":
            normal_attack = random.randint(20, 50)
            max_health = random.randint(100, 300)
            ult_attack = normal_attack * random.uniform(1.5, 2.5)
        elif unit_type == "Tank":
            normal_attack = random.randint(80, 150)
            max_health = random.randint(800, 1200)
            ult_attack = normal_attack * random.uniform(2, 3)
        elif unit_type == "Aircraft":
            normal_attack = random.randint(100, 180)
            max_health = random.randint(600, 900)
            ult_attack = normal_attack * random.uniform(2.5, 4)
        elif unit_type == "Mech":
            normal_attack = random.randint(120, 200)
            max_health = random.randint(1000, 1500)
            ult_attack = normal_attack * random.uniform(3, 4.5)
        elif unit_type == "Artillery":
            normal_attack = random.randint(150, 220)
            max_health = random.randint(500, 700)
            ult_attack = normal_attack * random.uniform(4, 5)
        else:  # Naval units
            normal_attack = random.randint(200, 300)
            max_health = random.randint(1500, 2500)
            ult_attack = normal_attack * random.uniform(3, 4)

        current_health = random.randint(0, max_health)

        unit = GameUnit(
            name, unit_type, normal_attack, max_health, int(ult_attack), current_health
        )
        units.append(unit.to_dict())

    return pd.DataFrame(units)


def df_1(N: int = 3):
    return pd.DataFrame({"hej": [int(random.random() * 100) for _ in range(N)]})


def df_2(N: int = 3):
    return generate_units(N)


def df_3(N: int = 3):
    return generate_patients_df(N)


def df_4(N: int = 3):
    return generate_patients_wider_df(N)


if "__main__" == __name__:
    pers = []
    for i in range(199):
        p = generate_person()
        pers.append(p)        
        
    df: pd.DataFrame = pd.DataFrame((pers))
    
    print(df)
    df.to_csv("exercise_people1.csv", index=False)