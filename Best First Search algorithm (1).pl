edge(0,1,3). edge(1,0,3).
edge(0,2,6). edge(2,0,6).
edge(0,3,5). edge(3,0,5).
edge(1,4,9). edge(4,1,9).
edge(1,5,8). edge(5,1,8).
edge(2,6,12). edge(6,2,12).
edge(2,7,14). edge(7,2,14).
edge(3,8,7). edge(8,3,7).
edge(8,9,5). edge(9,8,5).
edge(8,10,6). edge(10,8,6).
edge(9,11,1). edge(11,9,1).
edge(9,12,10). edge(12,9,10).
edge(9,13,2). edge(13,9,2).

best_first_search(Source, Target, Path) :-
    Frontier = [[0, Source, [Source]]],
    Visited = [Source],
    best_first(Frontier, Visited, Target, Path).

best_first([], _, _, _) :- !, fail.
best_first(Frontier, Visited, Target, Path) :-
    select_min(Frontier, [Prio, Node, PathSoFar], RestFrontier),
    write(Node), write(' '),
    ( Node == Target ->
        Path = PathSoFar, nl
    ;
        findall([Cost2, Neighbor, NewPath],
                ( edge(Node, Neighbor, Cost2),
                  \+ member(Neighbor, Visited)
                ,
                  append(PathSoFar, [Neighbor], NewPath)
                ),
                NewEntries),
        % mark newly discovered neighbors visited to mirror Python behavior
        collect_neighbors(NewEntries, NewNeighbors, NewVisited),
        append(RestFrontier, NewNeighbors, NewFrontier),
        append(Visited, NewVisited, UpdatedVisited),
        best_first(NewFrontier, UpdatedVisited, Target, Path)
    ).

collect_neighbors([], [], []).
collect_neighbors([[C,N,P]|T], [[C,N,P]|Ns], [N|Vs]) :-
    collect_neighbors(T, Ns, Vs).

select_min([E], E, []) :- !.
select_min(Frontier, Min, Rest) :-
    find_min_entry(Frontier, Min),
    select(Min, Frontier, Rest).

find_min_entry([E], E) :- !.
find_min_entry([[P,N,Path]|Es], Min) :-
    find_min_acc(Es, [P,N,Path], Min).

find_min_acc([], Min, Min).
find_min_acc([[P2,N2,Path2]|Es], [P1,N1,Path1], Min) :-
    ( P2 < P1 -> New = [P2,N2,Path2] ; New = [P1,N1,Path1] ),
    find_min_acc(Es, New, Min).
