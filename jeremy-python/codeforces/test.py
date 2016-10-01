x = 0
y = 0
global x
def func():
    global x, y 
    x = x + 1
    if x > 2:
        return
    func()
func()
print x
