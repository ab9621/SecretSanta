# Secret Santa 

This is a set of functions to generate pairings for Secret Santa. It has been used for a group of friends that contain several couples and has been done over multiple years so the following rules are implemented:
1. If person A has person B, person B cannot have person A.
2. If person A and person B are a couple, they cannot have each other.
3. If person A previously had person B then this time they will not have person B.

This does not check if a solution is possible, if this has been running for many years then some repetition will be required. Use some common sense when setting it up. It will also write this out to a text file so whoever generates it can just send it on to the correct person, the text file is named with the name of the person to send it to, so the person who generates it won't know who everyone has (if they don't look!).

Remember to customise the message that will go in the text file with relevant information such as price limit and when you are going to give them out.

## Quiz Edition

Due to COVID induced lockdowns, we started doing quizzes over VOIP with each person doing a round. This is essentially the same problem as the Secret Santa problem so the additional capability to generate pairs of people, the first decides a topic and sends it to the second person in the pair. It also randomly assigns a number of picture rounds. The rules above also apply here with the additional rule:
1. If you had a picture round last time, you won't have one this time.

## Installation

Use git to clone this repo or just download the SecretSanta.py file, it is all self contained in there. It does not using anything outside of the libraries that come with a standard version of Python. It was written in Python 3.7.x so is known to work with that version. Working with other versions is not guaranteed but really there is no reason it should not, it only uses basic functionality of the random and os libraries.

## Usage

At the bottom of the file, under the '__main__' construct is an example of using it.

## Issues

If you find any bugs in the code or would really like some functionality that is not currently there, feel free to post an issue and I will try to get around to it.