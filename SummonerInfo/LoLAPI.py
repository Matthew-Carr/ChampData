__author__ = 'Matthew Carr'

import json
import urllib2

class LoLAPI:
    """
    A library to make API calls to the official League of Legends API
    Attributes:
        api_key     Necessary to make api calls to riot. You can get one at https://developer.riotgames.com/sign-in?fhs=true
        region      The server you would like to access.

    Response Error Codes:
        400	Bad request
        401	Unauthorized
        429	Rate limit exceeded
        500	Internal server error
        503	Service unavailable

    """

    def __init__(self, api_key, region='na'):
        self.api_key = api_key
        self.regions = ('br', 'eune', 'euw', 'kr', 'lan', 'las', 'na', 'oce', 'ru', 'tr')
        if region in self.regions:
            self.region = region
        else:
            message = 'Invalid region, possibilities are: '
            for x in self.regions:
                message += str(x) + ', '
            raise TypeError(message)

        self.standard_api_url = 'https://na.api.pvp.net/api/lol/'
        self.observer_url = 'https://na.api.pvp.net/observer-mode/rest/'
        self.status_url = 'http://status.leagueoflegends.com/shards'
        self.static_url = 'https://global.api.pvp.net/api/lol/static-data/'

        self.queue_types = ('RANKED_SOLO_5x5', 'RANKED_TEAM_5x5', 'RANKED_TEAM_3x3')
        self.seasons = ('SEASON3', 'SEASON2014', 'SEASON2015')

    # main method for retrieving json
    def make_api_call(self, sub_url='', url_base='https://na.api.pvp.net/api/lol/',
                      include_region=True, query_string=[]):
        """Returns an api call to league of legends"""

        if not query_string:
            query_string.append(['api_key', urllib2.quote(self.api_key)])

        query = '?' + query_string[0][0] + '=' + query_string[0][1]

        for x in query_string[1:]:
            query += '&' + x[0] + '=' + x[1]


        url = url_base + (urllib2.quote(self.region + sub_url) if include_region else urllib2.quote(sub_url)) + query

        print 'making call to ', url
        return json.loads(urllib2.urlopen(url).read())

    # champion-v1.2
    def all_champions(self):
        """Retrieve all champions. (REST)"""
        return self.make_api_call(sub_url='/v1.2/champion')

    def champion_by_id(self, ID):
        """Retrieve champion by ID. (REST)"""
        return self.make_api_call('/v1.2/champion/' + str(ID))

    # current-game-v1.0
    def game_info_by_id(self, ID):
        """Get current game information for the given summoner ID. (REST)"""
        return self.make_api_call('consumer/getSpectatorGameInfo/NA1/' + str(ID), url_base=self.observer_url,
                                  include_region=False)

    # featured-games-v1.0
    def list_featured(self):
        """Get list of featured games. (REST)"""
        return self.make_api_call('featured', url_base=self.observer_url, include_region=False)

    # game-v1.3
    def recent_games_by_id(self, ID):
        """Get recent games by summoner ID. (REST)"""
        return self.make_api_call('/v1.3/game/by-summoner/' + str(ID) + '/recent')

    # league-v2.5
    def leagues_by_id(self, ID):
        """Get leagues mapped by summoner ID for a given list of summoner IDs. (REST)"""
        return self.make_api_call('/v2.5/league/by-summoner/' + str(ID))

    def league_entries_by_id(self, ID):
        """Get league entries mapped by summoner ID for a given list of summoner IDs. (REST)"""
        return self.make_api_call('/v2.5/league/by-summoner/' + str(ID) + '/entry')

    def leagues_by_team(self, team_ID):
        """Get leagues mapped by team ID for a given list of team IDs. (REST)"""
        return self.make_api_call('/v2.5/league/by-team/' + str(team_ID))

    def league_entries_by_team(self, team_ID):
        """Get league entries mapped by team ID for a given list of team IDs. (REST)"""
        return self.make_api_call('/v2.5/league/by-team/' + str(team_ID) + '/entry')

    def challenger_tier_leagues(self, type):
        """Get challenger tier leagues. (REST)"""
        if type in self.queue_types:
            return self.make_api_call(sub_url='/v2.5/league/challenger', url_base='https://na.api.pvp.net/api/lol/',
                                      query_string=[['type', type], ['api_key', urllib2.quote(self.api_key)]])
        else:
            message = 'Invalid season, possibilities are: '
            for x in self.queue_types:
                message += str(x) + ', '
            raise TypeError(message)

    def master_tier_leagues(self, type):
        """Get master tier leagues. (REST)"""
        types = ('RANKED_SOLO_5x5', 'RANKED_TEAM_5x5', 'RANKED_TEAM_3x3')
        if type in types:
            return self.make_api_call(sub_url='/v2.5/league/master', url_base='https://na.api.pvp.net/api/lol/',
                                      query_string=[['type', type], ['api_key', urllib2.quote(self.api_key)]])
        else:
            message = 'Invalid season, possibilities are: '
            for x in self.queue_types:
                message += str(x) + ', '
            raise TypeError(message)

    # lol-static-data
    def champion_list(self):
        """Retrieves champion list. (REST)"""
        return self.make_api_call('/v1.2/champion', url_base=self.static_url)

    def champion_data_by_id(self, ID):
        """Retrieves a champion by its id. (REST)"""
        return self.make_api_call('/v1.2/champion/' + str(ID), url_base=self.static_url)

    def item_list(self):
        """Retrieves item list. (REST)"""
        return self.make_api_call('/v1.2/item', url_base=self.static_url)

    def item_by_id(self, ID):
        """Retrieves item by its unique id. (REST)"""
        return self.make_api_call('/v1.2/item/' + str(ID), url_base=self.static_url)

    def language_strings(self):
        """Retrieve language strings data. (REST)"""
        return self.make_api_call('/v1.2/language-strings', self.static_url)

    def supported_languages(self):
        """Retrieve supported languages data. (REST)"""
        return self.make_api_call('/v1.2/languages', self.static_url)

    def map_data(self):
        """Retrieve map data. (REST)"""
        return self.make_api_call('/v1.2/map', self.static_url)

    def mastery_list(self):
        """Retrieves mastery list. (REST)"""
        return self.make_api_call('/v1.2/mastery', self.static_url)

    def mastery_item_by_id(self, ID):
        """Retrieves mastery item by its unique id. (REST)"""
        return self.make_api_call('/v1.2/mastery/' + str(ID), self.static_url)

    def realm_data(self):
        """Retrieve realm data. (REST)"""
        return self.make_api_call('/v1.2/realm', self.static_url)

    def rune_list(self):
        """Retrieves rune list. (REST)"""
        return self.make_api_call('/v1.2/rune', self.static_url)

    def rune_by_id(self, ID):
        """Retrieves rune by its unique id. (REST)"""
        return self.make_api_call('/v1.2/rune/' + str(ID), self.static_url)

    def summoner_spell_list(self):
        """Retrieves summoner spell list. (REST)"""
        return self.make_api_call('/v1.2/summoner-spell', self.static_url)

    def summoner_spell_by_id(self, ID):
        """Retrieves summoner spell by its unique id. (REST)"""
        return self.make_api_call('/v1.2/summoner-spell/' + str(ID), self.static_url)

    def version_data(self):
        """Retrieve version data. (REST)"""
        return self.make_api_call('/v1.2/versions', self.static_url)

    # lol-status-v1.0
    def shard_list(self):
        """Get shard list. (REST)"""
        return self.make_api_call(url_base=self.status_url, include_region=False)

    def shard_status(self):
        """Get shard status. Returns the data available on the status.leagueoflegends.com website for the given region. (REST)"""
        return self.make_api_call(url_base=self.status_url + '/' + self.region, include_region=False)

    # match-v2.2
    def match_by_id(self, match_ID):
        """Retrieve match by match ID. (REST)"""
        return self.make_api_call('/v2.2/match/' + str(match_ID))

    # match history-v2.2
    def match_history_by_id(self, ID):
        """Retrieve match history by summoner ID. (REST)"""
        return self.make_api_call('/v2.2/matchhistory/' + str(ID))

    # stats-v1.3
    def ranked_stats_by_id(self, ID, season='SEASON2015'):
        """Get ranked stats by summoner ID. (REST)"""
        if season in self.seasons:
            return self.make_api_call(sub_url='/v1.3/stats/by-summoner/' + str(ID) + '/ranked',
                                      query_string=[['season', str(season)], ['api_key', urllib2.quote(self.api_key)]])
        else:
            message = 'Invalid season, possibilities are: '
            for x in self.seasons:
                message += str(x) + ', '
            raise TypeError(message)

    def player_stats_by_id(self, ID):
        """Get player stats summaries by summoner ID. (REST)"""
        return self.make_api_call('/v1.3/stats/by-summoner/' + str(ID) + '/summary')

    # summoner-v1.4
    def summoner_objects_by_name(self, name):
        """Get summoner objects mapped by standardized summoner name for a given list of summoner names. (REST)"""
        return self.make_api_call(sub_url='/v1.4/summoner/by-name/' + str(name))

    def summoner_objects_by_id(self, ID):
        """Get summoner objects mapped by summoner ID for a given list of summoner IDs. (REST)"""
        return self.make_api_call(sub_url='/v1.4/summoner/' + str(ID))

    def mastery_pages_by_id(self, ID):
        """Get mastery pages mapped by summoner ID for a given list of summoner IDs (REST)"""
        return self.make_api_call(sub_url='/v1.4/summoner/' + str(ID) + '/masteries')

    def summoner_names_by_id(self, ID):
        """Get summoner names mapped by summoner ID for a given list of summoner IDs. (REST)"""
        return self.make_api_call(sub_url='/v1.4/summoner/' + str(ID) + '/name')

    def rune_pages_by_id(self, ID):
        """Get rune pages mapped by summoner ID for a given list of summoner IDs. (REST)"""
        return self.make_api_call(sub_url='/v1.4/summoner/' + str(ID) + '/runes')

    # team-v2.4
    def teams_by_id(self, ID):
        """Get teams mapped by summoner ID for a given list of summoner IDs. (REST)"""
        return self.make_api_call(sub_url='/v2.4/team/by-summoner/' + str(ID))

    def teams_by_team_id(self, team_ID):
        """Get teams mapped by team ID for a given list of team IDs. (REST)"""
        return self.make_api_call(sub_url='/v2.4/team/' + str(team_ID))
