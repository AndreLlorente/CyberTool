import pandas as pd
import mysql.connector

def exceltodbfunc():
    # Prompt the user for the Excel file path
    file_path = input("Enter the path to the Excel file: ")
    
    # Name of the worksheet in the Excel file
    worksheet_name = 'Sheet1'
    
    # Name of the column you want to print
    column_name = 'Endereço_ip'
    
    # Load the Excel file into a DataFrame
    data_frame = pd.read_excel(file_path, sheet_name=worksheet_name)
    
    # Print the values from the specific column
    column = data_frame[column_name]
    for value in column:
        print(value)
    
    # Prompt the user if they want to save the IP addresses in a database
    save_option = input("Do you want to save the IP addresses in a database? (Y/N): ")
    
    if save_option.upper() == 'Y':
    
        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="lawrence",
            password="123",
            database="cybertoolDB"
        )
        
        # Create a cursor to execute queries
        cursor = connection.cursor()
        
        # Create the IP addresses table if it doesn't exist
        create_table_query = "CREATE TABLE IF NOT EXISTS ip_addresses_excel (ip VARCHAR(15))"
        cursor.execute(create_table_query)
        
        # Insert the IP addresses into the database
        insert_query = "INSERT INTO ip_addresses_excel (ip) VALUES (%s)"
        values = [(value,) for value in column]
        cursor.executemany(insert_query, values)
        
        # Commit the changes to the database
        connection.commit()
        
        # Close the cursor and database connection
        cursor.close()
        connection.close()
        
        print("IP addresses saved in the database.")
    else:
        print("IP addresses not saved in the database.")
