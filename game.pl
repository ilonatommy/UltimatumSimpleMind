%TODO keep score (or should it be kept outside?)
%TODO enforce limit on offers
moveAccordingToEmotion(happy, Steps) :-
	\+towardsHappy(Steps).

moveAccordingToEmotion(sad, Steps) :-
	\+towardsSad(Steps).

moveAccordingToEmotion(angry, Steps) :-
	\+towardsAngry(Steps).	

moveAccordingToEmotion(fearful, Steps) :-
	\+towardsFearful(Steps).

moveAccordingToEmotion(calm, Steps) :-
	\+towardsCalm(Steps).

moveAccordingToEmotion(disgusted, Steps) :-
	\+towardsDisgusted(Steps).

moveAccordingToEmotion(surprised, Steps) :-
	\+towardsSurprised(Steps).

humanOffers(Offer, EmoFace, EmoVoice, RobotOffer) :-
	moveAccordingToEmotion(EmoFace, 2),
	moveAccordingToEmotion(EmoVoice, 1),	
	position(Y, X),
	board(Y, X, FieldValue), 
	reportRobotDecision(FieldValue > 0 -> yes ; no),
	plus(Offer, FieldValue, RobotOffer).

humanDecides(Decision) :-
	Decision == yes ->
		\+towardsHappy(1);
		\+towardsSad(1),
	write("Make your offer!").

init_state :- 
	setPosition(2,3).

reportRobotDecision(RobotDecision) :-
	write("Robot "), 
	RobotDecision == yes -> write("Agreed") ; write("Declined"), nl.