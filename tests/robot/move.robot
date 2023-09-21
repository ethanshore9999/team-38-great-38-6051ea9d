*** Settings ****
Documentation   https://raw.githubusercontent.com/level-up-program/team-38-great-38-6051ea9d/main/src/images/Triton.png \n\n I want to move my character.If they attempt to move past a boundry,the move results in no change in position. \n\n This is the test robot file \n\n https://raw.githubusercontent.com/level-up-program/team-38-great-38-6051ea9d/main/tests/robot/images/triton.png
Test Template   Move character
Library         MoveLibrary.py

*** Test Cases ***      StartingX   StartingY   Direction   EndingX EndingY
1Move in middle of board     5           5           NORTH       5       6
2Move in middle of board     5           5           SOUTH       5       4
3Move in middle of board     5           5           EAST        6       5
4Move in middle of board     5           5           WEST        4       5
5Move on edge of board   9           9           SOUTH       9       8
6Move on edge of board   9           9           NORTH       9       9
7Move on edge of board   9           9           EAST        9       9
8Move on edge of board   9           9           WEST        8       9
9Move on edge of board   9           0           SOUTH       9       0
10Move on edge of board   9           0           NORTH       9       1
11Move on edge of board   9           0           EAST        9       0
12Move on edge of board   9           0           WEST        8       0
13Move on edge of board   0           9           SOUTH       0       8
14Move on edge of board   0           9           NORTH       0       9
15Move on edge of board   0           9           EAST        1       9
16Move on edge of board   0           9           WEST        0       9
17Move on edge of board   0           0           SOUTH       0       0
18Move on edge of board   0           0           NORTH       0       1
19Move on edge of board   0           0           EAST        1       0
20Move on edge of board   0           0           WEST        0       0
21Move on edge of board   0           5           SOUTH       0       4
22Move on edge of board   0           5           NORTH       0       6
23Move on edge of board   0           5           EAST        1       5
24Move on edge of board   0           5           WEST        0       5
25Move on edge of board   5           9           SOUTH       5       8
26Move on edge of board   5           9           NORTH       5       9
27Move on edge of board   5           9           EAST        6       9
28Move on edge of board   5           9           WEST        4       9
29Move on edge of board   9           5           SOUTH       9       4
30Move on edge of board   9           5           NORTH       9       6
31Move on edge of board   9           5           EAST        9       5
32Move on edge of board   9           5           WEST        8       5
33Move on edge of board   5           0           SOUTH       5       0
34Move on edge of board   5           0           NORTH       5       1
35Move on edge of board   5           0           EAST        6       0
36Move on edge of board   5           0           WEST        4       0

 
*** Keywords ***
Move character
    [Arguments]     ${startingX}    ${startingY}    ${direction}   ${endingX}  ${endingY}
    Initialize character xposition with     ${startingX}
    Initialize character yposition with     ${startingY}
    Move in direction                       ${direction}
    Character xposition should be           ${endingX}
    Character yposition should be           ${endingY}
