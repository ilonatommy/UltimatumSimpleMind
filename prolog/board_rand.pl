:- module(
	board_rand,
    [
		board_r/3,
    	is_valid_r/2
	]
).

board_r(0, 2, -3).

board_r(1, 1, Y) :- 
	random_between(-2, 1, Y).
board_r(1, 2, Y) :-
	random_between(-3, 0, Y).
board_r(1, 3, Y) :-
	random_between(-2, 1, Y).

board_r(2, 0, 1).
board_r(2, 1, Y) :-
	random_between(-1, 1, Y).
board_r(2, 2, Y) :-
	random_between(-2, 1, Y).
board_r(2, 3, Y) :-
	random_between(-1, 1, Y).
board_r(2, 4, 1).

board_r(3, 0, 1).
board_r(3, 1, 1).
board_r(3, 2, 1).
board_r(3, 3, 1).
board_r(3, 4, 1).

board_r(4, 0, Y) :-
	random_between(1, 2, Y).
board_r(4, 1, 1).
board_r(4, 2, 1).
board_r(4, 3, 1).
board_r(4, 4, Y) :-
	random_between(1, 2, Y).

board_r(5, 0, Y) :-
	random_between(1, 2, Y).
board_r(5, 1, Y) :-
	random_between(1, 2, Y).
board_r(5, 2, Y) :-
	random_between(1, 2, Y).
board_r(5, 3, Y) :-
	random_between(1, 2, Y).
board_r(5, 4, Y) :-
	random_between(1, 2, Y).

board_r(6, 0, 2).
board_r(6, 1, Y) :-
	random_between(2, 3, Y).
board_r(6, 2, Y) :-
	random_between(2, 3, Y).
board_r(6, 3, Y) :-
	random_between(2, 3, Y).
board_r(6, 4, 2).

board_r(7, 1, Y) :-
	random_between(2, 3, Y).
board_r(7, 2, Y) :-
	random_between(2, 3, Y).
board_r(7, 3, Y) :-
	random_between(2, 3, Y).

board_r(8, 2, 3).

is_valid_r(Y, X) :-
    board_r(Y, X, _).