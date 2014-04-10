from django.http import HttpResponse
import json
from leagueoflegends import LeagueOfLegends, RiotError

def index(request):
    return HttpResponse("Hello, world!")

def info(request):
    lol = LeagueOfLegends('9dbdadfb-26c8-4545-b9b1-2dfe69140f0b')
    name = request.GET.get('name')
    summoner = lol.get_summoner_by_name(name)
    stats = lol.get_summoner_stats(summoner['id'])
    info = json.dumps(stats, indent=4)

    return HttpResponse(info)
