from typing import Dict, List, Union

from src.insights.jobs import read

# def verify_int(*values):
#     valid_value = True
#     for value in values:
#         if type(value) != int:
#             valid_value = False
#             break
#     return valid_value


def get_max_salary(path: str) -> int:
    file = read(path)
    salary = set()
    for row in file:
        if row["max_salary"].isdigit():
            salary.add(int(row["max_salary"]))
    return max(salary)


def get_min_salary(path: str) -> int:
    file = read(path)
    salary = set()
    for row in file:
        if row["min_salary"].isdigit():
            salary.add(int(row["min_salary"]))
    return min(salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        int(salary)
        max_salary = int(job.get("max_salary"))
        min_salary = int(job.get("min_salary"))

        if type(max_salary and min_salary and salary) != int:
            raise ValueError("Some of the values are not integers")
        elif int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError(
                "The minimum salary can't be greater than the maximum salary"
            )
    except TypeError:
        raise ValueError
    return int(min_salary) <= int(salary) <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_list = []

    for job in jobs:
        if "min_salary" not in job or "max_salary" not in job:
            min_salary = job["min_salary"]
            max_salary = job["max_salary"]
            if (min_salary, max_salary and salary != "") and (
                isinstance(min_salary and max_salary and salary, int)
            ):
                if min_salary <= salary <= max_salary:
                    jobs_list.append(job)
    return jobs_list
