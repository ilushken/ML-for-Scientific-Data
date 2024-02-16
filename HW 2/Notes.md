World consist of a grid made of n times m cells.
Each cell can produce an effect, for example:it can heal or damage or something different
Each cell has a place for an object
Each object has:
    - id (seen to user only)
    - xy, (2,) numpy array with it's coordinates 
    - some information (it can be nutrition value, weight, or just some numbers, e.g. feature values of a sample)
There may be only one object in each cell!!!

There are different types of objects, some heals, some makes damage, one just exists, some have some info in them.

There are also creatures.
Creatures can see (obtain lists of items in their region of vision which is circle obtained via midpoint circle algorhytm)
Creatures can interact with objects (different types of objects have different interactions)
Something like:
    - eat a berry to regain health
    - push object
    - lift object and move with the object (and drop it after)
In order to interact with an

All actions should be encoded by same number of numbers


Stats via point buy system
Initiative grid to do actions (roll + initiative value)