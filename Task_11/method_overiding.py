#parent class
class Father():
    def transport(self):
        print("The transport used is a car")

#subclass
class Son(Father):
    #pass
    def transport(self):
        print("The transport used is a bike")
        #pass

son_1 = Son()
# this will call the transport method from the parent class
son_1.transport()