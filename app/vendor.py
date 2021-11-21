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

            if self.get_by_category(item.category):
                if self.get_by_condition(item.condition):
                    self._dict_category[item.category].remove(item.condition) 
                
                return item
        
            del self._dict_category[item.category]
            return item

        return False
    

    def remove_by_category(self, category):
        """
        Documentation here
        """
        #validations
        assert isinstance(category, str), 'category must be a string!'

        if category in self._dict_category.keys():
            del self._dict_category[category]
            self.inventory = list(filter(lambda item: item.category != category, self.inventory))
            return True

        return False


    def remove_by_condition(self, condition):
        """
        Documentation here
        """
        #validations
        assert condition >= 0, 'condition must be greater or equal than zero'
        assert condition < 6, 'condition must be an integer between zero and five'

        for key, value in self._dict_category.items():
            if condition not in value:
                return False
            else:
                break
        
        self.inventory = list(filter(lambda item: item.condition != condition, self.inventory))
        for key in self._dict_category.keys():
            self._dict_category[key] = set(filter(lambda value: value != condition, self._dict_category[key]))

        return True


    def get_by_category(self, category):
        """
        Documentation here
        """
        #validations
        assert isinstance(category, str), 'category must be a string!'

        if category not in self._dict_category.keys():
            return False

        list_by_category = [item for item in self.inventory if item.category == category]

        return list_by_category


    def get_by_condition(self, condition):
        """
        Documentation here
        """
        #validations
        assert condition >= 0, 'condition must be greater or equal than zero'
        assert condition < 6, 'condition must be an integer between zero and five'

        for key, value in self._dict_category.items():
            if condition not in value:
                return False
            else:
                break

        list_by_condition = [item for item in self.inventory if item.condition == condition]

        return list_by_condition


    def swap_items(self, vendor, my_item, their_item):
        """
        Documentation here
        """
        #validations
        assert isinstance(vendor, Vendor), 'vendor must be instance of Vedor!'
        # assert isinstance(my_item, Item), 'my_item must be instance of Item!'
        # assert isinstance(their_item, Item), 'their_item must be instance of Item!'
        
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


    def get_by_age(self, age):
        """
        Documentation here
        """
        #validations
        assert isinstance(age, int), 'age must be an integer' 
        assert age < 10, 'age must be less than 5 years'

        list_by_age = [item for item in self.inventory if item.age == age]

        if list_by_age:
            return list_by_age
        
        return False


    def swap_by_age_condition(self, other, my_priority, their_priority, age_condition=''):
        """
        Documentation here
        """
        #validations
        assert isinstance(other, Vendor), 'other must be instance of Vedor!'
        assert isinstance(my_priority, str), 'my_priority must be a string!'
        assert isinstance(their_priority, str), 'their_priority must be a string!'
        assert isinstance(age_condition, str), 'age_condition must be a string!'
        assert age_condition == 'newest' or age_condition == 'oldest', 'age_condition must be newest or oldest'

        if age_condition:
            my_product_item_list = self.get_by_category(their_priority)
            my_product_item_list_ages = [item.age for item in my_product_item_list]

            their_product_item_list = other.get_by_category(my_priority)
            their_product_item_list_ages = [item.age for item in their_product_item_list]

            if age_condition == 'newest':
                my_product = list(filter(lambda item: item.age == min(my_product_item_list_ages), my_product_item_list))
                their_product = list(filter(lambda item: item.age == min(their_product_item_list_ages), their_product_item_list))

                self.swap_items(other, my_product[0], their_product[0])

                return True
            
            my_product = list(filter(lambda item: item.age == max(my_product_item_list_ages), my_product_item_list))
            their_product = list(filter(lambda item: item.age == max(their_product_item_list_ages), their_product_item_list))

            self.swap_items(other, my_product[0], their_product[0])

            return True

        return False
    

    def swap_by_old(self, other, my_priority, their_priority, my_aging_priority, their_aging_priority):
        pass


    def __repr__(self):
        return f"{self.__class__.__name__}({self.inventory})"


