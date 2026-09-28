customer_name = input("What is you name? ")

customer_age = int(input("What is your age? "))

is_active = input("Is active True or False? ")

print(customer_name, customer_age, is_active)
print(customer_age + 1)

customer_names = [
    "Joseph",
    "Joey",
    "Sarah"
]
print(customer_names[0])
print(customer_names[2])

customer_names.append("Mike")
print(customer_names)

customer_names.remove("Joey")
print(customer_names)

customer_names[1] = "Sara"
print(customer_names)

customer = {
    "name": "Joseph",
    "age": 40,

}
print(customer["name"])

customer["age"] = 41

print(customer)

customer["age"] = 25

if customer["age"] >= 65:
    print("Old Man")

elif customer["age"] >= 18:
    print("Old Enough")

else:
    print("Minor customer")

for name in customer_names:
    print(name)

for name in customer_names:
    if name == "Mike":
        print("Mike found")

def greet(name):
    print("Hello", name)
greet("Joseph")

def add_one(number):
    return number + 1
result = add_one(40)
print(result)

count = 1 
while count <= 3:
    print(count)
    count = count + 1

while True:
    print("Running")
    break

while True:
    choice = input("Type exit to quit: ")

    if choice == "exit":
        break 