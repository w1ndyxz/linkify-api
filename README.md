# Linkify API
This project is unofficial. I am not responsible for any issues that may arise while using it

## Function Parameters
- **authorization**: Bearer token for authentication
- **link**: The URL to be shortened
- **name**: Custom name for the shortened link
- **mode**: Monetization type (string):
    - `1` - Off
    - `2` - Low
    - `3` - High
- **browser_targeting**: Enable browser targeting (`True` or `False`)
- **id**: Link ID (get via `getLinks`)
- **page**: Page number for retrieving links

## How to get a Bearer token
1. Log in to https://linkify.ru
2. Go to the main menu: https://linkify.ru/my/overview
3. Open your browsers developer console (usually F12)
4. Enter the following command:
   ```javascript
   localStorage.getItem("token")
   ```
5. Copy the returned token and use it as `bearerToken`

## Note
If you log out of the website, you will need to get the token again

## Donate
- **Toncoin (TON)**: `UQA1WjvbtTe6tXgrwLAaHtzwtZgJSYZCNZMIRN6kl6LOHc03`
