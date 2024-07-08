def singleton(cls):
    instance = {}
    def get_instance():
        if cls not in instance:
            instance[cls] = cls()
        return instance[cls]
    return get_instance

@singleton
class MyClass:
    pass

