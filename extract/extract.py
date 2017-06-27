#coding=utf-8
import re

#往文件写要加这个
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def run():
    with open('d:/pages.241.extract_python_clear','a+') as wf:
        with open("d:/pages.241.extract_python") as f:
            doc = ''
            for line in f:
                try:
                    # print(line.decode("utf-8")),
                    # wf.write(line.decode('utf-8'))
                    line = line.decode('utf-8')
                except:
                        # print line.decode("gbk")
                        # wf.write(line.decode('gbk'))
                        line = line.decode('utf-8')
                line = line.strip()
                # print line,
                if line.__eq__('') or line.startswith('<docno>') or line.startswith('<url>'):
                    continue  # 去除空行 和 无用标签
                doc += line
                if line.__eq__('</doc>'):
                    wf.write('<doc>\n')
                    s = extract_str(doc)
                    for l in s:
                        #print l
                        l = l.lstrip('>').rstrip('<').strip()
                        l = replaceCharEntity(l)#替换实体
                        l = filter_str(l, 10, 0.5)     # 过滤短字符串 和非中文字符串
                        if not l.__eq__(''):
                            wf.write(l+'\n')
                    wf.write('</doc>\n')
                    doc = ''

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
        # print c
        if c >= u'\u4e00' and c <= u'\u9fa5':  # 是否是中文
            chinese_num += 1
    # print chinese_num,'/',char_num,'=',chinese_num / char_num, line
    return chinese_num / char_num


##提出与>..<匹配的内容  返回包含><
def extract_str(doc):
    re_str = re.compile(r'>[^><]*<')
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

    re_charEntity=re.compile(r'&#?(?P<name>\w+);')
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
    run()