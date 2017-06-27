# coding=utf-8
import os

def run(file_document_path,write_path):
    # 在linux中地址不用转码的
    file_document_path = unicode(file_document_path, "utf8")
    write_path = unicode(write_path, "utf8")

    file_list = os.listdir(file_document_path)
    with open(write_path,'a+') as wf:
        for file in file_list:
            # print file.decode('gbk')  # window
            # print file  # linux
            print(file+':processing......')
            with open(file_document_path+file) as rf:
                for line in rf:
                    wf.write(line)
    pass

def list_file(path):
    file_list = os.listdir(path)





if __name__ == '__main__':
    ## windows
    run('D:/NLP/语料/sogouT/test/','D:/NLP/语料/sogouT/test.merge')

    ## linux
    # run('/home/guanpf/语料/sogouT/segment/',/home/guanpf/语料/sogouT/segment/corpus.all)