import os

dir_path = 'E:\code\\test文件夹'

ret = []

def searchTargetFile(path:str, target='.htm'):
    """
    递归路径path下文件，找出以target为后缀的文件，并追加到列表ret中
    :param path: 需递归的文件路劲
    :param target: 目标后缀
    :return: 文件路劲数组
    """
    # ret = [] # ret空列表必须在函数外定义，否则每次递归都会创建一个仅在本次调用内生效的空列表

    dir_files = os.listdir(path)
    for point in dir_files:
        pointcut = os.path.join(path, point)
        if os.path.isfile(pointcut) and os.path.splitext(pointcut)[1] == target:
            ret.append(pointcut)
        if os.path.isdir(pointcut):
            searchTargetFile(pointcut)
    return ret




def alterFileSuffix(path: str, target='.htm', suffix='.html'):
    """
    递归路径path，找到以target为后缀的文件，并修改其文件后缀为suffix
    :param path: 文件路径
    :param target: 需修改的文件后缀
    :param suffix: 修改后的文件后缀
    :return: None
    """
    dir_files = os.listdir(path)
    for point in dir_files:
        # pointcut = os.path.abspath(point) # 使用绝对路径不成修改成功，原因？
        pointcut = os.path.join(path, point)
        if os.path.isfile(pointcut) and os.path.splitext(pointcut)[1] == target:
            os.rename(pointcut, os.path.splitext(pointcut)[0] + suffix)
        if os.path.isdir(pointcut):
            alterFileSuffix(pointcut)

    return

# alterFileSuffix(dir_path)

print(searchTargetFile(dir_path))