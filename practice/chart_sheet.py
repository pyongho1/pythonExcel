from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(["Day", "Revenue", "Customer"])

wb.save("test.xlsx")