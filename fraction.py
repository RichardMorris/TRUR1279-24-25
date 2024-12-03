# gcd algorithm

def gcd(a,b):
    print("aaa",a,b)
    while( b> 0):
        print("bBBB")
        t = b
        b = a % b
        a = t
        print("ccc",a,b)
    return a

def test_gcd():
    assert(gcd(48,18) == 6)
    # assert(gcd(48,0) == 48)
    # assert(gcd(0,48) == 48)
    # assert(gcd(48,1) == 1)
    # assert(gcd(1,48) == 1)
    # assert(gcd(1,1) == 1)
    # assert(gcd(0,0) == 0)
    print("All test cases pass")



# main program to run test

test_gcd()