import 清理授权模块
import configparser

配置文件 = configparser.ConfigParser()
配置文件.read('配置文件.ini', encoding='utf-8')

清理授权模块.清理授权(配置文件.get('目录', 'steam根目录'))

input("按下 enter 键退出...\n")
