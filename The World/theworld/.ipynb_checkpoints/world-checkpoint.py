import numpy as np
# import pandas as pd
# import time

# from IPython import display as dsp

# from matplotlib import pyplot as plt
# import matplotlib.colors as mcolors
# import matplotlib.patches as patches

# import tensorflow as tf
# from tensorflow.keras import Sequential
# from tensorflow.keras.layers import Dense
# from tensorflow.keras.optimizers import Adam

### Some functions ###
def getattr_vectorized(array, attribute_name):
    return np.frompyfunc(lambda x: getattr(x, attribute_name), 1, 1)(array)


### Classes ###
class world:
    """
    World is where all things are exist.
    """
    
    def __init__(self, shape):
        # And, there was nothing...
        self.num_entities = 0
        
        # ...at the beginning of time
        self.time = 0
        
        # Create array with cells
        # IS THERE MORE OPTIMAL WAY TO DO THIS?
        self.cells = np.zeros(shape, dtype=object)
        for xnd in range(shape[0]):
            for ynd in range(shape[1]):
                self.cells[xnd, ynd] = cell([xnd, ynd])
 

    def create_entity(self, xy, entity_type, name=None, silent=False, *args, **kwargs):
        if name is None:
            name = f'{self.num_entities:03d}'
            
        is_success = self.cells[xy[0], xy[1]].put(entity_type(world=self, name=name, *args, **kwargs))
        
        if is_success:
            self.num_entities = self.num_entities + 1
        else:
            if not silent:
                print("Error: unable to create, cell is occupied")
            return False
        
    
    def destroy_entity(self, xy, silent=False):
        is_success = self.cells[xy[0], xy[1]].clear()
        
        if is_success:
            self.num_entities = self.num_entities - 1
        else:
            if not silent:
                print("Error: nothing to delete, cell is empty")
            return False
        
        
    def move_entity(self, departure_xy, arrival_xy, silent=False):
        entity_copy = self.cells[departure_xy[0], departure_xy[1]].entity_inside
        
        if entity_copy is not None:
            is_success = self.cells[arrival_xy[0], arrival_xy[1]].put(entity_copy)
            
            if is_success:
                self.cells[departure_xy[0], departure_xy[1]].clear()
            else:
                if not silent:
                    print("Error: unable to move, arrival cell is ocupied")
        else:
            if not silent:
                print("Error: nothing to move, departue cell is empty")
            return False
    
    
    def evolve(self):
        """
        roll initiative
        create initiative table
        do actions
        delete all dead creatures
        """
        self.time = self.time + 1
            
    
class cell:
    """
    Unit cell of the world. Objects are located in the cells.
    """
    
    def __init__(self, xy, entity_inside=None):
        self.xy = xy
        self.entity_inside = entity_inside
    
    def __str__(self):
        return f"Cell with coordinates {self.xy}. Has {self.entity_inside} in it."
    
    def __repr__(self):
        return f"Cell{self.xy}"
    
    
    def put(self, entity):
        """
        Puts something to the cell
        
        If there was nothing before, places something and returns True.
        If there was something, returns False
        """
        if self.entity_inside is None:
            self.entity_inside = entity
            self.entity_inside.xy = self.xy
            return True
        else:
            return False
    
    
    def clear(self):
        """
        Removes something from the cell
        
        If there was something, removes it from the cell and returns True
        if there was nothing, returns False
        """
        if self.entity_inside is not None:  
            self.entity_inside = None
            return True
        else:
            return False
    

class entity:
    """
    Something that exist in the world
    """
    def __init__(self, world=None, name=None, xy=None):
        self.world = world
        self.name = name
        self.xy = xy
    
    
    def __str__(self):
        return f"An entity named {self.name} in the world {self.world} at {self.xy}"
    
    
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
        return f"A thing named {self.name} in the world {self.world} at {self.xy}"
    
    
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
        - Say (4 directions)
        - Mate
        - Do nothing
        
    """
    hitpoints_multiplier = 1
    view_dist_multiplier = 1
    num_steps_multiplier = 1
    
    
    def __init__(self, world=None, name=None, xy=None, csp=np.ones(3)*10):
        super().__init__(world=world, name=name, xy=xy)
        self.csp = special
        self.hitpoints, self.view_dist, self.num_steps = self.csp * [hitpoints_multiplier, view_dist_multiplier, num_steps_multiplier]
     
    
    def __str__(self):
        return f"A creature named {self.name} in the world {self.world} at {self.xy}"
    
    
    def __repr__(self):
        return "Thing"
    
    
        
        
        
        