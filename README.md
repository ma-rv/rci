# Projects of my studies in Robotics, Cognition, Intelligence

## Evaluation of "Towards 3D Human Pose Estimation in the Wild: a Weakly-supervised Approach" [PDF](https://github.com/ma-rv/rci/blob/master/Evaluation_%20Towards%203D%20Human%20Pose%20Estimation%20in%20the%20Wild%20a%20Weakly-supervised%20Approach.pdf)


## Techniques in Artificial Intelligence

#### Problem 1.1: Gathering allies while avoiding obstacles [Solution1.py](https://github.com/ma-rv/rci/blob/master/Techniques%20in%20Artificial%20Intelligence/Solution1.py)
A  robot,  who  is  hell-bent  on  conquering  the  universe,  needs  to  travel  to  different  planets  in  order  to gather allies.  Help it to navigate through asteroid belts (the obstacles) before its fuel runs out. We  illustrate  the  problem  with  a  matrix,  where ∗ represents  obstacles  in  the  astroid  belt, − valid positions  for  a  path, X the  position  of  the  ally  (hence  the  goal  destination),  and R the  starting position. 

Going different directions costs different amount of fuel: <br>
To move left/right: 5 units <br>
To move up/down: 6 units <br>
To move diagonally: 10 units <br>

Calculate the minimum units of fuel (in integer) the robot needs to reach the ally.  If not possible to reach
the ally, print “No path found!”.

#### Problem 1.2: Conquering space [Solution2.py](https://github.com/ma-rv/rci/blob/master/Techniques%20in%20Artificial%20Intelligence/Solution2.py)
Now that you have helped the robot to gather enough allies, it is time to battle.  We use a matrix again to model this problem, where X represents the ally’s spaceship and · (a dot) the enemy.  The robot’s army conquers all enemies which are fully surrounded by allies (i.e.  on all four sides) and turns them into allies.  Thus, all fully surrounded · are replaced by X.
