None

So one of the most interesting approaches to
local searches, evolutionary computation.
Evolutionary computation has
a unifying name for,
for algorithms that use evolution as
an inspiration for
searching for better solutions.
And it's actually more than,
there are four basic algorithms,
but there are countless variations.
And these are evolutionary programming,
which was developed by football in 960.
Scintillator,
evolutionary strategies, which was
developed by reckon Berg
and in 970, one in later.
Probably one of the more famous versions
is the genetic algorithm,
which was developed by Holland at
the University of Michigan to 970 9.
And finally genetic programming,
which was developed by cozy
who's at Stanford in 990.
And the basic idea
that evolutionary computation user's comment,
all of these is survival of
the fittest and
some form of genetic encoding.
And the basic algorithm as deaths
will go over the actual algorithm in
more detail later as we take
a population of candidate solutions,
we evaluate each of these using
the evaluation function or heuristic,
which determines
the fitness of each candidate.
We then pick candidate
set with replacement from
the population using
a distribution proportionate
to the fitness or some other means.
And then finally,
we take these individuals that we
pick and we breathe
them to create the next generation.
So when you do explain what we
mean by breeding solutions.
So the key element,
one of the key elements of
evolutionary computation is it
candidates solutions are expressed
in a kind of genetic code.
And it turns out that
this genetic code actually
influences the generation
of successor states.
So there's no successor state function
in evolutionary computation.
So let's take the example of
the genetic algorithm because
it's probably the easiest,
most well-known example and
actually apply it to
the other versions or variance.
So let's look at the four queens problem
and the map coloring problem.
So the genome, the genetic code
for a map phrase,
credit the solution for
four queens might just
be this vector of four row positions.
And the phenome is the actual expression of
those genes as queens on a board.
And for, so for example,
in and map coloring,
me might just have a vector of colors.
The expression of that genetic code,
the phenome, is the coloring of a map.
One thing to note
is that evolutionary computation
is inspired
by a earlier understanding of genetics.
So basically for the genetic algorithm,
the genome or genetic code
is a linear ordering
of symbols that encodes the state-space.
And for evolutionary computation in general,
for these problems, you're going to need
both an encoder and decoder.
You need something that takes a solution,
includes it into the genetic code,
and they need something
that expresses it back out.
Now then the genetic algorithm,
the symbols can be bits,
they can be characters, strings, integers,
even floating point values.
Okay, so now we have a genetic code.
So how do we breed
candidate solutions to get
new, slew, new candidates?
Well, the first thing we do is we
apply a crossover operator.
So imagine we've picked two candidates,
let's call one pop.
And these a vector of colors in
his genetic code is
green, green, green, blue.
And this is what he looks like.
Now imagine that we have also
picked another candidate.
This is mom, this is her genetic code.
This is blue, blue, red, green.
And this is what she looks like.
Now what we do is we pick
a gene location at random.
This is actually a crossover index.
So let's imagine we pick three that here.
This is one base,
should really be using zero-based arrays.
So measure we picked three
and this is the cross index.
So then what we're gonna do is we're going to
swap the two separate materials.
So here we can see where the sun
gets these first two genes from pop.
And these last two genes from
mom and the daughter is going to
get first two genes from
mom and the last two genes from Pub.
And so this is how
the crossover operator works.
And this is now what the data look like.
So this is their genetic codes and these are
the females or the expression of the genes.
Now after the crossover operator,
we apply mutation operator.
Let's take the Senate as an example.
So we have the genetic code for the sun.
And what we're going to do is we're going to
pick a gene location at random.
And then we're going to pick a
new symbol at random.
So let's imagine we picked
three and then blue.
And this means now that the
sun's new genetic code is
green, green, blue, blue.
Then we put the sudden daughter
into the next generation,
and we keep repeating this until we have
generated an entire new generation.
Crossover mutation.
And operators have to be
appropriate to the encoding.
So if the encoding where real numbers,
then we might use something like
Gaussian noise for our mutation operator.
And evolutionary computation tends
to have a lot of user-defined parameters.
You can also make
these parameters endogenous.
So you could actually have the gene in code
its own mutation rates so
that you can encode the variance in the gene.
Now, not all parents have children.
Sometimes they're copied directly
into the next generation.
And this is controlled by P sub c,
which is the probability of crossover.
If you picked two parents,
you get a random number.
If it's less than P sub c,
which you to around
0.9, then there is crossover.
Otherwise, you just put the parents
into the next-generation directly.
Similarly, not all children have mutations.
P sub m is the rate of mutation.
Usually around 0.05 could
be lower or higher depending
on what kind of
mutation operator you're using.
So here's the actual pseudocode.
And there's a lot of details in here and
we're going to discuss this is the,
for the genetic algorithm.
So for line when we have
generate a random population.
So essentially we need to generate
n random individuals, maybe 500100.
According to the encoding scheme,
the genetic code.
The loop is controlled by the number of
generations less than a limit.
Many of these algorithms
don't have a well-defined stopping point.
Unless there is a perfect solution.
You can identify.
Oftentimes you just sort of run
them until it's good enough.
Run them until you can grab
a person and in
the best solution so far and keep running it.
Like three we have evaluate
the population has an implementation detail.
Each individual should probably at least have
fields for its genome,
its genetic code and its fitness score.
Evaluate is essentially going
to apply the fitness function,
our evaluation function or
heuristic to each individual.
Now that evolutionary context.
Computation is really geared
towards maximization.
So if you have a minimization problem,
you're gonna need to transform
the fitness score.
1 over 1 plus the fitness score
is very often used for minimization problems.
Now outlined seven, There's reproduction.
As we discussed before,
we need to pick
a random number less than
the probability of crossover.
Otherwise we just return the parents.
Then we apply the cross over
operator needed to test
whether we're going to mutate the
first-child.
Need to test where they're going to
mutate the second child.
Going back up to line 6.
There are lots of different ways
to pick parents too.
These are
roulette wheel and tournament selection.
For roulette wheel,
each individual's fitness is
a proportion of total fitness.
So if you added up all the fitnesses,
that's total fitness and
each individual's fitness is
some share of that.
You can actually use that share as
a probability distribution
and sample from it.
And then you can pick individuals that way.
And you pick with replacement.
And it sort of looks like this,
which is why it's called the roulette wheel.
Each roulette space though,
is equal to the probability
based on the fitness of the individuals.
So more fit individuals have
bigger slots for tournament selection
and this is actually kind
of little bit easier.
Pick seven or so individuals
completely at random,
completely uniformly at random.
And then you pick one out of those seven,
the one that has the highest fitness.
Here's just note here that
reproduces often encoding specific.
You have to pick a crossover operator and
a mutation operator that
is geared towards the encoding scheme.
For the genic algorithm, we often have
a linear genome, something like this.
For genetic program, they actually,
It's often tree, it's a Lisp program.
So you actually are operating
on the abstract syntax tree.
And for evolutionary programming,
it's actually finite state machines.
So your crossover operators
need to be appropriate
for a finite state machine.
Then as I mentioned previously,
there are other, many
other different variations.
It in fact, there are many, many
variations on
all of the different components.
And that's evolutionary computation.