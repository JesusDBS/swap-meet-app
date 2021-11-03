from .item import Item

class Vendor():
    """
    Documentation here
    """

    def __init__(self, inventory=[]):

        #validations
        # assert all(isinstance(item, str) for item in inventory), 'all elements in inventory must be strings'

        self.inventory = inventory
        self._dict_category = dict()

        for item in inventory:
            self._add_category(item)
            self._add_condition(item)

    def _add_category(self, item):
        """
        Documentation here
        """
        if item.category not in self._dict_category.keys() :
            self._dict_category[item.category] = set()

    def _add_condition(self, item):
        """
        Documentation here
        """
        self._dict_category[item.category].add(item.condition)

    def add(self, item):
        """
        Documentation here
        """

        #validations
        # assert isinstance(item, str), 'The new item must be a string'

        self.inventory.append(item)
        self._add_category(item)
        self._add_condition(item)

        return item

    def remove(self, item):
        """
        Documentation here
        """

        #validations
        # assert isinstance(item, str), 'The item must be a string'

        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return False

    def get_by_category(self, category):
        """
        Documentation here
        """
        #validations
        assert isinstance(category, str), 'category must be a string!'

        list_by_category = [item for item in self.inventory if item.category == category]
        return list_by_category

    def swap_items(self, vendor, my_item, their_item):
        """
        Documentation here
        """
        #validations
        assert isinstance(vendor, Vendor), 'vendor must be instance of Vedor!'
        assert isinstance(my_item, Item), 'my_item must be instance of Item!'
        assert isinstance(their_item, Item), 'their_item must be instance of Item!'
        
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            self.add(their_item)

            vendor.add(my_item)
            vendor.remove(their_item)
            return True
        
        return False

    def swap_first_item(self, vendor):
        """
        Documentation here
        """
        #validations
        assert isinstance(vendor, Vendor), 'vendor must be instance of Vedor!'

        if self.inventory and vendor.inventory:
            self.inventory[0], vendor.inventory[0] = vendor.inventory[0], self.inventory[0]
            return True
        
        return False

    def get_best_by_category(self, category):
        """
        Documentation here
        """
        #validations
        assert isinstance(category, str), 'category must be a string!'

        if category in self._dict_category.keys():
            my_best_product = (
                category,
                max(self._dict_category[category])
            )

            for item in self.inventory:
                product = (
                    item.category,
                    item.condition
                )
                if product == my_best_product:
                    return item

        return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Documentation here
        """
        #validations
        assert isinstance(other, Vendor), 'other must be instance of Vedor!'
        assert isinstance(my_priority, str), 'my_priority must be a string!'
        assert isinstance(their_priority, str), 'their_priority must be a string!'

        my_best_product = self.get_best_by_category(their_priority)
        their_best_product = other.get_best_by_category(my_priority)

        if my_best_product and their_best_product:
            self.swap_items(other, my_best_product, their_best_product)
            return True
        
        return False
     

    def __repr__(self):
        return f"{self.__class__.__name__}({self.inventory})"


