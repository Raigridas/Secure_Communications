# Code taken from the lab sheet
import hashlib # importing the hashing library
some_string = "a2c83976c0adb482d280c6b10a042be3" # string is equal to some hash

hash = hashlib.md5() # specifying that we want to generate an md5 hash
hash.update((some_string).encode('utf-8')) # Generating the new hash, Unicode-objects must be encoded before hashing
print(hash.hexdigest()) # printing out the new hash value in the terminal

# nOOB = 4e0f9abf5b2e92b2cb1a1db1ee9c635c
# Noob = 654e1c2ac6312d8c6441282f155c8ce9

# ECSC = 5999842f44322b079b0a554f24dc4ea9
# ecsc = a2c83976c0adb482d280c6b10a042be3


# assuming that ecsc is the seed value, i manually tried to enter in the hash value until i found the value that we are looking for
# a2c83976c0adb482d280c6b10a042be3
# 41aacd22906a9bb855a12904e6a73296
# b6f0bbbcef793d9c0a89445eaf320992
# 6e1ef5d394cdbead0fc0fbeddbccf5bf
# b051020ce5c5a405f1eb901855ff33b0
# 492c1fe60a52d226aa7b6ba42f675c0d
# 6062076d6aa4dd0541fff278dfad5c7e
# 9305db6dc8fb8dc426076981f4ac7283
# 16124413ceccd0da014cc6a60974e3ae
# 4ba61864b13ecdb7aa66835be1dee5b2
# 0fe395003e8ffbb9429b3db91f0f9e86
# bc70b828e6f53430b2f4840bac7a58a1
# 2cdfe943949e962cd49ffcef6cabf1d9
# f81843c16a34124dcb31e5e06f7a08be
# 6d11282336c12d2c61b7592823318f7c
# 66c9fed319d1526e05f8d7e8cda744b0
# 1e5f327cab56a0d05cb1654dfc2c0ba9
# 8ea8165ea3efbef1c46a11f33ef1573e
# 999d079d33e4780f0baca8821ae0ab73


# trying to loop the hashing function until the i value is found, unsuccessful however, only scanned through numbers and not letters, and a string cant be entered in range()
# for i in range(99999999999999999999999999999999):
#     if i == 'c89aa2ffb9edcc6604005196b5f0e0e4':
#         continue
#     print(i)
