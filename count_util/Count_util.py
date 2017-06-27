# coding=utf-8

class Count_util:
    @staticmethod
    def count_doc_num(file_path):
        """
        计算文件中网页格式
        :param file_path:文件路径
        :return: 返回个数
        """
        num = 0
        with open(file_path,'rb') as f:
            for line in f:
                if line.startswith('<doc>'):
                    num += 1
            print('文件中网页的个数为{0}'.format(num))
        return num

    @staticmethod
    def count_sentence_num(file_path):
        """
        计算文件中的句子个数（默认每行一句，其实就是记录行数）
        :param file_path: 文件路径
        :return: 句子个数（行数）
        """
        num = 0
        with open(file_path,'rb') as f:
            for line in f:
                num += 1

        print('文件中句子的个数为{0}'.format(num))
        return num

    @staticmethod
    def count_char_num(file_path):
        """
        计算文件中的字符个数
        :param file_path: 文件路径
        :return: 字符个数
        """
        num = 0
        with open(file_path,'rb') as f:
            for line in f:
                num += len(line)
        print('文件中字符的个数为{0}'.format(num))
        return num

    @staticmethod
    def count_sentence_char_num(file_path):
        """
        计算文件中的句子数和字符数
        :param file_path: 文件路径
        :return: 句子数 字符数
        """
        sentence_num = 0
        char_num = 0

        with open(file_path,'rb') as f:
            for line in f:
                sentence_num += 1
                char_num += len(line)
        print('文件中句子个数为{0}，字符的个数为{1}'.format(sentence_num,char_num))
        return sentence_num,char_num


if __name__ == '__main__':
    Count_util.count_doc_num('d:/pages.241.extract_python')
    #Count_util.count_doc_num('h:/SogouT/pages.241/pages.241')
    # Count_util.count_sentence_num('d:/pages.241.extract_python')
    # Count_util.count_sentence_num('h:/SogouT/pages.241/pages.241')
    # Count_util.count_char_num('d:/pages.241.extract_python')
    # Count_util.count_sentence_char_num('d:/pages.241.extract_python')
