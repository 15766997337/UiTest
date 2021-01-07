import setting
import xlrd
from xlutils.copy import copy
import xlwt


class OperationExcel:

    def __init__(self, file_name=None, sheet_id=None):
        '''
        调用OperationExcel会先执行init函数的内容
        :param file_name: 表格文件地址路径
        :param sheet_id: 表格的sheet id
        '''
        if file_name:
            # 如果有传文件路径和id就用传入的文件路径和id
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            # 否则就用默认写好的路径和id
            self.file_name = setting.Yong_Li_path
            self.sheet_id = 0
        self.data = xlrd.open_workbook(self.file_name)
        self.table = self.data.sheets()[self.sheet_id]
        self.rows = self.table.nrows

    # 获取xlsx表格数据内容，以列表返回
    def get_data(self):
        result = []
        for i in range(1, self.rows):
            col = self.table.row_values(i)
            result.append(col)
        return result

    # 写入测试结果
    def write_value(self, hang, value):
        """
        :param row: 行数
        :param col: 列数
        :param value: 写入的数据值
        """
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(hang, 10, value)
        write_data.save(self.file_name)



if __name__ == '__main__':
    xls = OperationExcel()
    for i in range(5, 13):
        data = xls.get_data()[i][6]
        type = str(data.split('>')[0])
        value = str(data.split('>')[1])
        print(i, '--type=', type)
        print(i, '--value=', value)
