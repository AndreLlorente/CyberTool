import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
def jupyterfunc():
    # Step 1: Connect to the MariaDB database
    # Modify the connection details based on your database credentials
    
    connection = mysql.connector.connect(
        host="localhost",
        user="lawrence",
        password="123",
        database="cybertoolDB"
    )
    
    # Step 2: Display the menu options
    print("Which table from the CybertoolDB do you want to turn into a graphic:")
    print("1. ssh_attempts")
    print("2. http_attempts")
    print("3. https_attempts")
    
    # Step 3: Prompt the user for their choice
    option = input("-> ")
    
    # Step 4: Determine the table name based on the user's choice
    if option == '1':
        table_name = 'ssh_attempts'
    elif option == '2':
        table_name = 'http_attempts'
    elif option == '3':
        table_name = 'https_attempts'
    else:
        print("Invalid option. Exiting...")
        exit()
    
    # Step 5: Retrieve data from the specified table
    query = f"SELECT ip, count FROM {table_name}"
    
    # Read data into a Pandas DataFrame
    data = pd.read_sql(query, connection)
    
    # Step 6: Generate graphical statistics
    # Use Matplotlib to create a bar chart
    plt.figure(figsize=(40, 16))  # Increase the size as per your requirement
    plt.bar(data['ip'], data['count'])
    plt.xlabel('IP')
    plt.ylabel('Count')
    plt.title('Graphical Statistics')
    plt.show()
    
    # Step 7: Close the database connection
    connection.close()
