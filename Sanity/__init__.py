


def typecheck( *types ):
    def check( f ):
        def inner( *args ):
            try:
                assert len(types)==len(args)
                assert all( isinstance(t,T) for t,T in zip(args,types) )
            except AssertionError:
                raise TypeError("Expected %s but got %s" %
                    ( types, tuple(t.__class__ for t in args) )
                )
            return f( *args )
        return inner
    return check



def returns( type ):
    def check( f ):
        def inner( *args ):
            try:
                ret = f(*args)
                assert type( ret )
                return ret
            except AssertionError:
                raise TypeError("Invalid return type: %s" % ret.__class__)
        return inner
    return check

