import os
dir_name = input("请输入批量重命名的文件夹名字")
files = os.listdir(dir_name) #列表
os .chdir(dir_name)
for i in files:
	position = i.rfind(".")
	newname = i[:position]+"-腾讯"+i[position:]
	os.rename(i,newname)
