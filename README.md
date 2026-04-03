# The Adventures of the Turtle
___What was that noise?___

_You whip your head around, anxiously scanning the trees for whomever just snapped that twig. You quickly weigh your options: make a run for it, pick a fight, or freeze until the threat reveals itself—_

_—as a bunny. It's casually chewing on a piece of grass, looking so unbothered that you almost feel like it's mocking you. With a sigh of relief, you continue on your way._

You're on the run after stealing the local dictatorship's crown jewels. As the guards close in behind you, there's only one thing standing between you and freedom: the infamous forest surrounding the kingdom. Make it through, and you're home free—the jewels are enough to pay your debts and establish the life of your dreams. Get caught, however, and the rest of your days will become a nightmare. With only your wits to guide you, what will your fate be?

## What is our project about?
Our project is a choose-your-own-adventure personality test. Users face situations within the storyline, and their decisions inform the path they take through the forest, culminating in a unique ending that reveals something about their personality.

## Function Descriptions
Functions will cover three major domains: making the Tkinter display, controlling the Turtle within the Tkinter window, and handling files with questions, answer options, and user data. Each of these domains will likely have their own folder within the project directory for modularity.

- `survey.py` - Reading in the file for the questions, asking the questions, and saving the input from the user
- `trtle.py` - The turtle class
- `instructions.txt` - The instructions that show up for the user prior to the start of the adventure
- `questions.txt` - List of questions
- `answers.txt` - Stores list of answers from user
- `counting.py` - Counts the amount of times that the user has chosen each choice (a, b, or c), and gives output of which option the user had chosen the most

### 1. Making the Tkinter display
> NOTE: Lab 7 may be a helpful reference

Establish a class `Display` with the following methods:
- \_\_init\_\_(): Creates a Tkinter window. Calls the following methods.
- init_window(): Initializes window. Accounts for window name, screen size, and frame sizes.
- create_turtle_frame(): Adds frame that holds a canvas with a Turtle. Calls functions that control the Turtle.
- create_interface_frame(): Adds frame with buttons for user to interact with. Calls functions that will read and display text (questions and answer options).
 
### 2. Controlling the Turtle
Ideally, the Turtle display will show a maze with trees as blockades. If possible, this will be the Turtle canvas's background. If not, each tree might be a Turtle object itself placed at a particular location. The user's Turtle will start at the bottom center and navigate through the maze. At each fork, the user is given a question and will continue moving after making a response.

If we want to add complexity, we can make the Turtle's next move dependent on the response given. For now, it's easiest if the Turtle is on a fixed path (unbeknownst to the user), but the subsequent questions change depending on the response. Functions will look something like this, but with varying directions:
       
    if response:
      t.right(90)
      t.forward(10)

Also, the Turtle should have a function to "sense" when it reaches a fork (i.e., when the spaces on either side are not occupied by a blockade) to prompt a question.

### 3. Reading and displaying text from separate files, organizing user inputs
> NOTE: Homework 3 may be a helpful reference

Import questions.txt and options.csv. The answer options will be formatted as follows:

    OPTION,a  
    OPTION,b  
    OPTION,c  

to allow for easy tallying of the user's responses. If the user chooses mostly a's, they receive end result A, and so on (see below).

  - A - Despite the possibility of being harmed, you always choose to help.
  - B - You are a practical person who chooses to help when it does not hurt you, but you won't go out of your way to help.
  - C - You are a focused person, reliant on only your skills to reach your goals.

This will require the following functions:
- read_questions(): Read the questions file. Display questions one-at-a-time when prompted.
- read_options(): Read the answer options file. Display options either on or above buttons in the interface frame, but do not indicate a, b, or c (those are just for our organization).
- Add user responses to a .csv or list. Loop through and find the mode (maybe 1, 2, 3 is easier than a, b, c?), which will determine the final outcome.
- Display the user's final outcome.

## Testing

Throughout the game, the user should be able to see a turtle, that is appearing to go through a forest. As the turtle reaches certain parts of the forest, it should be stopped, and given the choice between three choices, and should be able to smootly pick between the three choices. This should happen eight times throughout the game, and at the very end, the user should be shown a conclusion of which personality their choices line up with depending on their choices throughout the game.

## Group Members + Github Usernames

Akhila: icearla16-hub  
Nora: noralz2  
Andrea: andrealo2432

## How our work is going to be split

  Each person will complete three functions. We will be working on it together in person.
  - Nora: The turtle, and how it is able to move around, incorporating user input.
  - Akhila: Based on the user input (ie. which object they choose), they turn a specific direction; In addition, the question asked for the person to decide which object they would like to choose (a text file).
  - Andrea: Visuals, math/tally of each of the chosen objects

#### How we are communicating: 
We have a group chat with each other to communicate with each other, and we would do weekly checkups.
