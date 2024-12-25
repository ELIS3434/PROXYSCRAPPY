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
        time.sleep(2)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        if url.startswith('https://raw.githubusercontent.com'):
            response = requests.get(url, headers=headers, timeout=10)
            for line in response.text.splitlines():
                if ':' in line:
                    ip, port = line.strip().split(':')
                    if format_type != 1:  # If not simple IP:PORT format
                        username, password = generate_random_credentials()
                        protocol = 'socks5' if 'socks5' in url.lower() else 'http'
                        proxy = format_proxy(ip, port, username, password, protocol, format_type)
                    else:
                        proxy = format_proxy(ip, port, format_type=format_type)
                    proxies.append(proxy)
            return proxies
            
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try different patterns to find proxies in the HTML
        for row in soup.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) >= 2:
                try:
                    ip = cols[0].text.strip()
                    port = cols[1].text.strip()
                    if format_type != 1:  # If not simple IP:PORT format
                        username, password = generate_random_credentials()
                        protocol = 'http'  # Default to HTTP for HTML-scraped proxies
                        proxy = format_proxy(ip, port, username, password, protocol, format_type)
                    else:
                        proxy = format_proxy(ip, port, format_type=format_type)
                    proxies.append(proxy)
                except:
                    continue
                    
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
    return proxies

def save_proxies_to_file(proxies, filename):
    with open(filename, 'w') as f:
        for proxy in proxies:
            f.write(f"{proxy}\n")
    print(f"Saved {len(proxies)} proxies to {filename}")

def gather_proxies(num_proxies, format_type):
    all_proxies = []
    for url in proxy_websites:
        if len(all_proxies) >= num_proxies:
            break
        print(f"Scraping {url}...")
        proxies = scrape_proxies(url, format_type)
        all_proxies.extend(proxies)
        
    # Remove duplicates and limit to requested number
    all_proxies = list(set(all_proxies))[:num_proxies]
    return all_proxies

def print_banner():
    """
    Print a vibrant and engaging banner for the proxy scraper
    """
    from colorama import init, Fore, Style, Back
    init(autoreset=True)
    
    banner = f"""
{Fore.CYAN}╔{'═' * 62}╗
{Fore.CYAN}║{Fore.MAGENTA}{Style.BRIGHT}  🌐 ProxyScrappy 3.0: Ultimate Proxy Harvesting Toolkit 🕸️  {Fore.CYAN}║
{Fore.CYAN}╠{'═' * 62}╣
{Fore.GREEN}║ 🚀 {Fore.WHITE}Blazing Fast Proxy Scraper{Fore.GREEN}               Performance Unleashed! ║
{Fore.GREEN}║ 🌈 {Fore.WHITE}Multiple Format Support{Fore.GREEN}                 Flexibility Redefined! ║
{Fore.GREEN}║ 🔒 {Fore.WHITE}Anonymity & Security{Fore.GREEN}                    Your Privacy Matters! ║
{Fore.GREEN}║ 🌍 {Fore.WHITE}Global Proxy Coverage{Fore.GREEN}                   Worldwide Connections! ║
{Fore.CYAN}╚{'═' * 62}╝
{Style.RESET_ALL}"""
    print(banner)

def get_format_choice():
    while True:
        print(f"{Fore.YELLOW}{Style.BRIGHT}🌈 Proxy Format Selection Menu 🌈{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╔{'═' * 70}╗")
        print(f"{Fore.CYAN}║ {Fore.MAGENTA}🔢 Choose Your Desired Proxy Format Transformation {Fore.CYAN}║")
        print(f"{Fore.CYAN}╠{'═' * 70}╣")
        
        formats = [
            (f"{Fore.CYAN}1. 📍 IP:PORT{Style.RESET_ALL}", "Basic IP:Port"),
            (f"{Fore.GREEN}2. 🔐 protocol://user:pass@ip:port{Style.RESET_ALL}", "Secure Authenticated"),
            (f"{Fore.BLUE}3. 🔑 user:pass@ip:port{Style.RESET_ALL}", "Simple Authentication"),
            (f"{Fore.MAGENTA}4. 🌐 protocol://ip:port{Style.RESET_ALL}", "Protocol Specified"),
            (f"{Fore.RED}5. 🔢 ip:port:user:pass{Style.RESET_ALL}", "Colon Separated"),
            (f"{Fore.YELLOW}6. 🚦 protocol:ip:port{Style.RESET_ALL}", "Protocol Prefix"),
            (f"{Fore.GREEN}7. 🛡️ protocol:ip:port:user:pass{Style.RESET_ALL}", "Full Protocol Auth"),
            (f"{Fore.BLUE}8. 🔓 user:pass@ip:port{Style.RESET_ALL}", "Auth with @ Symbol"),
            (f"{Fore.MAGENTA}9. 🌍 protocol://user:pass@ip:port{Style.RESET_ALL}", "Ultimate Format")
        ]
        
        for idx, (format_display, description) in enumerate(formats, 1):
            print(f"{Fore.CYAN}║ {format_display} {Fore.WHITE}➤ {description}{' ' * (50 - len(description))}{Fore.CYAN}║")
        
        print(f"{Fore.CYAN}╚{'═' * 70}╝{Style.RESET_ALL}")
        
        print("\n📝 Example Showcase:")
        examples = [
            f"{Fore.CYAN}1. 192.168.1.1:8080{Style.RESET_ALL}",
            f"{Fore.GREEN}2. http://user:pass@192.168.1.1:8080{Style.RESET_ALL}",
            f"{Fore.BLUE}3. user:pass@192.168.1.1:8080{Style.RESET_ALL}",
            f"{Fore.MAGENTA}4. http://192.168.1.1:8080{Style.RESET_ALL}",
            f"{Fore.RED}5. 192.168.1.1:8080:user:pass{Style.RESET_ALL}",
            f"{Fore.YELLOW}6. http:192.168.1.1:8080{Style.RESET_ALL}",
            f"{Fore.GREEN}7. http:192.168.1.1:8080:user:pass{Style.RESET_ALL}",
            f"{Fore.BLUE}8. user:pass@192.168.1.1:8080{Style.RESET_ALL}",
            f"{Fore.MAGENTA}9. http://user:pass@192.168.1.1:8080{Style.RESET_ALL}"
        ]
        
        for idx, example in enumerate(examples, 1):
            print(f"{Fore.WHITE}➤ Option {idx}: {example}")
        
        try:
            choice = int(input(f"\n{Fore.YELLOW}🎯 Select Your Proxy Format (1-9): {Style.RESET_ALL}"))
            if 1 <= choice <= 9:
                return choice
            else:
                print(f"{Fore.RED}❌ Please choose a number between 1 and 9{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}❌ Invalid input. Please enter a number.{Style.RESET_ALL}")

def main():
    print_banner()
    print(f"Available proxy sources: {len(proxy_websites)}")
    
    # Get user preferences
    format_type = get_format_choice()
    
    try:
        num_proxies = int(input("How many proxies do you want to gather? "))
    except ValueError:
        print("Invalid input. Using default value of 50")
        num_proxies = 50
    
    # Generate output filename based on format
    format_names = {
        1: "simple",
        2: "full_auth",
        3: "auth",
        4: "protocol",
        5: "auth_append",
        6: "protocol_simple",
        7: "protocol_auth",
        8: "auth",
        9: "full_auth"
    }
    output_file = f"proxies_{format_names[format_type]}.txt"
    
    print(f"\nGathering {num_proxies} proxies...")
    proxies = gather_proxies(num_proxies, format_type)
    save_proxies_to_file(proxies, output_file)
    
    print("\nDone! Check the output file for your proxies.")

if __name__ == "__main__":
    main()
