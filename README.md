# GSV-8_python_test-scripts
In the example script main.py:

- Open the serial connection
- A stop command is sent to end the automatic transmission of measured values (immediately after switching on the GSV8, the GSV8 starts the automatic transmission of measured values, according to the set data rate)
- Emptying the input buffer

- One-time query of all measured values
- SetZero (taring) on channel 1
- One-time query of all measured values
- SetZero (taring) all channels
- One-time query of all measured values

- Setting the UserScale of channel 2 to the value 2.0
- Reading out the UserScale from channel 2
- Setting the UserScale of channel 2 to the value 1.0
- Reading out the UserScale from channel 2

- Close the serial connection

In the GSVcommands.py script, some request frames are created according to the protocol specification for GSV8 (https://www.me-systeme.de/produkte/elektronik/gsv-8/anleitungen/GSV-ProtocolDefinitionEN.pdf).

In the GSVconvert.py script, some functions are stored for the conversion between the byte arrays transmitted in the request or response frames and the correspondingly necessary data types.
