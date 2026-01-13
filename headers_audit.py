import requests

def audit_headers(url):
    print(f"🚀 mimic_ starting audit on: {url}\n")
    
    # Custom headers to mimic a real browser (avoids IP blocks)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
        'X-mimic-audit': 'active'
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        security_headers = ['Content-Security-Policy', 'Strict-Transport-Security', 'X-Frame-Options']
        
        for header in security_headers:
            if header in response.headers:
                print(f"[+] {header} is present.")
            else:
                print(f"[❌] MISSING: {header} - Potential vulnerability found!")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target = "https://google.com" # Change this to test other sites
    audit_headers(target)
