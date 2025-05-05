import unittest
import pandas as pd
from Text_Preprocessing import remove_mentions, remove_punctuations, lower_case_remove_whitespace, remove_non_ascii


class test_text_preprocessing(unittest.TestCase):
    def test_remove_mentions(self):
        input_series = pd.Series(["Hello @user1!", "@someone123 How are you?", "No mention here"])
        expected = pd.Series(["Hello !", " How are you?", "No mention here"])
        result = remove_mentions(input_series)
        pd.testing.assert_series_equal(result, expected)

    def test_remove_punctuations(self):
        input_series = pd.Series(["Wow!!!", "Hey, you.", "Clean"])
        expected = pd.Series(["Wow", "Hey you", "Clean"])
        result = remove_punctuations(input_series)
        pd.testing.assert_series_equal(result, expected)

    def test_lower_case_remove_whitespace(self):
        input_series = pd.Series(["  THIS is A TEST  ", "\nNewLINE\t", "   Clean "])
        expected = pd.Series(["this is a test", "newline", "clean"])
        result = lower_case_remove_whitespace(input_series)
        pd.testing.assert_series_equal(result, expected)


    def test_remove_non_ascii(self):
        input_series = pd.Series(["This is normal", "This has emoji 😊", "Corrupt char: ø¹ù"])
        expected = pd.Series(["This is normal", "This has emoji ", "Corrupt char: "])
        result = remove_non_ascii(input_series)
        pd.testing.assert_series_equal(result, expected)







if __name__ == '__main__':
    unittest.main()