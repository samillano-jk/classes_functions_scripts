import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    def find_3rd(df, col):
            df = df.sort_values(by=col, ascending=False)[col].unique()
            if len(df)>2:
                return df[2]
            else:
                return df[len(df)-1]


    col_n = ["Department", "Employee", "Salary"]
    employee = employee.rename(columns={"name":col_n[1], "salary":col_n[2]})
    department = department.rename(columns={"name":col_n[0]})

    if not employee.empty and not department.empty:
        df_merged = pd.merge(employee, department, left_on="departmentId", right_on="id", how="left")
        df = df_merged.loc[:, col_n]

        departments = df[col_n[0]].unique()
        new_df = pd.DataFrame()
        for department in departments:
            dep_df = df.loc[df[col_n[0]] == department]
            top_3_val = find_3rd(dep_df, col_n[2])
            fin_df = dep_df.loc[dep_df[col_n[2]]>=top_3_val]
            new_df = pd.concat([new_df, fin_df])
        return new_df
    else: 
        return pd.DataFrame({col_n[0]:[], col_n[1]:[], col_n[2]:[]})