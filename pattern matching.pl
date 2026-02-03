% Pattern matching with facts
likes(john, pizza).
likes(mary, pasta).
likes(rahul, biryani).

% Pattern matching using rules
food_lover(Person) :-
    likes(Person, _).

% Pattern matching with lists
head_tail([H|T], H, T).

% Pattern matching to check a specific pattern in a list
starts_with_a([a|_]).
