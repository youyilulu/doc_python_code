# coding:utf-8
import codecs


class DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('baike.csv', 'w', encoding='utf-8')
        for data in self.datas:
            fout.writelines("%s,\"%s\",\"%s\"\n" %
                            (data['url'], data['title'], data['summary']))
