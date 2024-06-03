def add_numbers(a, b):
    return a + b

def test_add_numbers(self):
    # arrange 
    a = 10
    b = 20
    #act
    result = add_numbers(a, b)
    #assert
    self.assertEqual(result, 30)