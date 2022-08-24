def AddToStorage(no_of_teams):# to take input add  the data to storage
    storage={}
    for i in range(no_of_teams):
        nameofteam=input()#input the name of Team 
        pointsearaned=int(input())#points Team scored
        resultofpastfivemathes=[str(i) for i in input().split(',')]#five matches result
        stats_team={}# dictionary stores points, resultofpastfivemathes
        stats_team['points']=pointsearaned
        stats_team['pastfivematches']=resultofpastfivemathes
        storage[nameofteam]=stats_team
    return storage#finall datastructur stores the data regarding matches
    
def FindConsecutiveLoss(data):#to find team who has twoconsecutive loses 
    teamsconsecutiveloss={}
    for team,stats in data.items():
        #print(team,stats)
        list_=stats['pastfivematches']
        for i in list_:
            if (i=='lose'):# checking consecutive loses
                index_firstloss=list_.index(i)
                if (list_[index_firstloss+1]=='lose'):
                    teamsconsecutiveloss[team]=[stats['points'],len(list_)]# adding the length of the pastfivematches to get the average
        return teamsconsecutiveloss

def AverageForConsecutiveLose(average):# to print the average points of those two consecutive lose of those teams
    for team,stats in average.items():
        #print(team,stats)
        averagepoints=stats[0]//stats[1]
        print(team,"--AV points--",averagepoints)
    
no_of_teams=int(input())# taking input for no_of teams
storageset=AddToStorage(no_of_teams)
print(storageset)
average=FindConsecutiveLoss(storageset)
print(average)
AverageForConsecutiveLose(average)
