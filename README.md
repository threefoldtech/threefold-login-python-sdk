# Python package for interacting with threefold login

## Usage

### Initialize the authenticator
```python
from ThreefoldLoginPkg import ThreefoldLogin
import string 
import random 

api_host = 'https://login.staging.jimber.org'
app_id = 'testapp'
seed_phrase = seed_phrase = 'calm science teach foil burst until ' \
              'next mango hole sponsor fold bottom ' \
              'cousin push focus track truly tornado ' \
              'turtle over tornado teach large fiscal'
redirect_url = "/callback"
kyc_backend_url = 'https://openkyc.staging.jimber.org'
authenticator = ThreefoldLogin (api_host,
    app_id,
    seed_phrase,
    redirect_url,
    kyc_backend_url
)
```

### Generate a login request
```python 
allowed = string.ascii_letters + string.digits
state = ''.join(random.SystemRandom().choice(allowed) for _ in range(32))
url = authenticator.generate_login_url(state)
```

### Redirect the user to the giving URL
Redirect the user to `url` 

### Callback
The callback will be send to `https://{app_id}/{redirect_url}`

```python
try:
    authenticator.parse_and_validate_redirect_url(callback_url, state)
    print('successfully validated login attempt')
    if authenticator.is_email_verified():
        print('email is verified')
    else:
        print('email is not verified')
except ValueError:
    print('failed to validate login attempt')
```