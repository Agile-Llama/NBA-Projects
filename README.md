# NBA-Player-Similarity

## The Problem

There isn't any particular problem im looking to solve. However without a specific goal there is still plenty we can learn from an open-ended project. I will be looking at players from the 2017/2018 NBA season and looking for differences/similarities between them. To see if stats measure up to what fans and pundits hold up as truths about NBA players. NBA in recent years has become signifcantly more analytical, however, not everything can be measured with statsitics, and looking at individual stats in a game with 4 other players on the court only gives a fragmented view of the bigger picture. But even with this limitation, we can still gain insight through statsitics. I hope to come to some conclusions that we couldn't have reached by meerly glancing at the data, and hopefully find some interesting information about players.

## Data-Sets

Im going to using player data from the 2017-18 NBA regular season. The final data-set will be made up of three seperate data-sets which have been obtained from the websites, Basketball-reference and NBAmining.com. The first data-set from Basketball-reference is made up of the more traditional statistics (think points, rebounds assists). The player statistics have been normalized to 36 minutes of game-time as opposed to looking at per-game averages. The reason for normalizing by minutes-per-game is that it gives a fairer representation of each players contributions. If we looked at per-game statistics instead of per-36 players who play more minutes like LeBron James would look much better on paper then players like Steph Curry who plays less minutes because his team is much better. A player like Steph Curry often isn't required to play the end of a game because he is on the bench being rested. Theres an arguement to be made that this is unfair to players who play more minutes and that Lebron would possibly put up better per 36 numbers, if he played fewer minutes like Curry and wasn't forced to player longer increasing his exhaustion. Other stats like per-100-possessions exist which could be argued are better for evaluting a players impact, as they normalize a players stats by the teams pace. However, I think that statistic also has its draw backs as it reduces the impact of players who aren't go-to scoring options and therefore don't get used on possessions where the team is required to score in a rush. Unfortently, there isn't a perfect statistic which can rid of all bias. What we can do is try our best to minimize them and be concious of them when evaluating our results.  The second basketball-reference data-set we are using is made up of 'Advanced' statistics (think usage %, rebound %, fg %) from the same group of players as the first data-set. The third data-set is from a smaller website called NBAminer.com. This data-set has some more miscellaneous statistics (think points in the paint, fast break points). These stats offer a useful insight which tradiation statsitics do not offer. They don't just say that points were scored, but poitions on the court where they were scored. 

## Pre-processing: Data-cleaning

### Merging data sets and fixing mismatches