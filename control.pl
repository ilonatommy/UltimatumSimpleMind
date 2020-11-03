setPosition(Y,X) :-
	board(Y,X,_),
	% remove the previous position from KB
	retractall(position(_,_)),
	% add the current one
	asserta(position(Y,X)).

% PRIVATE SECTION
moveUp() :-
	position(Y,X),
	NY is Y-1,
	setPosition(NY,X).

moveDown() :-
	position(Y,X),
	NY is Y+1,
	setPosition(NY,X).

moveRight() :-
	position(Y,X),
	NX is X+1,
	setPosition(Y,NX).

moveLeft() :-
	position(Y,X),
	NX is X-1,
	setPosition(Y,NX).

moveUpOrLeft() :-
	(
		\+moveUp() ->
		moveLeft();
		callable(true)
	).

moveUpOrRight() :-
	(
		\+moveUp() ->
		moveRight();
		callable(true)
	).

moveDownOrLeft() :-
	(
		\+moveDown() ->
		moveLeft();
		callable(true)
	).

moveDownOrRight() :-
	(
		\+moveDown() ->
		moveRight();
		callable(true)
	).

% PUBLIC SECTION

% towardsEmotion should be used with negation, e.g.: \+towardsHappy(2).
% T is number of steps
towardsHappy(T) :-
	T > 0,
	% returns false if movement is possible (no wall blocks it)
	(
		% if move up failed then condition true
		\+moveUp() ->
		% and we try to move right
		(
			\+moveRight() ->
			moveLeft();
			callable(true)
		);
		callable(true)
	),
	TN is T-1,
	towardsHappy(TN).

towardsSad(T) :-
	T > 0,
	% returns false if movement is possible (no wall blocks it)
	(
		% if move up failed then condition true
		\+moveDown() ->
		% and we try to move right
		(
			\+moveRight() ->
			moveLeft();
			callable(true)
		);
		callable(true)
	),
	TN is T-1,
	towardsSad(TN).

towardsDisgusted(T) :-
	T > 0,
	position(Y,_),
	(	
		Y>2 ->
		moveUpOrLeft();
		(
			Y<2 ->
			moveDownOrLeft();
			moveLeft()
		)
	),
	TN is T-1,
	towardsDisgusted(TN).

towardsSurprised(T) :-
	T > 0,
	position(Y,_),
	(	
		Y>2 ->
		moveUpOrRight();
		(
			Y<2 ->
			moveDownOrRight();
			moveRight()
		)
	),
	TN is T-1,
	towardsSurprised(TN).

towardsAngry(T) :-
	T > 0,
	position(Y,_),
	(	
		Y>6 ->
		moveDownOrLeft();
		(
			Y<6 ->
			moveUpOrLeft();
			moveLeft()
		)
	),
	TN is T-1,
	towardsAngry(TN).

towardsFearful(T) :-
	T > 0,
	position(Y,_),
	(	
		Y>6 ->
		moveUpOrRight();
		(
			Y<6 ->
			moveDownOrRight();
			moveRight()
		)
	),
	TN is T-1,
	towardsSurprised(TN).

towardsCalm(T) :-
	T > 0,
	position(Y,X),
	(	
		Y==4 ->
		% we are at CALM row
		(
			X==2 ->
			% we are already at CALM field
			callable(true);
			(
				X<2 ->
				moveRight();
				moveLeft()
			)
		);
		% we are not at CALM row
		(
			Y<4 ->
			% we are above it
			moveDown();
			% we are below it
			moveUp()
		)		
	),
	TN is T-1,
	towardsCalm(TN).