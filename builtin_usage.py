import math
import random
import platform

random_number = random.randint(1, 100)
print("Random Number:", random_number)

squarert_value = math.sqrt(random_number)
squarert_floored = math.floor(squarert_value)
print("Square Root (floored):", squarert_floored)


os_name = platform.system()
python_version = platform.python_version()

print("Operating System:", os_name)
print("Python Version:", python_version)
