# -*- coding:utf-8 -*-
import os
import xlrd


class DataToParam(object):

    def file_exist(self, filename):
        if os.path.isfile(filename):
            return True
        else:
            raise Exception('参数化文件不存在')

    def text(self, filename):
        if self.file_exist(filename):
            with open(filename, 'r') as f:
                return_list = []
                for row in f:
                    t=row.strip().split(' ')

                    return_list.append(t)

                return return_list

    def excel(self,filename):
        if self.file_exist(filename):
            book=xlrd.open_workbook(filename)
            sheet=book.sheet_by_index(0)
            rows=sheet.nrows
            return_list=[]
            for row in rows:
                return_list.append(sheet.row_values(row))
            return return_list



