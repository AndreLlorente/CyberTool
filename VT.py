import requests
import json
def virustotalfunc():
    def get_ip_information(ip_address):
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
        headers = {
            "x-apikey": "871f3abca70d54454ad7e3eca99c3f1b6083f7d32e76ea337ebba0e293b6588d"  # Replace with your actual VirusTotal API key
        }
        
        response = requests.get(url, headers=headers)
        return response.text
    
    def display_ip_information(ip_information):
        # Parse the JSON response
        data = json.loads(ip_information)
    
        # Extract the relevant information
        country = data['data']['attributes']['country']
        last_analysis_stats = data['data']['attributes']['last_analysis_stats']
        whois = data['data']['attributes']['whois']
    
        # Print the extracted information
        print("Country: ", country)
        print("Last Analysis Stats: ", last_analysis_stats)
        print("Whois: ", whois)
    
    # Example usage
    ip_address = input("Enter the IP address you want to check: ")
    response = get_ip_information(ip_address)
    display_ip_information(response)

    # Prompt the user if they want to save the output in a text file
    save_option = input("Do you want to save the output in a text file? (Y/N): ")
    if save_option.upper() == "Y":
        filename = ip_address.replace(".", "") + "_VirusTotalReport.txt"
        with open(filename, "w") as file:
            file.write(response)
        print(f"Output saved in {filename}")