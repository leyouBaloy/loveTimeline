import os
# import re

# allpath = []


def getallfile(path):
    file_path = os.listdir(path)
    # 遍历该文件夹下的所有目录或者文件
    for file in file_path:
        fp = os.path.join(path, file)
        # 如果是文件夹
        if os.path.isdir(fp):
            print(file)
            paths = []
            for name in os.listdir(fp):
                paths.append({"src": os.path.join(fp, name).replace('\\', '/').replace("D:/GitHub/JSwcnm/Timeline/",""),
                       "thumb": os.path.join(fp, name).replace('\\', '/').replace("D:/GitHub/JSwcnm/Timeline/","")})
            print(paths,"\n")


path = 'D:\GitHub\JSwcnm\loveTimeline\images'
getallfile(path)
# print(allpath)
