%TODO keep score (or should be kept outside?)
%TODO enforce limit on offers

moveAccordingToEmotion(Emo, Steps) :-
	Emo == happy -> 
		\+towardsHappy(Steps);
	Emo == sad ->
		\+towardsSad(Steps);
	Emo == angry ->
		\+towardsAngry(Steps);
	Emo == fearful ->
		\+towardsFearful(Steps);
	Emo == calm ->
		\+towardsCalm(Steps);
	Emo == disgusted ->
		\+towardsDisgusted(Steps);
	Emo == surprised ->
		\+towardsSurprised(Steps);
	callable(true).	

humanOffers(Offer, EmoFace, EmoVoice, RobotOffer) :-
	moveAccordingToEmotion(EmoFace, 2),
	moveAccordingToEmotion(EmoVoice, 1),	
	position(Y,X),
	board(Y,X, FieldValue), 
	reportRobotDecision(FieldValue > 0 -> yes ; no),
	plus(Offer, FieldValue, RobotOffer).
	

humanDecides(Decision) :-
	Decision == yes ->
		towardsHappy(1);
		towardsSad(1).

init_state :- 
	setPosition(2,3).

reportRobotDecision(RobotDecision) :-
	write("Robot "), 
	RobotDecision == yes -> write("Agreed") ; write("Declined"), nl.
