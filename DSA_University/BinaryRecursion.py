def _fibonacci(num:int)->int:
    if num <=1:
        return num
    else:
        return _fibonacci(num-1)+_fibonacci(num-2)

def fibonacci(num):
    if num<0:
        return None
    else:
        return _fibonacci(num)

print(fibonacci(40))