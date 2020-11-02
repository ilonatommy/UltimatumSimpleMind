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

% TODO: T steps towards field HAPPY (returns too many values)
towardsHappy(0).
towardsHappy(T) :-
	towardsHappy_once(),
	TN is T-1,
	towardsHappy(TN).

towardsHappy_once() :-
	moveUp(),!.

towardsHappy_once() :-
	moveRight(),!.

towardsHappy_once() :-
	moveLeft().
