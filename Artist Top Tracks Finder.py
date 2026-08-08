from dotenv import load_dotenv
import os
import base64
from requests import post, get
#import json


script_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path)  

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET") 


if not client_id or not client_secret:
    print(f"ERROR: Credentials not found!")
    print(f"Please make sure your .env file is exactly here: {dotenv_path}")
    print("And contains CLIENT_ID=your_id and CLIENT_SECRET=your_secret")
    exit(1)


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    
    json_result = result.json() 
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query
    
    result = get(query_url, headers=headers) 
    
    json_result = json.loads(result.content)
    items = json_result.get("artists", {}).get("items", [])
    
    if len(items) > 0:
        return items[0]
    else:
        print("No artist found.")
        return None

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

token = get_token()
artist = search_for_artist(token, "Adele")


if artist:
    artist_id = artist["id"]
    print(f"ID for artist {artist['name']} is: {artist_id}")

    
    top_tracks = get_songs_by_artist(token, artist_id)
    print(f"\nTop Tracks:")
    for idx, track in enumerate(top_tracks):
        print(f"{idx + 1}. {track['name']}")
