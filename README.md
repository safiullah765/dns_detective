# DNS Detective
DNS Detective is a Python-based GUI tool designed for web information gathering. It retrieves basic information about a given domain, such as IP address, DNS records, server details, and WHOIS information. 


# Features
1. Get IP address of the domain
2. Retrieve DNS records (A, AAAA, MX, NS, TXT)
3. Fetch WHOIS information
4. Find subdomains using Certificate Transparency logs
5. Scan for open ports using Nmap

# Requirements
- Python 3.x
- tkinter
- socket
- whois
- dnspython

# Installation
1. Ensure you have Python 3.x installed on your system.
2. Install the required Python libraries:
     - pip install tkinter whois dnspython
  
#Usage
1. Clone this repository or download the script.
2. Run the script using Python:
     - python dns_detective.py
3. A GUI window will appear. Enter the domain you wish to investigate and click the "Investigate" button.
4. The information will be displayed in the text box below.
5. To save the information, click the "Save Document" button. The report will be saved as investigation_report.txt in the current directory.
