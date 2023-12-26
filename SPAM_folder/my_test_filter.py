from filter import MyFilter
from quality import compute_quality_for_corpus

if __name__ == "__main__":
    tests = MyFilter()
    tests.train("./test_data/1")
    tests.test("./test_data/1")
    quality = compute_quality_for_corpus("./test_data/1")
    print(f"Quality Score №1: {quality}")
    tests.train("./test_data/2")
    tests.test("./test_data/2")
    quality = compute_quality_for_corpus("./test_data/2")
    print(f"Quality Score №2: {quality}")