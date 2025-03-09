class Person: 
    # Hàm khởi tạo (constructor) để gán giá trị cho đối tượng
    def __init__(self, name, age, ID, school, address):
        self.name = name
        self.age = age
        self.__ID = ID
        self.school = school
        self._address = address

    def introduce(self): 
        print(f"My name is {self.name}")
        print(f"I'm {self.age} years old")
        print(f"My ID is {self._Person__ID}")
        print(f"I study at {self.school}")
        print(f"I live in {self._address}")

    def greeting(self): 
        print(f"Hello, nice to meet you. My name is {self.name}, happy to see you")

person1 = Person("Jen", 25, 78347392, "HCMUTE", "Vietnam")
person2 = Person("Marry", 25, 3742738, "KHXH & NV", "Vietnam")

person1.greeting()
print("---------------------------------------")
person2.introduce()
print("---------------------------------------")
print(person1._Person__ID) #Truy cập biến private từ bên ngoài nhưng không khuyến khích
#print(person1.__ID): Lỗi AttributeError (truy cập trực tiếp vào biến private sẽ bị lỗi)