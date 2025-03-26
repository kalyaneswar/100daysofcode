# Scope
# Local and Global scope

count = 1

def increase_count():
    # Local scope
    count =2 
    print(f"Now the count is {count}")

increase_count()
print(f"Now the count is {count}")
