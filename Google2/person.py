class Person():
    Name = 'Person name'
    age = 0

    def setPerson(self, Name, age):
        self.Name = Name
        self.age = age

    def birthday(self):
        self.age = self.age + 1

    def info(self):
        print(self.Name)
        print(self.age)

#martin = Person()
#martin.setPerson('Martin', 17)
#martin.info()

#margus = Person()
#margus.setPerson('Margus', 45)
#margus.info()