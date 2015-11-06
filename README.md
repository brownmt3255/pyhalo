# pyhalo

Python Wrapper for the Halo 5 API. More features to come.

Dependencies: 'requests' Python module.

Usage Example:
```
from pyhalo import PyHalo

ocp_apim_subscription_key = "my_api_key"
h = PyHalo(ocp_apim_subscription_key)

# Examples!
campaign_missions_json = h.get_campaign_missions()
emblem_image_url = h.get_emblem_image("Major Nelson")
player_matches_json = h.get_player_matches("Major Nelson")
service_records_json = h.get_arena_service_records(["Major Nelson", "B is for Bravo"])
```
