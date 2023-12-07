################### Scope ####################

enemies = 1#global scope

def increase_enemies():
  enemies = 2#local scope
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")