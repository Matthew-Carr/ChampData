from django.shortcuts import render
import LoLAPI

# Create your views here.
def summoner_info(request, summoner_name):
    lol = LoLAPI.LoLAPI(api_key='7f057410-5d0b-4174-b2e4-ad93f77c18d6')

    summoner_level = lol.summoner_objects_by_name(summoner_name)[summoner_name.lower()]['summonerLevel']
    summoner_id = lol.summoner_objects_by_name(summoner_name)[summoner_name.lower()]['id']

    #ranked_stats_table = lol.ranked_stats_by_id(self.id)['champions']
    player_stats_table = lol.player_stats_by_id(summoner_id)['playerStatSummaries']
    #masteries = lol.mastery_pages_by_id(self.id)
    #runes = lol.rune_pages_by_id(self.id)
    league = lol.leagues_by_id(summoner_id)[unicode(str(summoner_id), "utf-8")][0]
    for person in league['entries']:
        if person['playerOrTeamName'].lower() == summoner_name.lower():
            personal_league_data = person
    rank = league['tier'] + ' ' + personal_league_data['division']

    coop_vs_ai_5x5 = player_stats_table[0]
    coop_vs_ai_3x3 = player_stats_table[1]
    ranked_team_3x3 = player_stats_table[2]
    ranked_team_5x5 = player_stats_table[3]
    unranked_3x3 = player_stats_table[4]
    counterpick = player_stats_table[5]
    odin_unranked = player_stats_table[6]
    CAP5x5 = player_stats_table[7]
    ARAM = player_stats_table[8]
    unranked_5x5 = player_stats_table[9]
    URF = player_stats_table[10]
    ranked_solo_5x5 = player_stats_table[11]



    context = {'summoner_name': summoner_name,
               'summoner_id': summoner_id,
               'rank': rank,
               'coop_vs_ai_5x5': coop_vs_ai_5x5,
               'coop_vs_ai_3x3': coop_vs_ai_3x3,
               'ranked_team_3x3': ranked_team_3x3,
               'ranked_team_5x5': ranked_team_5x5,
               'unranked_3x3': unranked_3x3,
               'counterpick': counterpick,
               'odin_unranked': odin_unranked,
               'CAP5x5': CAP5x5,
               'ARAM': ARAM,
               'unranked_5x5': unranked_5x5,
               'URF': URF,
               'ranked_solo_5x5': ranked_solo_5x5,
               }
    return render(request, 'SummonerInfo/info.html', context)







