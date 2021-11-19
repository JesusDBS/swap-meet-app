from .item import Item

class Decor(Item):
    """
    Documentation here
    """
    
    def __init__(self, category="Decor", condition=0):
        super().__init__(category=category, condition=condition)

        self.__category = category

    def __str__(self):
        return "Something to decorate your space."