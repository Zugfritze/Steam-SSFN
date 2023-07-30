import os

def 清理授权(参数steam根目录: str) -> None:
    if os.path.isfile(os.path.join(参数steam根目录, 'steam.exe')):
        # 清理ssfn
        ssfn序列: list[str] = [i for i in os.listdir(参数steam根目录) if 'ssfn' in i]
        for ssfn in ssfn序列:
            os.remove(os.path.join(参数steam根目录, ssfn))
        # 清理config
        config路径: str = os.path.join(参数steam根目录, 'config', 'config.vdf')
        if os.path.isfile(config路径):
            os.remove(config路径)
        # 检查是否清理成功
        检查序列: list[str] = os.listdir(参数steam根目录)
        if "ssfn" in 检查序列:
            print(f"清理失败请自行删除{参数steam根目录}下的ssfn文件和{config路径}文件")
        else:
            print("清理完成")
    else:
        print("steam根目录错误请检查配置文件.ini")
