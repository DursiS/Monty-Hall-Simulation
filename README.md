# Monty-Hall-Simulation
The Montal Hall problem is a probability brain-teaser.


Context.

Suppose you're on a gameshow. Such that the host, Monty, prompts you the possibility to win a cat!
There are three doors you can chose from. Only 1 of which the cat is behind, the two other are empty.

So you chose on of the three doors at random. Without knowing what's behind it right away. 
Monty reveals that one of the two doors are empty.

The brain-teaser comes in 'the switch'. Monty prompts you to either keep your current door or switch 
To the other door he didn't reveal. But does it even matter if you switch or not, it's a 50/50 right?


Explaination.

No, in fact switching your door on average wins you the cat 2/3 of the times.
While picking and holding only wins 1/3 of the time.

I like to think this is because of a underrated fact about how Monty runs his show.
Suppose you chose the first door. When Monty reveals a empty door, it means one of three scenarios:
1. You hold the correct door, so Monty choses some door at random between 2 and 3.
2. You hold a empty door, so Monty skips over the correct door 2 and choses door 3 to reveal.
3. You hold a empty door, so Monty skips over the correct door 3 and choses door 2 to reveal.

He's not just picking any random door, he can't without possibily revealing the cat.
He's is providing you with information about the game. Filtering one of the answers out for you.
Making the odds twice as good as your original 1/3 pick and hold strategy.
