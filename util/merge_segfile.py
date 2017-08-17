# coding=utf-8
import os
import platform

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

    file_list = os.listdir(file_document_path)
    with open(write_path,'a+') as wf:
        for file in file_list:
            # print file.decode('gbk')  # window
            # print file  # linux
            print(file+':processing......')
            with open(file_document_path+file) as rf:
                for line in rf:
                    wf.write(line)

            ##############################################
            os.remove(file_document_path+file) # 因为占空间删除
            ##################################################
    pass

def list_file(path):
    file_list = os.listdir(path)

if __name__ == '__main__':
    ## windows
    # run('D:/NLP/语料/sogouT/test/','D:/NLP/语料/sogouT/test.merge')

    ## linux
    run('/home/guanpf/语料/sogouT/segment/','/home/guanpf/语料/sogouT/corpus.all_all')