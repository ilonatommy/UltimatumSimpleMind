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

% TODO: T steps towards field HAPPY (does not work for T>1)
towardsHappy(0).

towardsHappy(T) :-
	moveUp(); 
	T > 1,
	NT is T-1,
	towardsHappy(NT),!.

towardsHappy(T) :-
	moveRight();
	T > 1, 
	NT is T-1,
	towardsHappy(NT),!.

towardsHappy(T) :-
	moveLeft();
	T > 1,
	NT is T-1,
	towardsHappy(NT),!.
