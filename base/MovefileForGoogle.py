import os
import shutil

path = 'D:/xampp/zentao/tmp/backup/'
obj_path = r'C:\tmp\try'


def copyFiles(path):
    for dir_path, dir_names, file_names in os.walk(path):
        print('目前路徑：', dir_path)
        if len(dir_names) != 0:
            print('子目錄：', dir_names)
        else:
            print('沒有東西呢！')
        if len(file_names) != 0:
            print('檔案：', file_names)
        else:
            print('沒有東西哦！')
    for i in file_names:
        print('完整的檔案路徑：', os.path.join(dir_path, i))


# def copy(path, obj_path):
#     i = 0
#     # 遍歷path路徑下，所有檔案的根目錄，檔名，檔名加副檔名
#     for root, dirpath, filename in os.walk(path):
#         # 獲取每個filename列表的長度，即每個filaname資料夾所含的檔案個數
#         for index in range(len(filename)):
#             # 如果filename中的檔名第21位到最後的名稱是seg.nii.gz，繼續執行
#             if filename[index][21:] == 'seg.nii.gz':
#                 i += 1
#                 # 獲取你想要copy的檔案，帶副檔名的完整路徑
#                 old_path = os.path.join(root, filename[index])
#                 # 獲取你想要copy到的路徑，此處路徑依舊是檔案的完整路徑，即絕對路徑
#                 new_path = os.path.join(obj_path + '/' + filename[index][:20], filename[index])
#                 # shutil.copy將檔案複製到目標資料夾，如果目標資料夾已有該檔案會覆蓋
#                 # shutil.copyfile跟copy用法相同，但如果目標資料夾已有該檔案會報錯
#                 shutil.copy(old_path, new_path)
#     print('There have', i, 'seg file')

if __name__ == '__main__':
    copyFiles(path)
