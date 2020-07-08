#SMS based advanced voting system using Python and NodeMCU
This project was actually done for competing in the intra-departmental project competition and the project got first prize. 
You will need:
1. Python for main code
2. Arduino to program NodeMCU
3. GSM Module : I have used Air200. This is low price and comparitively good.

Procedure :
1. You have to use GSM with your NodeMCU. Actually this is the SMS reciever. After recieving the Arduino code will directly transfer the SMS to PC server via Serial communication.
2. Python code will count the incoming messages and parse them all continuously. 
3. After that the Python code will count the vote and publish it to the website. Here I have used IoT server.
