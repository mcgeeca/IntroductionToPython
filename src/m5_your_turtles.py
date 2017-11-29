"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Craig McGee Jr.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
caesar = rg.SimpleTurtle("turtle")
caesar.pen = rg.Pen("orange", 10)
caesar.speed = 10
brutus = rg.SimpleTurtle("turtle")
brutus.pen = rg.Pen("royal blue", 10)
brutus.speed = 10
size = 50
for k in range(5):
    caesar.draw_square(size)
    caesar.pen_up()
    caesar.backward(200)
    caesar.forward(100)
    caesar.pen_down()
    size = size + 50
    brutus.draw_square(size)
    brutus.pen_up()
    brutus.forward(200)
    brutus.backward(100)
    brutus.pen_down()
    size = size + 50




window.close_on_mouse_click()