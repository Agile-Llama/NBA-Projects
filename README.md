# NBA-Player-Similarity

## The Problem

There isn't any particular problem im looking to solve. However without a specific goal there is still plenty we can learn from an open-ended project. I'll be looking at players from different eras and within their own. I will be exploring differences/similarities between players from their own era and from different eras. To see if stats measure up to what fans and pundits hold up as truths about NBA players. NBA in recent years has become signifcantly more analytical, however, not everything can be measured with statsitics, and looking at individual stats in a game with 4 other players on the court only gives a fragmented view of the bigger picture. But even with this limitation, we can still gain insight through statsitics. I hope to come to some conclusions that we couldn't have reached by meerly glancing at the data, and hopefully find some interesting information about players from different eras.

## Defining an Era.  

Theres a few ways in which eras are definded in the NBA. There's by decade, by major rule change (think hand-checking of the late 90s), and by dominant teams/players of the time. For this project i'll be seperating eras based of dominant teams/players.
- 1979-1989 Larry Bird and Magic Johnson Era. 
- 1989-1999 Michael Jordan Era.
- 1999-2009 Kobe, Shaq and Duncan Era.
- 2009-2016 Lebron James and Golden State Warriors Era. 

These eras are by no means set, they are almost entriely subjective. But they do consist of whom most would consider the most dominant player(s)/team(s) of the time. 

## Data-Set

I am using a dataset whih contains stats on all players from 1978-2016 who played in the NBA. The dataset can be found here : https://data.world/jgrosz99/nba-player-data-1978-2016.  
I'm going to be normalize the data by minutes-per-game as it gives us a fairer represenation of each players contributions. If we looked at a per-game statistic, it would reward players who play a lot of minutes because they are on a bad team (Lebron on the cavs) and it would punish players who play on elite teams such as Steph curry, who might sit in the 4th quarter because their team has such a big lead. There is an agurment to be made that this method disadvantages players who play more minutes, it doesn't take into account things like fatigue which are gained by an increase in minutes. However, there isn't a simple stat that can be used to measure all the factors so this is what i'm going with.




