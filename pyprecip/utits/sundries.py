from .except_ import RaiseException as exc 

def check_param_type(value, expected_type, param_name):
    """
    检查参数的类型是否与期望的类型匹配。

    参数:
        value (any):要检查的参数值。
        expected_type (type或tuple of types):期望的类型或允许的类型的元组。
        param_name (str):参数名。

    提出了:
        TypeError:如果“value”的类型与“expected_type”不匹配。
    """

    if not isinstance(value, expected_type):
        if isinstance(expected_type, tuple):
            type_names = [t.__name__ for t in expected_type]
            expected_type_str = ' or '.join(type_names)
        else:
            expected_type_str = expected_type.__name__
        
        exc.raise_exception(f"{param_name} parameter must be of type {expected_type_str}.", TypeError)


if __name__ == "__main__": 
    # test 
    tuple1 = (1,2,3)
    expected_type = (str, int)
    check_param_type(tuple1, expected_type, "value1")