import os

# reading an entire file as a single string
with open('Project_description2.txt', 'rt') as f:
    data = f.read()
    f.close()
print(data)

# Built a real estate web application using Python(Django)
# that Manage listings, realtors, contact inquiries and
# website users via admin. I've learned and gained
# experienced using PostgreSQL in a large scale in
# a team of 3 developers as freelancers.
#
# Built a online Web Store application using Python(Django) that
# Manage game, shipping, customer inquiries and online payment.
# I've learned and gained experienced using MySQL and GatewayAPI.
#
# Built  Rest API using Django Rest Framework.
# I gained experiences and learned how interact API and Implement API.

# --printing to a file
with open('description2.txt', 'wt') as f:
    print('Thank you!', file=f)

# writing to a file that doesn't already exist
# with open('newtext.txt', 'xt') as f:
#     f.write('Hello World!')

# check if file already exist
if not os.path.exists('newtext.txt'):
    with open('newtext.txt', 'wt') as f:
        f.write("I like Pyhton")
else:
    print('File already exists!')

# File already exists!