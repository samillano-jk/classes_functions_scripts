import os
import requests
import hashlib
import subprocess

API_KEY = "Virus_total api key"
FOLDER = "file_path_to_scan"
VT_URL = "https://www.virustotal.com/api/v3/files/"
HEADERS = {"x-apikey": API_KEY}

def get_file_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def vt_scan(file_hash):
    url = VT_URL + file_hash
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        if response.status_code == 200:
            stats = response.json()["data"]["attributes"]["last_analysis_stats"]
            return stats
        else:
            return None
    except:
        return None

def clamav_scan(file_path):
    print("🛡️ Running ClamAV scan...")
    result = subprocess.run(["clamscan", file_path], capture_output=True, text=True)
    print(result.stdout)

def main():
    for file in os.listdir(FOLDER):
        if file.endswith(".apk"):
            file_path = os.path.join(FOLDER, file)
            print(f"\n🔎 Checking: {file}")

            # Step 1: VirusTotal
            file_hash = get_file_hash(file_path)
            stats = vt_scan(file_hash)
            if stats:
                print(f"🔒 VirusTotal results: {stats}")
            else:
                print(f"⚠️ No VirusTotal report available.")

            # Step 2: Always run ClamAV
            clamav_scan(file_path)

if __name__ == "__main__":
    main()
