from sql_database import sql_database,sql_table
from typing import List
from dlt.common.configuration.specs import ConnectionStringCredentials
import dlt


def sql_to_destination() -> None:
    database = sql_database()
   
    # load a single table, replace the table_name with the name of table you want to load
    table_name = sql_table(table='table_name')
    
    pipeline = dlt.pipeline(pipeline_name="sql_tables", destination='bigquery', dataset_name='sql_database_inc_load1', full_refresh=False )
   
    data = table_name
    print(pipeline.run(data))
    


if __name__ == '__main__':   
    sql_to_destination()
