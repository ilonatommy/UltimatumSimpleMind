/*  
    File:    control.pl
    Purpose: Defines control over the board
*/

% regexp ([A-Za-z]+,)(?!\s) - code fromatting

module(
    control_2_0,
    [
        setPosition/2,
        towardsHappy/3,
        towardsSad/3,
        towardsAngry/3,
        towardsFearful/3,
        towardsCalm/3,
        towardsDisgusted/3,
        towardsSurprised/3
    ]
).

setPosition(Y, X) :-
	board(Y, X, _),
	% remove previous position
	retractall(position(_, _)),
	% set current position
	asserta(position(Y, X)).

% PRIVATE SECTION
moveUp() :-
	position(Y, X),
	NY is Y-1,
	setPosition(NY, X).

moveDown() :-
	position(Y, X),
	NY is Y+1,
	setPosition(NY, X).

moveRight() :-
	position(Y, X),
	NX is X+1,
	setPosition(Y, NX).

moveLeft() :-
	position(Y, X),
	NX is X-1,
	setPosition(Y, NX).

moveUpOrLeft() :-
	moveUp(),
	write("Moved up"), nl.

moveUpOrLeft() :-
	\+moveUp(),
	moveLeft(),
	write("Moved left"), nl.

moveUpOrLeft() :-
	\+moveUp(),
	\+moveLeft(),
	write("Move impossible"), nl.

moveUpOrRight() :-
	moveUp(),
	write("Moved up"), nl.

moveUpOrRight() :-
	\+moveUp(),
	moveRight(),
	write("Moved left"), nl.

moveUpOrRight() :-
	\+moveUp(),
	\+moveRight(),
	write("Move impossible"), nl.

moveDownOrLeft() :-
	moveDown(),
	write("Moved up"), nl.

moveDownOrLeft() :-
	\+moveDown(),
	moveLeft(),
	write("Moved left"), nl.

moveDownOrLeft() :-
	\+moveDown(),
	\+moveLeft(),
	write("Move impossible"), nl.

moveDownOrRight() :-
	moveDown(),
	write("Moved up"), nl.

moveDownOrRight() :-
	\+moveDown(),
	moveRight(),
	write("Moved left"), nl.

moveDownOrRight() :-
	\+moveDown(),
	\+moveRight(),
	write("Move impossible"), nl.

% PUBLIC SECTION

% towardsEmotion should be used with negation, e.g.: \+towardsHappy(2).
% T is number of steps

towardsHappy(Y, X, T) :-
	T > 0,
	% returns false if movement is possible (no wall blocks it)
	(
		moveUpOrRight()
	),
	TN is T-1,
	towardsHappy(Y, X, TN).

towardsSad(Y, X, T) :-
	T > 0,
	% returns false if movement is possible (no wall blocks it)
	(
		moveDownOrRight()
	),
	TN is T-1,
	towardsSad(Y, X, TN).

towardsDisgusted(Y, X, T) :-
	T > 0,
	(	
		moveUpOrLeft()
	),
	TN is T-1,
	towardsDisgusted(Y, X, TN).

towardsSurprised(Y, X, T) :-
	T > 0,
	(	
		moveUpOrRight()
	),
	TN is T-1,
	towardsSurprised(Y, X, TN).

towardsAngry(Y, X, T) :-
	T > 0,
	(	
		moveDownOrLeft()
	),
	TN is T-1,
	towardsAngry(Y, X, TN).

towardsFearful(Y, X, T) :-
	T > 0,
	(	
		moveUpOrRight()
	),
	TN is T-1,
	towardsSurprised(Y, X, TN).

towardsCalm(Y, X, T) :- % TODO: consider refactoring i.e. devide in to clauses
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
	towardsCalm(Y, X, TN).
