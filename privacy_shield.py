import requests
import time

# List of known tracker domains (you can add more)
TRACKERS = [
    "doubleclick.net",
    "google-analytics.com",
    "facebook.com",
    "adservice.google.com",
    "adnxs.com",
    "linkedin.com",
    "x.com",
    "youtube.com",
    "hp.com",
    "dell.com",
    "twitter.com",
    "instagram.com",
    "tiktok.com",
    "bing.com",
    "microsoft.com"
]

# Function to check if a domain is a tracker
def is_tracker(domain):
    for tracker in TRACKERS:
        if tracker in domain:
            return True
    return False

# Function to simulate blocking trackers
def block_trackers():
    print("Privacy Shield: Active")
    print("=" * 40)
    
    # Use your TRACKERS list + some allowed domains
    domains_to_check = TRACKERS + ["example.com", "mywebsite.com"]
    
    blocked = 0
    for domain in domains_to_check:
        if is_tracker(domain):
            print(f"BLOCKED: {domain}")
            blocked += 1
        else:
            print(f"ALLOWED: {domain}")
    
    print("=" * 40)
    print(f"Total trackers blocked: {blocked}")
    print("Privacy Shield: Running...")

# Main loop
while True:
    block_trackers()
    time.sleep(10)  # Check every 10 seconds
