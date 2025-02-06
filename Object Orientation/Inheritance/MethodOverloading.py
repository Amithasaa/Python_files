class Demo:
    def disp(self):
        print("inside disp1 with 0 parameter")
        
    def dsip(self, a):
        print("Inside disp2 with 1 parameter")
        
    def disp(self,a,b):
        print("Inside disp3 with 2 parameter")
        
d = Demo()
#d.disp()
#d.disp(10)
d.disp(10, 20) #Inside disp3 with 2 parameter
#Only last method can be accessed
