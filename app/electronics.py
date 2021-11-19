from .item import Item

class Electronics(Item): 
    """
    Documentation here
    """
    
    def __init__(self, category="Electronics", condition=0):
        super().__init__(category=category, condition=condition)

        self.__category = category

    def __str__(self):
        return "A gadget full of buttons and secrets."