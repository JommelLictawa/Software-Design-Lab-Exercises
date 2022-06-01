#algorithm
1. definition of function BFS (T):
2. Initialize queue Q to contain T.root( )
3. while Q is not empty 
4. p = Q.dequeue( )#to be executed under while loop
5. perform the “visit” action for position p
6. for each child c in T.children(p) do #for all neighbours with p is Graph T
7. Q.enqueue(c) #stores c in Q to visit more its neighbours
