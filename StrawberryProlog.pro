sibling(X,Y):-
	parent(X,Z),
	parent(Y,Z).

sister(X,Y):-
	sibling(X,Y),
	female(Y).

grandson(X,Y):-
	male(X),
	parent(X,Z),
	parent(Z,Y).

granddaughter(X,Y):-
	female(X),
	parent(X,Z),
	parent(Z,Y).

descendant(X,Y):-
	parent(X,Y);
	grandson(X,Y).
	

father(X,Y):-
	parent(X,Y),
	male(Y).

mother(X,Y):-
	parent(X,Y),
	female(Y).

myappend([],List,List).
myappend([H|T],List,[H|List2]):-
	myappend(T,List,List2).

remove(E,[],[]).
remove(E,[E|T],T).
remove(E,[H|T],[H|T2]):-
	remove(E,T,T2).

subsequence(List,List).
subsequence(L1, [H,H1|L2]):-
	subsequence(L1,[H,H1]);
	subsequence(L1,L2).
	
union([],[],[]).
union([],L2,R).
union([H|T],L2,R):-
	remove(H,L2,R),
	union(T,L2,R).
		
	
	
	

?- 

union([0],[1,2,3,4,5],R),
	write(R).

myappend([1,2,3], [1,2,5], R),
	write(R).

remove(a,[b,a,d,a],R),
	write(R).

remove(E,[b,a,d,a],R),
	write(R).

remove(E,L,[b,a,d]),
	write(R).

remove(p(X),[a,p(a),p(p(a)),p(p(p(a)))],R),
	write(R).
