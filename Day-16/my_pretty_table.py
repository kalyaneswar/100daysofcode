from prettytable import PrettyTable

# pip install prettytable

Table = PrettyTable()
print(Table)

Table.add_column("Pokemon Name", ["Pikkachu", "Squitare"])
Table.add_column("type", ["fire", "water"])
print(Table)