#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
word_count = 0
dict_count = {}
line_num =0
error_num = 0

start_time = time.clock()
temp1_time = time.clock()
temp2_time = 0.0
try:
    #with open('/home/guanpf/word2vec/w2v/trunk/train/corpus.all_all','r') as f:
    with open('/home/guanpf/word2vec/w2v/trunk/train/corpus.1_978788633', 'r') as f:
        for line in f:
            line_num = line_num+1
            if line_num%1000000 == 0:
                temp2_time=temp1_time
                temp1_time=time.clock()
                print line_num,'本次用时：',(temp1_time-temp2_time),'s,共用时：',(temp1_time-start_time)/60,'min'
            # line = line.decode('gbk')
            # print line
            for word in line.strip().split(' '):
                word_count = word_count+1
                if word in dict_count:
                    dict_count[word] = dict_count[word]+1
                else:
                    try:
                       dict_count[word] = 1   # 内存小时会MemoryError
                    except:
                        print '####error###',line_num
                        error_num = error_num+1
                        with open('/home/guanpf/vocab_error{}.txt'.format(error_num), 'a+') as fout:
                            list = sorted(dict_count.items(), key=lambda item: item[1])
                            for word, num in list:
                                fout.write('{}\t{}\t{}\n'.format(word, num, (num * 1.0) / word_count))
                        dict_count.clear()
                        word_count = 0
                        dict_count[word] = 1
except:
    error_num=error_num+1
finally:
    print 'error_num:',error_num
    print 'word_count',word_count
    print 'line_num',line_num
    print '共用时：',(time.clock()-start_time)/3600,'h'
    with open('/home/guanpf/vocab.txt','a+') as fout:
        list = sorted(dict_count.items(),key=lambda item:item[1])
        for word,num in list:
            fout.write('{}\t{}\t{}\n'.format(word,num,(num*1.0)/word_count))
    print '结束'
# line = '我 斯蒂芬 阿 阿哈 赛 a a'
# for word in line.split(' '):
#     word_count = word_count + 1
#     if word in dict_count:
#         dict_count[word] = dict_count[word] + 1
#     else:
#         dict_count[word] = 1
# print dict_count,word_count
#
# list = sorted(dict_count.items(),key=lambda item:item[1])
# for word,num in list:
#     # fout.write(word+'\t'+num+'\t'+num/word_count)
#     print word,'\t',num,'\t',(num*1.0)/word_count