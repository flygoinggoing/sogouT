#coding=utf-8
import re
import time

#往文件写要加这个
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 将字符串连接操作 由 “+” 改为   [].append()  然后‘’。jion（[]）
# 加入简单的去重，以doc为基本单元
def run(read_path, limit_sent_length, limit_doc_row = 10000):
    """
    抽取的主程序
    :param read_path: 欲抽取文件路径，输出文件在同路径下
    :param limit_sent_length:限制句子的长度，大于限制长度的句子才会被抽出
    :param limit_doc_row:限定文件的行数，和运行效率有关（一般设置为10000）
    :return:
    """
    start = time.clock()  # 开始时间
    doc_num = 0    # 记录处理的doc数
    rows = 0   # 记录doc中的行数
    write_path = read_path + '.clear_' + str(limit_sent_length) + '_' + str(limit_doc_row)  # 初始化输出文件路径

    with open(write_path, 'a+') as wf:
        with open(read_path, 'rb') as f:
            doc = []   # 存每一个doc的内容
            for line in f:
                # 转码，因为文件内的编码不一致
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

                line = line.strip()  # 去除首尾的空格tab回车换行
                # print line,
                # 去除空行 和 无用标签
                if line.__eq__('') or line.startswith('<docno>') or line.startswith('<url>'):
                    continue

                rows += 1
                # doc += line  # 慢
                doc.append(line)
                if line.__eq__('</doc>'):

                    # 显示过程（此处的doc_num是未经删减的）
                    doc_num += 1
                    if (doc_num % 1000) == 0:
                        print('已经处理了:{0}个文件，已用时{1}s'.format(doc_num,(time.clock()-start)))

                    # 如果文件的行数大于limit_doc_row，处理时间太长，则直接舍去
                    if rows > limit_doc_row:
                        doc = []
                        rows = 0
                        continue

                    out_doc = []
                    s = extract_str(''.join(doc))
                    for l in s:
                        l = replaceCharEntity(l)#替换实体
                        l = filter_str(l, limit_sent_length, 0.5)     # 过滤短字符串 和非中文字符串
                        if (not l.__eq__('')) and (not out_doc.__contains__(l)): # doc去重
                            out_doc.append(l)
                    if len(out_doc) != 0:
                        wf.write('<doc>\n'+ '\n'.join(out_doc) +'\n</doc>\n')
                    doc = []
                    rows = 0
    # 结束时间
    end = time.clock()
    print('程序结束，共用时：{0}'.format(end - start))

##过滤短字符串 和 非中文字符串（过滤掉中文占比小的）
# limit_length:小于等于限定长度即舍去
# proportion: 汉子占字符串的比例
def filter_str(line, limit_length, proportion):
    line = line.strip()
    if len(line) <= limit_length :
        return ''
    # 判断中文的比例
    if proportion_chinese(line) < proportion:
        return ''
    return line

##判断中文字符串占总字符的比例
def proportion_chinese(line):
    char_num = len(line)
    chinese_num = 0.0
    # 统计汉字的个数
    for c in line:
        if c >= u'\u4e00' and c <= u'\u9fa5':  # 是否是中文
            chinese_num += 1
    # print chinese_num,'/',char_num,'=',chinese_num / char_num, line
    return chinese_num / char_num


##提出与>..<匹配的内容  返回包含><
def extract_str(doc):
    re_str = re.compile(r'>([^><]*)<')    # 提取出> < 中间的部分
    s = re_str.findall(doc)
    return s

##替换常用HTML字符实体.
#使用正常的字符替换HTML中特殊的字符实体.
#你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
#@param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES={'nbsp':' ','160':' ',
                'lt':'<','60':'<',
                'gt':'>','62':'>',
                'amp':'&','38':'&',
                'quot':'"','34':'"',}

    re_charEntity=re.compile(r'&#?(?P<name>\w+);?')
    sz=re_charEntity.search(htmlstr)
    while sz:
        entity=sz.group()#entity全称，如&gt;
        key=sz.group('name')#去除&;后entity,如&gt;为gt
        try:
            htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
            sz=re_charEntity.search(htmlstr)
        except KeyError:
            #以空串代替
            htmlstr=re_charEntity.sub('',htmlstr,1)
            sz=re_charEntity.search(htmlstr)
    return htmlstr


if __name__=='__main__':
    ## windows
    run('h:/SogouT/pages.244/pages.244',50)

    ## linux
    # run('/home/guanpf/语料/sogouT/corpus/pages.242',50)