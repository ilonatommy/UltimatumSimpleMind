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

humanOffers(Y, X, Offer, EmoFace, EmoVoice, RobotOffer, RobotDecision, Y_out, X_out) :-
	moveAccordingToEmotion(Y, X, EmoFace, 2),
	moveAccordingToEmotion(Y, X, EmoVoice, 1),
	board(Y, X, RobotDecision), 
	Y_out = Y,
	X_out = X,
	reportRobotDecision(RobotDecision > 0 -> yes ; no),
	plus(Offer, RobotDecision, RobotOffer).

humanDecides(Y,X,yes,Y_out,X_out) :-
	\+towardsHappy(Y,X,1),
	Y_out = Y,
	X_out = X,
	write("Make your offer!").

humanDecides(Y,X,no,Y_out,X_out) :-
	\+towardsSad(Y,X,1),
	Y_out = Y,
	X_out = X,
	write("Make your offer!").
	
init_state(Y,X) :- 
	Y = 3,
	X = 2,
	setPosition(Y,X).

reportRobotDecision(RobotDecision) :-
	write("Robot "), 
	RobotDecision == yes -> write("Agreed") ; write("Declined"), nl.
