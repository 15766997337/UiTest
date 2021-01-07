#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tools.operation_xlsx import OperationExcel
from tools.actionMethod import Judge_method
import unittest
from ddt import ddt, data
import time

xls_data = OperationExcel()
test_data = xls_data.get_data()


@ddt
class Testcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.run_method = Judge_method()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(2)

    @data(*test_data)
    def test_run_main(self, data):

        case_id = data[0]  # 用例id
        Module_name = data[1]  # 模块名称
        want_run = data[2]  # 是否运行
        operation = data[3]  # 操作说明
        method = data[4]  # 执行方法
        input_data = data[5]  # 输入的数据
        elenium = data[6]  # 操作元素
        Assertion_method = data[7]  # 断言方法
        Assertion_value = data[8]  # 断言值
        Actual_result = data[9]  # 预期结果
        want_through = data[10]  # 是否通过
        if want_run == 'yes':
            self.run_method.run_method(method, input_data, elenium)
            result = None
            if Assertion_method != '':
                result = self.run_method.run_method(Assertion_method, Assertion_value)
                if Actual_result in result:
                    xls_data.write_value(case_id, '通过')
                else:
                    xls_data.write_value(case_id, '失败')
            else:
                xls_data.write_value(case_id, '没有断言方法')
            self.assertIn(Actual_result, result)


if __name__ == '__main__':
    unittest.main()
