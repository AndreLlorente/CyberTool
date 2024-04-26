import mysql.connector
import requests
import json
def vtdatabasefunc():
    def get_ip_information(ip_address):
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
        headers = {
            "x-apikey": "871f3abca70d54454ad7e3eca99c3f1b6083f7d32e76ea337ebba0e293b6588d"
        }
        
        response = requests.get(url, headers=headers)
        return response.text
    
    # Prompt the user for database and table names
    database_name = input("Enter the name of the database: ")
    table_name = input("Enter the name of the table: ")
    
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="lawrence",
        password="123",
        database=database_name
    )
    
    # Create a cursor to execute queries
    cursor = connection.cursor()
    
    # Retrieve IP addresses from the table
    select_query = f"SELECT ip FROM {table_name}"
    cursor.execute(select_query)
    ip_addresses = cursor.fetchall()
    
    # Iterate over the IP addresses and perform research
    for ip_address in ip_addresses:
        ip = ip_address[0]
        response = get_ip_information(ip)
        ip_information = json.loads(response)
        
        # Process the IP information as per your requirements
        # Extract the relevant data and perform necessary operations
        
        # Print the IP information
        print(f"IP: {ip}")
        print(json.dumps(ip_information, indent=4))
        print("------------------------------")
    
    # Prompt the user if they want to save the output in a text file
    save_option = input("Do you want to save the output in a text file? (Y/N): ")
    if save_option.upper() == "Y":
        filename = input("Enter the filename to save the output: ")
        with open(filename, "w") as file:
            for ip_address in ip_addresses:
                ip = ip_address[0]
                response = get_ip_information(ip)
                ip_information = json.loads(response)
                file.write(f"IP: {ip}\n")
                file.write(json.dumps(ip_information, indent=4))
                file.write("\n------------------------------\n")
        print(f"Output saved in {filename}")
    
    # Close the cursor and database connection
    cursor.close()
    connection.close()
