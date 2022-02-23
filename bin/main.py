import sys



class Main:
    __slots__ = ()

    @staticmethod
    def main():
        print("Hello, world!")
        print("Goodbye, world!")


class haxe_iterators_ArrayIterator:
    __slots__ = ("array", "current")

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return python_internal_ArrayImpl._get(self.array, _hx_local_2())
        return _hx_local_3()



class python_internal_ArrayImpl:
    __slots__ = ()

    @staticmethod
    def _get(x,idx):
        if ((idx > -1) and ((idx < len(x)))):
            return x[idx]
        else:
            return None


class python_internal_MethodClosure:
    __slots__ = ("obj", "func")

    def __init__(self,obj,func):
        self.obj = obj
        self.func = func

    def __call__(self,*args):
        return self.func(self.obj,*args)




Main.main()
