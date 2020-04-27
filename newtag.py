#!/usr/bin/python3
import hmac

def HashComparison():
    with open("tags.txt", "r") as f:
        with open("PATH_CRY_03_Lab_master.key", "r") as g:
            key = g.read()
            for line in f:
                plaintext, hash = line.strip().split(":")
                newhash = hmac.new(key.encode(), plaintext.encode()).hexdigest()
                if newhash != hash:
                    print(plaintext + " Has a BAD HASH!!!!!")

if __name__ == "__main__":
    HashComparison()
