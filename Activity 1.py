class Myclass:



    __privatevar = 27

    def __privMeth(self):
        print("I am inside class Myclass")


    def hello(self):
        print(f"Variable value is {Myclass.__privatevar}")

foo = Myclass()
foo.hello()
foo.__privatevar
