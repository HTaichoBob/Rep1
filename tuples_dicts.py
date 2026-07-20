
months = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

print("First month:", months[0])
print("Last month:", months[-1])


try:
    months[0] = "NewMonth"
except TypeError as e:
    print(f"Tuples are immutable, error: {e}")


students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92,
    "Diana": 88
}


students["Evan"] = 79
print("\nAfter adding Evan:")
print(students)


students["Bob"] = 95
print("\nUpdated Bob's grade:")
print("Bob:", students["Bob"])


print("\nStudent Grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")
