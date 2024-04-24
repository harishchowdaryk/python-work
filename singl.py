class a:
     def function(self):
          print("function")
     def function1(self):
          print("function1")
class b(a):
     def function3(self):
          print("function3")
        
     def function4(self):
          print("function4")
o=a()
p=b()
p.function3()
p.function1()
