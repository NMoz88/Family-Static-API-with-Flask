
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

        for members in group:
            new_members = {
                "id": self._generateId(),
                "first_name": member["first_name"],
                "last_name": self.last_name,
                "age": members["age"],
                "lucky_numbers": members["lucky_numbers"]
            }
            self._family.append(new_members)
        print(self._family)

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self,  first_name, age, lucky_numbers):
        # fill this method and update the return
        new_members = {
        "id": self._generateId(),
        "first_name": first_name,
        "last_name": self.last_name,
        "age": age,
        "lucky_numbers": lucky_numbers
    }
    self._family.append(new_member)
        
    pass

    def delete_members(self, id):
        # fill this method and update the return
         
        for member in self._family:
            if _members["id"] == id:
                self._family.remove(members)
                return True
        
        return False
        pass       

    def get_members(self, id):
        # fill this method and update the return
        for _members in self._family:
            if members["id"] == id:
                return _members
         
       
        return None
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
