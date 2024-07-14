
# DNS Detective:
DNS Detective is a Python-based GUI tool designed for web information gathering. It retrieves basic information about a given domain, such as IP address, DNS records, server details, and WHOIS information. 


## Features:
- Get IP address of the domain
- Retrieve DNS records (A, AAAA, MX, NS, TXT)
- Fetch WHOIS information
- Find subdomains using Certificate Transparency logs
- Scan for open ports using Nmap

## Requirements:
- Python 3.x
- tkinter
- socket
- whois
- dnspython

# Installation:
1. Ensure you have Python 3.x installed on your system.
2. Install the required Python libraries:
    ```bash
   pip install tkinter whois dnspython
  
## Usage:
1. Clone this repository or download the script.
2. Run the script using Python:
     ```bash
     python dns_detective.py
3. A GUI window will appear. Enter the domain you wish to investigate and click the "Investigate" button.
4. The information will be displayed in the text box below.
5. To save the information, click the "Save Document" button. The report will be saved as investigation_report.txt in the current directory.


## Contributing:
If you have suggestions for improvements or find any bugs, please open an issue or submit a pull request.


## Note:
This tool is for educational and informational purposes only. Be responsible and avoid using it on domains without proper authorization.
The script attempts to retrieve basic server information, but success may vary depending on the server configuration.

## Disclaimer:
The author assumes no responsibility for any misuse of this script. Always adhere to ethical hacking practices and respect website terms of service.
