import pokernew
from pokernew import pokernew
import unittest
from newworkpoker import comparechecking

player1 = pokernew(['s','s','s','s','s'],[14,13,12,11,10])
player2 = pokernew(['s','s','s','s','s'],[5,2,3,4,1])

whowins = comparechecking(player1,player2)

print whowins.win 