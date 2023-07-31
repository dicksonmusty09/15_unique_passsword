import random
import string

password = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 15))

print(password)