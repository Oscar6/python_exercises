#   1. Basics
class Person: 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
#   Add an Instance Varible (attribute) 
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1

#   Add a Method 2 
    def print_contact_info(self):
        return ('{} \'s email: {}, {}\'s phone number {}'.format(self.name, self.email, self.name, self.phone))

    def add_friend(self, other_person):
        self.friends.append(other_person)
        print('{} has made {} a friend'.format(self.name, other_person.name))

    def num_friends(self):
        print('{} has {} friend\'s'.format(self.name, len(self.friends)))
    
    # def greeting_count(self, other_person):
    #     self.greeted += 1
    #     print('Hello hello {}, I am {}!'.format(other_person.name, self.name))

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# sonny.greet(sonny)

jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
# sonny.greet(jordan)

# jordan.friends.append(sonny)
# print(len(jordan.friends))

#   Add a add_friend method
# jordan.add_friend(sonny)

#   Add num_friends method
# jordan.num_friends()

#   Count number of greetings
sonny.greet(jordan)
print(sonny.greeting_count) #1

sonny.greet(jordan)
print(sonny.greeting_count) #2

sonny.greet(jordan)
print(sonny.greeting_count) #3

# print(sonny.email, sonny.phone)
# print(sonny.print_contact_info())

#### //////////////// #### //////////////// ####

#   2. Make your own class

# class Vehicle: 
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def print_info(self, car):
#         return ('Type of vehicle: {}, {}, {} '.format(self.year, self.make, self.model))

#   Add a Method
# car = Vehicle('Nissan', 'Leaf', 2015)
# print(car.year, car.make, car.model)