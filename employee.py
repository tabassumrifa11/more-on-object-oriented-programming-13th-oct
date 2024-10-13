print("\033c")

class Employee:
    
    def __init__(self):
        print("Employee created")
        
        
    def __del__(self):
        print("Destructor called")
        
        
        
def Create_obj():
    print('Making Object.')
    objFunc = Employee()
    print('function end.')
    return objFunc



print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End..')