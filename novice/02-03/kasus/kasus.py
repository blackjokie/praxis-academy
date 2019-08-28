#!/usr/bin/env python3
import argparse
import concurrent.futures
import requests
import threading
import time

# make argument
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="input url (ex: https://google.com)", type=str, required=True)
args = vars(parser.parse_args())

thread_local = threading.local()

# function create session
def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

# function get respon from website
def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

# set total max. workers
def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

# pass argument "url" start function "download_site"
if __name__ == "__main__":
    sites = [
        args["url"],
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
