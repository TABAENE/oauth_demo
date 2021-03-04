# oauth_demo

## Steps to get your token and use your API - 

 - Point your browser to http://127.0.0.1:8000/o/applications/register/ lets create an application.

 - Hit below URL: This identifies your application, the user is asked to authorize your application to access its resources.
http://127.0.0.1:8000/o/authorize/?response_type=code&client_id=eM9iQSn7iT1GjQOSAjaYRww2TNf3RlM2RsdmPtn8&redirect_uri=http://127.0.0.1:8000/noexist/callback

 - on registration you will be redirected to below URL.
http://127.0.0.1:8000/noexist/callback?code=lxZjgcWB2c3ZGYMXxoh804FP40FK9d

 - Now that you have the user authorization is time to get an access token:
 
curl -X POST \
    -H "Cache-Control: no-cache" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    "http://127.0.0.1:8000/o/token/" \
    -d "client_id=eM9iQSn7iT1GjQOSAjaYRww2TNf3RlM2RsdmPtn8" \
    -d "client_secret=AJuLUWfAlVbblVLmfyMMTnJkBs2RIRJLkVMYVzf1Hj9vq6DhT3PaSEJ5gmn6xf4RqRWwj1E6fPiMFbqkTWJDRLcGhSSR7XRvqakE4q63HdDr5lYhdhWGn9CXAEFKrybr" \
    -d "code=wJ0Y9N9S0nWgQsDJyofMR0dFUfbjH8" \
    -d "redirect_uri=http://127.0.0.1:8000/noexist/callback" \
    -d "grant_type=authorization_code"

 - To access the user resources we just use the access_token:
 
curl \
    -H "Authorization: Bearer xAgIQn9MbujwB0MOEUhrgtTHToAZt4" \
    -X GET http://localhost:8000/resource
