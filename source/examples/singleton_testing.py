class NoInstancesAllowed:
    def __init__(self):
        raise NotImplementedError("This class cannot be instantiated.")

    @classmethod
    def create_instance(cls):
        return cls()

# Attempt to instantiate the class
# try:
#     obj = NoInstancesAllowed()
# except NotImplementedError as e:
#     print(e)  # Output: This class cannot be instantiated.

# Create an instance using the class method
obj = NoInstancesAllowed.create_instance()
print(obj)  # Output: <__main__.NoInstancesAllowed object at 0x...>
