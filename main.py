import inspect


def introspection_info(obj):
    return obj


number_info = introspection_info(42)
print(number_info)

some_function_module = inspect.getmodule(introspection_info)

info = {'type': type(number_info),
        'attributes': dir(number_info),
        'module': some_function_module.__name__}
print(info)

for attr_name in dir(number_info):
    attr = getattr(number_info, attr_name)
    print(attr_name, type(attr))