# coding=utf-8
import os
import jieba
import time
import threading

# 目前cpu利用率仅占120%

#往文件写要加这个
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

threads = [] # 线程池

def thread(file, write_path):
    print(file + ':processing......')
    start_each = time.clock()
    with open(write_path, 'a+') as wf:
        with open(file) as rf:

            for line in rf:
                if line.startswith('</doc>') or line.startswith('<doc>'):
                    continue
                seg_list = jieba.cut(line)
                list = []
                for word in seg_list:
                    if (not word.__eq__(' ')) and (not word.__eq__('　') and (not word.__eq__('\t'))):
                        list.append(word)
                wf.write(' '.join(list))
        end_each = time.clock()
        print(file + ":用时{0}s".format(end_each - start_each))

# 将文件夹下所有的文件分词并写出到一个文件里
def run(file_document_path,write_path):
    # 在linux中地址不用转码的
    # file_document_path = unicode(file_document_path, "utf8")
    # write_path = unicode(write_path, "utf8")
    start = time.clock()

    file_list = os.listdir(file_document_path)
    for file in file_list:
        # print file.decode('gbk')  # window
        # print file  # linux
        # 多线程

        threads.append(threading.Thread(target=thread, args=(file_document_path+file, write_path+file)))

    for t in threads:
        t.setDaemon(True)  # 将线程声明为守护线程，必须在start()调用之前设置，不设置将会无限挂起
        t.start()
    threads.join()  # 在子线程完成之前父线程会已知阻塞，防止提前结束

    end  = time.clock()
    print("共用时{0}s".format(end-start))
    pass



if __name__ == '__main__':

    ## windows
    # run('D:/NLP/语料/sogouT/test/','D:/NLP/语料/sogouT/test.merge')

    ## linux
    run('/home/guanpf/语料/sogouT/test/','/home/guanpf/语料/sogouT/segment/')
