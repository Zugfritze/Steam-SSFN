import os


def 清理授权(参数steam根目录):
    if os.path.isfile(参数steam根目录 + "\\steam.exe"):  # 检查是不是正确的steam根目录
        # 清理ssfn
        序列 = os.listdir(参数steam根目录)  # 定义变量，文件夹下文件序列
        ssfn序列 = [i for i in 序列 if 'ssfn' in i]  # 找出序列中含ssfn的元素，组成新的序列
        for m in ssfn序列:  # 循环出新序列中的元素
            os.remove(os.path.join(参数steam根目录 + "\\" + m))  # 删除新序列中元素的文件，指定文件路径
        # 清理config.vdf
        if os.path.isfile(参数steam根目录 + "\\config\\config.vdf"):
            os.remove(os.path.join(参数steam根目录 + "\\config\\config.vdf"))
        # 检查是否清理成功
        检查序列 = os.listdir(参数steam根目录)
        if "ssfn" in 检查序列:
            print("清理失败请自行删除\n" + 参数steam根目录 + "\\" + "\n下的ssfn文件和\n"
                  + 参数steam根目录 + "\\config\\" + "\n下的config.vdf")
        else:
            print("清理完成")

    else:  # 如果不是正确的steam根目录
        print("steam根目录错误请检查：配置文件.ini")
