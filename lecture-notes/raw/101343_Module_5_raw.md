So now we're going to talk about games.
The sort of games we're going to
talk about are tic-tac-toe,
connect for checkers, chess,
Go, backgammon, and even poker.
And what we're going to find is
that from an agent perspective,
games are just a special form
of state space search.
So for states, we
have game and board configurations,
pieces, cards,
the cards are showing or not showing.
We have actions which are going to be moods
or rolling the dice
and other gang-related play.
We have a transition model which is
given a game or
board configuration and a move,
what the next game state
is and also whose turn it is.
But also have costs.
Or the costs are usually
modeled as being uniform.
We're going to add is this notion of payoffs.
So when you get to a final game state,
a terminal game state,
and there's going to be some utility.
And this can either be explicit in the form
of points for games like bridge cleavage,
or it can be implicit.
For example, we might award 1 for
when deducted point for
a loss and 0 for a draw, our tie.
So now let's talk about some of
the specialized terms for search.
The first is a game tree.
Game tree shows the entire
game from beginning to
end as a succession of
game states and actions,
moods alternating between the players.
The game tree starts with
a root node to the root state column nodes.
And this is just a board.
So for tic-tac-toe, this is
just the empty board getting before x goes.
And now this is x and x
has nine possible moves.
And depending on which move x makes,
that will be the board for the other player.
And so each of these nodes here is
now a state after X is gone.
Now to confuse things, this
is called not a move.
Apply. So one action
on the part of one
of the two players is called Apply.
And now it's going to be zeros turn.
And each of these nodes
represents a new state
where 0 has gone
either in one of
the other possible positions that are left.
And this is also apply.
And two-ply is what
constitutes move in game terminology.
And we can continue on down the tree where
green now gets to go from
any one of these possible states.
And red gets ago and we can
show that this tree continues on.
And it continues on until some of the nodes
get to be winning or losing or tie boards.
And we call these terminal or leaf nodes.
And so this is one of the possible boards.
And here's another part.
Although this isn't a terminal part,
so we better change the color up anode.
And so play would continue on from there.
And this is called the extensive-form game.
And the alternative is
a normal form and we'll
talk about that in another video.
Game is considered to be solved.
If the entire game tree has
been or can be generated for it.
That's from beginning to all possible,
possible winning,
losing draw States on terminal nodes.
And this is really only been done
for two or three games.
Tic-tac-toe checkers, some versions of them.
So now that we're given again,
we can ask ourselves, how does
an agent learn to play it optimally?
So let's look at a really
simple game for this,
where each agent player
gets to go either left or right.
So here we have
the agent which is at the root,
and there's a game state and
starts and go left to right.
The opponent can go left to right.
And then the agent gets to make
one more move and going left or right.
And then that will result
in some terminal state.
And its terminal states will just
score using one and minus
10 for wins, losses, and ties.
So we can think of how we play games.
So we're at a current board
and we think, well,
what F there's now
and these are the future moves.
And you can think, well, if I do this,
what will, what will my opponent do?
It's the smart thing for my opponent to do.
And then if he does that, she does that.
What should I do in, in, in response?
So we can look at these sub trees here.
I'm starting here on the left.
We can look and say, well,
if that's the situation,
I'm going to the left because
that results in the win.
Let's carry that value up.
For this other one, I'll
go left because it results
in a tie and that's better than
the loss for this other one.
I can also go, I can go
right and I can go right again.
Now, what is my opponent going to do?
My opponent is going to go, right,
because that would result in a tie for him.
And now we're going to say if
two moves have the same value,
we'll break them randomly.
And now we propagate the value to the top.
And it says, Well,
we should definitely go right,
because that will be a win for us.
And then we want to go left because that will
be when Mark than at random.
And then we're going to do Go right,
because that's a win.
And there's actually an algorithm that does
this is called the minimax algorithm.
Any Min situation as I
put myself in my opponent's shoes.
And those are the red nodes.
And any MAC situation is
what was the best thing I can do.
What I mean, I mean the agent.
So we always start out
the root is a max and we
alternate between max, Min and max.
So this, the main difference between
regular state space search and games.
Agent wants to achieve a goal.
But there's an adversary who wants to achieve
at least a conflicting goal
and perhaps an opposite goal.
But there's a catch.
Of course.
For almost all games of any great interest.
We simply cannot generate
the entire game tree in memory.
That is, we can't solve most games,
we simply can't solve.
That is go from an empty board
to all of the winning and losing boards.
So what should we do? What can we do?
It turns out we have
this basic idea that says,
well, let me think of the current board.
And way off hundreds of plays later.
There are these winning and losing boards.
But right now I have two moves.
One will result in board a,
and one will result in board b.
And a is on the path to this winning,
and B is on the path to this losing game.
I would want some way to
indicate that I should pick a over B.
Now, given that I
don't know what will eventually happen.
Similarly, I made it this later game
state and have these choices between C and D.
C which leads to a winning board, D,
which leads to a losing board,
would want something that tells
me how I should pick C over D.
So what we need to be
able to do is we need to
be able to assign scores to
game states that indicate how good they
are that they're going to
lead to either a win or a loss.
And so we would want, say,
a higher score for a game
that we know is on the way to
a win and a low score for
a board we know is on the way to a loss.
So all we need is a heuristic function.
And we are going to have a lot of
different heuristic functions in this course.
And this one is not the same thing as
the A-star search heuristic.
So for a game, a good heuristic
is one that's going to be able to
distinguish boards that are on the way to
a win from boards
that are on the way to the loss.
In this case, it should have been able to
distinguish that a was a better board than B,
and at C was a better board than
D. And now we're target.
In this particular case, we're talking
about good, not admissible.
There's no sense of an invisible or
an admissible heuristic function
in game states search.
So how do we use a heuristic?
Because we know we can't expand
the game tree all the way out.
So let's assume that we're in.
Again,
we don't know whether this is the root,
is the start of
the game or it's someplace in the game tree.
We don't know how we got there.
I don't care how we got there and
say we're at a max situation.
And we're going to say that
the limitations of the game as such,
we're only able to generate three ply.
So the max is now and the future expansion
of the tumour apply is going to
be future moves of the opponent.
And then the agent.
Once again, these boards here are
not necessarily terminal states.
They're just the limit of our memory.
Now we're going to assume that we have
some sort of heuristic,
but scores game states from 0 to a 100,
with 100 being a win for the agent.
I'm going to go through and we can
score all of his game
States isn't the heuristic function.
Now we can apply minimax
just before the agent is max,
the opponent is men.
The agent has max.
When you take the max of
5271 and the max of 9340,
and the max of 3 is 7 at a max of 25 and 47,
take the men of 7193,
and the men and seven and
ninety seven, forty seven.
And then the max of 717,
which is 71, which means we should go left.
Now after the adversary moves,
we'll pick up again at
the current game state
and generate three play again and repeat,
and we'll just keep repeating
that until the game ends.
And so the game might go like this.
And this, this is what we've predicted,
how the game will go.
And again, might not actually go like that.
But the agent does pick the left to move,
then we can regenerate from there.
So basically the heuristic allows
the agent to use Minimax
even if the entire game
tree can't be generated.
So even if the game tree can only
be generated for a few apply.
And so a better game play is dependent on
a better heuristic because
it would make you more likely to win.
And interestingly,
we're modelling the opponent
using our heuristic,
but the actual opponent may have a
different or a better heuristic.
One thing to note is that as
a result of evaluating the tree further,
after we come down to this move here,
we may actually pick
a different move than
we originally thought we would peg.
Because now we're able to generate
essentially two more Apply down.
And we can see further than we could
see when we were back here at the root.
So it may actually pick a tariff.
We can pick this move here.
Instead of the mood that we thought
we were going to take
a picture with lead to 71.

Now, other approaches to improving
gameplay try to generate more applies.
Because obviously,
as we just saw in the previous video,
if we can generate more applied,
if you look further ahead,
we can get a better sense of whether we're on
a path to a win or a loss.
One way to do this is to exploit symmetry.
So we can see here in tic tac toe that
these four moves are
actually symmetric at all,
basically the same board
if we just do a rotation.
And when we do exploit symmetries like that,
we can actually make the number of
plywood can generate larger.
You can also exploit some of
the properties of the game tree itself.
So if we look at this game tree,
and it's the game tree we've
been investigating so far.
Where we have a move by the agent,
either go left or right,
followed by the opponent, go left to right.
And for this one, what we're gonna
do is we're going to just,
this is the exact
ordered the algorithm is exploring the tree.
So imagine are we looking at left?
We're looking at the Punnett going left
and we're looking at
the ancient going left again.
And we have its board
here and we do a score and we see it's 52.
And of course anytime
it's the agents move it to max,
anytime if the opponent's move it to men.
So we're at a max node and the question is,
do we need to look at the other end game?
Is this the best
that the agent is going to be able to do?
And so we can imagine what if we
get a 0? What if that was a 0?
Well, the agent couldn't do better than 52.
So, but if it was a 100
than the agent would definitely
want to take that move.
So the agent does need to find
out what that game status.
So we do need to expand here.
And let's say that the value is 71.
And this being a max,
we pick 71 up.
And that value comes up to the men's node.
And this would be the opponent.
So there's a Min node.
We ask ourselves again,
do we even need to find out what any of
these other boards are worth if we
already know that this tree is worth 71.
So let's imagine what have we found
out that this tree was worth 200?
Men would want to pick 0.
So we're definitely going
to want to explore further down here.
So we explore down further,
it becomes a max node.
We look at the left board and we find that
the board is worth 93 points.
So looking
for the ages point of view, that's a 93.
And we can carry the 93 up here to the max.
And we can look to see that
there's a 71 here.
And if there's a 0,
we're going to pick 93, but
Min is going to pick 71.
And if there are other ones where the a 100,
we're going a 100.
But the opponent
is still going to pick the 71.
So we don't actually need to expand
this other board because
no matter what it is,
we already know that our opponent
wants is going to pick
the move that puts us into
that other game tree.
So now we can pick the
71 and we can bring up to the top.
We can ask ourselves again,
do we even need to find
out what the right move
might generate? Might generate 0.
Of course, we'll want to 71,
but it also might generate a 100.
So we're going to want to find out whether it
generates 100
or at least something better than 71.
Let me use the same reasoning down the,
down the left move on the part of
the impulse and the opponent left
mood by us and
we played up that board is worth three.
And so we can ask ourselves, do we need to
find out what the other port is worth?
And since it's worth three and its max,
and the other may be worth.
If it's worth 0,
whatever, we're not going to take it,
but it's worth a 100,
then we are going to want a ticket.
So we're going to want to find out whether
that's worth a 100 or not.
And we've point out it's worth seven.
So we'd bring the seven up,
bring it up to the Min node.
And we ask ourselves once again,
do we need to find out whether this
is what this tree is worth?
Is worth 0. Then Min
is going to pick the 0,
but we're going to pick the 71.
That tree is worth a 100 than men,
it is going to pick the seven
and we're still going to pick the 71.
So we don't need to find out
what this entire tree is worth.
On this entire right side.
It's called minimax with alpha-beta pruning.
And accomplishes the same thing by keeping
track of two values is
the tree is traversed Alpha,
which is the high score for
any max node on the path so far.
And Beta, which is
the low score for
any Min node on the path so far.
And what it does is, since we don't have
to expand entire subtrees,
it allows us to search deeper,
often several ply deeper.
So let us search more of the game tree.
And the more of the game tree with concerts,
the more likely we are to pick a better move.
Now, how much of the game tree you don't have
to expand depends on move ordering.
So you're gonna need to find some way
to score your moves so
you can pick goodness first.

So far, all of
our games have been deterministic.
But some games involve chance.
That is, there are dice and
there are cards, there are coins.
For example, in backgammon,
you have to roll dice before it
determines what your range of moves is.
And in poker you have to shuffle the cards.
So how do we handle this?
Well, we extend the game tree idea
to model chance as a player.
So we're going to look at
a simple game where we'd
have left and right as before,
but we also have a coin involves
suitors, heads or tails.
And so we assume that the agent has just
flipped heads and there's
the current game state.
And they're going to move left or right.
And then it's going to be the opponent's turn
to flip a coin heads or tails.
Now, the game state
at the top of this pink hair or the
upside down triangle is going to be
the same state that gets
carried down to this red nodes.
It's just a state were
heads has been flipped.
In a state where tails has been flipped.
And then the opponent gets to move.
And that's why we can stop
our game tree expansion
here at these chance nodes.
Because the chance node
is going to be after the opponent
moved and just before It's
the agents turn again to flip the coin.
So this is the ancient as
the current player which is max.
This is a chance node
for the men or the opponent.
This is the Min move they
get to make after they flipped the coin,
which result in the game state
where the current player,
the agent, gets to flip a coin.
That we're going to say this is
our expansion limit.
And before we have a heuristic
and we can score all of these game states.
And the question is now is,
how are we going to pick a move?
How is the ancient going to pick a move?
Well, it turns out the first part
is easy because this is
just a Min node over
to heuristically scored games.
And so minuss just going to pick
the game state that has the lowest value,
106, 12, or 16.
Now the real problem comes when we look at
the agent deciding whether
to go left to right.
Because now we have probabilities.
And so what the agent needs to
do is look at actually
an expected value of the heuristic scores.
So it's a value of 10
times the probability of
a head plus the
probability times
6 times the probability of getting a tail,
heads or tails, 50 percent, 1.551.
So that's ten times a
half plus six times a half.
It's going to be 5 plus 3.
So we say the expected value of
moving left is now 8.
And we can say that saying,
what's the expected value of moving right?
Well, that's going to be
12 times probability of
heads plus 16 times the probability of tails,
which is 12 times a half,
plus 16 times a half,
which is going to be six plus eight,
which is an expected value of
14 for this right subtree.
And now we're back to
a regular max node for regular minimax.
And so we just pick the maximum value,
maximum expected value, which is going to
be 14. And so we move right.
But we don't know what the outcome
of men's role as yet.
We don't know where
we're going to go in this subtree.
And tall man actually flips the coin.
And so that's how we handle
chance in the game tree.
And this algorithm is called expectimax.
So what we do is we calculate
the expected value of
future games States and
use the mics max or the Min as appropriate.
So if we were able to
expand this tree out further,
we would see that men would
also be taking the minimum
of expected values of subtrees.
And you can also use alpha-beta pruning
with expectimax,
especially if the scores are bounded.
Now, what we'll look at is all,
these are all classic games.
So from 990 when I first started,
of course there weren't video games
because many things didn't
even have good or video terminals.
So the question is,
what kind of AI is used in video games?
As it turns out,
they don't really use game theory,
which is what we've been using.
They use a star search for path finding.
They use a variety of
different techniques to model behavior,
one of them being finite state machines.
So here we can think of how the state is
B patrol or in his other state attack.
And here's another state flee.
And depending on triggers,
you move into different states.
So if you visit an NPC non-player character,
they see an enemy, they move
into attack mode.
If they're defeated, they go back to patrol.
Or if they defeat
player that go back to
patrol at their defeated, they flee.
If they get healed,
they go back to portal.
So here you can see that the MPC
is just transitioning between
all the states based on events.
And that's how actually a lot
of AI is modeled in video games.
It's finite state machines.
Now, they're very complicated.
So other techniques have been, had been used.
One is decision trees,
which are actually
a machine learning technique,
which we'll investigate later in the course.
But for game AI, they actually don't
learn them from data, which we'll be doing.
They construct them by hand.
And they also use behavior trees.
There is hierarchical task networks,
which actually a form of planning.
And we'll go over planning
and in future modules.
And there's also a lot of scripting,
which is just telling
the non-player characters what to do.
So for very long time,
almost all of this CPU cycles
in games went to do graphics.
And now with GPUs and faster processors,
more cores these days,
there are actually finally
spare cycles left for AI.
And so they're starting to use
more interesting things like
hierarchical task networks.

So now we're going to shift gears a little
bit and start talking about game theory.
Game theory covers interactions
between players
and extends far beyond what
we normally think of as a game.
Things like the Cuban Missile Crisis,
tactical interactions between Coke and Pepsi,
even Pokemon at first when
you're choosing which Pokemon to use.
Let's look at an example.
These are caught. There's really
only enough evidence to convict each of
them for two years unless
one confesses, rats out the other.
And he gets one year and the other guy
who wrote it out gets 10 years.
But if they both confess,
then they each get five years
and there's
no communication between the thieves.
And we can model this in extensive form.
The way we've been doing makes it look like
a sequential interaction between the players.
That's not really the case.
So we take arbitrarily
take peter going first,
either confesses or denies.
And then depending on what Peter does,
John will either confess or deny.
And then based on little story we laid out,
we can tell how many years
their sentences will be.
So if Peter confesses and John confesses,
then they're each going to get five years.
And if Peter confesses,
but John denies that
Peter is going to get one year,
but John who got read it out,
it's going to get 10 years.
Alternatively, if Peter denies,
but John confesses, then
Peter is going to be the one rat
it out with ten years.
And then if they both deny as we
started out, they both get two years.
And again, this is extensive form.
Normally in game theory
we will look at games and in normal form,
which should have shows the actions
appropriately as simultaneous actions.
So we can show the,
what we'll call strategies,
both John and Peter,
which is just the actions
they have available to
them, confess or deny.
And then we show the payoffs,
and we showed this on the grid.
And this has exactly the same information
that was inlay extensive-form game.
So instead of a move,
we speak of a strategy game theory.
So Peter, strategies are
either confess or deny.
And we can see what the payoffs
are for Peter and
John when Peter picks the confessed strategy.
So the question is this, what should they do?
Should they confess or deny?
Which is the same as answering the question,
what strategies should each of them pursue?
So now let's look at the game and
assume that each of them denies.
We see that their payoff is
two years of prison age.
We can ask ourselves,
can Peter improve
his outcome by switching strategies?
So what does that mean?
What does Peter wanna do?
Peter wants to look at his current pay off
and see if it's worth switching.
So his current payoff is two.
And if he were to confess,
we'd see that his payoff was one,
so it only gets one year in prison.
So yes, he is better off by switching.
Now we can ask ourselves,
given that Peter is
confessing and John was denying,
can John improve as outcome by switching?
And we compare ten years
of prison to five years of prison.
And so, yes, John
can improve his outcome by switching.
And so we end up with
both of them confessing.
Now looking at both of them confessing,
we can ask, Can either of
them improve their outcomes by switching?
Well, if John switches back to denying,
he goes from five years to 10 years.
And if Peter switches back
from confessing to dying,
he also moves from fires
five years to 10 years.
So no they can't.
And this is the Nash equilibrium of the game.
And this is named for John Nash,
who originated just analysis of games.
And you might remember his
portrayal in the movie,
a Beautiful Mind by Russell Crowe.
Here this is actually a picture of John Nash,
actually looks a little
bit like Russell Crowe.
This particular game is called
the prisoner's dilemma.
And it illustrates that what is
individually rational is not,
doesn't necessarily always lead
to the best outcome for everyone.
And for this, Nash was awarded the echidna,
the Nobel Prize in Economics.
In order to solve this game,
we use cell inspection to find the solution.
Another approach is to apply
this successive elimination
of dominated strategies.
And that
means we have to answer the question,
what does it mean for
strategy to be dominated?
So let's look again at the game.
If we look just at Peter's payoffs.
Ignoring John's payoffs, we see that for
one strategy he gets 10 years or five years.
And for the other option,
he either gets one year or two years.
So in every case,
deny is always worse than confess,
no matter what John does.
So repeater.
In completely independent of
what John does for Peter,
confess always leads to
a shorter prison term.
Now let's look at John's payoffs.
And as he has the same payoffs.
So it's 10 years versus five years,
two ears versus one year.
So confess always leads
to a shorter prison term,
no matter what Peter does, gram.
So for each of them, confess
strictly dominates deny,
or say that deny is dominated by confess.
And what we can do is you can always
just eliminate dominated strategies.
You should never play a dominated strategy.
Okay, so let's define a dominant strategy.
And is just some notation.
So we're going to let Player
one have the strategies a, B,
and C. And we're going to let player
to have strategies x, y, and z.
And unlike our previous game,
but the prisoner's dilemma here,
bigger numbers are better and going forward,
Arabic numbers are better.
Okay? So if the payoff function
for shadow GC for some strategy
I is always better
than some other strategy j for the same eyes,
then C is allele the dominant.
Now that's a little obscure.
So let's take an example.
We're going to have the three strategies,
ABC and XYZ are
the strategies for player two.
And now these are the f
ij's for all of the players.
And what we're gonna do is
we're going to compare
for a given strategy for player one,
For five against to 10,
against 88, against three.
And because this greater than relation
holds for c as compared to b,
then c strictly dominates B.
Or we can say that B is dominated by C.
Now we can also compare a and C. Now five is
greater than four and
10 is greater than five,
but eight is not greater than 10.
So this relation doesn't hold.
So C does not strictly dominate a.
Now there's a weaker form of dominance.
And this is kind of hard to say.
If they're all equal.
But one or more is greater than,
than we can say that
c weekly dominates strategy j.
So strictly dominant.
All of strategy sees
payoffs have to be larger
than strategy j's weakly dominant.
Some of them can be equal,
which is the easier way of saying this.
So let's look at another example.
So here are the payoffs for strategies C. And
actually we don't even
need to write in player
sees payoff for player two.
Payoffs here, but we're going to anyway.
Five is greater than 2,
10 is greater than 88 is greater than three.
Now this falls under the first definition.
So all of them are greater than all of
the payoffs for c or
greater than the payoffs for B.
That's the first definition.
Now compare C and a 504 is greater,
ten to ten is equal,
88 is equal to c weekly dominates a.
This falls under the second definition.
Now we can talk about
the successive elimination part.
It doesn't matter
which player you start with,
but the first thing you
do is you identify an,
a dominated strategy and you remove
it without regard to the other player.
And then you switch to the opponent,
ignoring the player and
remove a dominated strategy.
And you keep alternating,
repeating this until you
find a solution or you fail.
Let's work through an example.
We have the economist and Business Week,
and how much their profits are
for a week depends on which cover they run.
For The Economist a or B with these profits.
And for business week it's going to be
cover XOR y with these profits.
Now we're going to
apply successive elimination
of dominated strategies.
So the first thing we're gonna start with
the economist and
identify the dominated strategy.
So we look here comparing the
payoffs between a and b,
and we see the a 100 is greater than 90
and a 100 is also greater than 90.
So B is dominated and
we can simply eliminate it.
Now we switch to business week.
Now we've eliminated strategy be for
the economists so we can
pretend it's not even there, we can erase it.
And we can look at Businessweek
strategies x and y.
And we see that a 100 is greater than 80.
And this means that strategy x
dominates strategy Y and
we can eliminate bad.
So here we've eliminated
economists be Strategy,
and we've eliminated business
piecewise strategy.
And we have a, we have
the solution is the Nash
equilibrium of the game.
So now let's get something
interesting at the beginning of the game.
If we'd started with Business Week,
100 is greater than 80,
but 0 isn't greater than 80.
So business, we didn't
have a dominant strategy.
And this will often happen.
So you may need to switch opponents
when I'm applying this.
Successive elimination
will not always succeed.
So normally end up with a different game.
Smaller game they can use
cell its inspection on.
Additionally,
there's more than one equilibrium.
You will find only one and order of
elimination will determine
which equilibrium you fight.

Now let's look at a slightly
different type of game.
What about rock, paper, scissors?
Now, this is a strategic game that
everyone is familiar with.
And we can write this out in normal form.
We have the blue player here for rock,
paper, scissors, and the pink player.
And the payoff for rock if
the other one plays rock is 0.
The payoff for rock of yellow
and placed paper is
going to be minus one
because paper covers rock.
And the payoff for rock if the other plays
scissors is going to be one
because rock beats scissors,
then there's going to be the
same for all of these.
We can just transfer this information to
the other combinations of
rock, paper, and scissors.
Now this is a 0 sum game.
The payoff to each player sum to 0,
not one, they sum to 0.
So what one loses, the other one gets.
This is the definition of
a win-lose game, not win-win.
Additionally,
this game is interesting because
no pure strategy equilibrium.
You can try to find one by cell inspection.
But I'm sure you know as a kid,
that there is no strategy to play every time.
You can't win by playing rock every time.
So instead we use a max strategy,
a mixed strategy equilibrium.
We play each strategy with
some random probability and
actually turns out it's 33 percent.
So the definition of a mixed
strategy is that it's
a probability distribution
over pure strategies.
Let's do an example derivation.
Find out where that 33 percent came from.
Snare, we have a normal form game where
we're going to have
an employer and employees.
And the player is either
going to watch their employees,
which costs money to
make sure they're working or
ignore them and just hope they're working.
And the employee can either work or
they can shirk and play
Tetris or mine sweeper instead.
And so the payoff to the employee,
if they are watched and work is 50.
And if they're watch Shark, it's 0.
And if they're ignored and work It's
50 and there are ignored and shortcuts,
a 100 for the employer if they
watch and the employer employee
works and it's 90,
it's minus 10 if they watch and they shirk,
whereas it's a 100 if they ignore and work.
And if they ignore and
check them into minus a 100.
So really employer wants to
ignore and the employee
really wants to shirk.
So just go ahead and verify that there is
no pure strategy equilibrium here.
So we're going to need
to find probability distributions
over working in shirking on
the part of employees and
watching and ignoring on the point of,
on the part of employers.
So let p equal the probability of shirking,
and we're going to add 1 minus p equal
the probability of working for the employee.
And Q equal the probability of watching.
And one minus q equal
the probability of ignoring for the employer.
And so what we do Start
is from the employee's point of view,
we're going to calculate the expected values
of working and shirking given Q.
And we don't know what Q is yet,
but we're just going to fill out what's
the expected value of
working of the strategy.
And it's going to be 50 times Q
and 50 times one minus q,
which is 50 q plus 50 minus
50 q, which equals 50.
And the expected value of
shirking, on the other hand,
is going to be 0 times q plus
100 times one minus q,
which is a 100 minus 100 times q.
So we can find the best response by finding
the queue where the expected value of
working and the expected value of
shirking or the same to the employees.
So we're going to set these two
quantities equal to each other.
50 is equal to a 100 minus a 100 q,
100, Q equals 50,
and so Q equals 1.5.
So employers should,
with 1.5 probability pick
between watching and ignoring. So why?
Well, consider if the probability of
watching is less than a half,
say it's a quarter,
then 100 minus 100 times
a quarter is a 100 minus 25,
which is 75 is that's greater than 50.
So the payoff to workers is greater to shirk.
Now, if the probability
of watching is greater than half,
say it's three quarters,
then we have 100 minus
a 100 times three quarters
is going to be a 100 minus 75.
It was 25, which is less than 50.
And so the incentive is going to be to work.
And then so you're spending
money to watch people.
So you, you want to pick the probability
that makes workers in
different to working in shirking.
So now what are the expected values
of watch and ignore?
Then calculate the same way
we want to take the expected value of
watch is equal to
90 times one minus p minus 10 p,
or 90 minus p minus 10 P. Site correct?
90 p minus 10 p,
which is 90 minus
a 100 P. For the expected value
ignore we have
a 100 times one minus p minus a 100 P,
500 minus 200 p minus a 100 P,
which is a 100 minus 200 p.
And again, as before,
we can find the employee's best response
by finding the probability p
where the expected value
of watching is equal to
the expected value of ignoring.
And so we're just going to set these two
things equal to each other.
So nine d minus
a 100 P is equal to a 100 miles,
200 p, which is a 100 P equals ten,
which is P equals 1 tenth.
And again, why, why is this the good value?
Okay, the mass here is exactly
the same as it was before,
except now we're doing it from
the employer's perspective.
The important point is really the intuition.
And why is it that if the probability of
cirque is greater than 10 percent
where they want to watch.
And what happens is if they
shirk more often than 10 percent
and the employers will watch.
And if they shirk less often than 10 percent,
the employer will ignore.
But if they do shirt,
then the employer will be
encouraged to watch more.
And so this isn't stable,
these aren't stable percentages of
ignore and watch and work and shirk.
And we want to know what the equilibrium,
equilibrium probabilities
are, the stable ones.
And that's what we've solved for,
is what the stable shares of working and
shirking and watching and ignoring r.
So let's find out what
the expected payoffs are.
And this is from
the employee's point of view.
And we can see here the 10 percent and
the nine tenths or their probabilities
of shirking and working
inside of that or the weighted average,
essentially probabilities of the payoffs from
the employer monitoring are
watching and ignoring That's equal to 50.
And then when we look at the employer,
we have these inverted.
So the outside probabilities that
the probability of watching
and ignoring and the inside probabilities
or the probabilities of shirking at working.
And you should be able to work
through this and see where these came from.
So strangely, the strategy
for each of them is to wake up in
the morning and sample from
these probability distributions
and decide whether
that day there to work
or shirt or a watch and ignore,
and those will be their payoffs.
So now the question is,
what are the payoffs for rock-paper-scissors?