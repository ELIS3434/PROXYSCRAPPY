import requests
from bs4 import BeautifulSoup
import random
import time
from colorama import init, Fore, Style, Back
import ipaddress

# Initialize colorama
init()

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

# Define IP ranges for different regions and countries
IP_RANGES = {
    'europe': {
        'ranges': [
            '2.0.0.0/8', '5.0.0.0/8', '31.0.0.0/8', '37.0.0.0/8', '46.0.0.0/8',
            '62.0.0.0/8', '77.0.0.0/8', '78.0.0.0/8', '79.0.0.0/8', '80.0.0.0/8',
            '81.0.0.0/8', '82.0.0.0/8', '83.0.0.0/8', '84.0.0.0/8', '85.0.0.0/8',
            '86.0.0.0/8', '87.0.0.0/8', '88.0.0.0/8', '89.0.0.0/8', '90.0.0.0/8',
            '91.0.0.0/8', '92.0.0.0/8', '93.0.0.0/8', '94.0.0.0/8', '95.0.0.0/8',
            '109.0.0.0/8', '178.0.0.0/8', '188.0.0.0/8', '193.0.0.0/8', '194.0.0.0/8',
            '195.0.0.0/8', '212.0.0.0/8', '213.0.0.0/8', '217.0.0.0/8'
        ],
        'countries': {
            'germany': ['46.0.0.0/8', '78.0.0.0/8', '91.0.0.0/8', '178.0.0.0/8', '217.0.0.0/8'],
            'france': ['2.0.0.0/8', '5.0.0.0/8', '37.0.0.0/8', '82.0.0.0/8', '88.0.0.0/8'],
            'uk': ['2.0.0.0/8', '5.0.0.0/8', '31.0.0.0/8', '77.0.0.0/8', '109.0.0.0/8'],
            'netherlands': ['2.0.0.0/8', '31.0.0.0/8', '77.0.0.0/8', '83.0.0.0/8', '84.0.0.0/8'],
            'italy': ['2.0.0.0/8', '5.0.0.0/8', '31.0.0.0/8', '37.0.0.0/8', '80.0.0.0/8'],
            'spain': ['2.0.0.0/8', '5.0.0.0/8', '31.0.0.0/8', '37.0.0.0/8', '81.0.0.0/8'],
            'poland': ['5.0.0.0/8', '31.0.0.0/8', '37.0.0.0/8', '46.0.0.0/8', '77.0.0.0/8'],
            'russia': ['2.0.0.0/8', '5.0.0.0/8', '31.0.0.0/8', '37.0.0.0/8', '46.0.0.0/8']
        }
    },
    'asia': {
        'ranges': [
            '1.0.0.0/8', '14.0.0.0/8', '27.0.0.0/8', '36.0.0.0/8', '39.0.0.0/8',
            '42.0.0.0/8', '43.0.0.0/8', '49.0.0.0/8', '58.0.0.0/8', '59.0.0.0/8',
            '60.0.0.0/8', '61.0.0.0/8', '101.0.0.0/8', '103.0.0.0/8', '106.0.0.0/8',
            '110.0.0.0/8', '111.0.0.0/8', '112.0.0.0/8', '113.0.0.0/8', '114.0.0.0/8',
            '115.0.0.0/8', '116.0.0.0/8', '117.0.0.0/8', '118.0.0.0/8', '119.0.0.0/8',
            '120.0.0.0/8', '121.0.0.0/8', '122.0.0.0/8', '123.0.0.0/8', '124.0.0.0/8',
            '125.0.0.0/8', '126.0.0.0/8', '175.0.0.0/8', '180.0.0.0/8', '182.0.0.0/8',
            '183.0.0.0/8', '202.0.0.0/8', '203.0.0.0/8', '210.0.0.0/8', '211.0.0.0/8',
            '218.0.0.0/8', '219.0.0.0/8', '220.0.0.0/8', '221.0.0.0/8', '222.0.0.0/8',
            '223.0.0.0/8'
        ],
        'countries': {
            'china': ['1.0.0.0/8', '14.0.0.0/8', '27.0.0.0/8', '36.0.0.0/8', '42.0.0.0/8'],
            'japan': ['1.0.0.0/8', '14.0.0.0/8', '27.0.0.0/8', '49.0.0.0/8', '58.0.0.0/8'],
            'korea': ['1.0.0.0/8', '14.0.0.0/8', '27.0.0.0/8', '39.0.0.0/8', '42.0.0.0/8'],
            'india': ['1.0.0.0/8', '14.0.0.0/8', '27.0.0.0/8', '39.0.0.0/8', '42.0.0.0/8'],
            'singapore': ['1.0.0.0/8', '14.0.0.0/8', '27.0.0.0/8', '36.0.0.0/8', '42.0.0.0/8'],
            'indonesia': ['1.0.0.0/8', '14.0.0.0/8', '27.0.0.0/8', '36.0.0.0/8', '39.0.0.0/8']
        }
    },
    'america': {
        'ranges': [
            '23.0.0.0/8', '24.0.0.0/8', '50.0.0.0/8', '63.0.0.0/8', '64.0.0.0/8',
            '65.0.0.0/8', '66.0.0.0/8', '67.0.0.0/8', '68.0.0.0/8', '69.0.0.0/8',
            '70.0.0.0/8', '71.0.0.0/8', '72.0.0.0/8', '73.0.0.0/8', '74.0.0.0/8',
            '75.0.0.0/8', '76.0.0.0/8', '96.0.0.0/8', '97.0.0.0/8', '98.0.0.0/8',
            '99.0.0.0/8', '107.0.0.0/8', '108.0.0.0/8', '138.0.0.0/8', '142.0.0.0/8',
            '162.0.0.0/8', '166.0.0.0/8', '167.0.0.0/8', '168.0.0.0/8', '169.0.0.0/8',
            '170.0.0.0/8', '172.0.0.0/8', '173.0.0.0/8', '174.0.0.0/8', '184.0.0.0/8',
            '192.0.0.0/8', '198.0.0.0/8', '199.0.0.0/8', '204.0.0.0/8', '205.0.0.0/8',
            '206.0.0.0/8', '207.0.0.0/8', '208.0.0.0/8', '209.0.0.0/8'
        ],
        'countries': {
            'usa': [
                '23.0.0.0/8', '24.0.0.0/8', '50.0.0.0/8', '63.0.0.0/8', '64.0.0.0/8',
                '65.0.0.0/8', '66.0.0.0/8', '67.0.0.0/8', '68.0.0.0/8', '69.0.0.0/8',
                '70.0.0.0/8', '71.0.0.0/8', '72.0.0.0/8', '73.0.0.0/8', '74.0.0.0/8'
            ],
            'canada': ['24.0.0.0/8', '50.0.0.0/8', '67.0.0.0/8', '69.0.0.0/8', '71.0.0.0/8'],
            'brazil': ['138.0.0.0/8', '142.0.0.0/8', '168.0.0.0/8', '170.0.0.0/8', '172.0.0.0/8'],
            'mexico': ['167.0.0.0/8', '168.0.0.0/8', '170.0.0.0/8', '172.0.0.0/8', '174.0.0.0/8'],
            'argentina': ['168.0.0.0/8', '170.0.0.0/8', '172.0.0.0/8', '174.0.0.0/8', '181.0.0.0/8']
        }
    }
}

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

def check_ip_region(ip, region):
    """
    Check if an IP belongs to a specific region or country
    """
    if region.lower() == 'all':
        return True
        
    try:
        ip_obj = ipaddress.ip_address(ip)
        
        # Check if region is a continent
        if region.lower() in ['europe', 'asia', 'america']:
            for ip_range in IP_RANGES[region.lower()]['ranges']:
                if ip_obj in ipaddress.ip_network(ip_range):
                    return True
        else:
            # Check if region is a country
            for continent in IP_RANGES.values():
                if region.lower() in continent['countries']:
                    for ip_range in continent['countries'][region.lower()]:
                        if ip_obj in ipaddress.ip_network(ip_range):
                            return True
        return False
    except Exception as e:
        print(f"{Fore.RED}Error checking IP region: {str(e)}{Style.RESET_ALL}")
        return False

def scrape_proxies(url, format_type, region):
    proxies = []
    try:
        print(f"{Fore.YELLOW}Scraping URL: {url}{Style.RESET_ALL}")
        
        response = requests.get(url, timeout=10)
        
        if 'github.com' in url or url.endswith('.txt'):
            raw_proxies = response.text.split('\n')
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            raw_proxies = [
                text.strip() 
                for text in soup.get_text().split('\n') 
                if ':' in text
            ]
        
        print(f"{Fore.GREEN}Raw proxies found: {len(raw_proxies)}{Style.RESET_ALL}")
        
        for raw_proxy in raw_proxies:
            cleaned_proxy = raw_proxy.strip()
            
            if ':' in cleaned_proxy:
                try:
                    ip, port = cleaned_proxy.split(':')[:2]
                    ip_parts = ip.split('.')
                    if (len(ip_parts) == 4 and 
                        all(0 <= int(part) <= 255 for part in ip_parts) and
                        0 <= int(port) <= 65535):
                        
                        # Check region filter
                        if check_ip_region(ip, region):
                            username, password = generate_random_credentials()
                            formatted_proxy = format_proxy(ip, port, username, password, None, format_type)
                            if formatted_proxy not in proxies:
                                proxies.append(formatted_proxy)
                
                except (ValueError, IndexError):
                    continue
                
    except Exception as e:
        print(f"{Fore.RED}Error scraping {url}: {str(e)}{Style.RESET_ALL}")
    
    return proxies

def save_proxies_to_file(proxies, filename):
    try:
        with open(filename, 'w') as f:
            for proxy in proxies:
                f.write(f"{proxy}\n")
        print(f"{Fore.GREEN}Successfully saved {len(proxies)} proxies to {filename}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error saving proxies to file: {str(e)}{Style.RESET_ALL}")

def get_region_choice():
    """
    Enhanced region selection with more options
    """
    print(f"\n{Fore.CYAN}Select Region Filter:{Style.RESET_ALL}")
    print("1. All (Default)")
    print("2. Europe")
    print("3. Asia")
    print("4. America")
    print("5. Specify Country")
    
    choice = input(f"\n{Fore.YELLOW}Enter your choice (1-5): {Style.RESET_ALL}")
    
    if choice == "5":
        print(f"\n{Fore.CYAN}Available Countries:{Style.RESET_ALL}")
        print("\nEurope:")
        print("- Germany, France, UK, Netherlands, Italy, Spain, Poland, Russia")
        print("\nAsia:")
        print("- China, Japan, Korea, India, Singapore, Indonesia")
        print("\nAmerica:")
        print("- USA, Canada, Brazil, Mexico, Argentina")
        
        country = input(f"\n{Fore.YELLOW}Enter country name: {Style.RESET_ALL}").lower()
        
        # Validate country input
        valid_countries = []
        for continent in IP_RANGES.values():
            valid_countries.extend(continent['countries'].keys())
        
        if country not in valid_countries:
            print(f"{Fore.RED}Invalid country. Using 'all' as default.{Style.RESET_ALL}")
            return "all"
        
        return country
    
    region_map = {
        "1": "all",
        "2": "europe",
        "3": "asia",
        "4": "america"
    }
    
    return region_map.get(choice, "all")

def get_format_choice():
    print(f"\n{Fore.CYAN}Select proxy format:{Style.RESET_ALL}")
    print("1. IP:PORT")
    print("2. protocol://user:pass@ip:port")
    print("3. user:pass@ip:port")
    print("4. protocol://ip:port")
    print("5. ip:port:user:pass")
    print("6. protocol:ip:port")
    print("7. protocol:ip:port:user:pass")
    print("8. user:pass@ip:port")
    print("9. protocol://user:pass@ip:port")
    
    choice = input(f"\n{Fore.YELLOW}Enter your choice (1-9): {Style.RESET_ALL}")
    return int(choice) if choice.isdigit() and 1 <= int(choice) <= 9 else 1

def print_banner():
    banner = """
    ╔═══════════════════════════════════════════╗
    ║             PROXY SCRAPER 5.0             ║
    ║         With Region Filtering!            ║
    ╚═══════════════════════════════════════════╝
    """
    print(f"{Fore.CYAN}{banner}{Style.RESET_ALL}")

def gather_proxies(num_proxies, format_type, region):
    all_proxies = []
    
    print(f"\n{Fore.CYAN}Starting proxy gathering...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Region Filter: {region.upper()}{Style.RESET_ALL}")
    
    for url in proxy_websites:
        if len(all_proxies) >= num_proxies:
            break
            
        new_proxies = scrape_proxies(url, format_type, region)
        all_proxies.extend(new_proxies)
        
        print(f"{Fore.GREEN}Total proxies gathered so far: {len(all_proxies)}{Style.RESET_ALL}")
        time.sleep(1)  # Delay to prevent rate limiting
    
    return list(set(all_proxies))[:num_proxies]

def main():
    print_banner()
    
    try:
        num_proxies = int(input(f"{Fore.YELLOW}Enter number of proxies to gather: {Style.RESET_ALL}"))
        format_type = get_format_choice()
        region = get_region_choice()
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"proxies_{timestamp}.txt"
        
        proxies = gather_proxies(num_proxies, format_type, region)
        save_proxies_to_file(proxies, filename)
        
    except ValueError:
        print(f"{Fore.RED}Please enter a valid number{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Proxy gathering interrupted{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
