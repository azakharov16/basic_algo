#Going out on a limb here: If you're composing mixins or using abstract base classes, which aren't intended to be instantiated, #an empty __slots__ in those parents seems to be the best way to go in terms of flexibility for subclassers.

#To demonstrate, first, let's create a class with code we'd like to use under multiple inheritance

class AbstractBase:

    __slots__ = ()

    def __init__(self, a, b):

        self.a = a

        self.b = b

    def __repr__(self):

        return f'{type(self).__name__}({repr(self.a)}, {repr(self.b)})'

#We could use the above directly by inheriting and declaring the expected slots:

class Foo(AbstractBase):

    __slots__ = 'a', 'b'

#But we don't care about that, that's trivial single inheritance, we need another class we might also inherit from, maybe with a #noisy attribute:

class AbstractBaseC:

    __slots__ = ()

    @property

    def c(self):

        print('getting c!')

        return self._c

    @c.setter

    def c(self, arg):

        print('setting c!')

        self._c = arg

#Now if both bases had nonempty slots, we couldn't do the below. (In fact, if we wanted, we could have given AbstractBase #nonempty slots a and b, and left them out of the below declaration - leaving them in would be wrong):

class Concretion(AbstractBase, AbstractBaseC):

    __slots__ = 'a b _c'.split()
    
    
    
    
