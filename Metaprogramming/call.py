class Test:
    def __call__(self):
        print("ok")
    def __contains__(self, valeur):
        return True
print( 2 in [1,2])
test = Test()
test()
test.__call__()
print( "a" in test)

def function():
    print("ok")
function.
print("end")