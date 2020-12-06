/*  
    File:    game.pl
    Purpose: Definies user interaction with the module
*/

:- module(
	game,
	[
		init_state/0,
		humanOffers/5,
		humanDecides/1
	]
).

%TODO keep score (or should it be kept outside?)
%TODO enforce limit on offers
moveAccordingToEmotion(Y,X,happy, Steps) :-
	\+towardsHappy(Y,X,Steps).

moveAccordingToEmotion(Y,X,sad, Steps) :-
	\+towardsSad(Y,X,Steps).

moveAccordingToEmotion(Y,X,angry, Steps) :-
	\+towardsAngry(Y,X,Steps).	

moveAccordingToEmotion(Y,X,fearful, Steps) :-
	\+towardsFearful(Y,X,Steps).

moveAccordingToEmotion(Y,X,calm, Steps) :-
	\+towardsCalm(Y,X,Steps).

moveAccordingToEmotion(Y,X,disgusted, Steps) :-
	\+towardsDisgusted(Y,X,Steps).

moveAccordingToEmotion(Y,X,surprised, Steps) :-
	\+towardsSurprised(Y,X,Steps).

moveAccordingToFaceEmotion(Y, X, EmoFace) :-
	moveAccordingToEmotion(Y, X, EmoFace, 2).

moveAccordingToVoiceEmotion(Y, X, EmoVoice) :-
	moveAccordingToEmotion(Y, X, EmoVoice, 1).

humanOffers(Offer, EmoFace, EmoVoice, RobotOffer, RobotDecision) :-
	position(Y, X),
	moveAccordingToFaceEmotion(Y, X, EmoFace),
	moveAccordingToVoiceEmotion(Y, X, EmoVoice),
	board(Y, X, RobotDecision), 
	% reportRobotDecision(RobotDecision > 0 -> yes ; no),
	plus(Offer, RobotDecision, RobotOffer).

humanDecides(yes) :-
	position(Y, X),
	\+towardsHappy(Y, X, 1),
	write("Make your offer!").

humanDecides(no) :-
	position(Y, X),
	\+towardsSad(Y, X, 1),
	write("Make your offer!").
	
init_state() :-
	setPosition(1, 2).

reportRobotDecision(RobotDecision) :-
	write("Robot "), 
	RobotDecision == yes -> write("Agreed") ; write("Declined"), nl.
