#coding=utf-8

#文件去重
#1.最容易重复的是与本doc内的重复
#2.然后是文章之间的重复
#采用最笨的方法  逐行比较
def re_repeat(read_file, write_file):
    with open(write_file,'a+') as wf:
        with open(read_file) as  rf:
            for line_rf in rf:
                print '#################################################'
                flag = False
                with open(write_file,'r') as r_wf:
                    for line_wf in r_wf:
                        print 'rf',line_rf
                        print 'wf',line_wf
                        if line_rf.__eq__(line_wf):
                            print 'break'
                            flag = True
                            break
                    if not flag:
                        wf.write(line_rf)
                    r_wf.close()

if __name__ == '__main__':
    re_repeat('d:/repeat.txt','d:/re_repeat.txt')
