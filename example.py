# coding=utf-8

from table import Table

table = Table(rowNames = ["1", "2", "3"], columnNames=["a", "b", "c"], matrix=[[1, 2, 3], [3, 4, 5], [5, 6, 7]])

print("Whole table:")
print(table)

print("Just a cell:")
print(table["1", "a"])

print("A row:")
print(table["2", :])

print("A column:")
print(table[:, "b"])

print("A range:")
print(table["2":, :])
print("Second range:")
print(table[:, "b":])

print("Add an empty row")
print(table.addRow())
print(table)

print("Add a row with values")
print(table.addRow(i=2, values=(9,8,7)))
print(table)

print("Add an empty column")
print(table.addColumn())
print(table)

print("Add a column with values")
print(table.addColumn(i=2, values=(9,8,7,6,5)))
print(table)


