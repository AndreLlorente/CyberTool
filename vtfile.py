import requests
import webbrowser

API_KEY = "871f3abca70d54454ad7e3eca99c3f1b6083f7d32e76ea337ebba0e293b6588d"  # Replace with your VirusTotal API key

def scan_file(file_path):
    url = "https://www.virustotal.com/vtapi/v2/file/scan"
    params = {
        "apikey": API_KEY
    }
    
    files = {"file": (file_path, open(file_path, "rb"))}
    
    response = requests.post(url, files=files, params=params)
    
    if response.status_code == 200:
        result = response.json()
        print("\nYou successfully uploaded the file to VirusTotal")
        
        permalink = result.get("permalink")
        if permalink:
            print("Report Link: ", permalink)
            choice = input("\nDo you wish to open the report link? (y/n): ")
            if choice.lower() == "y":
                webbrowser.open(permalink)
    else:
        print("Error occurred while submitting the file for scanning.")

def file_scan_function():
    file_path = input("Enter the path of the file to scan: ")
    scan_file(file_path)

if __name__ == "__main__":
    file_scan_function()
