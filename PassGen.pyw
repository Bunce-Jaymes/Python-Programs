import string
import random

def main(size=140, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    password= "".join(random.choice(chars) for _ in range(size))
    print (password)
while True:
    main()
