import duckdb
import glob
import os
import re
from datetime import datetime as dt
def persToForm():
    # Create a new database in formatted or connect to the existing one
    con = duckdb.connect(database="../data/formatted/crimesPrices.db")

    # Delete any existing tables
    tables = con.execute("SHOW TABLES").df()
    for table in tables['name']:
        con.execute("DROP TABLE " + table)

    # Regex to remove non-alphanumeric characters 
    regex = re.compile(r'\W+')

    cFiles = glob.glob("../data/landing/persistent/crimes/*.csv")
    tables = []
    
    # Get last timestamp of previously processed crime files
    with open("../data/formatted/crimesTime.txt") as f:
            lastTimestamp = f.readlines()

    # Create a table for each version of data source  if the file hasn't been processed
    for file in cFiles:
        #Get timestamp to check whether file has been processed
        timestamp = os.path.basename(file).split("t-")[1].split(".")[0]
        if len(lastTimestamp) == 0 or timestamp > lastTimestamp[0]:
            # Get file base name for table name
            fileBase = os.path.basename(file).split(".")[0]
            # Remove non-alphanumeric characters
            fileBase = regex.sub('', fileBase)
            # Add tables name to tables
            tables.append(fileBase)
            # Save in a new table
            con.execute("CREATE OR REPLACE TABLE {0} AS SELECT * FROM read_csv_auto('{1}');".format(fileBase, file))

    # Log name of tables in crimesTables.txt
    f = open("../data/formatted/crimesTables.txt", "w")
    f.writelines("\n".join(tables))
    f.close()

    # Log timestamp in crimesTime.txt
    f = open("../data/formatted/crimesTime.txt", "w")
    f.writelines(dt.now().strftime("%Y-%m-%d-%H_%M_%S"))
    f.close()

    cFiles = glob.glob("../data/landing/persistent/prices/*.csv")
    tables = []
    
    # Get last timestamp of previously processed price files
    with open("../data/formatted/pricesTime.txt") as f:
            lastTimestamp = f.readlines()
    
    # Create a table for each version of data source  if the file hasn't been processed
    for file in cFiles:
        #Get timestamp to check whether file has been processed
        timestamp = os.path.basename(file).split("t-")[1].split(".")[0]
        if len(lastTimestamp) == 0 or timestamp > lastTimestamp[0]:
            # Get file base name for table name
            fileBase = os.path.basename(file).split(".")[0]
            # Remove non-alphanumeric characters
            fileBase = regex.sub('', fileBase)
            # Add tables name to tables
            tables.append(fileBase)
            # Save in a new table
            con.execute("CREATE OR REPLACE TABLE {0} AS SELECT * FROM read_csv_auto('{1}');".format(fileBase, file))

    # Log name of tables in pricesTables.txt
    f = open("../data/formatted/pricesTables.txt", "w")
    f.writelines("\n".join(tables))
    f.close()

    # Log timestamp in pricesTime.txt
    f = open("../data/formatted/pricesTime.txt", "w")
    f.writelines(dt.now().strftime("%Y-%m-%d-%H_%M_%S"))
    f.close()

    con.close()