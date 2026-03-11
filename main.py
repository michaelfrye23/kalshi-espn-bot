import requests
import json

response = requests.get('https://site.web.api.espn.com/apis/site/v2/sports/basketball/nba/summary?region=us&lang=en&contentorigin=espn&event=400878160')

print(response.status_code)
print(json.dumps(response.json(), indent=2))
