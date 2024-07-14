import tkinter as tk
import socket
import whois
import dns.resolver
import os

def gather_info(domain):
    try:
        # IP Address
        ip_address = socket.gethostbyname(domain)

        # DNS Records
        resolver = dns.resolver.Resolver()
        a_records = resolver.resolve(domain, 'A')
        ns_records = resolver.resolve(domain, 'NS')
        mx_records = resolver.resolve(domain, 'MX')

        # Whois Information
        w = whois.whois(domain)

        # Server Details (basic)
        try:
            server_info = socket.gethostbyaddr(ip_address)
        except socket.herror:
            server_info = "Unable to retrieve server information"

        # Combine information
        info = f"Domain: {domain}\nIP Address: {ip_address}\n\nDNS Records:\nA Records: {', '.join([str(record) for record in a_records])}\nNS Records: {', '.join([str(record) for record in ns_records])}\nMX Records: {', '.join([str(record) for record in mx_records])}\n\nWhois Information:\n{w}\n\nServer Information:\n{server_info}"

        return info
    except Exception as e:
        return f"An error occurred: {str(e)}"

def save_info(info, filename):
    with open(filename, 'w') as f:
        f.write(info)

def main():
    root = tk.Tk()
    root.title("DNS Detective")

    domain_label = tk.Label(root, text="Enter Domain:")
    domain_entry = tk.Entry(root) 
    gather_button = tk.Button(root, text="Investigate", command=lambda: display_info(domain_entry.get()))
    save_button = tk.Button(root, text="Save Document", command=lambda: save_info(text_box.get("1.0", tk.END), "investigation_report.txt"))
    text_box = tk.Text(root, height=20, width=50)

    domain_label.pack()
    domain_entry.pack()
    gather_button.pack()
    save_button.pack()
    text_box.pack()

    def display_info(domain):
        info = gather_info(domain)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, info)

    root.mainloop()

if __name__ == "__main__":
    main()
