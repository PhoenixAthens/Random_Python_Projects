x = 1
def A():
    y = 2
    def B():
        z = 3
        print(vars())
        print(dir())
    B()
    print(vars())
    print(dir())
A()
"""OUTPUT
{'z': 3}
['z']
{'y': 2, 'B': <function A.<locals>.B at 0x100489d00>}
['B', 'y']
"""