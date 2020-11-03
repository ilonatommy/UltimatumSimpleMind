setPosition(Y,X) :-
	board(Y,X,_),
	% remove the previous position from KB
	retractall(position(_,_)),
	% add the current one
	asserta(position(Y,X)).

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

% TODO: how to write other TowardsEmotion predicates?