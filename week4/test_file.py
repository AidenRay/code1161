"""
save a file
"""
# can use ./
file1 = open("random.txt", 'w')
file1.write("RANDOM TEXT")
file1.close()

## relative pathing
filename = "desktop_file.txt"
filepath = "../../"  # my Desktop'
print(filepath + filename)
file2 = open('../../desktop_file.txt', 'w')
file2.write("DIFFERENT RANDOM TEXT")
file2.close()

"""
Loading and Reading Files
"""
random_file = open("random.txt",'r')
random_text = random_file.read()
print("the text in the file was: " + random_text)


"""
Dictionaries
"""
value = "hello"
my_dict = {"key": value}
my_nested_dict = {"Name": {"Last_Name": "Kerr", "First_Name": "Joe"},
                  "Date of Birth": {"Day": 1, "Month": "April", "Year": 1999},
                  "Height": 183}
print(my_dict["key"])
print(my_nested_dict["Height"])

"""
Loading and Dumping JSON Dicts to files
"""
import json
# magic conversion to json
my_json = json.dumps(my_nested_dict)
json_file = open('profile.json', 'w') 

json_file.write(my_json)
json_file.close()

open_json_file = open('profile.json', 'r')
open_json_file = open_json_file.read()
my_profile = json.loads(open_json_file)
# open_json_file.close()
"""
Requests and URLS
"""

import requests
import webbrowser

# https://en.wikipedia.org/wiki/Fibonacci_number#Origins
# github, reddit, spotify
# http://docs.python-requests.org/en/master/

r = requests.get('https://api.github.com/user', auth=('Username', 'Password'))
r_json = r.json()
# because I'm not gonig to hsow you my password
r_json = {'login': '****', 'id': 22095390, 'avatar_url': 'https://avatars0.githubusercontent.com/u/22095390?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/AidenRay', 'html_url': 'https://github.com/AidenRay', 'followers_url': 'https://api.github.com/users/AidenRay/followers', 'following_url': 'https://api.github.com/users/AidenRay/following{/other_user}', 'gists_url': 'https://api.github.com/users/AidenRay/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/AidenRay/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/AidenRay/subscriptions', 'organizations_url': 'https://api.github.com/users/AidenRay/orgs', 'repos_url': 'https://api.github.com/users/AidenRay/repos', 'events_url': 'https://api.github.com/users/AidenRay/events{/privacy}', 'received_events_url': 'https://api.github.com/users/AidenRay/received_events', 'type': 'User', 'site_admin': False, 'name': None, 'company': None, 'blog': '', 'location': None, 'email': None, 'hireable': None, 'bio': None, 'public_repos': 4, 'public_gists': 1, 'followers': 2, 'following': 4, 'created_at': '2016-09-09T09:04:58Z', 'updated_at': '2018-03-23T04:24:43Z', 'private_gists': 0, 'total_private_repos': 3, 'owned_private_repos': 2, 'disk_usage': 83383, 'collaborators':
          0, 'two_factor_authentication': False, 'plan': {'name': 'developer', 'space': 976562499, 'collaborators':
                                                          0, 'private_repos': 9999}}
print(r_json) 
webbrowser.open(r_json["followers_url"])


"""
Recursion
"""
def factorial_print(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(", n-1, "): ", res)
        return res


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def iterative_factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial_print(5))
print(factorial(7))
print(iterative_factorial(7))

""" exercise: Write the fibonnaci series recursively
e.g. fib(5) should return the 5th number in the fibonnaci series
0,1,1,2,3,5,8,13,21...

"""














def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(7))
"""
n= 1, fib: 0.000011, fibi:  0.000015, percent:       0.73
n= 2, fib: 0.000011, fibi:  0.000013, percent:       0.85
n= 3, fib: 0.000012, fibi:  0.000014, percent:       0.86
n= 4, fib: 0.000012, fibi:  0.000015, percent:       0.79
n= 5, fib: 0.000012, fibi:  0.000016, percent:       0.75
n= 6, fib: 0.000011, fibi:  0.000017, percent:       0.65
n= 7, fib: 0.000012, fibi:  0.000017, percent:       0.72
n= 8, fib: 0.000011, fibi:  0.000018, percent:       0.61
n= 9, fib: 0.000011, fibi:  0.000018, percent:       0.61
n=10, fib: 0.000010, fibi:  0.000020, percent:       0.50
n=11, fib: 0.000011, fibi:  0.000020, percent:       0.55
n=12, fib: 0.000004, fibi:  0.000007, percent:       0.59
n=13, fib: 0.000004, fibi:  0.000007, percent:       0.57
n=14, fib: 0.000004, fibi:  0.000008, percent:       0.52
n=15, fib: 0.000004, fibi:  0.000008, percent:       0.50
n=16, fib: 0.000003, fibi:  0.000008, percent:       0.39
n=17, fib: 0.000004, fibi:  0.000009, percent:       0.45
n=18, fib: 0.000004, fibi:  0.000009, percent:       0.45
n=19, fib: 0.000004, fibi:  0.000009, percent:       0.45
n=20, fib: 0.000003, fibi:  0.000010, percent:       0.29
n=21, fib: 0.000004, fibi:  0.000009, percent:       0.45
n=22, fib: 0.000004, fibi:  0.000010, percent:       0.40
n=23, fib: 0.000004, fibi:  0.000010, percent:       0.40
n=24, fib: 0.000004, fibi:  0.000011, percent:       0.35
n=25, fib: 0.000004, fibi:  0.000012, percent:       0.33
n=26, fib: 0.000004, fibi:  0.000011, percent:       0.34
n=27, fib: 0.000004, fibi:  0.000011, percent:       0.35
n=28, fib: 0.000004, fibi:  0.000012, percent:       0.32
n=29, fib: 0.000004, fibi:  0.000012, percent:       0.33
n=30, fib: 0.000004, fibi:  0.000013, percent:       0.31
n=31, fib: 0.000004, fibi:  0.000012, percent:       0.34
n=32, fib: 0.000004, fibi:  0.000012, percent:       0.33
n=33, fib: 0.000004, fibi:  0.000013, percent:       0.30
n=34, fib: 0.000004, fibi:  0.000012, percent:       0.34
n=35, fib: 0.000004, fibi:  0.000013, percent:       0.31
n=36, fib: 0.000004, fibi:  0.000013, percent:       0.31
n=37, fib: 0.000004, fibi:  0.000014, percent:       0.29
n=38, fib: 0.000004, fibi:  0.000014, percent:       0.29
n=39, fib: 0.000004, fibi:  0.000013, percent:       0.31
n=40, fib: 0.000004, fibi:  0.000014, percent:       0.29
"""
