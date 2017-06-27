#coding=utf-8
# 按照doc的编号的截取文件
# 写这个的主要目的是为了检查程序为什么会停很久
import time

#往文件写要加这个
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def count(file_path):
    """
    计算文件中网页格式
    :param file_path:文件路径
    :return: 返回个数
    """
    start_time = time.clock()
    doc_num = 0
    rows = 0
    row_below_500 = 0
    row_below_1000 = 0
    row_below_5000 = 0
    row_below_10000 = 0
    row_below_20000 = 0
    row_below_50000 = 0
    row_below_80000 = 0
    row_below_100000 = 0
    row_below_200000 = 0
    row_below_300000 = 0
    row_below_400000 = 0
    row_more_400000 = 0
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
            rows += 1
            if line.startswith('<doc>'):
                doc_num += 1
                if (doc_num % 1000) == 0:
                    print('已经处理了:{0}个文件，已用时{1}s'.format(doc_num, (time.clock() - start_time)))
            # 统计行数
            if line.startswith('</doc>'):
                if rows < 500:
                    row_below_500 += 1
                elif rows < 1000:
                    row_below_1000 += 1
                elif rows < 5000:
                    row_below_5000 += 1
                elif rows < 10000:
                    row_below_10000 += 1
                elif rows < 20000:
                    row_below_20000 += 1
                elif rows < 50000:
                    row_below_50000 += 1
                elif rows < 80000:
                    row_below_80000 += 1
                elif rows < 100000:
                    row_below_100000 += 1
                elif rows < 200000:
                    row_below_200000 += 1
                elif rows < 300000:
                    row_below_300000 += 1
                elif rows < 400000:
                    row_below_400000 += 1
                else:
                    row_more_400000 += 1

                rows = 0

    print 'row_below_500 =', row_below_500
    print 'row_below_1000 = ',row_below_1000
    print 'row_below_5000 = ',row_below_5000
    print 'row_below_10000 = ',row_below_10000
    print 'row_below_20000 = ',row_below_20000
    print 'row_below_50000 = ',row_below_50000
    print 'row_below_80000 = ',row_below_80000
    print 'row_below_100000 = ',row_below_100000
    print 'row_below_200000 = ',row_below_200000
    print 'row_below_300000 = ',row_below_300000
    print 'row_below_400000 = ',row_below_400000
    print 'row_more_400000 = ',row_more_400000

count('/home/guanpf/语料/sogouT/pages.241')