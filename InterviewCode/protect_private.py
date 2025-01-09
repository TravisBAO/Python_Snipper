class Person:

    def __init__(self):
        self.name = "Bob"
        self._gender = "male"
        self.__age = "18"

    def show_name(self):
        return self.name
    
    def _show_name_protect(self):
        return self.name
    
    def __show_name_private(self):
        return self.name
    
    @property
    def info_gender(self):
        return self._gender
    
    @info_gender.setter
    def info_gender(self, value):
        self._gender = value
    
    @property
    def info_age(self):
        return self.__age
    
    @info_age.setter
    def info_age(self, value):
        self.__age = value

class Child(Person):

    def show_parent_name(self):
        return self.name
    
    def show_parent_gender(self):
        return self._gender
    
    def show_parent_age(self):
        return self.__age
    
    def call_parent_public_method(self):
        return self.show_name()
    
    def call_parent_protect_method(self):
        return self._show_name_protect()

    def call_parent_private_method(self):
        return self.__show_name_private()
    
class Example:
    def __init__(self):
        self._protected_attr = "I am protected"

obj = Example()
print(obj._protected_attr)  # Output: I am protected (but it's discouraged)    