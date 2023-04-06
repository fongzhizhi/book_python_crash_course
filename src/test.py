import unittest

def get_formatted_name(first_name, last_name, middle = ''):
    """生成格式话完整姓名"""
    full_name = f"{first_name} {middle} {last_name}" if middle else f"{first_name} {last_name}"
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """测试Dongoog Chiang"""
        full_name = get_formatted_name('dongoog', 'chiang')
        self.assertEqual(full_name, 'Dongoog Chiang')

    def test_middle_name(self):
        """测试middle name"""
        full_name = get_formatted_name('dongoog', 'chiang', 'chi')
        self.assertEqual(full_name, 'Dongoog Chi Chiang')

if __name__ == '__main__':
    unittest.main()

