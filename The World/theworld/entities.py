import numpy as np

class entity:
    """
    Something that exist in the world
    """
    def __init__(self, world=None, name=None, xy=None):
        self.world = world
        self.name = name
        self.xy = xy
    
    
    def __str__(self):
        return f"An entity named {self.name} in the world \"{self.world.name}\" at {self.xy}"
    
    
    def __repr__(self):
        return "Entity"
    
    
class thing(entity):
    """
    A thing. Not living creature. But not an entity.
    Things have labels (float or array???).
    """
    def __init__(self, world=None, name=None, xy=None, label=0):
        super().__init__(world=world, name=name, xy=xy)
        self.label = label
     
    
    def __str__(self):
        return f"A thing named {self.name} in the world \"{self.world.name}\" at {self.xy}"
    
    
    def __repr__(self):
        return "Thing"
    

class creature(entity):
    """
    A living creature.
    Strength – to lift and move objects
    Perception – how far you can see
    Endurange – how much health do you have
    Charisma - /something about interaction, maybe something with mating, your attractiveness, or with number of initial points/
    Intelligence - /something with NN, maybe number of layers/
    Agility – how far you can get in one round
    Luck – /something with randomizers, or maybe with number of initial points/
    
    OROROROROROROROROROROR
    
    Constitution – max hitpoints
    Perception – view distance
    Speed – max walking distance
    
    Creatures can:
        - See (circle, labels also)
        - Do actions
    
    Actions:
        - Walk (4 directions)
        - Interact (basically, same as walk but you need to walk in the cell of an object)
        - Say (get a label)
        - Mate
        - Do nothing
        
    """
    
    
    def __init__(self, world=None, name=None, xy=None, hp=10):
        super().__init__(world=world, name=name, xy=xy)
        self.hp = hp
        self.environ = None
     
    
    def __str__(self):
        return f"A creature named {self.name} in the world \"{self.world.name}\" at {self.xy}"
    
    
    def __repr__(self):
        return f"Creatue \"{self.name}\", {self.hitpoints}, {self.view_dist}, {self.num_steps}"
    
    
    def observe(self):
        
        
    
    
    def walk(self, direction):
        self.world.move_entity(self.xy, self.xy + direction)
        
        
    