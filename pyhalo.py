#!/usr/bin/env python
"""
__pyhalo__

Python wrapper for the Halo 5 API provided at https://www.haloapi.com
"""

import requests
import json


class PyHalo:

    def __init__(self, api_key):
        """
        Initialize the PyHalo object with
        the 'Ocp-Apim-Subscription-Key' provided.

        :param str api_key: The 'Ocp-Apim-Subscription-Key' provided.
        """
        self.api_key = api_key
        self.root_url = "https://www.haloapi.com"
        self.title = "h5"

    def _haloapi_request(self, url, params=None):
        """
        Make a request to the provided haloapi target url.

        :param str url: The haloapi target url.
        :returns Response: Request's response.
        """
        headers = {'Ocp-Apim-Subscription-Key': self.api_key}
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response

    def _metadata_request(self, endpoint, params=None):
        """
        Make a request to the provided haloapi metadata endpoint.
        
        :param str endpoint: The target metadata endpoint.
        :param dict params: A list of (optional) params to send with the request.
        :returns dict: Response JSON.
        """
        url = "{root}/metadata/{title}/metadata/{endpoint}".format(
                root=self.root_url,
                title=self.title,
                endpoint=endpoint
            )
        response = self._haloapi_request(url, params)
        return response.json()

    def get_campaign_missions(self):
        """
        Retrieves campaign metadata.
        """
        return self._metadata_request("campaign-missions")

    def get_commendations(self):
        """
        Retrieves commendations metadata.
        """
        return self._metadata_request("commendations")

    def get_csr_designations(self):
        """
        Retrieves CSR designations metadata.
        """
        return self._metadata_request("csr-designations")

    def get_enemies(self):
        """
        Retrieves enemies metadata.
        """
        return self._metadata_request("enemies")

    def get_flexible_stats(self):
        """
        Retrieves flexible stats metadata.
        """
        return self._metadata_request("flexible-stats")

    def get_game_base_variants(self):
        """
        Retrieves game-base-variants metadata.
        """
        return self._metadata_request("game-base-variants")

    def get_game_variant(self, id):
        """
        Retrieves game varient metadata.

        :param str id: The game variant id.
        """
        return self._metadata_request("game-variants/{id}".format(id=id))

    def get_impulses(self):
        """
        Retrieves impulses metadata.
        """
        return self._metadata_request("impulses")

    def get_map_variant(self, id):
        """
        Retrieves map varient metadata.

        :param str id: The map variant id.
        """
        return self._metadata_request("map-variants/{id}".format(id=id))

    def get_maps(self):
        """
        Retrieves maps metadata.
        """
        return self._metadata_request("maps")

    def get_medals(self):
        """
        Retrieves medals metadata.
        """
        return self._metadata_request("medals")

    def get_playlists(self):
        """
        Retrieves playlists metadata.
        """
        return self._metadata_request("playlists")

    def get_requisition_pack(self, id):
        """
        Retrieves REQ pack metadata.

        :param str id: The REQ pack id.
        """
        return self._metadata_request("requisition-packs/{id}".format(id=id))

    def get_requisition(self, id):
        """
        Retrieves REQ item metadata.

        :param str id: The REQ item id.
        """
        return self._metadata_request("requisitions/{id}".format(id=id))    

    def get_skulls(self):
        """
        Retrieves skulls metadata.
        """
        return self._metadata_request("skulls")  

    def get_spartan_ranks(self):
        """
        Retrieves spartan ranks metadata.
        """
        return self._metadata_request("spartan-ranks")

    def get_team_colors(self):
        """
        Retrieves team-color metadata.
        """
        return self._metadata_request("team-colors")  

    def get_vehicles(self):
        """
        Retrieves vehicles metadata.
        """
        return self._metadata_request("vehicles")

    def get_weapons(self):
        """
        Retrieves weapons metadata.
        """
        return self._metadata_request("weapons")

    def _profile_request(self, endpoint, params=None):
        """
        Make a request to the provided haloapi profile endpoint.
        
        :param str endpoint: The target profile endpoint.
        :param dict params: Optional list of params to send with the request.
        :returns str: Image URL.
        """
        url = "{root}/profile/{title}/profiles/{endpoint}".format(
                root=self.root_url,
                title=self.title,
                endpoint=endpoint
            )
        response = self._haloapi_request(url, params)
        for response_history in response.history:
            return response_history.headers["Location"]


    def get_emblem_image(self, player, size=None):
        """
        Get a URL to the emblem image for the specified player.
        
        :param str player: The player's gamertag.
        :param int size: The size (in pixels) of the emblem in the returned URL.
                         Value must be one of: 95, 128, 190, 256, 512, or None,
                         otherwise a HTTP 400 will be returned.
        :returns str: The URL of the emblem.
        """
        endpoint = "{player}/emblem".format(
                player=player
            )
        params = dict()
        if size is not None:
            params['size'] = size
        return self._profile_request(endpoint, params)

    def get_spartan_image(self, player, size=None, crop=None):
        """
        Get a URL to the emblem image for the specified player.
        
        :param str player: The player's gamertag.
        :param int size: The size (in pixels) of the emblem in the returned URL.
                         Value must be one of: 95, 128, 190, 256, 512, or None,
                         otherwise a HTTP 400 will be returned.
        :param str crop: An optional crop that will be used to determine what
                         portion of the Spartan is returned in the image. The
                         value must be either "full" or "portrait". If no value
                         is specified, "full" is used. If an unsupported value is
                         provided, the API returns HTTP 400 ("Bad Request").
        :returns str: The URL of the emblem.
        """
        endpoint = "{player}/spartan".format(
                player = player
            )
        params = dict()
        if size is not None:
            params['size'] = size
        if crop is not None:
            params['crop'] = crop
        return self._profile_request(endpoint, params)

    def _stats_request(self, endpoint, params=None):
        """
        Make a request to the provided haloapi stats endpoint.
        
        :param str endpoint: The target stats endpoint.
        :param dict params: A list of (optional) params to send with the request.
        """
        url = "{root}/stats/{title}/{endpoint}".format(
                root=self.root_url,
                title=self.title,
                endpoint=endpoint
            )
        response = self._haloapi_request(url, params)
        return response.json()

    def get_player_matches(self, player, modes=None, start=None, count=None):
        """
        Retrieves a list of matches that the player has participated in
        and which have completed processing. If the player is currently
        in a match, it is not returned in this API. Matches will usually
        appear in this list within a minute of the match ending. 
        
        :param str player: Player's gamertag.
        :returns dict: JSON response.
        """
        endpoint = "players/{player}/matches".format(
                player=player
            )
        params = dict()
        if modes is not None:
            params['modes'] = modes
        if start is not None:
            params['start'] = start
        if count is not None:
            params['count'] = count
        return self._stats_request(endpoint, params)

    def get_arena_match(self, match_id):
        """
        Retrieves detailed statistics for a arena match. Some match details
        are available while the match is in-progress, but the behavior for 
        incomplete matches in undefined.
        
        :param str match_id: Unique arena match id.
        :returns dict: JSON response.
        """
        return _get_match(mode="arena", match_id=match_id)

    def get_campaign_match(self, match_id):
        """
        Retrieves detailed statistics for a campaign match. Some match details
        are available while the match is in-progress, but the behavior
        for incomplete matches in undefined. Every time a player plays
        a portion of a Campaign mission, a match will be generated whether
        the player finishes the mission or not. If the "match" ends because
        the mission was completed, this will be indicated in the response.
        
        :param str match_id: Unique campaign match id.
        :returns dict: JSON response.
        """
        return _get_match(mode="campaign", match_id=match_id)

    def get_custom_match(self, match_id):
        """
        Retrieves detailed statistics for a custom match. Some match details
        are available while the match is in-progress, but the behavior
        for incomplete matches in undefined.
        
        :param str match_id: Unique custom match id.
        :returns dict: JSON response.
        """
        return _get_match(mode="custom", match_id=match_id)

    def get_warzone_match(self, match_id):
        """
        Retrieves detailed statistics for a warzone match. Some match 
        details are available while the match is in-progress, but the 
        behavior for incomplete matches in undefined.
        
        :param str match_id: Unique warzone match id.
        :returns dict: JSON response.
        """
        return _get_match(mode="warzone", match_id=match_id)

    def _get_match(self, mode, match_id):
        endpoint = "{mode}/matches/{match_id}".format(
                mode=mode,
                match_id=match_id
            )
        return self._stats_request(endpoint)

    def get_arena_service_records(self, players):
        """
        Retrieves players' arena Service Records. A Service Record 
        contains a player's lifetime statistics in the game mode.
        
        :param list players: List of player gamertags.
        :returns dict: JSON response.
        """
        return self._get_service_records(mode="arena", players=players)

    def get_campaign_service_records(self, players):
        """
        Retrieves players' campaign Service Records. A Service Record 
        contains a player's lifetime statistics in the game mode.
        
        :param list players: List of player gamertags.
        :returns dict: JSON response.
        """
        return self._get_service_records(mode="campaign", players=players)

    def get_custom_service_records(self, players):
        """
        Retrieves players' custom game Service Records. A Service Record 
        contains a player's lifetime statistics in the game mode.
        
        :param list players: List of player gamertags.
        :returns dict: JSON response.
        """
        return self._get_service_records(mode="custom", players=players)

    def get_warzone_service_records(self, players):
        """
        Retrieves players' warzone Service Records. A Service Record 
        contains a player's lifetime statistics in the game mode.
        
        :param list players: List of player gamertags.
        :returns dict: JSON response.
        """
        return self._get_service_records(mode="warzone", players=players)

    def _get_service_records(self, mode, players):
        endpoint = "servicerecords/{mode}".format(
                mode=mode
            )
        params = dict()
        params["players"] = players
        return self._stats_request(endpoint, params)
