import requests

def sql_injection_scan(url):
    # Define a list of common SQL injection payloads
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' OR '1'='1' #",
        "' OR '1'='1' /*",
    ]
    
    for payload in payloads:
        # Append the payload to the URL and send the request
        injection_url = f"{url}{payload}"
        print(f"Testing: {injection_url}")
        
        try:
            response = requests.get(injection_url, timeout=10)
            if "error" in response.text or "SQL" in response.text:
                print(f"[!] Potential SQL Injection vulnerability found at: {url}")
                return True
            else:
                print(f"[+] No SQL Injection vulnerability found at: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
    
    return False
