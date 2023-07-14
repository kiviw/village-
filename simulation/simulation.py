import random
from village import Village

# List of male and female names for entity naming
male_names = ["John", "Michael", "William", "David", "James", "Robert", "Joseph", "Daniel", "Richard", "Thomas", "Charles", "Matthew", "Christopher", "Andrew", "Joshua", "Anthony", "Mark", "Paul", "Steven", "Kevin", "Brian", "George", "Edward", "Donald", "Ronald", "Kenneth", "Steven", "Larry", "Jeffrey", "Frank", "Scott", "Eric", "Stephen"]
female_names = ["Mary", "Jennifer", "Linda", "Patricia", "Susan", "Nancy", "Lisa", "Karen", "Donna", "Michelle", "Sandra", "Jessica", "Helen", "Emily", "Amanda", "Sarah", "Melissa", "Ashley", "Kimberly", "Elizabeth", "Mary", "Sharon", "Laura", "Amy", "Stephanie", "Rebecca", "Carol", "Cynthia", "Angela", "Patricia"]

class Entity:
    def __init__(self, position, gender, behavior=None, parents=None, age=0):
        self.position = position
        self.gender = gender
        self.partner = None
        self.children = []
        self.behavior = behavior or {}
        self.parents = parents or []
        self.age = age
        self.history = []

    def move(self, new_position):
        self.position = new_position

    def marry(self, partner):
        if self.partner is None and partner.partner is None and self.gender != partner.gender:
            self.partner = partner
            partner.partner = partner
            self.add_to_history(f"{self} and {partner} got married!")

    def give_birth(self):
        if self.partner is not None and 13 <= self.age <= 45 and self.gender == "female":
            # Generate a new child entity based on available resources and inherit traits
            if len(self.children) < random.randint(1, 13):
                child_behavior = self.inherit_behavior()
                child = Entity(position=self.position, gender=random.choice(["male", "female"]),
                               behavior=child_behavior, parents=[self, self.partner])
                self.children.append(child)
                self.partner.children.append(child)
                self.add_to_history(f"{self} and {self.partner} had a child: {child}!")
            else:
                self.add_to_history(f"{self} and {self.partner} tried to have a child but couldn't due to resource limitations.")

    def inherit_behavior(self):
        # Implement logic to randomly inherit traits from parents
        child_behavior = {}
        for trait, value in self.behavior.items():
            if random.random() < 0.5:  # Randomly inherit traits from either parent
                child_behavior[trait] = value
            else:
                child_behavior[trait] = self.partner.behavior[trait]
        return child_behavior

    def age_entity(self):
        self.age += 1
        if self.gender == "female" and (self.age >= 45 or self.age >= 50):  # Menopause at age 45 to 50
            self.partner = None  # Female can no longer have children

    def add_to_history(self, event):
        self.history.append(event)

    def interact(self, other_entity):
        # Implement logic for social interaction between entities
        pass

    def celebrate_holiday(self, holiday):
        # Implement logic for celebrating holidays and associated activities
        pass

    def construct_house(self):
        # Implement logic for entity to construct a house
        pass

    def construct_cultural_grounds(self):
        # Implement logic for entity to construct cultural grounds
        pass

    def mourn(self, deceased_entity):
        self.add_to_history(f"{self} mourns the death of {deceased_entity}.")

    def __str__(self):
        return f"Entity ({self.gender}) at position {self.position}"

# Creating initial entities with unique names
entity1 = Entity(position=(0, 0), gender="male", name=random.choice(male_names))
entity2 = Entity(position=(2, 3), gender="female", name=random.choice(female_names))
entity3 = Entity(position=(4, 1), gender="male", name=random.choice(male_names))
entity4 = Entity(position=(3, 2), gender="female", name=random.choice(female_names))

# Creating a village
village = Village()
village.add_entity(entity1)
village.add_entity(entity2)
village.add_entity(entity3)
village.add_entity(entity4)

# Assigning names to founding individuals
entity1.name = "Dave"
entity2.name = "Rita"
entity3.name = "Jimmy"
entity4.name = "Sharon"

# Marrying entities
entity1.marry(entity2)
entity3.marry(entity4)

# Simulating the village for 100 years (30 days = 1 year in village time)
for _ in range(100):
    village.simulate()
        
