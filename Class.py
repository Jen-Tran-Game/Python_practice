import cv2
class Person: 
    # Hàm khởi tạo (constructor) để gán giá trị cho đối tượng
    def __init__(self, name, age, ID, school, address, image_path = None ):
        self.name = name
        self.age = age
        self.__ID = ID
        self.school = school
        self._address = address
        self.image_path = image_path

    def introduce(self): 
        print(f"My name is {self.name}")
        print(f"I'm {self.age} years old")
        print(f"My ID is {self._Person__ID}")
        print(f"I study at {self.school}")
        print(f"I live in {self._address}")

    def greeting(self): 
        print(f"Hello, nice to meet you. My name is {self.name}, happy to see you")
    

    def show_image(self, scale_percent = 50): 
        if self.image_path: 
            image = cv2.imread(self.image_path)
            if image is not None: 
                width = int(image.shape[1] * scale_percent/250)
                height = int(image.shape[0] * scale_percent/250)
                resized_image = cv2.resize(image,(width, height))

                cv2.imshow(f"Image of {self.name}", resized_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else: 
                print ("Cannot load image, please check the image_path")
        else: 
            print(f"No image available for {self.name}")

person1 = Person("Jen", 25, 78347392, "HCMUTE", "Vietnam", "Jen_image.jpg")
person2 = Person("Marry", 25, 3742738, "KHXH & NV", "Vietnam", "Marry_image.jpg")

person1.greeting()
print("---------------------------------------")
person2.introduce()
print("---------------------------------------")
print(person1._Person__ID) #Truy cập biến private từ bên ngoài nhưng không khuyến khích
#print(person1.__ID): Lỗi AttributeError (truy cập trực tiếp vào biến private sẽ bị lỗi)
person1.show_image()