from faker import Faker
from utils.custom_types import Gender
import random


class RegistrationDataGeneration:
    def __init__(self):
        self.GENDER= random.choice([Gender.MALE, Gender.FEMALE])
        self.fake = Faker("pl_PL")
        if self.GENDER == Gender.MALE:
            self.FIRST_NAME = self.fake.first_name()
        else:
           self.FIRST_NAME = self.fake.first_name()

d =RegistrationDataGeneration()
print(d.FIRST_NAME)
