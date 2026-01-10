import requests
import json
import time
import os

# Warna untuk terminal (biar keren ala Parrot OS)
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

def get_geo_info(ip=""):
    """Mengambil data geolocation dari API."""
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
    try:
        response = requests.get(url, timeout=10)
        return response.json()
    except Exception as e:
        return {"status": "fail", "message": str(e)}

def save_result(data):
    """Menyimpan hasil ke file txt."""
    filename = "tracking_results.txt"
    with open(filename, "a") as f:
        f.write(f"--- {time.ctime()} ---\n")
        f.write(json.dumps(data, indent=4))
        f.write("\n\n")
    print(f"{BLUE}[i] Hasil telah ditambahkan ke {filename}{RESET}")

def display_info(data):
    """Menampilkan informasi ke layar."""
    if data.get('status') == 'fail':
        print(f"{RED}[!] Gagal: {data.get('message')}{RESET}")
        return

    print(f"\n{GREEN}--- INFORMASI TARGET ---{RESET}")
    print(f"{YELLOW}IP Address  :{RESET} {data.get('query')}")
    print(f"{YELLOW}Negara     :{RESET} {data.get('country')} ({data.get('countryCode')})")
    print(f"{YELLOW}Kota       :{RESET} {data.get('city')}, {data.get('regionName')}")
    print(f"{YELLOW}Kode Pos   :{RESET} {data.get('zip')}")
    print(f"{YELLOW}ISP        :{RESET} {data.get('isp')}")
    print(f"{YELLOW}Organisasi :{RESET} {data.get('org')}")
    print(f"{YELLOW}Koordinat  :{RESET} {data.get('lat')}, {data.get('lon')}")
    print(f"{YELLOW}Timezone   :{RESET} {data.get('timezone')}")
    
    # Link Google Maps
    maps_link = f"https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}"
    print(f"{GREEN}Lokasi Peta:{RESET} {maps_link}")
    print(f"{GREEN}------------------------{RESET}")

    # Simpan otomatis
    save_result(data)

def main():
    os.system('clear')
    print(f"{BLUE}")
    print("="*45)
    print("   ADVANCED IP GEOLOCATION TRACKER   ")
    print("="*45 + f"{RESET}")
    
    print("1. Lacak IP Saya Sendiri")
    print("2. Lacak IP Spesifik")
    print("3. Keluar")
    
    choice = input(f"\n{YELLOW}Pilih opsi (1/2/3): {RESET}")

    if choice == '1':
        data = get_geo_info()
        display_info(data)
    elif choice == '2':
        ip_target = input(f"{YELLOW}Masukkan IP Target: {RESET}")
        data = get_geo_info(ip_target)
        display_info(data)
    elif choice == '3':
        print("Sampai jumpa!")
        exit()
    else:
        print(f"{RED}Opsi tidak valid!{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Program dihentikan.{RESET}")
