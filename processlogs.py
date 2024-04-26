#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from collections import Counter
import mysql.connector

def process_ssh_log_filesfunc():
    def process_ssh_log_files(log_files):
        ssh_attempts = []
    
        for file in log_files:
            with open(file, 'r') as log_file:
                for line in log_file:
                    if 'sshd' in line and 'Failed' in line:
                        match = re.search(r'from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
                        if match:
                            ssh_attempts.append(match.group(1))
    
        ssh_attempts_sorted = Counter(ssh_attempts).most_common()
    
        if len(ssh_attempts_sorted) >= 2:
            print("Improper SSH access attempts detected:")
            print("\nAttacker IP       |       Tries")
            for attempt, count in ssh_attempts_sorted:
                print(attempt, count, sep='           ')
            
            # Ask the user if they want to check the hour and date of attempts for a specific IP
            ip_choice = input("\nDo you want to check the failed ssh attempts for a specific IP? (Y/N): ")
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
            print("Insufficient improper SSH access attempts found.")
    
    
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
            
            # Create the SSH attempts table if it doesn't exist
            create_ssh_table_query = "CREATE TABLE IF NOT EXISTS ssh_attempts (ip VARCHAR(15), count INT)"
            cursor.execute(create_ssh_table_query)
            
            # Insert the SSH attempts into the database
            insert_ssh_query = "INSERT INTO ssh_attempts (ip, count) VALUES (%s, %s)"
            ssh_attempts_with_count = [(attempt, count) for attempt, count in ssh_attempts_sorted]
            cursor.executemany(insert_ssh_query, ssh_attempts_with_count)
            
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
    
    # Process the SSH log files in the given directory
    log_files = [directory]  # Replace with actual log file paths
    process_ssh_log_files(log_files)

