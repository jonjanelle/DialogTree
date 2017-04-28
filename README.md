# Dialog Tree
A relatively simply dialog tree building system developed for use in an adventure game project. Uses a linked list approach an a custom data storage format. 

## Data Format Example:
.Stop right there!; Whatever. | Howdy | Bye.

..Excuse me? ; You're excused. | I'm sorry. | Bye.

...This isn't going well. ; Okay, bye then. 

...No problem, go right ahead! ; Thanks, have a nice day!

..She gives you a silent, stern glare ; WOOOO! | Bloop! | Glorp!

...What?; See ya! [Run away] | Yay dinosaurs! [Run away] 

..Bye bye! ; [Wave with gusto]

### Explanation
* Leading periods represent the level in the hierarchy, with the single-period statement being the root node. Each dialog tree must have exactly one root node. 
* Player and non-player text is separated by a semicolon. Statements said by non-player entities appear to the left of the semicolon, and player reponse options appear to the right.
* Player response options are separated by the '|' character.
* The position of an item in the user response options corresponds to the location of the next message in the dialog tree. 

* If the user chooses "Whatever", the first option in level 1, then "Excuse me?" is next because it is the first level 2 message.   

Similarly in level 1:
* 'Howdy' --> 'She gives you a silent, stern glare'
* 'Bye' --> 'Bye bye!'

This pattern is continued throughout subsequent levels. 
