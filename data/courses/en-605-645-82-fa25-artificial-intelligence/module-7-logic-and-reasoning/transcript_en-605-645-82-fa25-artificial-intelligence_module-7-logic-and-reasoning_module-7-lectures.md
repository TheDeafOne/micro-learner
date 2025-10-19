# Transcript for EN.605.645.82.FA25 Artificial Intelligence – Module 7: Logic and Reasoning – Module 7 - Lectures

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9fbe707f-da1f-44cb-b73c-b0c1017767ce

So this module is about logic,
and we're going to start first with
an introduction and motivation.
So far we've been talking about
states, state space search.
And we've talked about representation,
states,
actions, transition function and costs.
We've talked about the mechanisms of state,
state, space search, global, local.
When we talked about the result,
whether we find the goal
or whether we find a plan to get to the goal.
And we've looked at algorithms
such as blind search,
AStarSearch, adversarial search,
constraint satisfaction,
reinforcement learning, and local search.
Now adversarial search or games had
a very big influence
on early artificial intelligence.
Mainly because playing chess,
games like that was
considered to be
a hard and intelligent thing to do.
Although they started actually with checkers.
Logic had the same kind
of influence on earlier.
And for the same reasons.
Proving theorems and differentiating
equations was
considered hard and intelligent.
Now, as it turned out,
what was hard to intelligent for
a person was not necessarily
hard and intelligent for our computer,
but that's a different story.
Logic also provides a way for
reasoning about what the agent knows.
So we need to start out with a common ground.
Common understanding of logic.
We're going to start
with prepositional logic.
So in propositional logic,
T and F are constants.
A propositional symbol is a sentence.
Normally you see them as P,
Q, R capital letters.
And if P is a sentence and Q is a sentence,
then the following are also sentences.
Specifically.
If we put parentheses around P,
then that's still a sentence.
If we put this little NOT symbol
in front of P,
that's still a sentence.
And we use this symbol for or P or Q,
then that's also still a sentence.
And all of these rules fall underneath
syntax is the syntax of propositional logic.
Now we're going to assign to the constant t,
the value true into f, the value false.
So if P is true,
so is the parenthesis ation of p.
And if p is true,
then not p is false.
And if either P or Q is true or both,
then P or Q is true.
This is our semantics.
This is what logic, logical symbols mean.
Further wanted to introduce this idea
of a model of the world.
A model of a world is assignment of t and
f to the symbols of sentences.
So we're going to give
an example of that here.
And sort of the classic way of talking
about these is using truth tables.
A truth table is simply
a simple enumeration of all possible models.
So each row here is
going to be a model of the world.
So let's start out with p and q.
And we can assign
the constants to each of the values,
true, true, true, false,
false, true, false, false.
These are all possible worlds.
Now let's see what NOT P is.
Well, NOT P, according to our semantics,
if it's true, then false.
If it's true, then false
if it's false and true,
if it's false than true.
Fairly simple, and we'll say p or q.
For p or q, we have
p is true or Q is true, That's true.
True or false is true,
false and true is true and false,
or false is false.
A sentence that can be true or
false is called satisfiable.
Now let's look at p or not.
P, which is true,
true or false is true,
false and true is true,
false and true is also true.
A sentence that is true for
every possible state of
the world is called a valid sentence.
Now let's look at P and Q.
Remember this is, and because it looks
like an a without the crossbar,
true and true is true,
true and false is false.
False and true is false,
false and false is false.
This is also satisfiable.
So I get p and not p.
True and false is false,
true and false is false,
false and true is false,
false and true is false.
This is unsatisfiable.
A sentence that cannot be true in
any possible state of the world
is called an unsatisfiable.
This we get p implies q.
It's important to know that implication
here is not causation.
It's called the material conditional.
In actually in logic, you'd end up
with some very strange things such as,
if Paris is the capital of France,
then two plus two is four.
So this is the truth values for implication.
It turns out that implication is only ever
false if q is false.
Here we have an equivalence.
Equivalence look to see if
the implication is true in both directions.
If p implies q and q implies p.
So with a little hat here,
the a will have the crossbar we have and the
v we have r. And then we have implication,
and we have equivalents.
So these are the basic operators
and relations of prepositional logic.
So now, although NOT OR and parentheses
ation are sufficient to
drive all of propositional logic.
There are a number of shorthand rules
and relations that are
useful for prepositional inference.
We'll talk about a few of them.
One is modus ponens.
And this is the
one probably all familiar with
is if P implies
Q and P is true, then Q is true.
The other one is modus tollens,
which is if P implies Q and Q,
Oops, p implies q and not q, then not p.
And the convention is that
everything above the line is taken to be
true and then everything
below the line follows from TEA.
We can actually prove these
using truth tables.
So we can add P,
Q, P implies Q and not Q.
So here's P, Q, P implies Q.
Once again, we have our assignments,
true, true, true,
false, false, true, false,
true, true, false, false.
If we look here, for p implies q
being true and p being true.
There's only one case.
And that has to be that Q is true.
So that's modus ponens.
Let's add and not q here.
Just take the not Q.
Similarly, if we have,
it's true that p implies q and not q,
then the only thing here that
follows is that p is false.
And that's modus tollens.
Notice that P being
false is the same as not p being true.
Now, now the rules are like this.
Some of them are valid for all sentences.
They are simply manipulations.
So a very common one is something
like De Morgan's law.
So NOT P and Q is equal to not p or not q.
And as we'll see,
there are a few other useful rules.
I'll introduce others as we need them.
One is unit called unit resolution,
which is that a p or q,
not q implies p. And the other is resolution,
which is p or q is
true and not q or r is true,
then P or are true.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=509be047-be0d-4868-9993-b0cc008732a0

So how can we use this for AI?
How can we use this in an agent to permit it,
to reason about its environment,
the world around it.
It does at least give a first pass
at an answer to that question.
We're going to look at a toy example,
a typical one from artificial
intelligence called lumps world.
More just world is a grid.
Add. There are pits and
somewhere then there is
gold and one of the squares.
But there's also a one plus.
If the Olympus get you, you die.
If you fall into a pit, you die.
But if you get the gold,
then you win and you have one arrow.
The thing is, is that when
you're in a square,
if you smell a stench,
you know that the one piece
is in a neighboring square.
If you feel the breeze, there has
to be a pit in a neighboring square.
If there's glitter and mean
squared error and has gold,
feel a bump, you hit a wall.
If you're a screen,
that means you hit them up as.
And when we start out, we have
these five features that are true and false.
Start out in 11, where one is the row,
the first one is the row,
the second one is the column.
Everything is false.
And since we don't
smell anything and we don't feel the breeze,
we're going to see that 21 and 12 are safe.
So let's explore those squares that we
can increase our knowledge
about the world around us.
So our first step will be to go to 21.
And 21, we're going
to say that we feel the breeze.
And this must mean that either at 31 or 22,
there's a pit, but we don't know wedge.
So let's go ahead and explore 12.
And in 12, we're going to smell a stench.
Well, this means that 22 doesn't have a pet,
otherwise we would fill a breeze.
There's always means the one piece
has to be in 13.
Otherwise we would have
had a stench. We're into one.
So let's get some notation for this.
For CIJ is a cell
where I is the row, j is the column.
So SIJ is true if
CIJ has a stench and BIJ is true.
If c I, j has a breeze,
and WIJ is true,
you have CIJ has a want us.
And so we can start with
a knowledge base of facts about the world.
And basically this is going
to be a set of implications.
And our first implication is that
there's not a stench and 11,
then we know the oneness isn't 10,
11, and 12.
And this is not into one.
And there's no distention to one,
then there's not a one person 11,
there's not a one person to one.
There's not a one person, 22,
and there's not a 1% 31.
Similarly, if there's no distention 12,
there's not a one person
11 is not a one person.
12. There's not a one person to one.
There's not a one in 13.
And if there is a standard 12,
then either the emphasis in
11 or the one in 12,
or the oneness isn't to two,
or the one isn't 13.
So we have here logic as a represent,
as a knowledge representation for the agent.
Now, now we're not saying that any of
these particular things are true.
We're saying if they
obtain that what follows.
So we're gonna start out with S11.
We know doesn't have a stench.
That's a fact.
But by the rule that we have,
we know that we
introduced earlier modus ponens.
We know that it must also be true
then that one is not in the streets squares.
And that's modus ponens.
And what we know by the rule called and
elimination is that if
all of these things are true together,
then they must be true separately.
Because that's what and means,
and means that everything is true.
So we can do
something called and elimination.
We're going to find out which of
these individual effect.
And we know that each of these
individual facts are true.
Skin. Now we can explore to one
and we find out there isn't a stench.
That's a fact.
And we have
another implication that covers this.
As we know, if there's not extension to one.
And all of these things
obtain from modus ponens.
And then we can actually Pi
and elimination again.
We have all these individual facts about
where the Olympus isn't.
And now we move into
12 and we see that there is a stench.
That's a fact.
And we have an implication that covers that.
And this for modus ponens.
So now either we know that the one pieces,
one of these areas, but
we know from our previous facts,
the Olympus can't be in 11.
So by resolution, we can rule that out.
And remember this is the rule for
resolution P or Q, not Q key.
So W1 one is our q.
And so the P is these other facts.
Now we can match our W12 with
a known fact that the lump is not in W12.
And we used resolution, resolution again.
And now we can match up
W2 with a known fact
that there is no one person W2.
And we can apply resolution again.
And so we have reasoned out using
logic and some basic rules of logic.
Where
now this is nice.
Propositional logic is very powerful,
but it lacks a few things that make
it convenient to use.
And one of these things as variables,
there's no variables here.
We had to specify everything.
There are no functions and relations.
And so taken together is very cumbersome.
Said, well, we'd really like to
write each of the individual implications
above is something like not SIJ implies
that not WIJ and not
wi minus one j and not wi
plus 1 j and not WIJ minus one,
and w I j plus one.
So if there's no stench,
Then there's no one person
each of the cardinal directions.
Ignoring the idea of possibility walls.
Similarly, if there is
a stench in aij and we'd like to
say that the one pieces in I j or i j,
I minus 1 j or I plus 1 j or i j minus one,
or i j plus one.
So it would be very convenient
if we could represent all of
our implications like this
would be much more compact.
So the question is,
can we, can't, we can't we.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2078e79d-1643-4987-a699-b0c6011d6834

So last time we left off,
we were talking about propositional logic
and how we'd like to use it
for reasoning for an agent.
But it wasn't very compact
because it lacked functions and variables.
And it turns out that there is
a logic that has these things,
first-order logic, or it's
also called the predicate calculus.
Prepositional logic, by the way,
is also sometimes
called propositional calculus.
So in first-order logic we have constants,
primitives, things like King John, JHU too.
We have functions which
essentially properties
are in mathematics are projections.
So left leg of King John.
So essentially it takes a constant as
an argument and it returns
some property of that constant.
We have predicates
which are special functions,
and then return true or false.
So we might have a predicate called Brother
that takes two arguments
and returns true if they're brothers.
So in this case, King John
and Richard the Lionheart it.
Whereas if it were
King John and Little Richard,
it will return false.
We have variables which do
what you expect them to do.
Xyz. We have connectives
which to confirm prepositional logic,
sure, not.
And, or implication and equivalence.
We have quantifiers which
are special to first-order logic.
There's for all the up sound down,
upside down a, and
there exists the backwards E.
And we'll talk about those more in a minute.
We'd actually need to use these here and,
or make these true
the census in first-order logic.
And we'll see later how this works.
And we have equality.
Now, except for the quantifiers.
Everything works pretty much
well as you'd expect.
So let's make a few simple sentences
in the predicate calculus.
We have parent of John and Sam and Male
John implies that Father John, Sam.
But you can't do
truth values on bare functions.
So the left foot of John
implies left leg of John wouldn't be right.
Because left foot of John
doesn't return true or false.
It returns the left foot of John.
Instead, you want to have
a different predicate which has light has.
So if John has a left foot,
this implies John has a left leg.
So has left foot of John,
goes left leg of John.
Replies.
Okay, so let's talk about
quantification in more detail.
Let's look up for all x P of
x. G of x is some predicate.
This means for every instantiation of x,
p of x is true.
Now you may well ask yourself for every,
for every instantiation, well,
for every relevant instantiation.
So we may have something like the,
the brother of the Mona Lisa
and the Rock of Gibraltar.
So that's not true.
Everything in logic is, is defined either by
the university or you can add
predicates that
introduces sort of type system.
So for all is kind of like
an and over all the x's.
And it actually, it has an infinity,
it has an affinity for implication.
So what does that mean?
Well, we're going to write something
like for every person.
For every x, where x is a person
implies X Loves Raymond.
You can interpret that
is Everyone Loves Raymond.
There exists x P of x means
that P a true for
at least one instantiation of x.
And in this respect,
there exists is like a big
or over all possible x's.
And as an example,
we have something like there
exists an X where
X is at UMD and x is smart.
Which means someone at
University of Maryland is smart.
There's a bit of an art to this.
So for example, you might ask yourself,
why not write something like there exists x.
Where x Loves Raymond.
And this might be interpreted to
be everything Loves Raymond.
So this is where you sort
of have to think about
the universe of discourse or whether you
want to sort of type system that says,
well, x has to be a person.
And we can certainly ask ourselves,
there exists an x at
U of Maryland implies that x is smart.
This means if there is someone at
your University of Maryland
than that person is smart,
which is not exactly the same thing as
someone at University of Maryland is smart.
And to keep looking
at these examples were safe for all x.
Where x is at Johns Hopkins
implies that x is smart,
is means everyone at Johns Hopkins is smart.
Whereas for all x at JHU and x is Smart,
says that everyone is at
Johns Hopkins and everyone is smart.
And these are not the same thing.
So let's talk about some properties of
the quantifiers.
For all x, for all y is the same as
for all y for our AT, for all acts,
as long as you keep them
within their proper scope,
the order of the variables doesn't
matter. Now.
It's only true if both
of the quantifiers are the same.
If you have mixed quantifiers,
you can't change the ordering
or you change the meaning.
For example, there exists an x for all
y. X loves y versus for all y,
there exists an x where x loves y.
The first case there's someone
acts that loves everyone.
And in the second case,
everyone loves someone.
Or at least one someone.
However, they are the duals of
each other and this
will become important later.
So you are able to take
one and express it as
the other through negation.
So for example, for all x, there is an exit,
likes ice cream, is equivalent to saying
there does not exist
an x who doesn't like ice cream.
And there exists an x that likes
broccoli is the same thing as
saying, there doesn't exist.
All x's that don't like broccoli.
Which is a lot harder to say that way.
In general, almost every thing
in terms of inference in
propositional logic
applies to first-order logic,
except that we can't work
directly with these universal quantifier.
The quantifiers, either
universal or existential.
Which is ironic because we,
we wanted to have them.
So what we generally have to do is
for a specific problem,
we have to apply universal elimination
and existential elimination.
So an universal elimination for,
for all x, P of x is true.
Then P of c is
true for any appropriate
constant in the domain.
And what this means is we can take
this general implication that we had from
OnePlus world that said for all I j,
there's not a tension i j implies that
the one pus is not in any of these cells.
If we instantiate it with
no stench and square 22 is true,
then we can instantiate the rest of the,
of this particular implication.
And this is where the power of the predicate,
predicate calculus comes from.
Similarly, for existential elimination,
if there exists an x,
P of x is true,
then PFC is some,
is true for some constant c,
not appearing in any other sentence.
Now this is a little abstract,
but we'll see later
on why this makes a difference.
It'll, it'll, it'll make more sense later.
And this c is called a Skolem constant.
But otherwise everything else
supplies from prepositional logic.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d3bc6ed9-98c8-43e5-823f-b0c800cbb51a

So now we're going to be able
to do some inference.
And a lot of these are sort of
strange word games, word puzzles.
And it's not immediately clear
these would help in an agent,
but this was sort of the thinking at
the time of how you might turn
things into knowledge bases.
So here we have Bob is a buffalo,
Pat is a pagan, buffalos outrun pigs.
Now we need to convert this
to first-order logic.
We have two predicates here.
Bob is a buffalo, Pat is a peg,
and then we have a,
a universally
quantified implication that says for all x,
y, where x is a Buffalo,
NY is a pig, then x is faster than y.
And we can use
our regular logic rules to reason with these.
So we can use and introduction,
which is the opposite of an elimination,
which basically says if two things are true,
the end of them must be true.
We can use universal elimination here
by introducing some values for x and y.
And this is our substitution analyst,
which we will talk about more later,
which says that we assigned
to x and pad to y.
And now just using modus ponens,
we end up with that Bob is faster than Pat.
So the question would be, how do we
get a computer to do this?
It's kind of a search.
So the goal is something
to prove or disprove.
So we would want to do prove
the presence of a one-plus at C22,
starting with the facts, our knowledge base.
And then the reasoner could apply
various rules and come up with a conclusion.
So you can think of this sort of
is a state-space search
around logical rules to manipulate the facts.
But how would we know we're
done if we did that?
So we'd like to apply
something that's a
little bit more systematic.
And for that we can do forward
chaining and backward chaining.
And we'll start first with forward chaining.
So let's write down
our initial knowledge base.
We know that if x is a buffalo and
why as a pig that x is faster than y?
We know that the pig is Y
and Z is a slug bit.
Why is faster than z?
And we know that if x is faster than
y and y is faster than z,
then x is faster than Z,
which is famous triangle inequality.
Now there's something important
to note here, as we'll see later,
that the x in each sentence here is not the
same as the x in another sentence.
So it isn't necessarily the case.
The exit to Buffalo is the x in sentence
three of The faster
than silver forward chaining,
what we want to do is we want to
match on the left-hand side of
our implications using the facts
we have and produce new facts,
which will then be matched
on the left-hand side,
which will produce a new facts.
And then we can keep consuming rules and
facts and that way until
we either prove or disprove what we want.
Let's start with some facts. We have
Bob is a buffalo,
paddies a pig, and Steve as a slug.
Let's work with the first two.
We can plug these in to the first sentence.
And we can find out that Bob
is faster than Pat by modus ponens.
And we have a substitution of
Bob for x and for y.
So that combines 145.
Now we have Steve as a slug
and we have Pat is a pig.
And we can plug that
into the second sentence.
And again by modus ponens.
This gives us that
Pat is faster than Steve and that uses
sentences seven with Pat for y and z for z,
5 and 7,
5 and 2.
Now by sentence three,
we can combine fact 68
and do substitutions to find out that
now Bob is faster than Steve.
With backward chaining, we reverse this.
We're going to match right hand sides
of implications to create
new left-hand sides that we
want to match until we hit a ground truth.
So this is starting with
a goal and working backwards.
So we have basically the same rules before.
We have that. F x is
a buffalo and y is the pig.
The next is faster than y.
If we have, we have y.
If y is a pig and Z is a slug,
then why is faster than z?
And finally, that if x is
faster than y and y is faster than z,
then x is faster than Z.
And we have Barbosa Buffalo.
And how does the pig?
And this time we have Steve as a slug.
So we're going to start with
an instantiation from the back,
which says that Bob
is faster than Steve and we're going to
substitute in Bob for x and Steve for z.
So we're starting here on
the right hand side.
This will generate two facts
that we then need to prove to be true.
So let's start with the first one.
We have Bob is faster than some y.
And for the other fact we have
that sum Y is faster than Steve.
Let's work with 8 first.
Working with one of
the other sentences we have, which is one,
we can do a substitution in for Pat,
for y, for Pat and 8.
And we're matching again here
on the right hand side of one,
which generates instantiations for
the left-hand side of one,
which are that Bob
is a buffalo and Pat is a pig.
And it turns out that these
are indeed ground truth.
So we then know that
at least part chain is true.
Or wherever we need to, we need to prove
the other part that sum
Y is faster than Steve.
So if we instantiate this
by looking at sentence two,
we can instantiate y with Pat again.
And this will generate a,
that y is a pig and Z is
a slug that we need to prove is true.
When we fill in the y and z,
we see that Pat is a pig,
Steve was a slug.
And when we look in our knowledge base,
we see that these are indeed
facts that we have.
And this is backward chaining.
Now, I'm sure that you
are immediately seeing that
this could go horribly awry.
That I could have instantiated
different values for x
and z at the beginning,
perhaps Stephen Pat add
it would have come
to some sort of contradiction.
And when the agent
comes to some sort of contradiction,
then we end up with backtracking.
So you can see this is
actually sort of a form of,
of depth-first search that
proves bits and pieces of what you
need to prove the overall.
And this actually become very important
in the module on planning.
Now the problem is this leads to some sort of
combinatorial explosion
of things you need to try.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a30a1a5f-76f6-4b34-b51e-b0cb0014a337

In the previous video, I didn't
really explain how I was
exciting constants two variables.
And the process of assigning constants
two variables actually has
a name and it has a process.
And we're going to discuss it in this video.
It's called unification.
So basically you have some function
unify P and Q,
which returns Theta,
which is the substitution list.
It's possibly empty.
And there's different ways
of indicating failure.
One is that it's an
empty substitution unless the other,
you actually return null.
That the empty list actually indicates
that a substitution wasn't necessary.
So here's an example.
We want to unify P
of a and X and P of a and B.
And we can see when this unifies
by substituting b.
Next, we want to
unify P of a and x and p of y and b.
And we see that this unifies by
substituting b and Ax and Ay and a y.
And now we'd like to unify
P of a and x and p of y, f of y.
Now this one's a little more complicated.
We can see that we can do
a substitution of a into y,
and then y, and then a into y,
and then f of a into x.
So now we actually can assign
functions to variables as well.
Now, not everything can unify.
So for example, I might have unify P
of a and x and unify P of x and b.
And in this case I'm trying to assign a to X
and I'm trying to assign
b to x at the same time.
And so that's a failure unification.
Except that we need to be careful.
Remember previously I mentioned that X is in
some sentences are not necessarily
the same axes at another sentence.
To be careful that in this case,
that the x's are just some, some variable.
And that they happen to both be x.
Simply by coincidence that
somebody could have picked z,
g, h, or k instead.
So before Unification, All sentences
need to be what's called standardized apart.
And it's really just a fancy name for
picking fresh unique variable names.
So P of a and X becomes P of
a and x one and P of
X and B becomes p of x two and b.
Just to introduce fresh
unique variable names.
So now when we try to unify,
we have unify P of a and x
one with p of x2 and B.
And we see that these
unify because we can assign b
to x one and we can sign a to x2.
Even with standardizing apart,
not everything will unify.
Imagine we tried to
unify P of a and B with p of x and x.
Well, here we're trying to assign
a to x one and b to x one,
and that won't work.
So there's generally one unification fails.
Might fail for more complicated reasons
where functions are involved.
Here we're unable to assign x to
a and f of x to be.
Which is really the same thing as saying
that a constant can unify with,
with a function that has no variables in it.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b773f86b-5c0e-4e58-9735-b0c1013ca025

Okay, In this lecture
we're going to talk about resolution.
And we previously saw
resolution as a rule, actually two rules.
The first one is unit resolution,
where we have p or q,
not q implies p.
The second one is a little more
complicated, but not much.
It's p or q.
Not q or r implies p or r.
L.
Amazingly enough, all we need to do
is add proof by contradiction.
And we have
a powerful automatic theorem prover.
Well, how does that happen?
Mentioned we have a query P,
and we also have a knowledge
base that happens to contain
the fact p. And somehow we want to prove it.
Well, it turns out that f We negate
our query and combine it with
the knowledge base so that now we have
this new knowledge base with p and not
p. I note that off
all facts and knowledge base
are added two together implicitly.
So now we have a knowledge base P,
and we've combined it with not
p. So we have P and not P.
Let's contradiction.
So our original query must be true.
So p must be true,
must be true in
the knowledge, knowledge base.
So the negation of the query
causes the knowledge base
to contradict itself.
Bigquery must have been in there.
And true, we say that
the knowledge base entails the query.
Now for single atomic facts like this,
this is pretty easy to do.
So how are we going to do it from our
complicated facts and sentences?
Really need to take a little detour.
We're going to talk
a little about resolution requires
something called conjunctive
normal form or cnf.
And cnf looks like this.
It looks like we're
inside the parentheses you only have or,
and the parentheses statements
are connected together by ads.
And that's what allows them to
write us to write them on
separate lines and
be implicitly added together.
So C and F is a conjunction of disjuncts,
where conjunction is and,
and disjunction is or.
And this means that we need to get rid
of the universal and existential quantifiers.
So let's start at the top.
We have the knowledge base.
Does the following statements.
Whoever can read is literate.
Dolphins are not literate.
Some dolphins are intelligent.
Now, we have something we
want to know is true.
Is it true that some who
are intelligent cannot read?
So the first step is to convert this textual,
narrative knowledge base
into first-order logic.
Of course, if you were actually doing this,
you would probably have it all ready.
Always convert into first-order logic,
even do this every time.
So for all X, where
X can read implies x is literate.
For all x, where x is a dolphin,
implies that it's not, x is not literate.
And there exist X, where X is
a dolphin and x is intelligent.
So there's our first-order logic.
The next step is to convert
to conjunctive normal form.
And this has a number of steps,
but I love them.
We're going to apply for this example.
I'll try to give examples
of the steps where it's relevant.
First thing when you use in need
of a limit implication,
turns out that P implies Q is equivalent
to not P or Q.
And if you don't see why you
should do a truth table
to see why that's the case.
But it just means that we can now
turn these into disjunctions.
The first two extent
universally quantified sentence has
been get rid of the implication,
turn them into disjunctions.
The next step is B is to
reduce the scope of negations,
the system to actually apply in this example.
Where you want to do is you might have
a long parenthesize sentence that is
negated and you want to move
the negation inside.
So imagine might have something
like NOT a and B.
And you're going to want to change it to not,
not a and not B.
Let's just reduce scope
of the negations means.
Next thing you do is in need
to rename variables.
This also doesn't apply here
because our sentences
are actually fairly simple.
But it might be
the case that you have a sentence where
you've used a variable more than once.
And they're actually in
different scopes so they don't
actually apply to the same thing.
So when we write out this sort
of nonsensical complex example,
where I have for all x,
P of x implies for all y,
P of y implies P of X of X and Y,
and not for all y.
Q of x and y implies P of y.
No idea what this means.
But we note here that these two uses
of y have different scopes.
They actually don't refer to the same thing.
They're just using the same name.
So this is what rename variables would be,
just as simple as changing the
second Y two W's.
The next step is to eliminate
the existential quantifier.
Remember we talked about this a long time.
A guy just said
existential elimination Skolem constants.
This will become important later.
So we don't have to do this
for this first two rules,
the copy these down
because these are universally quantified.
But the third one is
existentially quantified.
Remember that X initial quantification
says that there is some
x out there for which this is true.
And we're going to name it now.
I'm going to name it a, you know,
what actually is this is a Skolem constant.
The important thing here is
a must not appear in
any other sentence and it
doesn't all the other ones have variables.
The next step is to move the universal
quantifiers to the left.
I'm going to have to do that in this case,
the sensors are really simple.
Next we want to rewrite is
conjunctive normal form,
which is fairly simple.
We're just going to
drop our universal quantifiers.
The next step is to separate
out into clauses.
All this means is anything that has an,
and we're going to move the end and put
the two sentences on separate lines.
And as we saw from the discussion on
unification now we have
separate sentences here,
all of them using AKS,
many of them, two of them using x.
And x is don't
necessarily refer to the same thing.
So we need to standardize apart.
Now note that within a sentence
they do refer to the same thing.
So the uses of x
in not read and literate is the same
x. Dx and not
read and not Dolphin are not the same x.
So let's go ahead and just
standardize these apart by adding subscripts.
And again, the really
only need to do this once.
And depending on your problem,
you may never have
plain English sentences that
you need to convert into first-order logic.
Step 3 involves working with the query.
So we have the query some who
are intelligent cannot read.
When you turn this into first-order logic.
There exists an x who is
intelligent and x can't read.
Now we need to negate the query.
So there does not exist an x
is intelligent and cannot read.
Now, this has to be converted to cnf,
but we wanted to keep the variables fresh.
So we don't want to use
existential elimination
because we're trying to find out if there
is some constant in the database,
it can unify here. So we don't want to use.
So what we're going to use
instead is duality,
which we discussed before,
to changes into something
that is universally quantified.
And we do this by negating
both the outside and the inside.
Now we have double negation
and get rid of the outside.
Double negation.
Now we can apply De Morgan's law
in order to move,
reduce the scope of the knot.
And then we can use, just use
and the elimination of the universal.
So now we have not intelligent x or reads.
And we're just going to add this
to the knowledge base.
For an implementation detail should keep
a fresh knowledge base around
so you can reuse it with new queries.
Now I'm going to do this as a tree,
but the next step is step
four is to actually do resolution.
So let's record our, our knowledge base.
Now if you did everything right before,
your crew should already
be standardized apart,
but I'm going to standardize apart again,
I'm gonna add subscripts.
Subscript 3 to the x is here.
So resolution is actually a form of
search. So where do we start?
Where do we start to look for
this contradiction is
actually a number of strategies.
The first one is resident is unit resolution.
As we wanted to pick clauses
that we can resolve,
as we saw before against single literals.
So that would be the p or q,
not q, therefore p.
Another approach would be to use the,
the set of support.
And this is essentially start with a query.
Only resolve against its descendants.
And there are others.
So I'm actually going to
start with the query.
So remember that resolution is p or q, not q,
therefore p. Some look in
for one of these to be the Q.
The other one is p or q,
not q or not r or so.
I'm always trying to find
something to be in the role of Q here.
Find the negation of it.
So I can actually match this not
intelligent x, too intelligent a.
And I can use unification to assign a to x3.
And this is a substitution list.
You always have to show your theta,
your substitution
list when you're doing this.
That means these cancel out
and buy resolution.
I have read a now you just keep applying it.
So I have read a.
I can actually resolve it against
this periods I match with the not read X1.
I can do the substitution of a for x one.
And then the read a and not read a,
cancel out and buy resolution.
I'm left with liver at a.
Now I need to match literal
a to a not litter at a.
If I can't, I'm done
and the query is proven false.
But it turns out here I can actually
match into this clause here,
not dolphin x2 or not literate.
And I can substitute in a
for x as my substitution a for x2.
Not literate a and literate
a cancel by resolution,
I'm left with not dolphin a.
Not dolphin a actually
matches a single literal here, dolphin a.
But now I'm left with not
dolphin a and dolphin a.
But that's a contradiction.
So I have nil.
And by proof, by contradiction,
it means that
my original query must have been true,
must be true, must have been
entailed by the knowledge base.
So resolution is a very powerful algorithm.
In fact, resolution is actually what
powers the logic programming language prolog.
So as it turns out, sometimes we're actually
interested in the substitution set itself.
Remember that in some
of our search algorithms,
we're interested in the goal or the plan.
Sometimes we're interested in
the substitution said for the same reason.
Because it may and substitution.
So maybe the solution to our problem.
As with all search
backtracking maybe necessary.
And sometimes, and this is
where the other rules
for picking which literals to unify against.
Sometimes it gets a little com,
there'll be very complex concepts.
And the major agent may have to work with
multiple resolution trees to
come to a final conclusion.
So what that means is I may start
the resolution tree here
and match it up in
a resolve and I'm at
something else happened to resolve.
But I may not be able to match this up,
but I'm able to,
to produce the negation and match it
up with by starting somewhere else.
And then these two match and resolve.
And then I prove that the original query was
true. And that's resolution.