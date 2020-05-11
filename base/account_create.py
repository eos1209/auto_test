from openpyxl import load_workbook


# 先利用CreateFile function創建跟example.xlsx檔同樣格式的檔案,再將Data寫入


# def CreateFile(): # Create same type xlsl file
#     for i in range(1, 3):
#         wb = load_workbook('../test_data/document/AccountExaple.xlsx')
#         wb.save(f'../test_data/accountcreate/AccountExaple{i}.xlsx')


def WriteData():
    account = 'QA_YT'
    nums_start = 0
    One_time_num = 200000

    for times in range(1, 3):
        save_path = f'./AccountCreate/accounttest{times}.xlsx'
        wb = load_workbook(save_path)
        ws = wb.active

        for index, num in enumerate(range(nums_start, nums_start + One_time_num), 1):
            ws[f'A{index + 1}'] = 'QAtwo_million_A'
            ws[f'B{index + 1}'] = 'QAtwo_million_B'
            ws[f'C{index + 1}'] = 'QAtwo_million_C'
            ws[f'D{index + 1}'] = 'QAtwo_million_D'
            ws[f'E{index + 1}'] = account + str(num + 1).zfill(10)
            ws[f'F{index + 1}'] = 'a123456'
            ws[f'G{index + 1}'] = 'a123456'

            ws[f'H{index + 1}'] = '王小明'
            ws[f'I{index + 1}'] = '1234567890'
            ws[f'J{index + 1}'] = 'example1@qq.com'
            ws[f'K{index + 1}'] = '1234567890'
            ws[f'L{index + 1}'] = '0'
            ws[f'M{index + 1}'] = '是'

            ws[f'N{index + 1}'] = '是'
            ws[f'O{index + 1}'] = '2000/01/01'
            ws[f'P{index + 1}'] = 'exampleweixin1'
            ws[f'Q{index + 1}'] = '建设银行'
            ws[f'R{index + 1}'] = '山西省'
            ws[f'S{index + 1}'] = '太原市'
            ws[f'T{index + 1}'] = '99876543210'
            ws[f'U{index + 1}'] = '帐号备注1'

        wb.save(save_path)
        nums_start = nums_start + One_time_num


# CreateFile()
WriteData()
