1. **Class**

* Tạo một class `Person` có các đặc tính: **name, age, ID, school, address** và có phương thức: **greeting, introduce**

  ```
  class Person: 
      # Hàm khởi tạo (constructor) để gán giá trị cho đối tượng
      def __init__(self, name, age, ID, school, address):
          self.name = name
          self.age = age
          self.ID = ID
          self.school = school
          self.address = address

      def introduce(self): 
          print(f"My name is {self.name}")
          print(f"I'm {self.age} years old")
          print(f"My ID is {self.ID}")
          print(f"I study at {self.school}")
          print(f"I live in {self.address}")

      def greeting(self): 
          print(f"Hello, nice to meet you. My name is {self.name}, happy to see you")
  ```


* Cách sử dụng class đã tạo:
  Sau khi tạo class, có thể tạo đối tượng (instance) từ class và gọi các phương thức của nó.

  ```
  person1 = Person("Jen", 25, 78347392, "HCMUTE", "Vietnam")
  person2 = Person("Marry", 25, 3742738, "KHXH & NV", "Vietnam")

  person1.greeting()
  print("---------------------------------------")
  person2.introduce()
  ```

*Giải thích: 

* `def __init__ (self, name, age, ID, school, address):`

  Đây là **hàm khởi tạo (constructor),** chạy khi tạo một đối tượng mới từ class

  `self` đại diện cho đối tượng của class và cho phép truy cập các thuộc tính, phương thức
* `self.name`, `self.age`, `self.ID`, `self.school`, `self.address`

  Đây là **đặc tính (attributes)** class, được gán giá trị từ đối số đầu vào
* `greeting(self)`, `introduce(self)`:

  Đây là **phương thức (methods)** để thực hiện các hành vi của class
