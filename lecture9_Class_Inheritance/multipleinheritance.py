# inporting time module
import time
class Printer:
    def start_print(self):
        # simulating the printer starting, computer is waiting for the printer to start
        time.sleep(1)
        for i in range (3):
            print(f"printing page {i+1} .......")
            time.sleep(1)
        print("printing complete")

printer= Printer()
printer.start_print()

# creating a scanner class
class Scanner:
    def start_scan(self):
        # simulating the scanner starting, computer is waiting for the scanner to start
        time.sleep(1)
        for i in range (3):
            print(f"scanning page {i+1}.......")
            time.sleep(1)
        print("scanning complete")

class ModernPrinter(Printer, Scanner):
    def print_and_scan(self):
        self.start_print()
        self.start_scan()

New_Printer = ModernPrinter()
New_Printer.print_and_scan()

class Printer2:
    def __init__(self, pages_left) -> None:
        self.pages_left = pages_left

    def start_print(self):
        # simulating the printer starting, computer is waiting for the printer to start
        time.sleep(1)
        for i in range (3):
            print(f"printing page {i+1} .......")
            time.sleep(1)
        print("printing complete")

# creating a scanner class
class Scanner2:
    def __init__(self, pages_scanned) -> None:
        self.pages_scanned = pages_scanned

    def start_scan(self):
        # simulating the scanner starting, computer is waiting for the scanner to start
        time.sleep(1)
        for i in range (3):
            print(f"scanning page {i+1}.......")
            time.sleep(1)
        print("scanning complete")

class ModernPrinter2(Printer2, Scanner2):

    def __init__(self, pages_left, pages_scanned) -> None:
        # only one of the __init__ methods is called using super()
        #super() is used to call the __init__ method of the parent class, automatically gets the pages_left attribute and self
        super().__init__(pages_left)
        # need to use scanner.__init__ to call the __init__ method of the scanner class defining the pages_scanned attribute
        Scanner2.__init__(self, pages_scanned)


    def print_and_scan(self):
        self.start_print()
        self.start_scan()

New_Printer = ModernPrinter2(500, 1000)
New_Printer.print_and_scan()
print(New_Printer.pages_left)
print(New_Printer.pages_scanned)