# coding=utf-8
import os
import jieba
import time
import multiprocessing
import platform

# 多进程

#往文件写要加这个
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def process(file, write_path):
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

    # 运行环境判断是否对路径转码(windows有中文要转码)
    system_path = platform.system()
    if system_path.__eq__('Windows'):
        print ("运行环境为Windows")
        # 在Windows中地址中含有中文要转码的
        file_document_path = unicode(file_document_path, "utf8")
        write_path = unicode(write_path, "utf8")
    elif system_path.__eq__('Linux'):
        print ("运行环境为Linux")

    procss_pool = multiprocessing.Pool(processes = 9) # 进程池声明要放在里边,物理核数不够时有几个可用就用几个

    start = time.clock()

    file_list = os.listdir(file_document_path)
    for file in file_list:
        # 多进程

        # 手动添加
        # procss.append(multiprocessing.Process(target=thread, args=(file_document_path+file, write_path+file)))

        # 进程池添加
        procss_pool.apply_async(process, (file_document_path+file, write_path+file, ))

    procss_pool.close()  # 不在接受进程，调用join之前，先调用close函数，否则会出错
    procss_pool.join()  # 在子进程完成之前父进程阻塞，防止提前结束

    end  = time.clock()
    print("共用时{0}s".format(end-start))
    pass



if __name__ == '__main__':

    ## windows
    run('h:/SogouT/测试/','h:/SogouT/testseg/')

    ## linux
    # run('/home/guanpf/语料/sogouT/corpus/','/home/guanpf/语料/sogouT/segment/')