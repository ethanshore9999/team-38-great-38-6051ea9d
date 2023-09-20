*** Settings ****
Documentation   I want to move my character.If they attempt to move past a boundry,the move results in no change in position.
Test Template   Move character
Library         MoveLibrary.py

*** Test Cases ***      StartingX   StartingY   Direction   EndingX EndingY
Move in middle of board 5           5           NORTH       5       6
Move in middle of board 5           5           SOUTH       5       4
Move in middle of board 5           5           EAST        6       5
Move in middle of board 5           5           WEST        4       5
Move on edge of board   9           9           SOUTH       9       8
Move on edge of board   9           9           NORTH       9       9
Move on edge of board   9           9           EAST        9       9
Move on edge of board   9           9           WEST        8       9
Move on edge of board   9           0           SOUTH       9       0
Move on edge of board   9           0           NORTH       9       1
Move on edge of board   9           0           EAST        9       0
Move on edge of board   9           0           WEST        8       0
Move on edge of board   0           9           SOUTH       0       8
Move on edge of board   0           9           NORTH       0       9
Move on edge of board   0           9           EAST        1       9
Move on edge of board   0           9           WEST        0       9
Move on edge of board   0           0           SOUTH       0       0
Move on edge of board   0           0           NORTH       0       1
Move on edge of board   0           0           EAST        1       0
Move on edge of board   0           0           WEST        0       0
Move on edge of board   0           5           SOUTH       0       4
Move on edge of board   0           5           NORTH       0       6
Move on edge of board   0           5           EAST        1       5
Move on edge of board   0           5           WEST        0       5
Move on edge of board   5           9           SOUTH       5       8
Move on edge of board   5           9           NORTH       5       9
Move on edge of board   5           9           EAST        6       9
Move on edge of board   5           9           WEST        4       9
Move on edge of board   9           5           SOUTH       9       4
Move on edge of board   9           5           NORTH       9       6
Move on edge of board   9           5           EAST        9       5
Move on edge of board   9           5           WEST        8       5
Move on edge of board   5           0           SOUTH       5       0
Move on edge of board   5           0           NORTH       5       1
Move on edge of board   5           0           EAST        6       0
Move on edge of board   5           0           WEST        4       0

 
*** Keywords ***
Move character
    [Arguments]     ${startingX}    ${startingY}    ${direction}   ${endingX}  ${endingY}
    Initialize character xposition with     ${startingX}
    Initialize character yposition with     ${startingY}
    Move in direction                       ${direction}
    Character xposition should be           ${endingX}
    Character yposition should be           ${endingY}
Documentation
	This is the test robot file
	/config/workspace/images/levelup/images/Triton.png