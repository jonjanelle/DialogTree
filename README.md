# Dialog Tree
A relatively simply dialog tree building system developed for use in an adventure game project. Uses a linked list approach an a custom data storage format. 

* The following is an example of the data format:

** .I knew this day would come.; Psh... | Howdy | Hola
** ..You've got some nerve. ; What? | I'm sorry | Who are you?
** ...Stay a while, and listen ; You're creepy. | Sure, I've got nowhere to be. | Spoon! [Run away]
** ...Would you like some tea? ; Coffeeeeee! [Attack!] | I thought you'd never ask
** ...I don't...I can remember!; boooooooooooring
** ..She gives you a silent, stern glare ; WOOOO! | Bloop | Glip!
** ...oh frip frap; grawr | dinosaurs are cool |
** ...SHOW ME WHAT YOU'VE GOT.; okey dokey | ground sloths love avocados | time to get schwifty
** ..What do you want? ; nada. | tu. | todo.


Leading periods represent the level in the hierarchy, with the single-period statement being the root node. Statements said by non-player entities appear to the left of the semicolon, and player reponse options are to the right separated by the '|' character.
The position of an item in the user response options corresponds to the location of the next message in the dialog tree. 

If the user says "Psh.." first, then the first message in the next level is chosen as 'Psh..' was the first option. Thus, 'Psh..' leads to 'You've got some nerve', 'Howdy' to 'She gives you a silent, stern glare', and 'Hola' to 'What do you want'?
