#coding=utf-8
import jieba
import jieba.posseg as pos
import time

#往文件写要加这个
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# def test():
#     # seg_list = jieba.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")
#     seg_list = jieba.cut("工信处女   干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")
#     list = []
#     for word in seg_list:
#         if not word.__eq__(' '):
#             list.append(word)
#     print ' '.join(list)
#
#     pos_list = pos.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")
#     for word,flag in pos_list:
#         print('{0}/{1}'.format(word,flag))

def run(read_path, write_path):
    start = time.clock()  # 开始时间
    rows = 0   # 记录doc中的行数

    # 在linux中地址不用转码
    read_path = unicode(read_path, "utf8")
    write_path = unicode(write_path, "utf8")

    with open(write_path, 'a+') as wf:
        with open(read_path, 'rb') as f:
            for line in f:
                rows += 1
                if (rows % 1000) == 0:
                    print('已经处理了:{0}行，已用时{1}s'.format(rows,(time.clock()-start)))
                if line.startswith('</doc>') or line.startswith('<doc>'):
                    continue
                seg_list = jieba.cut(line)
                list = []
                for word in seg_list:
                    if (not word.__eq__(' ')) and (not word.__eq__('　') and (not word.__eq__('\t'))):
                        list.append(word)
                wf.write(' '.join(list))

    # 结束时间
    end = time.clock()
    print('程序结束，共用时：{0}'.format(end - start))

if __name__ == '__main__':
    # run('D:/NLP/语料/sogouT/pages.241.clear_50','D:/NLP/语料/sogouT/segment/sogouT.seg')
    run('H:/SogouT/pages.288/pages.288.clear_50_10000','D:/NLP/语料/sogouT/segment/sogouT288.seg')
    # test()
