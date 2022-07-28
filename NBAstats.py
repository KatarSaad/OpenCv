from requests import  get
from pprint import PrettyPrinter
##############
#Vistor Team ,HomeTeam,period,clock

def get_scoreboard ():
    scoreBoard = get_links()["currentScoreboard"]
    data=get(BASE_URL+scoreBoard).json()
    games=data["games"]



    for game in games :
        home_team = game["hTeam"]
        vistor_team = game["vTeam"]
        clock=game["clock"]
        period = game["period"]
        tickets = game["tickets"]
        #score=game["score"]
        print("**********")
        print(f"{home_team['triCode']} vs {vistor_team['triCode']} ")
        print("__________________________")
        print(f"Scores  ",f"home Team score:{home_team['score']} ....away Team score:{vistor_team['score']}")
        print("_____________________________  ")
        print(f"clock:{clock}--{period['current']}")



def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data["links"]

    return links



def get_rank():
    stats=get_links()["leagueTeamStatsLeaders"]

    teams=get(BASE_URL+stats).json()["league"]["standard"]["regularSeason"]["teams"]
    #league=teams["league"]
   # standard=league["standard"]
    #regular=standard["regularSeason"]



    #pprinter.pprint(teams.keys())
    #print(league.keys())
    #print(regular["teams"])

    ###filter teams with a certain criteria..
    teams= list(filter(lambda  x:x['name']!="Team",teams))
    teams.sort(key=lambda  x:int(x["ppg"]["rank"]))

    for i, team in enumerate(teams):
        name=team["name"]
        nickname=team["nickname"]
        ppg=team["ppg"]["avg"]
        print(f"team rank:{i+1}.: {name}--nickname:  {nickname}--PPG: {ppg}")


###########








BASE_URL="https://data.nba.net"
ALL_JSON="/prod/v1/today.json"
pprinter=PrettyPrinter()
#get_scoreboard()
#pprinter.pprint(get_scoreboard()["games"])
#pprinter.pprint(get_links())
get_rank()
###
#now we have to access data from the web via an _api


#pprinter.pprint(data)



#pprinter.pprint(scoreBoard)


