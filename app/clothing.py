from .item import Item

class Clothing(Item):
    """
    Documentation here
    """
    
    def __init__(self, category="Clothing", condition=0):
        super().__init__(category=category, condition=condition)

        self.category = category

    def __str__(self):
        return "The finest clothing you could wear."