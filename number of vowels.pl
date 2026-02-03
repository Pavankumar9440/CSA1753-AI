% Predicate to check if a character is a vowel
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).
vowel('A').
vowel('E').
vowel('I').
vowel('O').
vowel('U').

% Base case: empty list has 0 vowels
count_vowels([], 0).

% If head is a vowel, increment count
count_vowels([H|T], Count) :-
    vowel(H),
    count_vowels(T, Rest),
    Count is Rest + 1.

% If head is not a vowel, do not increment
count_vowels([H|T], Count) :-
    \+ vowel(H),
    count_vowels(T, Count).
