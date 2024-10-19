import argparse
from scanners.sql_injection_scanner import sql_injection_scan
from scanners.xss_scanner import xss_scan
from reporting.report_generator import generate_report

def run_vapt_toolkit(target_url):
    vulnerabilities = []

    print(f"Scanning target: {target_url}")
    
    print("Running SQL Injection Scanner...")
    if sql_injection_scan(target_url):
        vulnerabilities.append(f"SQL Injection at {target_url}")
    
    print("Running XSS Scanner...")
    if xss_scan(target_url):
        vulnerabilities.append(f"XSS at {target_url}")
    
    if vulnerabilities:
        print(f"[!] Vulnerabilities found: {vulnerabilities}")
        generate_report(vulnerabilities)
    else:
        print("[+] No vulnerabilities found!")

if __name__ == "__main__":
    # Use argparse to parse command-line arguments
    parser = argparse.ArgumentParser(description='Vulnerability Assessment and Penetration Testing Toolkit')
    
    # Add the target URL argument
    parser.add_argument('target_url', help='Target URL to scan for vulnerabilities')
    
    # Parse the argument from the command line
    args = parser.parse_args()
    
    # Pass the target_url to the main function
    run_vapt_toolkit(args.target_url)
