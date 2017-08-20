#coding=utf-8
# 按照行号的编号的截取文件
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
                num += 1
                if (num % 1000000) == 0:
                    print('已经处理了:{0}行，已用时{1}s'.format(num, (time.clock() - start_time)))
                if num >= start and num <= end:
                    wf.write(line)
                elif num > end:
                    break

cut('/home/guanpf/word2vec/w2v/trunk/train/corpus.all_all','/home/guanpf/word2vec/w2v/trunk/train/corpus',1,978788633)