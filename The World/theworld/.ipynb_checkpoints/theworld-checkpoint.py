import numpy as np

# Helper functions
def getattr_vectorized(array, attribute_name):
    return np.frompyfunc(lambda x: getattr(x, attribute_name), 1, 1)(array)


# Classes
class world:
    """
    World is where all things are exist.
    """
    
    def __init__(self, shape, name="main"):
        self.name = name
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
            
            
    def __str__(self):
        return f"World \"{self.name}\" with {self.num_entities} and shape {self.cells.shape}"
    
    
    def __repr__(self):
        return f"World \"{self.name}\", shape={self.cells.shape}, {self.num_entities} entities"
 

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
        return f"Cell at {self.xy}"
    
    
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