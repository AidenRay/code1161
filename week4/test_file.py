"""
Dictionaries
"""

"""
Loading Files
"""

"""
Requests
"""
import requests
# github, reddit, spotify
r = requests.get('https://api.github.com/user', auth=('AidenRay', '123Random'))
print(r.status_code)
print(r.text)


