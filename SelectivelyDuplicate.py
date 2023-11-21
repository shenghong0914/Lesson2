import os
import shutil

# 指定原始資料夾路徑
source_folder = 'C:/Users/PearlWu/Documents/PythonProject/Projects100/LV2/OperateFiles/SelectivelyDuplicate/projects'

# 指定目標資料夾路徑
destination_folder = 'C:/Users/PearlWu/Documents/PythonProject/Projects100/LV2/OperateFiles/SelectivelyDuplicate/convert_projects'

# 檢查目標資料夾是否存在，如果不存在就創建它
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 列出原始資料夾中的子資料夾並進行處理
for foldername in os.listdir(source_folder):
    if 'convert' in foldername.lower():
        # 組合原始子資料夾的完整路徑
        source_subfolder = os.path.join(source_folder, foldername)

        # 組合目標子資料夾的完整路徑
        destination_subfolder = os.path.join(destination_folder, foldername)
            
        # 複製子資料夾及其內容到目標資料夾
        shutil.copytree(source_subfolder, destination_subfolder)
