import lb_file as lf


wb = lf.open_file('./test.xlsx')
ws = lf.open_sheet(wb, 'Arkusz1')
value_list = lf.read_file(ws, 'B', 4 ,11 )
lf.write_file(ws, 3, 'C', 4, value_list)
lf.save_file(wb, 'test.xlsx')
print(value_list)
