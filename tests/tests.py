import unittest
from myproject.Graber.secret_date.auth import *

class DefautlTest(unittest.TestCase):
    def test_get_id_lists:
        for name in names_lists:
            name_list = name
            i = get_id_list(id_board, name_list)
            if i:
                print(i)