from django.http import HttpResponse
import json
from summoners.leagueoflegends import LeagueOfLegends, RiotError
from summoners.parsestats import ParseStats

def index(request):
    return HttpResponse("Hello, world!")

def info(request):
    lol = LeagueOfLegends('9dbdadfb-26c8-4545-b9b1-2dfe69140f0b')
    name = request.GET.get('name')
    summoner = lol.get_summoner_by_name(name)
    stats = lol.get_summoner_stats(summoner['id'])
    info = json.dumps(stats, indent=4)
    
    nicelookingdata = ParseStats(info)
    info = nicelookingdata.return_stats_html()
        
    #return HttpResponse("<html><body><font face=\"arial\">" + info + "</font></body></html>")
    return HttpResponse(info)