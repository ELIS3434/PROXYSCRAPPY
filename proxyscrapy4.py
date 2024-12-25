import requests
from bs4 import BeautifulSoup
import random
import time
from colorama import init, Fore, Style, Back

# List of websites to scrape proxies from
proxy_websites = [
    # Standard proxy lists
    "https://www.sslproxies.org/",
    "https://free-proxy-list.net/",
    "https://www.socks-proxy.net/",
    "https://www.proxy-list.download/SOCKS5",
    "https://www.proxynova.com/proxy-server-list/",
    "https://www.proxy-list.download/HTTP",
    "https://www.proxyscan.io/",
    "https://spys.one/en/",
    "https://hidemy.name/en/proxy-list/",
    
    # GitHub proxy lists
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    
    # Additional proxy websites
    "https://proxylist.geonode.com/api/proxy-list",
    "https://www.proxyniche.com/proxy-list/",
    "https://premproxy.com/proxy-list/",
    "https://www.proxy-daily.com/",
    "https://proxy-list.org/english/index.php",
    "https://www.freeproxylists.net/",
    "https://www.proxydocker.com/en/proxylist/",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
    
    # Additional GitHub sources
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list",
    "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
    "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt",
    "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/socks4.txt",
    "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/socks5.txt",
    
    # API endpoints
    "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=http%2Chttps%2Csocks4%2Csocks5",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    
    # Additional sources
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/socks5.txt",
    
    # More API endpoints
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5",
    "https://www.proxyscan.io/api/proxy?format=txt&level=anonymous",
    "https://www.proxyscan.io/api/proxy?format=txt&level=elite",
    "https://www.proxyscan.io/api/proxy?format=txt&type=http",
    "https://www.proxyscan.io/api/proxy?format=txt&type=socks4",
    "https://www.proxyscan.io/api/proxy?format=txt&type=socks5",
    
    # Additional proxy list websites
    "https://openproxy.space/list/http",
    "https://openproxy.space/list/socks4",
    "https://openproxy.space/list/socks5",
    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt"
]

def generate_random_credentials():
    usernames = ['user', 'proxy', 'anon', 'guest']
    passwords = ['pass', 'secure', 'proxy123', '12345']
    return random.choice(usernames), random.choice(passwords)

def format_proxy(ip, port, username=None, password=None, protocol=None, format_type=1):
    """
    Format proxy string based on user's choice:
    1. IP:PORT
    2. protocol://user:pass@ip:port
    3. user:pass@ip:port
    4. protocol://ip:port
    5. ip:port:user:pass
    6. protocol:ip:port
    7. protocol:ip:port:user:pass
    8. user:pass@ip:port
    9. protocol://user:pass@ip:port
    """
    if format_type == 1:
        return f"{ip}:{port}"
    elif format_type == 2:
        if not protocol:
            protocol = 'http'
        return f"{protocol}://{username}:{password}@{ip}:{port}"
    elif format_type == 3:
        return f"{username}:{password}@{ip}:{port}"
    elif format_type == 4:
        if not protocol:
            protocol = 'http'
        return f"{protocol}://{ip}:{port}"
    elif format_type == 5:
        return f"{ip}:{port}:{username}:{password}"
    elif format_type == 6:
        if not protocol:
            protocol = 'http'
        return f"{protocol}:{ip}:{port}"
    elif format_type == 7:
        if not protocol:
            protocol = 'http'
        return f"{protocol}:{ip}:{port}:{username}:{password}"
    elif format_type == 8:
        return f"{username}:{password}@{ip}:{port}"
    elif format_type == 9:
        if not protocol:
            protocol = 'http'
        return f"{protocol}://{username}:{password}@{ip}:{port}"
    else:
        return f"{ip}:{port}"

def scrape_proxies(url, format_type):
    proxies = []
    try:
        # Print the URL being scraped for debugging
        print(f"{Fore.YELLOW}Scraping URL: {url}{Style.RESET_ALL}")
        
        # Fetch the content
        response = requests.get(url, timeout=10)
        
        # Print raw response content for debugging
        print(f"{Fore.BLUE}Raw response content (first 500 chars):{Style.RESET_ALL}")
        print(response.text[:500])
        
        # Different parsing strategies based on URL
        if 'github.com' in url or url.endswith('.txt'):
            # For raw text files, split by lines
            raw_proxies = response.text.split('\n')
        else:
            # For web pages, use BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Try to find proxy-like text
            raw_proxies = [
                text.strip() 
                for text in soup.get_text().split('\n') 
                if ':' in text
            ]
        
        # Print raw proxies found
        print(f"{Fore.GREEN}Raw proxies found: {len(raw_proxies)}{Style.RESET_ALL}")
        
        # Process each raw proxy
        for raw_proxy in raw_proxies:
            # Clean and validate proxy
            cleaned_proxy = raw_proxy.strip()
            
            # Basic proxy format check
            if ':' in cleaned_proxy:
                try:
                    ip, port = cleaned_proxy.split(':')
                    # Validate IP and port
                    ip_parts = ip.split('.')
                    if (len(ip_parts) == 4 and 
                        all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts) and
                        port.isdigit() and 0 < int(port) <= 65535):
                        
                        # Optional: format based on user's choice
                        formatted_proxy = format_proxy(ip, port, format_type=format_type)
                        proxies.append(formatted_proxy)
                        print(f"{Fore.GREEN}✓ Valid proxy: {formatted_proxy}{Style.RESET_ALL}")
                except Exception as e:
                    # Silently ignore invalid proxies
                    pass
        
        print(f"{Fore.CYAN}Processed proxies: {len(proxies)}{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}Error scraping {url}: {str(e)}{Style.RESET_ALL}")
    
    return proxies

def save_proxies_to_file(proxies, filename):
    # Debug: print total number of input proxies
    print(f"{Fore.YELLOW}Total input proxies: {len(proxies)}{Style.RESET_ALL}")
    
    with open(filename, 'w') as f:
        # Comprehensive list of unwanted patterns to remove
        unwanted_patterns = [
            # Previous patterns
            'Proxy servers sorted by country',
            'Proxies sorted by ASN/ORG',
            'Proxy servers sorted by cities',
            'Free SSL/HTTPS',
            'Proxy servers sorted by ports',
            'Squid proxy servers',
            'Mikrotik open proxies list',
            'Anonymous proxies',
            'IP checker / Anonymity test',
            'SOCKS proxy list',
            'Proxy list TXT: Proxy servers sorted by',
            
            # New patterns based on the example you showed
            'Proxy search',
            'Country ALL',
            'Anonymity All proxies',
            'ANM & HIA',
            'Only HIA',
            'Only NOA',
            'Last 100:',
            'Port '
        ]
        
        # Filter out unwanted lines and clean up the proxies
        filtered_proxies = []
        for proxy in proxies:
            # Debug: print each proxy being processed
            print(f"{Fore.BLUE}Processing: {proxy}{Style.RESET_ALL}")
            
            # Skip lines containing any unwanted patterns
            if not any(pattern.lower() in proxy.lower() for pattern in unwanted_patterns):
                # Additional cleaning: remove any leading/trailing whitespace
                cleaned_proxy = proxy.strip()
                
                # Basic validation: ensure it looks like an IP:PORT
                parts = cleaned_proxy.split(':')
                if len(parts) == 2:
                    ip, port = parts
                    # Validate IP format (basic check)
                    ip_parts = ip.split('.')
                    if (len(ip_parts) == 4 and 
                        all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts) and
                        port.isdigit() and 0 < int(port) <= 65535):
                        filtered_proxies.append(cleaned_proxy)
                        print(f"{Fore.GREEN}✓ Valid proxy: {cleaned_proxy}{Style.RESET_ALL}")
        
        # Remove duplicates while preserving order
        unique_proxies = []
        seen = set()
        for proxy in filtered_proxies:
            if proxy not in seen:
                unique_proxies.append(proxy)
                seen.add(proxy)
        
        # Write cleaned proxies to file
        for proxy in unique_proxies:
            f.write(proxy + '\n')
    
    # Enhanced console output
    print(f"{Fore.GREEN}✓ {Fore.WHITE}Saved {Fore.YELLOW}{len(unique_proxies)}{Fore.WHITE} unique proxies to {Fore.CYAN}{filename}{Style.RESET_ALL}")

def gather_proxies(num_proxies, format_type):
    all_proxies = []
    total_scraped = 0
    
    print(f"{Fore.CYAN}🌐 Starting Proxy Gathering Process...{Style.RESET_ALL}")
    
    for url in proxy_websites:
        if len(all_proxies) >= num_proxies:
            break
        
        # Enhanced scraping status
        print(f"{Fore.YELLOW}➤ {Fore.WHITE}Scraping: {Fore.GREEN}{url}{Style.RESET_ALL}")
        
        proxies = scrape_proxies(url, format_type)
        total_scraped += len(proxies)
        all_proxies.extend(proxies)
        
        # Progress indicator
        print(f"{Fore.BLUE}  ↳ {Fore.WHITE}Gathered {Fore.YELLOW}{len(proxies)}{Fore.WHITE} proxies{Style.RESET_ALL}")
    
    # Remove duplicates and limit to requested number
    all_proxies = list(set(all_proxies))[:num_proxies]
    
    # Final summary
    print(f"\n{Fore.GREEN}✓ {Fore.WHITE}Proxy Gathering Complete{Style.RESET_ALL}")
    print(f"{Fore.CYAN}  Total Sources Scraped: {Fore.YELLOW}{len(proxy_websites)}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}  Total Proxies Scraped: {Fore.YELLOW}{total_scraped}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}  Unique Proxies Retained: {Fore.YELLOW}{len(all_proxies)}{Style.RESET_ALL}")
    
    return all_proxies

def get_format_choice():
    print(f"\n{Fore.CYAN}🔧 Proxy Format Selection{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Choose your desired proxy format:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}1. {Fore.WHITE}IP:PORT{Style.RESET_ALL}")
    print(f"{Fore.GREEN}2. {Fore.WHITE}protocol://user:pass@ip:port{Style.RESET_ALL}")
    print(f"{Fore.GREEN}3. {Fore.WHITE}user:pass@ip:port{Style.RESET_ALL}")
    print(f"{Fore.GREEN}4. {Fore.WHITE}protocol://ip:port{Style.RESET_ALL}")
    
    while True:
        try:
            choice = int(input(f"\n{Fore.YELLOW}Enter your choice (1-4): {Style.RESET_ALL}"))
            if 1 <= choice <= 4:
                return choice
            else:
                print(f"{Fore.RED}❌ Invalid choice. Please select between 1-4.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}❌ Please enter a valid number.{Style.RESET_ALL}")

def print_banner():
    """
    Print a vibrant and engaging banner for the proxy scraper
    """
    from colorama import init, Fore, Style, Back
    init(autoreset=True)
    
    banner = f"""
{Fore.CYAN}╔{'═' * 62}╗
{Fore.CYAN}║{Fore.WHITE}  🌐 Advanced Proxy Scraper & Anonymity Tool {' ' * 20}{Fore.CYAN}║
{Fore.CYAN}╠{'═' * 62}╣
{Fore.GREEN}║ Features:{Fore.WHITE}
{Fore.GREEN}║  ✓ Multi-Source Proxy Gathering
{Fore.GREEN}║  ✓ Proxy Format Customization
{Fore.GREEN}║  ✓ Anonymous Proxy Detection
{Fore.CYAN}╚{'═' * 62}╝{Style.RESET_ALL}
"""
    print(banner)

def main():
    # Clear screen (works on Windows and Unix-like systems)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_banner()
    
    try:
        num_proxies = int(input(f"{Fore.YELLOW}Enter number of proxies to gather: {Style.RESET_ALL}"))
        format_type = get_format_choice()
        
        print(f"\n{Fore.CYAN}🕹️ Proxy Gathering Configuration:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  Proxies Requested: {Fore.GREEN}{num_proxies}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  Format Type: {Fore.GREEN}{format_type}{Style.RESET_ALL}")
        
        proxies = gather_proxies(num_proxies, format_type)
        
        if proxies:
            filename = f"proxies_{time.strftime('%Y%m%d_%H%M%S')}.txt"
            save_proxies_to_file(proxies, filename)
        else:
            print(f"{Fore.RED}❌ No proxies could be gathered. Check your internet connection.{Style.RESET_ALL}")
    
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}❌ Operation cancelled by user.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
