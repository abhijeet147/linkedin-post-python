import requests

access_token = "your_access_token"
api_url = "https://api.linkedin.com/v2/ugcPosts"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

post_data = {
    "author": "urn:li:person:your_profile_id",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {"text": "Hello LinkedIn from Python!"},
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
}

response = requests.post(api_url, headers=headers, json=post_data)
print("Post Status:", response.status_code)
