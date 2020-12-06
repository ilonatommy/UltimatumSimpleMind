:- module(
    board_fixed,
    [
        board/3,
        is_valid/2
    ]
).

board(0, 2, -3).

board(1, 1, -2).
board(1, 2, -3).
board(1, 3, -2).

board(2, 0, 1).
board(2, 1, -1).
board(2, 2, -2).
board(2, 3, -1).
board(2, 4, 1).

board(3, 0, 1).
board(3, 1, 1).
board(3, 2, 1).
board(3, 3, 1).
board(3, 4, 1).

board(4, 0, 1).
board(4, 1, 1).
board(4, 2, 1).
board(4, 3, 1).
board(4, 4, 1).

board(5, 0, 1).
board(5, 1, 1).
board(5, 2, 1).
board(5, 3, 1).
board(5, 4, 1).

board(6, 0, 2).
board(6, 1, 2).
board(6, 2, 2).
board(6, 3, 2).
board(6, 4, 2).

board(7, 1, 2).
board(7, 2, 2).
board(7, 3, 2).

board(8, 2, 3).

is_valid(Y, X) :-
    board(Y, X, _).