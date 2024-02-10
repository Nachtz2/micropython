from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0 
total_turns = 0

while True:
    #right state
    if state == 0:
        mycontroller.drive_forwards()
        if mycontroller.left_odom.get_count()>= 1000 and mycontroller.right_odom.get_count() >=1000:
            state = 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()
  
    #turning state of right 
    elif state == 1:
        mycontroller.raft.led_on()
        mycontroller.right_turn()
        turns_made +=1
        