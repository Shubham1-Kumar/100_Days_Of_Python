from prettytable import PrettyTable

table = PrettyTable()
table.field_names=["Pokemon Name","Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirrel","Water"])
table.add_row(["Charmane","Fire"])
table.align = "l"
print(table.align)

table.add_column("Character",["A","B","C"])
print(table)