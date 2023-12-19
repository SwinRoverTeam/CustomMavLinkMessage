# CustomMavLinkMessage
MavLink can be used to do many different things for the Rover, including movement (velocity or orientation) control, mission planning, etc. 
But when we send something that is not in the protocol, we have to define our own messageID to send to the system the other side. 
This repository includes the code that we can use to create a new message that can be sent.

In the XML file is the creation of a new message. The ID and command can be chosen depending on how we want the message to do.
After that, we have to load the Mavlink repo and put this message (XML file) into the cloned MAVlink repo.
Now we can use this command to generate a new Python libraries using this message.

python -m pymavlink.tools.mavgen --lang=Python --wire-protocol=2.0 --output=generated/mavlinkv2 message_definitions/v1.0/custom_messages.xml

where "generated/mavlinkv2" is the output path of our file and custom_messages.xml is the name of our newly created custom messages.

The GCS_sender.py is used to send our messages from the Ground Control Station to the Rover and MavLinkReceiver.py can handle the message and do whatever we want to the Rover with it. 
