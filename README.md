# The Adventures of the Turtle
_What was that noise?_

_You whip your head around, anxiously scanning the trees for whomever just snapped that twig. You quickly weigh your options: make a run for it, pick a fight, or freeze until the threat reveals itself—_

_—as a bunny. It's casually chewing on a piece of grass, looking so unbothered that you almost feel like it's mocking you. With a sigh of relief, you pick up your pace once more._

You're on the run after stealing the local dictatorship's crown jewels. As the guards close in behind you, there's only one thing standing between you and freedom: the infamous forest surrounding the kingdom. Make it through, and you're home free—the jewels are enough to pay your debts and establish the life of your dreams. Get caught, however, and the rest of your days become a nightmare. With only your wits to guide you, what will your fate be?

## What is our project about?
Our project is a choose-your-own-adventure personality test. Users face situations within the storyline, and their decisions inform the path they take through the forest, culminating in a unique ending that reveals something about their personality.

## Function Descriptions
Functions will cover three domains: making the Tkinter display, reading and displaying text from separate files, and interpreting user inputs to shape their ending.

### 1. Making the Tkinter display
- Establish a class `Display` with the following methods:
  - \_\_init\_\_(): Creates a Tkinter window. Calls the following methods.
  - init_window(): Initializes window. Accounts for window name, screen size, and frame sizes.
  - create_turtle_frame(): Adds frame that holds a canvas with a Turtle.
  - create_interface_frame(): Adds frame with buttons for user to interact with. Calls functions that will read and display text (questions and answer options).
 
### 2. Reading and displaying text from separate files

(separate functions - quiz, interactive function - turtle) 
- read the text file, assign the results to each of the functions. 
- the turtle: the turtle moves in response to the input from the user. The turtle would either stay on the route that its going on, or a different direction, depending on the choice of a, b, or c. - a, b, and c are different objects
- user will have a choice of a, b, c. Depending on which choice you choose the most, you are assigned to a certain personality type.

### Personality traits assigned depending on which choice is chosen the most

A - Despite the possibility of being harmed, you always choose to help.

B - You are a practical person who chooses to help when it does not hurt you, but you won't go out of the way to help.

C - You are a focused person, reliant on only your skills to reach your goals.

## Group Members + Github Usernames

Akhila: icearla16-hub, Nora: noralz2, Andrea: andrealo2432

## How our work is going to be split

  Each person will complete three functions. We will be working on it together in person.
  - Nora: The turtle, and how it is able to move around, incorporating user input.
  - Akhila: Based on the user input (ie. which object they choose), they turn a specific direction; In addition, the question asked for the person to decide which object they would like to choose (a text file).
  - Andrea: Visuals, math/tally of each of the chosen objects

#### How we are communicating: 
We have a group chat with each other to communicate with each other, and we would do weekly checkups.
