#coding=utf-8

def find(file_path):
    """
    计算文件中网页格式
    :param file_path:文件路径
    :return: 返回个数
    """
    num = 0
    with open(file_path, 'rb') as f:
        for line in f:
            if line.startswith('<doc>'):
                num += 1
            if line.__contains__('眼迷离间的魅力'):
                break
            if line.__contains__('浙江宏达松下数码相机价格_泡泡经销商'):
                break
        print('文件中网页的个数为{0}'.format(num))
    return num

find('h:/SogouT/pages.241/pages.241')