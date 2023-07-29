class Singleton:
    # class variable __instance will keep track of the lone object instance
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Singleton object already created!")
        else:
            Singleton.__instance = self

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance


s1 = Singleton.getInstance()
print(s1)
s2 = Singleton.getInstance()
print(s2)

# if we set an attribute on s1, s2 will have the same value because they
# both refer to the same object
s1.x = 5
print(s2.x)

s3 = Singleton()
if id(s3) == id(s1):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")