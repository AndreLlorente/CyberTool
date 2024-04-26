import re
import mysql.connector

def processlogshttphttps():
    def process_http_log_files(log_files):
        http_attempts = list()
        https_attempts = list()

        for file in log_files:
            with open(file, 'r') as log_file:
                for line in log_file:
                    if 'UFW BLOCK' in line:
                        if 'DPT=80' in line:
                            ip_match = re.search(r'SRC=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
                            mac_match = re.search(r'MAC=([0-9a-fA-F:]+)', line)
                            if ip_match and mac_match:
                                ip = ip_match.group(1)
                                mac = mac_match.group(1)
                                http_attempts.append((ip, mac))
                        elif 'DPT=443' in line:
                            ip_match = re.search(r'SRC=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
                            mac_match = re.search(r'MAC=([0-9a-fA-F:]+)', line)
                            if ip_match and mac_match:
                                ip = ip_match.group(1)
                                mac = mac_match.group(1)
                                https_attempts.append((ip, mac))

        http_attempts_filter = sorted(set(http_attempts))
        https_attempts_filter = sorted(set(https_attempts))

        if len(http_attempts) >= 2:
            print("Improper HTTP access attempts detected by the firewall:")
            print("\nAttacker IP       |       MAC Address                                 |       Tries")
            for attempt in http_attempts_filter:
                ip, mac = attempt
                count = http_attempts.count(attempt)
                print(ip, mac,count, sep='           ')
        else:
            print("Insufficient improper HTTP access attempts found.")

        if len(https_attempts) >= 2:
            print("\nImproper HTTPS access attempts detected by the firewall:")
            print("\nAttacker IP       |       MAC Address                                 |       Tries")
            for attempt in https_attempts_filter:
                ip, mac = attempt
                count = https_attempts.count(attempt)
                print(ip, mac,count, sep='            ')
        else:
            print("Insufficient improper HTTPS access attempts found.")

        # Ask the user if they want to check the hour and date of attempts for a specific IP
        ip_choice = input("\nDo you want to check the hour and date of attempts for a specific IP? (Y/N): ")
        if ip_choice.upper() == 'Y':
            ip_to_check = input("Enter the IP to check: ")
            print(f"\nLogs for IP: {ip_to_check}\n")

            # Iterate through the log files again to find lines with the specified IP
            for file in log_files:
                with open(file, 'r') as log_file:
                    for line in log_file:
                        if ip_to_check in line:
                            print(line)
        else:
            pass
            
        # Ask the user if they want to add the information to a database
        db_choice = input("\nDo you want to add the obtained information to a MariaDB database? (Y/N): ")
        if db_choice.upper() == 'Y':
            # Connect to the MariaDB database
            connection = mysql.connector.connect(
                host="localhost",
                port="3306",
                user="lawrence",
                password="123"
            )
            
            # Create a cursor to execute queries
            cursor = connection.cursor()
            
            # Create the cybertoolDB3 database if it doesn't exist
            create_db_query = "CREATE DATABASE IF NOT EXISTS cybertoolDB"
            cursor.execute(create_db_query)
    
            # Select the cybertoolDB3 database
            use_db_query = "USE cybertoolDB"
            cursor.execute(use_db_query)
            
            # Create the HTTP attempts table if it doesn't exist
            create_http_table_query = "CREATE TABLE IF NOT EXISTS http_attempts (ip VARCHAR(15), mac VARCHAR(70), count INT)"
            cursor.execute(create_http_table_query)
            
            # Insert the HTTP attempts into the database
            insert_http_query = "INSERT INTO http_attempts (ip, mac, count) VALUES (%s, %s, %s)"
            http_attempts_with_count = [(ip, mac, http_attempts.count((ip, mac))) for ip, mac in http_attempts_filter]
            cursor.executemany(insert_http_query, http_attempts_with_count)
            
            # Create the HTTPS attempts table if it doesn't exist
            create_https_table_query = "CREATE TABLE IF NOT EXISTS https_attempts (ip VARCHAR(15), mac VARCHAR(70), count INT)"
            cursor.execute(create_https_table_query)
            
            # Insert the HTTPS attempts into the database
            insert_https_query = "INSERT INTO https_attempts (ip, mac, count) VALUES (%s, %s, %s)"
            https_attempts_with_count = [(ip, mac, https_attempts.count((ip, mac))) for ip, mac in https_attempts_filter]
            cursor.executemany(insert_https_query, https_attempts_with_count)
            
            # Commit the changes to the database
            connection.commit()
            
            # Close the cursor and database connection
            cursor.close()
            connection.close()
            
            print("Information added to the database.")
        else:
            print("Information not added to the database.")

    # Prompt the user for the directory of the file
    directory = input("Enter the directory of the file to process: ")

    log_files = [directory]  # Replace with actual log file paths
    process_http_log_files(log_files)


