# def print_kwargs(name, power):
#     print("Name ", name, "Power: ", power)

def print_kwargs(**kwargs):
    # print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "shaktiman", power = "lazer")
print_kwargs(name = "shaktiman")
print_kwargs(name="shaktiman", power = "lazer", enemy = "Dr. Jackaal")