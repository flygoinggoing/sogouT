#coding=utf-8
# 按照doc的编号的截取文件
# 写这个的主要目的是为了检查程序为什么会停很久
# 切完用nodepad打开查找全部的doc 看第几个文件占的行数多

import time

#往文件写要加这个
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def cut(file_path,out_path,start,end):
    """
    计算文件中网页格式
    :param file_path:文件路径
    :return: 返回个数
    """
    start_time = time.clock()
    num = 0
    with open(out_path+'.'+str(start)+'_'+str(end),'a+') as wf:
        with open(file_path, 'rb') as f:
            for line in f:
                try:
                    line = line.decode('utf-8')
                except:
                    try:
                        line = line.decode('gbk')
                    except:
                        try:
                            line = line.decode('iso-8859-1')
                        except:
                            continue
                if line.startswith('<doc>'):
                    num += 1
                    if (num % 1000) == 0:
                        print('已经处理了:{0}个文件，已用时{1}s'.format(num, (time.clock() - start_time)))
                if num >= start and num <= end:
                    wf.write(line)
                    print('输出文件为{0}：'.format(num))
                if num > end:
                    break

cut('h:/SogouT/pages.241/pages.241','h:/SogouT/pages.241/pages.241.cut',1423600,1423700)