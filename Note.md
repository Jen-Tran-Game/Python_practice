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

  > Đây là **hàm khởi tạo (constructor),** chạy khi tạo một đối tượng mới từ class
  >

  > `self` đại diện cho đối tượng của class và cho phép truy cập các thuộc tính, phương thức
  >
* `self.name`, `self.age`, `self.ID`, `self.school`, `self.address`

  > Đây là **đặc tính (attributes)** class, được gán giá trị từ đối số đầu vào
  >
* `greeting(self)`, `introduce(self)`:

  > Đây là **phương thức (methods)** để thực hiện các hành vi của class
  >

  ---


  2. **Public, protected, private**

     `public`: truy cập công khai, bất kỳ class nào cũng có thể truy cập

     **Dùng khi:** Muốn thuộc tính/ phương thức có thể được truy cập ở mọi nơi

     ```
     class Product:
         def __init__(self, name):
             self.name = name  # Biến public

         def show(self):
             print(f"Product: {self.name}")  # Phương thức public

     item = Product("Laptop")
     print(item.name)  # ✅ Truy cập trực tiếp
     item.show()       # ✅ Truy cập trực tiếp

     ```

     **Kết quả:**

     ```
     Laptop
     Product: Laptop
     ```

     `protected`: truy cập nội bộ và con, chỉ có thể truy cập trong class và class con dùng `_`

     **Dùng khi:** Muốn giới hạn truy cập nhưng vẫn cho phép kế thừa

     ```
     class Product:
         def __init__(self, name, price):
             self.name = name  
             self._price = price  # Biến protected

         def _show_price(self):  # Phương thức protected
             print(f"Price: {self._price}")

     class Laptop(Product):
         def show_details(self):
             print(f"Laptop: {self.name}")
             self._show_price()  # ✅ Truy cập protected trong class con

     item = Laptop("MacBook", 1500)
     item.show_details()  # ✅ OK (trong class con)
     print(item._price)   # ⚠️ Có thể truy cập nhưng không nên

     ```

     **Lưu ý:**

     - `_protected` chỉ là quy ước trong Python, **vẫn có thể truy cập bên ngoài class nhưng không nên,** dùng `__`
     - **Trong C++ và Java**, protected thực sự giới hạn quyền truy cập từ bên ngoài

       private: truy cập nội bộ, không thể truy cập từ bên ngoài hoặc class con

       **Dùng khi:** Muốn bảo vệ dữ liệu, không cho sửa trực tiếp từ bên ngoài

       ```
       class Product:
           def __init__(self, name, price):
               self.name = name  
               self.__price = price  # Biến private (dùng `__` trước biến)

           def show_price(self):
               print(f"Price: {self.__price}")  # ✅ Truy cập trong class

       item = Product("iPhone", 1200)
       item.show_price()  # ✅ OK (trong class)
       print(item.__price)  # ❌ Lỗi! Không thể truy cập

       ```

       **Lỗi xuất hiện:**

       > AttributeError: 'Product' object has no attribute '__price'
       >

       **Cách vẫn có thể truy cập private (Python mang tính private chứ không tuyệt đối):**

       ```
       print(item._Product__price)  # ⚠️ Không nên dùng

       ```

       > **!!! Không thể kế thừa hoặc truy cập từ class con**
       >

       **Summary:**

       | Mức truy cập          | Truy cập được ở đâu  | Ký hiệu trong Python | Dùng khi nào                                                 |
       | ----------------------- | --------------------------- | ---------------------- | -------------------------------------------------------------- |
       | ***Public***    | Ở mọi nơi                | `self.variable`      | Khi dữ liệu cần mở rộng                                   |
       | ***Protected*** | Trong class và class con   | `_self.variable`     | Khi cần hạn chế chỉnh sửa nhưng vẫn kế thừa           |
       | ***Private***   | Chỉ trong class hiện tại | `__self.variable`    | Khi cần bảo vệ dữ liệu tránh chỉnh sửa ngoài ý muốn |

       |     Mức truy cập     | Ký hiệu trong Python | Truy cập từ bên ngoài class | Truy cập từ subclass (kế thừa) | Truy cập trong chính class |
       | :---------------------: | ---------------------- | ------------------------------- | ---------------------------------- | ---------------------------- |
       |  ***Public***  | `self.variable`      | ✅ Có thể truy cập           | ✅ Có thể truy cập              | ✅ Có thể truy cập        |
       | ***Protected*** | `_self.variable`     | ❌ Không thể truy cập        | ✅ Có thể truy cập              | ✅ Có thể truy cập        |
       |  ***Private***  | `__self.variable`    | ❌ Không thể truy cập        | ❌ Không thể truy cập           | ✅ Có thể truy cập        |
