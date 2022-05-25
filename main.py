import library as lb


wb = lb.open_file('./test.xlsx')
row_value = lb.read_file(wb, 'Arkusz1', 'B', 5, 10)
print(row_value)
