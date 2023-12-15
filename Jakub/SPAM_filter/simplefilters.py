from basefilter import BaseFilter

class NaiveFilter:
    def test(folder_path):
        BaseFilter(folder_path, "OK", "!truth_OK").write_to_file()

class ParanoidFilter:
    def test(folder_path):
        BaseFilter(folder_path, "SPAM", "!truth_SPAM").write_to_file()

class RandomFilter:
    def test(folder_path):
        BaseFilter(folder_path).write_to_file()


if __name__ == "__main__":
    NaiveFilter.test("./Python/SPAM_filter/test_folder")
    ParanoidFilter.test("./Python/SPAM_filter/test_folder")
    RandomFilter.test("./Python/SPAM_filter/test_folder")