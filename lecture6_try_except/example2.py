try:
    var_one = int(input("Enter a number of muffins stollen : "))
    print(f"you have stollen {var_one} muffins")
except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
except NameError as e:
    print(f"Error: {e}")


#example 2
while True:
        try:
            var_two = int(input("Enter a number of muffins you want to order : "))
            if var_two > 1:
                print(f"you have ordered {var_two} muffins")
            else:
                print(f"you have ordered {var_two} muffin")
            break
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")
        except NameError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt as e:
            print(f"Error: {e}")
        except EOFError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("This is the end of the try and except block")