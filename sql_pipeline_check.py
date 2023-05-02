from sql_database import sql_database,sql_table
from typing import List
from dlt.common.configuration.specs import ConnectionStringCredentials
import dlt
import pandas as pd

def sql_to_destination() -> None:
    # reflect a database
    # TODO: fix the mandatory password field in ConnectionStringCredentials
    credentials = ConnectionStringCredentials()
    credentials.parse_native_representation("mysql+pymysql://rfamro@mysql-rfam-public.ebi.ac.uk:4497/Rfam")
    credentials.__is_resolved__ = True
    database = sql_database(credentials)
   

    # load a single table
    family_table = sql_table(credentials="mysql+pymysql://rfamro@mysql-rfam-public.ebi.ac.uk:4497/Rfam", table='family', write_disposition="merge")
  
    #df=pd.DataFrame(family_table)
    #print(df)
    pipeline = dlt.pipeline(
        pipeline_name="sql_tables",
        destination='bigquery',
        dataset_name='sql_database_data1231',
        full_refresh=False,
    )
    data = family_table
    print(pipeline.run(data))


if __name__ == '__main__':
    
    sql_to_destination()