setPosition(Y,X) :-
	board(Y,X,_).

% PRIVATE SECTION
moveUp(Y,X) :-
	NY is Y-1,
	setPosition(NY,X).

moveDown(Y,X) :-
	NY is Y+1,
	setPosition(NY,X).

moveRight(Y,X) :-
	NX is X+1,
	setPosition(Y,NX).

moveLeft(Y,X) :-
	NX is X-1,
	setPosition(Y,NX).

moveUpOrLeft(Y,X) :-
	(
		\+moveUp(Y,X) ->
		moveLeft(Y,X);
		callable(true)
	).

moveUpOrRight(Y,X) :-
	(
		\+moveUp(Y,X) ->
		moveRight(Y,X);
		callable(true)
	).

moveDownOrLeft(Y,X) :-
	(
		\+moveDown(Y,X) ->
		moveLeft(Y,X);
		callable(true)
	).

moveDownOrRight(Y,X) :-
	(
		\+moveDown(Y,X) ->
		moveRight(Y,X);
		callable(true)
	).

% PUBLIC SECTION

% towardsEmotion should be used with negation, e.g.: \+towardsHappy(2).
% T is number of steps
towardsHappy(Y,X,T) :-
	T > 0,
	% returns false if movement is possible (no wall blocks it)
	(
		% if move up failed then condition true
		\+moveUp(Y,X) ->
		% and we try to move right
		(
			\+moveRight(Y,X) ->
			moveLeft(Y,X);
			callable(true)
		);
		callable(true)
	),
	TN is T-1,
	towardsHappy(Y,X,TN).

towardsSad(Y,X,T) :-
	T > 0,
	% returns false if movement is possible (no wall blocks it)
	(
		% if move up failed then condition true
		\+moveDown(Y,X) ->
		% and we try to move right
		(
			\+moveRight(Y,X) ->
			moveLeft(Y,X);
			callable(true)
		);
		callable(true)
	),
	TN is T-1,
	towardsSad(Y,X,TN).

towardsDisgusted(Y,X,T) :-
	T > 0,
	(	
		Y>2 ->
		moveUpOrLeft(Y,X);
		(
			Y<2 ->
			moveDownOrLeft(Y,X);
			moveLeft(Y,X)
		)
	),
	TN is T-1,
	towardsDisgusted(Y,X,TN).

towardsSurprised(Y,X,T) :-
	T > 0,
	(	
		Y>2 ->
		moveUpOrRight(Y,X);
		(
			Y<2 ->
			moveDownOrRight(Y,X);
			moveRight(Y,X)
		)
	),
	TN is T-1,
	towardsSurprised(Y,X,TN).

towardsAngry(Y,X,T) :-
	T > 0,
	(	
		Y>6 ->
		moveDownOrLeft(Y,X);
		(
			Y<6 ->
			moveUpOrLeft(Y,X);
			moveLeft(Y,X)
		)
	),
	TN is T-1,
	towardsAngry(Y,X,TN).

towardsFearful(Y,X,T) :-
	T > 0,
	(	
		Y>6 ->
		moveUpOrRight(Y,X);
		(
			Y<6 ->
			moveDownOrRight(Y,X);
			moveRight(Y,X)
		)
	),
	TN is T-1,
	towardsSurprised(Y,X,TN).

towardsCalm(Y,X,T) :- % TODO: consider refactoring i.e. devide in to clauses
	T > 0,
	(	
		Y==4 ->
		% we are at CALM row
		(
			X==2 ->
			% we are already at CALM field
			callable(true);
			(
				X<2 ->
				moveRight(Y,X);
				moveLeft(Y,X)
			)
		);
		% we are not at CALM row
		(
			Y<4 ->
			% we are above it
			moveDown(Y,X);
			% we are below it
			moveUp(Y,X)
		)		
	),
	TN is T-1,
	towardsCalm(Y,X,TN).
