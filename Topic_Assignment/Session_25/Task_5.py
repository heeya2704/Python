# Use ChatGPT or Copilot to generate Python code that demonstrates the first step of an 
# OAuth 2.0 login flow (for example, generating the URL to redirect a user to Spotify's 
# OAuth login page). Paste the generated code and briefly explain what it does.

import urllib.parse

# --- Generated Code: Step 1 of OAuth 2.0 Authorization Flow ---

CLIENT_ID = "your_spotify_client_id"
REDIRECT_URI = "https://localhost:8888/callback"
SCOPE = "user-read-private user-read-email playlist-read-private"
RESPONSE_TYPE = "code"
AUTH_BASE_URL = "https://accounts.spotify.com/authorize"

def generate_spotify_auth_url():
    """
    Generates the Spotify OAuth 2.0 authorization URL to redirect users for login.
    """
    params = {
        "client_id": CLIENT_ID,
        "response_type": RESPONSE_TYPE,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        "state": "random_secure_state_string_123"
    }
    
    auth_url = f"{AUTH_BASE_URL}?{urllib.parse.urlencode(params)}"
    return auth_url

if __name__ == "__main__":
    url = generate_spotify_auth_url()
    print("Generated Spotify OAuth 2.0 Login URL:")
    print(url)
    
    print("\nExplanation:")
    print("1. This code constructs an authorization URL using Spotify's OAuth 2.0 auth endpoint.")
    print("2. It includes parameters: client_id (app identifier), response_type ('code' for authorization code flow),")
    print("   redirect_uri (where Spotify redirects back after login), scope (permissions requested), and state (CSRF protection).")
    print("3. When a user opens this URL, Spotify prompts them to log in and authorize the application.")
