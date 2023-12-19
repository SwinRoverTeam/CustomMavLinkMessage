import sys
sys.path.append("path/to/generated/mavlinkv2")  
from pymavlink import mavutil
from custom_messages import MAVLink_rfid_control_message  # Replace with your actual library name and class

# Establish a MAVLink connection (change this string depends on our Rover)
connection = mavutil.mavlink_connection('/dev/ttyAMA0', baud=57600)  # Serial connection example

def handle_rfid_control_message(msg):
    """
    Handle the incoming RFID control message.
    """
    print(f"Received RFID control message: Command={msg.command}, Duration={getattr(msg, 'pause_duration', 0)}")

    # https://www.youtube.com/watch?v=P893c13Q160&ab_channel=PATHFINDER%28SangeethPrasanga%29

    # I have found this tutorial on how to handle RFID on/off switch, due to time constraint, I haven't understood it all. I will try to add if I can.
    

# Main loop to listen for incoming messages
while True:
    msg = connection.recv_match(blocking=True)
    if msg is not None:
        if msg.get_type() == 'RFID_CONTROL':  # Check if it is the custom message
            handle_rfid_control_message(msg)
