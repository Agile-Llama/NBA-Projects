# NBA-Player-Similarity

## The Problem

There isn't any particular problem I'm looking to solve. However, without a specific goal, there is still plenty we can learn from an open-ended project. I will be looking at players from the 2017/2018 NBA season and looking for differences/similarities between them. To see if stats measure up to what fans and pundits hold up as truths about NBA players. NBA in recent years has become significantly more analytical, however, not everything can be measured with statistics, and looking at individual stats in a game with 4 other players on the court only gives a fragmented view of the bigger picture. But even with this limitation, we can still gain insight through statistics. I hope to come to some conclusions that we couldn't have reached by merely glancing at the data, and hopefully find some interesting information about players.

## Data-Sets

I'm going to using player data from the 2017-18 NBA regular season. The final data-set will be made up of three separate data-sets which have been obtained from the websites, Basketball-reference and NBAminer. The first data-set from Basketball-reference is made up of the more traditional statistics (think points, rebounds assists). The player statistics have been normalized to 36 minutes of game-time as opposed to looking at per-game averages. The reason for normalizing by minutes-per-game is that it gives a fairer representation of each player's contributions. If we looked at per-game statistics instead of per-36 players who play more minutes like LeBron James would look much better on paper then players like Steph Curry who play fewer minutes because his team is much better. A player like Steph Curry often isn't required to play the end of a game because he is on the bench being rested. There's an argument to be made that this is unfair to players who play more minutes and that Lebron would possibly put up better per 36 numbers if he played fewer minutes like Curry and wasn't forced to player longer increasing his exhaustion. Other stats like per-100-possessions exist which could be argued are better for evaluating a player's impact, as they normalize a player's stats by the team's pace. However, I think that statistic also has its drawbacks as it reduces the impact of players who aren't go-to scoring options and therefore don't get used to possessions where the team is required to score in a rush. Unfortunately, there isn't a perfect statistic that can rid of all bias. What we can do is try our best to minimize them and be conscious of them when evaluating our results.  The second basketball-reference data-set we are using is made up of 'Advanced' statistics (think usage %, rebound %, FG%) from the same group of players as the first data-set. The third data-set is from a smaller website called NBAminer. This data-set has some more miscellaneous statistics (think points in the paint, fast breakpoints). These stats offer useful insight that traditional statistics do not offer. They don't just say that points were scored, but positions on the court where they were scored. 

## Pre-processing: Data-cleaning

***Merging data-sets and fixing mismatches***. Because the first two data-sets are from the same source merging these two are easy. The third datasets are from a different source so some discrepancies need to be addressed. The first thing is that there is information on 19 fewer players. Looking deeper we can see that 45 total players don't have any data on the third. There are some small things we can do to reduce this number. In data-set one and two they have special characters for player names. For example, J.J Barea, where are in the third these special characters have been removed. The solution is to remove the special characters from the first two data-sets. Some players have Suffixes or numerical values in their name (ex: IV) or (ex: Jr) these are also removed from the first two data-sets before we merge. The remaining names which are missing are players that have very limited minutes for very few games. I'm not going to add these players because they'd have been anyway.

***Removing Features***. After merging the data-sets, repeated features need to be removed (ex: player name repeated). After this, we need to remove redundant features (ex: team name). We also remove features such as ranking, it's a meaningless indexing variable. Finally, we also remove points-per-quarter for all four quarters. The reason for this is because they are not normalized per-36 which isn't in line with our other attributes. 

***Feature Extraction***. After removing redundant features there are two more important features that we can extract. The first one is minutes-per-game. This can be calculated by taking the total minutes played (MP) and the total games played (G) and dividing these two numbers. This value will be used later to subset the data. The second is the Assist-to-turnover ratio. This metric is a good indicator of how careless a player is with the ball on offense.

***Missing Values***. The only features which have missing values are 3P%, 2P%, FT%, and TS%. After sub-setting our data-set, the only feature which has missing values is 3P%. The value is missing because there are players who have not attempted a single 3 pointer in the whole season. With this being the case, I'm going to replace the value with 0%. It seems reasonable to assume that if a player has not attempted a single 3 pointer, their shooting skills are probably similar to others who have attempted but not made a single 3 pointer throughout the season. After subsetting the data there are only 2 rows that are missing values. Replace these with 0.0 manually. 

***Sub-Setting Data***. The goal of this project is to make comparisons between players who make significant contributions to games. Therefore I'm going to remove players who do not play a significant amount of minutes per game. By doing this it will reduce clusters from getting to cluttered. I'm going to sub-set the data based on the value which was created previously, minutes per game. If a player has less then 28.5 minutes per game they will be removed from the data-set. By doing this the data-set is reduced to 100 players. After combining the 3 tables, feature-engineering, and sub-setting our data, we have data on 104 players with the following 51 features:

1. **Player** - Player name
2. **Pos** - Position
3. **FG** - Field Goals Per 36 Minutes
4. **FGA** - Field Goals Attempted Per 36 Minutes
5. **FG**% - Field Goal Percentage
6. **3P** - 3-Pointers Made Per 36 Minutes
7. **3PA** - 3-Pointers Attempted Per 36 Minutes
8. **3P%** - 3-Point Percentage
9. **2P** - 2-Point Field Goals Per 36 Minutes
10. **2PA** - 2-Point Field Goals Attempted Per 36 Minutes
11. **2P%** - 2-Point Field Goal Percentage
12. **FT** - Free-Throws Made Per 36 Minutes
13. **FTA** - Free Throws Attempted Per 36 Minutes
14. **FT%** - Free Throw Percentage
15. **ORB** - Offensive Rebounds Per 36 Minutes
16. **DRB** - Defensive Rebounds Per 36 Minutes
17. **TRB** - Total Rebounds Per 36 Minutes
18. **AST** - Assists Per 36 Minutes
19. **STL** - Steals Per 36 Minutes
20. **BLK** - Blocks Per 36 Minutes
21. **TOV** - Turnovers Per 36 Minutes
22. **PF** - Personal Fouls Per 36 Minutes
23. **PTS** - Points Per 36 Minutes
24. **G** - Games Played
25. **MP** - Minutes Played In A Season
26. **PER** - Player Efficiency Rating- A measure of per-minute production standardized such that the league average is 15.
27. **TS%** - True Shooting Percentage- A measure of shooting efficiency that takes into account 2-point field goals, 3-point field goals, and free throws.
28. **3PAr** - 3 Point Attempt Rate- Percentage of FG Attempts from 3-Point Range
29. **FTr** - Free Throw Attempt Rate- Number of FT Attempts Per FG Attempt
30. **ORB%** - Offensive Rebound Percentage- An estimate of the percentage of available offensive rebounds a player grabbed while he was on the floor.
31. **DRB%** - Defensive Rebound Percentage- An estimate of the percentage of available defensive rebounds a player grabbed while he was on the floor.
32. **TRB%** - Total Rebound Percentage- An estimate of the percentage of available rebounds a player grabbed while he was on the floor.
33. **AST%** - Assist Percentage- An estimate of the percentage of total assists a player had while he was on the floor.
34. **STL%** - Steal Percentage- An estimate of the percentage of total steals a player had while he was on the floor.
35. **BLK%** - Block Percentage- An estimate of the percentage of total blocks a player had while he was on the floor.
36. **TOV%** - Turnover Percentage- An estimate of turnovers committed per 100 plays.
37. **USG%** - Usage Percentage- An estimate of the percentage of team plays used by a player while he was on the floor.
38. **OWS** - Offensive Win Shares- An estimate of the number of wins contributed by a player due to his offense.
39. **DWS** - Defensive Win Shares- An estimate of the number of wins contributed by a player due to his defence.
40. **WS/48** - Win Shares Per 48 Minutes- An estimate of the number of wins contributed by a player per 48 minutes (league average is approximately .100.
41. **OBPM** - Offensive Box Plus/Minus- A box score estimate of the offensive points per 100 possessions a player contributed above a league-average player, translated to an average team.
42. **DBPM** — Defensive Box Plus/Minus- A box score estimate of the defensive points per 100 possessions a player contributed above a league-average player, translated to an average team.
43. **BPM** — Box Plus/Minus- A box score estimate of the points per 100 possessions a player contributed above a league-average player, translated to an average team.
44. **VORP** - Value over Replacement Player- A box score estimate of the points per 100 TEAM possessions that a player contributed above a replacement-level (-2.0. player, translated to an average team and prorated to an 82-game season.
45. **Fast Break Pts** - Fast break points per game
46. **Points in Paint** - Points Scored in Paint per game
47. **Points off TO** - Points Scored Off Turnovers per game
48. **2nd Chance Points** — Any points scored during a possession after an offensive player has already attempted one shot and missed
49. **Points Scored per Shot** — Calculated by dividing the total points (2P made and 3P made. by the total field goals attempts.
50. **A2TO** - Assists to turnover ration
51. **MPG** - Minutes Played per game

## Methods for Data Analysis

Im going to be using three different statistical methods for analysising the data.

1) Principle Component Analysis
2) K-means Clustering
3) Hierarchical Clustering

For each method, I am are going to compare the players in terms of Overall impact. In some cases I will also be looking at offensive and defensive impact. This will be done by excluding stats which don't impact the defensive side of the game.

***Overall Impact Calculations*** 