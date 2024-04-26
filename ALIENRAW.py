from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
import json
def alienvaultipreportfunc():
    # Replace with your AlienVault OTX API key
    API_KEY = "abb9a43177a07d0fd78b36932319568a6c660499da8add6f85d396f40a2d74dc"
    
    otx = OTXv2(API_KEY)
    
    def format_json(obj, indent=0):
        if isinstance(obj, dict):
            for key, value in obj.items():
                print('\t' * indent + str(key) + ':')
                format_json(value, indent + 1)
        elif isinstance(obj, list):
            for item in obj:
                format_json(item, indent)
        else:
            print('\t' * indent + str(obj))
    
    # Prompt the user to enter the IP address
    ip = input("Enter the IP to search: ")
    
    # Search AlienVault by IP
    resultado = otx.get_indicator_details_full(IndicatorTypes.IPv4, ip)
    res = json.dumps(resultado["general"]["pulse_info"], indent=4)
    
    # Display the output
    format_json(json.loads(res))
    
    # Prompt the user if they want to save the output in a text file
    save_option = input("Do you want to save the output in a text file? (Y/N): ")
    if save_option.upper() == "Y":
        filename = ip.replace(".", "") + "_AlienReport.txt"
        with open(filename, "w") as file:
            file.write(res)
        print(f"Output saved in {filename}")
