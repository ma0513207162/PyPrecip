

def test_unit_func(num = 11):
    if num < 1:
        return; 
    elif num == 1:
        return 1
    else:
        return num * test_unit_func(num-1) 











