# coding=utf-8
import os

def run(file_document_path):
    file_list = os.listdir(file_document_path)
    for file in file_list:
        # print file.decode('gbk')  # window
        print file
        # with open(file) as f:


    pass

def list_file(path):
    file_list = os.listdir(path)





if __name__ == '__main__':
    ## windows
    # run('d:/')

    ## linux
    run('/home')