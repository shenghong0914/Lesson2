import os
import shutil

# 指定原始資料夾路徑
source_folder = r'C:\Users\PearlWu\Documents\PythonProject\Projects100\LV2\OperateFiles\SelectivelyMove\projects'

# 指定目標資料夾路徑
destination_folder = r'C:\Users\PearlWu\Documents\PythonProject\Projects100\LV2\OperateFiles\SelectivelyMove\requirements'

# 確保目標資料夾存在，如果不存在就創建它
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# 遍歷原始資料夾以尋找檔名為"requirements"檔案
for root, dirs, files in os.walk(source_folder):
    # root：目前資料夾的路徑
    # dirs：目前資料夾中的子資料夾列表
    # files：目前資料夾中的檔案列表
    # （root, dirs, files） 會在每次迴圈中提供一個新資料夾的資訊

    for file in files:
        if file == 'requirements.txt':            
            # 組合原始檔案的完整路徑
            source_subfolder = os.path.join(root, file)
            # 組合目標子資料夾的完整路徑
            destination_subfolder = os.path.join(destination_folder, root.split("projects\\")[1]+"_"+file)
            # 移動檔案到目標資料夾
            shutil.move(source_subfolder, destination_subfolder)


