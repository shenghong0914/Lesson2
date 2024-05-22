# 從Python標準函式庫中引入操作系統相關功能的模組
import os

# 設定存放檔案的資料夾路徑
folder_path = 'C:\Users\hankw\OneDrive\桌面\python_code\Lesson2\images'

# 列出資料夾中的檔案並進行批次處理
for filename in os.listdir(folder_path):
    #從檔名中擷取需要的部分，此處以 "o_" 為分隔字串
    #取第2部分作為新的檔名
    #加上前綴字串"Rename_"
    new_filename = "rename_" + filename.split("o_")[1]
    # 使用 os.rename() 函式進行檔案重新命名
    os.rename(f"{folder_path}\\{filename}", f"{folder_path}\\{new_filename}")

# 批次處理完成
print("已完成。")





