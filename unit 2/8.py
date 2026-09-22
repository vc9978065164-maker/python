name = "Prince"
def demo():
    x = 10
    global name
    name = "Gupta"
    def call():
        nonlocal x
        x = 20
        print("Non local :", x)
    call()
    print("Name Inside fn updated: ", name)
    print(x)

print("Name Outside fn: ",name)
demo()
