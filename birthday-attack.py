import hashlib
import random

#BadHash40 function
#Parameter message: a hex string representing the message to be hashed
def BadHash40(message):
	#Encode the message into a byte format
	encodedMessage = bytes.fromhex(message)
	hash = hashlib.sha256(encodedMessage).hexdigest()

	#Return first 10 hex characters, which are the first 40 bits
	return hash[0:10]

n = 40
message_hashes = {}	#Will map hashes to messages
					#To allow for optimal search time

file = open("hash.csv", "w")

#Randomly generate 2^(n/2) messages and hashes
#While searching for collisions to ensure optimal running time
for i in range(0, int(2**(n/2))):
	#Generate random message of 256 bits
	random_message = random.getrandbits(256)

	#Convert to hex and remove leading '0x' characters
	hex_message = hex(random_message)[2:]

	#Ensure the message representation does have 64 hex characters
	#Since leading 0's can get removed
	while len(hex_message) != 64:
		hex_message = "0" + hex_message

	hash = BadHash40(hex_message)
	file.write(f"{random_message}, {hash}\n")

	#Check for collision
	if hash in message_hashes:
		print(f"Found collision.  BadHash40({random_message}) = {hash} = BadHash40({message_hashes[hash]})")
		file.close()
		exit()

	message_hashes[hash] = random_message		

print("Finished birthday attack.  No collision found; please run again.")
file.close()
