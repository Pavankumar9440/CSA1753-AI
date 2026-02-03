% simple expert system: disease diagnosis interactive program

% initial entry point
run :-
    init_console,
    write('What is the patient''s name? '),
    read_line_atom(Patient),
    ( hypothesis(Patient, Disease) ->
        write(Patient), write(' probably has '), write(Disease), write('.'), nl
    ;
        write('Sorry, I don''t seem to be able to'), nl,
        write('diagnose the disease.'), nl
    ).

% initialize console for portability (no-op for many Prologs)
init_console.

% read a line from input and return it as an atom
read_line_atom(Atom) :-
    read_line_chars(Chars),
    ( Chars = [] -> Atom = '' ; atom_chars(Atom, Chars) ).

read_line_chars(Chars) :-
    get_char(C),
    ( C = '\n' -> Chars = [] ; read_line_chars(Rest), Chars = [C|Rest] ).

% read a single non-newline character as response (y/n)
response(Reply) :-
    get_char(C),
    ( C = '\n' -> response(Reply) ; Reply = C ).

% symptoms (each asks user and reads y/n)
symptom(Patient, fever) :-
    write('Does '), write(Patient), write(' have a fever (y/n) ? '),
    response(Reply), Reply = 'y'.
symptom(Patient, rash) :-
    write('Does '), write(Patient), write(' have a rash (y/n) ? '),
    response(Reply), Reply = 'y'.
symptom(Patient, headache) :-
    write('Does '), write(Patient), write(' have a headache (y/n) ? '),
    response(Reply), Reply = 'y'.
symptom(Patient, runny_nose) :-
    write('Does '), write(Patient), write(' have a runny_nose (y/n) ? '),
    response(Reply), Reply = 'y'.
symptom(Patient, conjunctivitis) :-
    write('Does '), write(Patient), write(' have a conjunctivitis (y/n) ? '),
    response(Reply), Reply = 'y'.
symptom(Patient, cough) :-
    write('Does '), write(Patient), write(' have a cough (y/n) ? '),
    response(Reply), Reply = 'y'.
symptom(Patient, body_ache) :-
    write('Does '), write(Patient), write(' have a body_ache (y/n) ? '),
    response(Reply), Reply = 'y'.
symptom(Patient, chills) :-
    write('Does '), write(Patient), write(' have chills (y/n) ? '),
    response(Reply), Reply = 'y'.
symptom(Patient, sore_throat) :-
    write('Does '), write(Patient), write(' have a sore_throat (y/n) ? '),
    response(Reply), Reply = 'y'.
symptom(Patient, sneezing) :-
    write('Does '), write(Patient), write(' have sneezing (y/n) ? '),
    response(Reply), Reply = 'y'.
symptom(Patient, swollen_glands) :-
    write('Does '), write(Patient), write(' have swollen_glands (y/n) ? '),
    response(Reply), Reply = 'y'.

% hypotheses (disease rules)
hypothesis(Patient, measles) :-
    symptom(Patient, fever),
    symptom(Patient, cough),
    symptom(Patient, conjunctivitis),
    symptom(Patient, runny_nose),
    symptom(Patient, rash).

hypothesis(Patient, german_measles) :-
    symptom(Patient, fever),
    symptom(Patient, headache),
    symptom(Patient, runny_nose),
    symptom(Patient, rash).

hypothesis(Patient, flu) :-
    symptom(Patient, fever),
    symptom(Patient, headache),
    symptom(Patient, body_ache),
    symptom(Patient, conjunctivitis),
    symptom(Patient, chills),
    symptom(Patient, sore_throat),
    symptom(Patient, runny_nose),
    symptom(Patient, cough).

hypothesis(Patient, common_cold) :-
    symptom(Patient, headache),
    symptom(Patient, sneezing),
    symptom(Patient, sore_throat),
    symptom(Patient, runny_nose),
    symptom(Patient, chills).

hypothesis(Patient, mumps) :-
    symptom(Patient, fever),
    symptom(Patient, swollen_glands).

hypothesis(Patient, chicken_pox) :-
    symptom(Patient, fever),
    symptom(Patient, chills),
    symptom(Patient, body_ache),
    symptom(Patient, rash).

% alternate measles-like rule (kept as additional pattern)
hypothesis(Patient, measles) :-
    symptom(Patient, cough),
    symptom(Patient, sneezing),
    symptom(Patient, runny_nose).

% entry point compatible with some environments
main :- run.
