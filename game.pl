moveAccordingToEmotion(Emo, Steps) :-
	Emo == happy -> 
		towardsHappy(Steps);
		Emo == sad ->
			towardsSad(Steps);
			Emo == angry ->
				towardsAngry(Steps);
				Emo == fearful ->
					towardsFearful(Steps);
					Emo == calm ->
						towardsCalm(Steps);
						Emo == disgusted ->
							towardsDisgusted(Steps);
							Emo == surprised ->
								towardsSurprised(steps);
								callable(true).	


% RobotOffer is not returned as deduced value. Why? 
% TODO: fix it
humanOffers(Offer, EmoFace, EmoVoice, RobotDecision, RobotOffer) :-
	moveAccordingToEmotion(EmoFace, 2),
	moveAccordingToEmotion(EmoVoice, 1),	
	position(Y,X),
	FieldValue = board_r(Y,X),
	% TODO: add boundaries of 1 and 9:
	RobotOffer = Offer + FieldValue,
	FieldValue > 0 ->
		RobotDecision = true;
		RobotDecision = false.

humanDecides(Decision) :-
	Decision == yes ->
		towardsHappy(1);
		towardsSad(1).

% TODO: add a predicate for one round of game and a predicate with 
% startup (setting the player on the board at initial location).