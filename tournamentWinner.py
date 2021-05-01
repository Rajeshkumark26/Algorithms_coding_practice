def tournamentWinner(competitions, results):
    # Write your code here.
	currentBestTeam=''
	scores={}
	for idx,competition in enumerate(competitions):
		result=results[idx]
		homeTeam,awayTeam=competition
		winner= homeTeam if result==1 else awayTeam
		scores[winner]=scores[winner]+3 if winner in scores.keys() else 3
		currentBestTeam = winner if idx==0 else currentBestTeam
    	currentBestTeam= winner if scores[winner] > scores[currentBestTeam]	else currentBestTeam
    return currentBestTeam