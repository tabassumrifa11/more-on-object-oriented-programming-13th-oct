print("\033c")

class IOString():
    
    def __init__(self):
        self.str1 = ""
        
        
    def get_String(self):
        self.str1 = input("Enter string : ")
        
        
    def print_String(self):
        print("Result is :", self.str1.upper())




strobj = IOString()

strobj.get_String()
strobj.print_String()