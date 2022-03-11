from google.oauth2 import service_account
import pandas_gbq
import pandas as pd


credentials = service_account.Credentials.from_service_account_file(
    "../cfg/service-account.json",
)

project_id = "constant-height-160002"

df = pd.DataFrame(
    {
        "my_string": ["a", "b", "c"],
        "my_int64": [1, 2, 3],
        "my_float64": [4.0, 5.0, 6.0],
        "my_bool1": [True, False, True],
        "my_bool2": [False, True, False],
        "my_dates": pd.date_range("now", periods=3),
    }
)

# df = pandas_gbq.read_gbq(sql, project_id="constant-height-160002", credentials=credentials)
table_id = "botdata.firstdf"
pandas_gbq.to_gbq(
    df, table_id, project_id=project_id, credentials=credentials, if_exists="append"
)
