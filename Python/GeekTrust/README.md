# Thame Of Thrones
## Problem 1 - A GOLDEN CROWN
There is no ruler in the universe of Southeros and pandemonium reigns. Shan, the gorilla king of the Space kingdom
wants to rule all Six Kingdoms in the universe of Southeros. He needs the support of 3 more kingdoms to be the ruler.
Each kingdom has an animal emblem and Shan needs to send a message with the animal in the message to win them over.
LAND emblem - Panda, WATER emblem - Octopus, ICE emblem - Mammoth, AIR emblem - Owl, FIRE emblem - Dragon.

Your coding challenge is to have King Shan send secret message to each kingdom and win them over.

Once he wins 3 more kingdoms, he is the ruler! The secret message needs to contain the letters of the animal in their
emblem. For example, secret message to the Land kingdom (emblem: Panda) needs to have the letter 'p','n','d' atleast
once and 'a' at-least twice. If he sends "a1d22n333a4444p" to the Land kingdom, he will win them over.

## Problem 2 - BREAKER OF CHAINS
The other kingdoms in the Universe also yearn to be the ruler of Southeros and war is imminent! The High Priest of Southeros
intervenes and is trying hard to avoid a war and he suggests a ballot system to decide the ruler.

Your coding challenge is to help the High Priest choose the ruler of Southeros through the ballot system.

Rules of the Ballot system
1. Any kingdom can compete to be the ruler.
2. They should send a message to all other kingdoms asking for allegiance.
3. This message will be put in a ballot from which the High Priest will pick 6 random messages.
4. The High Priest then hands over the 6 messages to the respective receiving kingdoms.
5. The kingdom that receives the highest number of allegiance is the ruler.

Rules to decide allegiance by a kingdom
1. The receiving kingdom has to give allegiance to the sending kingdom if the message contains the letters of the animal in their
emblem (same as problem 1).
2. If the receiving kingdom is competing to be the ruler, they will not give their allegiance even if the message they received is correct.
3. A kingdom cannot give their allegiance twice. If they have given their allegiance once, they will not give their allegiance again even
if they get a second message and the message is correct.
In case there is a tie
1. If there is a tie, the whole ballot process is repeated but only with the tied kingdoms till there is a winner.
Sending messages
The format of the message dropped in the ballot should contain :
1. The Sender kingdom
2. The Receiver kingdom
3. The Message (should be selected randomly from the messages.txt)
