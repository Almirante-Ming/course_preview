x = 10

def set_x(value):
    global x
    x = value

def get_x():
    return x

if __name__ == "__main__":
    print(get_x())
    set_x(20)
    print(get_x())
