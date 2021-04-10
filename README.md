# TCP_CHAT-with-hybrid-encription



## Main contents of the project

1. What is the hybrid system and cryptography schema
2. RSA implementation 
3. AES/DES implementation 
4. Hybrid implementation 
5. GUI
6. Demonstration
7. Presantation

## Presentation
1. Introduction
2. About RSA Algorithm
3. About AES Algorithm
4. About DES Algorithm
5. About hybrid system
6. Analytical informations
7. Conclusions

**GCM mode**

Galois/Counter Mode, defined in NIST SP 800-38D. It only works in combination with a 128 bits cipher like AES.

The new() function at the module level under Crypto.Cipher instantiates a new GCM cipher object for the relevant base algorithm.

Crypto.Cipher.<algorithm>.new(key, mode, *, nonce=None, mac_len=None)
Create a new GCM object, using <algorithm> as the base block cipher.

Parameters:	
key (bytes) – the cryptographic key
mode – the constant Crypto.Cipher.<algorithm>.MODE_GCM
nonce (bytes) – the value of the fixed nonce. It must be unique for the combination message/key. If not present, the library creates a random nonce (16 bytes long for AES).
mac_len (integer) – the desired length of the MAC tag, from 4 to 16 bytes (default: 16).
Returns:	
a GCM cipher object

The cipher object has a read-only attribute nonce.

## If you want to execute this code, do below steps

1. First install th python
Visit this  site install - [https://www.python.org/downloads/]

2. Then install library that given below
Using this commands to install the library
  ```sh
 pip install pycrptodome
  ```
  
 3. Then you goto folder that pyhton install then copy the hybrid.py into the Lib file
 **After you can goto the path that repo store using cmd**
 **Then you can run Server using cmd**
 
  ```sh
 python server.py
  ```
 4. Then you can run the client files using several cmd
 
  ```sh
 python client.py
  ```
