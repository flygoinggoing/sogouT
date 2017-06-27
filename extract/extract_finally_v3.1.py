#coding=utf-8
import re
import time
import io

#往文件写要加这个
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def run(read_path, limit_sent_length, limit_doc_row):
    # 开始时间
    start = time.clock()
    doc_num = 0    # 记录处理的doc数
    rows = 0   # 记录doc中的行数
    write_path = read_path + '.clear_' + str(limit_sent_length) + '_' + str(limit_doc_row)
    with open(write_path, 'a+') as wf:
        with open(read_path, 'rb') as f:
            doc = io.StringIO()
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

                line = line.strip()
                # print line,
                if line.__eq__('') or line.startswith('<docno>') or line.startswith('<url>'):
                    continue  # 去除空行 和 无用标签
                rows += 1
                # doc += line
                doc.write(line)

                if line.__eq__('</doc>'):
                    # 如果文件的行数大于limit_doc_row，处理时间太长，则直接舍去
                    if rows > limit_doc_row:
                        doc.close()
                        doc = io.StringIO()
                        rows = 0
                        continue

                    out_doc = ''
                    doc_num += 1
                    if (doc_num % 1000) == 0:
                        print('已经处理了:{0}个文件，已用时{1}s'.format(doc_num,(time.clock()-start)))
                    s = extract_str(doc.getvalue())
                    for l in s:
                        l = l.strip()
                        l = replaceCharEntity(l)#替换实体
                        l = filter_str(l, limit_sent_length, 0.5)     # 过滤短字符串 和非中文字符串
                        if not l.__eq__(''):
                            out_doc += l + '\n'
                    if not out_doc.__eq__(''):
                        wf.write('<doc>\n'+ out_doc +'</doc>\n')
                    doc.close()
                    doc = io.StringIO()
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
    # run('h:/SogouT/pages.241/pages.241',50,10000)
    run('H:/SogouT/pages.241/pages.241.cut.1423600_1423700', 50, 200000)