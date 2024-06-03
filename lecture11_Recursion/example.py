def recursive_function(input):
    # base case
    if base_condition (input):
        #return the base result directly
        return base_result
    # recursive case
    else:
        # modify the input and make a recursive call
        modifies_input = modify_input(input)
        recursive_result = recursive_function(modifies_input)

        # process the recursive result
        result = process_result(recursive_result)
        return result