#!/usr/bin/python3
from wallet import walletgen
a = True
print("Please choose an option")
print("[0]: Generate a wallet")
print("[1]: Input a Private Key")
while a:
user = input("Choose one [0]: ")
if user == "0":
  print("Generating a Wallet... ")
  walletgen()
elif user == "1":
  key = input("Private Key: ")
