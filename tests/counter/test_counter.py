from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    count = count_ocurrences(path, "end")
    assert count == 5889
