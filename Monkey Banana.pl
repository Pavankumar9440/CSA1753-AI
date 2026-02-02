% Initial and goal states
initial_state(state(at_door, on_floor, at_window, hanging)).
goal_state(state(_, _, _, has)).

% Possible actions
move(state(P1, on_floor, B, H),
     walk(P1, P2),
     state(P2, on_floor, B, H)).

move(state(P1, on_floor, P1, H),
     push(P1, P2),
     state(P2, on_floor, P2, H)).

move(state(middle, on_floor, middle, H),
     climb,
     state(middle, on_box, middle, H)).

move(state(middle, on_box, middle, hanging),
     grab,
     state(middle, on_box, middle, has)).

% Solver with visited-state checking
solve(State, _, []) :-
    goal_state(State).

solve(State, Visited, [Action|Plan]) :-
    move(State, Action, NewState),
    \+ member(NewState, Visited),
    solve(NewState, [NewState|Visited], Plan).

% Start predicate
start :-
    initial_state(State),
    solve(State, [State], Plan),
    write('Solution Steps:'), nl,
    write(Plan), nl.
