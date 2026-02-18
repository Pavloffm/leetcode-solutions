import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, employee, left_on='managerId', right_on='id', how='inner',suffixes=('_emp', '_mgr'))
    return merged[merged['salary_emp'] > merged['salary_mgr']][['name_emp']].rename(columns={'name_emp': 'Employee'})
