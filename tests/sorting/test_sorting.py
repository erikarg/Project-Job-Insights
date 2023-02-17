from src.pre_built.sorting import sort_by

jobs = [
    {"min_salary": 800, "max_salary": 2000, "date_posted": "2022-01-03"},
    {"min_salary": 5000, "max_salary": 10000, "date_posted": "2015-07-09"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-01-02"},
    {"min_salary": 3500, "max_salary": 7500, "date_posted": "2021-07-01"},
]


def test_sort_by_criteria():
    max_salary_ordened = [
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "2015-07-09"},
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2021-07-01"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-01-02"},
        {"min_salary": 800, "max_salary": 2000, "date_posted": "2022-01-03"},
    ]
    sort_by(jobs, "max_salary")
    assert jobs == max_salary_ordened

    min_salary_ordened = [
        {"min_salary": 800, "max_salary": 2000, "date_posted": "2022-01-03"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-01-02"},
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2021-07-01"},
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "2015-07-09"},
    ]
    sort_by(jobs, "min_salary")
    assert jobs == min_salary_ordened

    date_posted_ordened = [
        {"min_salary": 800, "max_salary": 2000, "date_posted": "2022-01-03"},
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2021-07-01"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-01-02"},
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "2015-07-09"},
    ]
    sort_by(jobs, "date_posted")
    assert jobs == date_posted_ordened
