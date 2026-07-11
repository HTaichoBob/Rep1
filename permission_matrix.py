Read = 4
Write = 2
Execute = 1

full_permission = 3

print("Permission Matrix:")

if (full_permission & Write) == Write:
    print("Write permission granted.")
else:
    print("Write permission denied.")




