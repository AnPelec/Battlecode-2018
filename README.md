# Battlecode-2018
## Our team's (obas) participation in Battlecode 2018, an AI programming competition held in MIT.

In this repository, you may find our progress in the Battlecode 2018 Competition. Even though it was our team's first try, our bot performed ery well, losing a ticket for the final on the second to last round!


###### In this repository you may find:
  * **slow_strategy:** Our first strategy. This bot was playing very efficiently, but was timing out in the early rounds due to the excessive number of computations required in each round
  * **fast_strategy:** After experiencing slow_strategy's limitations, we decided to include randomization in our bot. This was our first try to trade some time for accuracy. Unfortunately, even if this bot turned out to be extremely fast, its actions were suboptimal.
  * **Project Hephaestus:** Project Hephaestus is the intersection of fast_strategy's randomization and speed with slow_strategy's accuracy. Furthermore, we introduced in Project Hephaestus the notion of strategy as a set of probabilities for each action.
  Every action (ie attack, harvest, move etc) has a certain probability to happen in each round.These probabilities can be found in strategy.json and in the end were hardcoded in the program by the dictionary data.
  This kind of strategy allowed us to implement **reinforcement learning**. By creating a large number of strategies, we gave each strategy an initial weight '''wi'''. Then we let the strategies "fight" between them in various matches and the strategies that were victorious had their weight increased by some constant factor. The result was that more successful strategies had higher weight and hence more probability to be chosen and reveal the best of them. The resulting winning strategy was used in Project Hephaestus.
  * **Project Achilles:** Even though Project Hephaestus was very randomized, it behaved very well on the average match. However, there were some instances where luck was not favoring our bot. In some of those instances, the bot preferred to only build factories and there were no rockets to send robots to Mars. Some other times the opponent was being very aggressive and our bot was defeated by the first 200 rounds, while it was still trying to build up its army. This is why Project Achilles introduced some "emergency states", which made sure that if something "unlucky" was happening, the robot would react accordingly, until the problem was resolved. In project Achilles we also introduced some other micro-optimizations regarding rockets etc that seemed to have a very good impact. This was our robot's **reactive strategy.**
  * **Helping Modules:** Modules that organize and implement every possible action for our entities (robots and structures). They are also included in the individual projects with minor modifications.
  
