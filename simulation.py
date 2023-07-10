import random

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
        if self.partner is not None and self.age >= 13 and self.age <= 45 and self.gender == "female":
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

class Village:
    def __init__(self):
        self.entities = []
        self.trees = []
        self.rainfall_patterns = [
            # Rainfall probabilities for each month (January to December)
            0.075, 0.06, 0.05, 0.05, 0.06, 0.06, 0.07, 0.07, 0.07, 0.1, 0.095, 0.085
        ]
        self.year = 1
        self.population_threshold = 100000
        self.infrastructure_destruction_range = (0.01, 0.18)  # Destruction range in percentage
        self.land_boundary = 100  # Initial land boundary
        self.disaster_interval = 5  # Interval in years between natural disasters
        self.years_since_disaster = 0
        self.founding_individuals = ["Dave", "Rita", "Jimmy", "Sharon"]
        self.used_names = set(self.founding_individuals)

    def add_entity(self, entity):
        self.entities.append(entity)

    def add_tree(self, tree):
        self.trees.append(tree)

    def simulate(self):
        # Simulate the behavior of entities in the village
        for entity in self.entities:
            # Perform actions based on entity's behavior and environment
            entity.give_birth()
            entity.age_entity()
            self.interact_with_others(entity)
            self.observe_and_celebrate_holidays(entity)
            if len(self.entities) >= self.population_threshold:
                self.handle_supernatural_disasters(entity)
            self.construct_houses_and_cultural_grounds(entity)
            if len(self.entities) >= self.population_threshold:
                self.expand_land()
            self.mourn_deceased(entity)

        self.year += 1

    def interact_with_others(self, entity):
        # Implement logic for entity to interact with other entities in the village
        pass

    def observe_and_celebrate_holidays(self, entity):
        if self.year == 1:
            self.add_to_history(f"{entity} is one of the founding individuals of the village.")

        if self.year % 365 == 0:
            entity.celebrate_holiday("Creation Day")
        # Implement logic for observing and celebrating other holidays based on entity's experiences and events in the simulation

    def handle_supernatural_disasters(self, entity):
        if self.years_since_disaster >= self.disaster_interval and random.random() < 0.01:  # Randomly trigger supernatural disaster with 1% chance
            destruction_percentage = random.uniform(*self.infrastructure_destruction_range)
            self.destroy_infrastructure(destruction_percentage)
            self.years_since_disaster = 0
        else:
            self.years_since_disaster += 1

    def destroy_infrastructure(self, destruction_percentage):
        # Implement logic to destroy a percentage of the developed infrastructure in the village
        pass

    def construct_houses_and_cultural_grounds(self, entity):
        if random.random() < 0.01:  # Randomly trigger construction action with 1% chance
            entity.construct_house()
        if random.random() < 0.005:  # Randomly trigger cultural grounds construction with 0.5% chance
            entity.construct_cultural_grounds()

    def expand_land(self):
        if len(self.entities) >= self.population_threshold and random.random() < 0.01:  # Randomly trigger land expansion with 1% chance
            self.land_boundary += 10  # Increase the land boundary by 10 units

    def mourn_deceased(self, entity):
        # Implement logic for entities to mourn the death of other entities in the village
        pass

    def add_to_history(self, event):
        for entity in self.entities:
            entity.add_to_history(event)

    def get_unique_name(self, gender):
        # Generate a unique name for an entity of the specified gender
        name = ""
        while name == "" or name in self.used_names:
            if gender == "male":
                name = random.choice(male_names)
            elif gender == "female":
                name = random.choice(female_names)
        self.used_names.add(name)
        return name

# List of male and female names for entity naming
male_names = ["John", "Michael", "William", "David", "James", "Robert", "Joseph", "Daniel", "Richard", "Thomas", "Charles", "Matthew", "Christopher", "Andrew", "Joshua", "Anthony", "Mark", "Paul", "Steven", "Kevin", "Brian", "George", "Edward", "Donald", "Ronald", "Kenneth", "Steven", "Larry", "Jeffrey", "Frank", "Scott", "Eric", "Stephen"]
female_names = ["Mary", "Jennifer", "Linda", "Patricia", "Susan", "Nancy", "Lisa", "Karen", "Donna", "Michelle", "Sandra", "Jessica", "Helen", "Emily", "Amanda", "Sarah", "Melissa", "Ashley", "Kimberly", "Elizabeth", "Mary", "Sharon", "Laura", "Amy", "Stephanie", "Rebecca", "Carol", "Cynthia", "Angela", "Patricia"]

# Creating initial entities with unique names
entity1 = Entity(position=(0, 0), gender="male", name=village.get_unique_name("male"))
entity2 = Entity(position=(2, 3), gender="female", name=village.get_unique_name("female"))
entity3 = Entity(position=(4, 1), gender="male", name=village.get_unique_name("male"))
entity4 = Entity(position=(3, 2), gender="female", name=village.get_unique_name("female"))

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
            
