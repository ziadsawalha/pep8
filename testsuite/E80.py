#: E800
class notok(object):
    pass
#: E800
class Good(object):
    class notok(object):
        pass
    pass
#:


#: E801
def __bad():
    pass
#: E801
def bad__():
    pass
#: E801
def __bad__():
    pass
#: E801
def NotOK():
    pass
#: E801
class ClassName(object):
    def notOk(self):
        pass
#: E801
class ClassName(object):
    def method(self):
        def __bad():
            pass
#:


#: E802
def b11(**BAD):
    pass
#: E802
def b12(*BAD):
    pass
#: E802
def b13(BAD, *VERYBAD, **EXTRABAD):
    pass
#: E802
def b14(BAD):
    pass
#: E802
class Test(object):
    def __init__(self, BAD):
        pass
#: E802
class Test(object):
    @classmethod
    def test(cls, BAD):
        pass
#:


#: E803
class Foo(object):
    @classmethod
    def mmm(cls, ads):
        pass

    @classmethod
    def bad(self, ads):
        pass

    @calling()
    def test(self, ads):
        pass
#: E803
class TestA:
    def open(f):
        pass
    open = classmethod(open)
#:


#: E804
class Foo(object):
    def good(self, ads):
        pass

    def bad(ads, self):
        pass
#:


#: E805
def test():
    Bad = 1
#: E805
def test():
    VERY = 2
#: E805
def test():
    def test2():
        class Foo(object):
            def test3(self):
                Bad = 3
#: E805
def bad():
    global Bad

    def foo():
        Bad = 1
#:
