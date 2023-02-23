
class Person:
    
    def __init__(self, firstname, lastname, dob, gender, address):
        self.firstname = firstname
        self.lastname = lastname
        self._dob = dob
        self.gender = gender
        self.address = address
        
    # we can now focus on adding getters, setters for the properties above and maybe getters and setters for any other properties we can think of
    # next step would be to add behaviour - methods
    
