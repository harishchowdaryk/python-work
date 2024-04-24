class a:
     def function(self):
          print("function")
     def function1(self):
          print("function1")
class b:
     def function3(self):
          print("function3")
        
     def function4(self):
          print("function4")
class c(a,b):
     def fun(self):
          pass
o=a()
p=b()
p.function3()
p.function4()
i=c()
i.function()
i.fun