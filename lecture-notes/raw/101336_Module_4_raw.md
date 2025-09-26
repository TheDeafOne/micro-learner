Hello, I'm Dr. Ian Mccullough.
In this module we're going to be
talking about social network analysis.
By the end of the module,
you'll be familiar with
terms used in social network analysis.
You'll know how to calculate
basic centrality measures by hand.
The reason why we do this by
hand is many software packages are different.
So if you can identify a toy problem,
solve it by hand, and then see
how the software is calculating it,
it's going to give you a better understanding
of what the software is actually doing,
how it's scaled, make sure that
you understand the
metrics you're calculating.
We'll also talk about
a few graph level metrics that's
measures across the network as a whole.
We're going to begin by
talking about terminology,
just so we're all on the same vocabulary.
For the objectives
for this particular lecture,
you will be able to
understand
different social network terminology,
identify types of networks,
and construct a network from
given data. Let's begin.
You'll see in the picture in
the upper left here is
a screenshot from the movie
Goodwill Hunting with
Matt starring Matt Damon.
If you haven't seen, it's a great movie.
But in the movie there's
a janitor played by Matt Damon at it.
And a professor would
post chal***ge problems for his students.
And the janitor would come
in at night and solve the problems.
Then they find him,
they realize he's a genius.
And then there's this whole drama of what
that means and how he comes of age.
In that situation,
the genius problem that was
considered unsolvable or super
hard is actually posted here.
Let G figure 1.1 which I've drawn upright.
Find the adjacency matrix A of the graph G.
Find the matrix giving the number of
three steps walks for the graph graph.
Now, for people that
aren't familiar with graph theory,
they've never been exposed to that,
that can seem a little bit daunting,
which is why it was
a good candidate for the movie.
But if you're familiar with graph theory,
it's far simpler than most problems in
calculus and easier to solve.
It's just not something we're exposed to.
I think it's because we're not
exposed to graph theory
that we just don't know what
exists or problems seem
a little bit more difficult.
But in network science
and in social network analysis,
graph theory is the core
mathematics that we'll be using.
Let's define some of these things.
A graph is a set of points, right?
These are the 1234 dots that you see there,
that semicircle
with the little head above it.
The little circle above it is
a little abstracted icon for a person.
You'll see me use those
throughout the course here.
But a graph is a set of points.
We call the points either vertices or nodes.
Vertices is more common in mathematics,
Nodes is more common in
social science or application.
Then there's also a set of
line segments called edges or links.
We have vertices and edges,
or we have nodes and links,
but the edges or links are
the lines that are then connecting the dots.
A social network is
a graph which contains
a finite set of actors.
We call them agents, and
the relationships defined between them.
There are many types of graphs, right?
You can have nodes that are people.
You can have nodes representing
resources, tasks,
knowledge bridges, physical locations.
There's lots of things that you can
use that can be represented by graphs.
But a social network is
a subset of networks or graphs
where all the nodes are people
and the links or
edges are relationships between them.
Graphs we've highlighted in
blue the key terms here that we're
using when we move
from one vertex to
another along a senior single edge.
It's sometimes helpful to think
of this as information,
maybe information or money if
you're dealing with transactions like
the path of $1 through people, right?
But moving from one vertex to another,
along a single edge that
joins them is a step, okay?
So that's what we call a step.
And then a series of steps, right?
So if I went 1-4 to two to three,
back to two, back to one, right?
A series of steps is called a walk.
Then the number of steps in
a walk is the ***gth of that walk,
that one to four,
to two to three,
back to two, back to one.
Right. That would be a walk of ***gth five.
Right? Because there's five steps in what I
just described, a trail.
Right. We're now getting more
restrictive here. A trail is a walk.
Which all of the links are distinct.
But you may include
some nodes more than once.
In that example where I went
one to four, to two to three,
back to two, back to one.
That was a trail because
there were two edges,
2-3 there's two different steps between them.
Right?
But all the other ones, there's only one.
Then once I've gone all the way back to one,
right now I can't go any farther.
Right, that's my trail.
A path is a walk in
which all the nodes and links are distinct.
That would mean that description I had
of one to four to two to three to two to one.
I couldn't go back to one
because then it would be included twice.
That would not be a path,
It would be a trail.
Note that every path is a trail.
Every trail is a walk.
Every walk contains a number of steps.
That's how we talk about this idea of ideas,
knowledge, materials,
things, knowledge and resources.
Moving through a social network.
We're thinking about that in terms of
paths, trails, walk, steps.
An important property is
whether there is a path between them.
If there's two nodes, nodes 1.2
nodes are said to be reachable
if there's a path between them.
If you think of two clusters in
a network that don't connect, right?
Sometimes if you think
about elementary students, right,
there might be a group of
elementary kids in one school
and a group of
elementary kids in another school.
And there is nobody between them.
Network relationships between them, right?
Then they're not reachable
to each other, right?
That's an example of a non reachable network.
A walk that begins and ends with
the same node, like I said,
in that one to
four to two to three to two to one, right,
is a closed walk,
and a cycle is
a closed walk of at least three nodes.
Cycles are important because
there's some properties we
deal with in social relations
which need to be defined by cycles,
which we'll get to later in the course.
Social networks can be represented
as graphs or matrices.
This is a graph, and this is
a social network representing
friendship between the actors.
Here, I'll use this throughout the module.
Here, this network, the names
are unique. There's only one.
You can represent them as ABCDEFG,
or you can represent them with names,
whatever is easier for you
to think about in your mind.
But this type of
representation is a graph, right?
It's a visual depiction
of the nodes and links,
or vertices and edges between them.
We can also represent this as
a matrix in the matrix,
right, or the adjacency matrix as we call it.
You'll see that all of the rows
correspond to the nodes
and all of the columns also
correspond to the nodes.
The one is there if there
is a relationship between
or if there's an edge between them.
If there's no edge, it's a zero.
We can look and see that
in the lower node here,
John is connected to
an above him to the upper right.
When I look at John on the bottom row,
and I go over to the second to last column,
there's a one there connecting them to,
You also see there's
one connecting them to Frank.
John is not connected to George there over in
the lower right that
is listed as a zero, right?
This is how we can either depict
a social network as
a graph or we can
depict it as an adjacency matrix.
Elements in the adjacency
matrix, which will represent,
with a lower case a subcase I and j.
That is, meaning there a link
between node and no j.
It is a one if there is an edge
between node and no
j and zero if there's no edge.
That's the simplest
dichotomous network that we have.
We're also going to be talking
about using some other notation.
I just want to make sure that
if you haven't seen this before,
that you are all on the same page.
The first thing is the summation.
We're going to be using a lot of
these throughout this module,
that sigma large sigma symbol is a sum.
I at the bottom is a set.
We're summing over a set.
And then the equation
that we're actually going to sum,
in this case I, what does that mean?
It means x one plus two plus three,
all the way up till we've done all of the Xs.
A large capital letter
is going to be used for an adjacency matrix.
I'll probably use the capital letter
A most of the time.
That is a matrix.
And you'll see the lower case notation
for elements in the matrix.
And they will be subset by the row n column,
which means from row to column.
Right? That's the notation that we will
be using from row to column.
Then we'll use either a capital subscripted
or a quotation mark.
The upper subscript
to represent the transpose.
What is a transpose? A transpose.
It's a little bit subtle in that matrix.
But the rows become columns.
The columns become rows
from a graph orientation,
if there is a direction,
you're going from node to no j.
When you take the transpose,
you're now going from no back to node.
It reverses the directionality.
But it's basically row
become columns. Columns become rows.
That's the transpose.
That is an important concept,
especially when we get
later in the course into
some of the linear algebra
aspects of what we're going to be doing.
But I'm introduced the notation
here, back to goodwill hunting.
As it turns out, the adjacency matrix A
is the key to solving the problem.
Because it says, find
the adjacency matrix of graph G. What you'll
see is for the second part is
by taking multiple compositions
of the adjacency matrix.
When you, the adjacency matrix is telling you
how many single step
walks there are to get
from a node to another.
Then when I multiply
that by itself three times,
that will tell me the number of three step
walks between all of
the different nodes in the network.
We will get into that a little bit more
when we start talking
about relational algebra,
but I just introduced
it here to motivate you,
there is the presence of
networks in movies and it's
an exciting field of
math with or without
the social network aspect of it.
Now there's different types of networks.
This is just to show you
a little bit about
different kinds of structures.
You can learn a lot about what's happening
socially within an organization
of its social networks.
Because there are
a huge number of factors that
happen from social psychology,
from cognitive psychology,
the way humans act in groups that
will shape the way the network looks.
It can also be what you're trying to
measure or what you're trying to look at.
It can also affect the shape of networks.
I just want to give you some common
topologies that we talk about.
The core Periphery network
is defined as a small core.
See that inner circle, right?
There's a small core of
networks that are all pretty much
connected to each other and then there are
a lot of nodes that are
connected to one of those core groups, right?
But aren't
necessarily connected to each other.
The core periphery network is often found in
volunteer organizations or churches,
religious organizations,
where there's like a core group
of people that are doing things.
And most of the attendees,
most of the participants
are doing this part time and
aren't as well connected
as the others that are
doing that group, right?
That's very common in
a core periphery network.
Cellular networks where again a core group
but then there's these cells
that are highly connected on the sides.
It's not exactly a coreripherycellres view
that this is how covert operations work.
What we've actually found
in the global war on terror
that the US conducted in
Iraq and Afghanistan is
the US military got very good
at finding and targeting cellular networks.
And as a result, cellular networks don't,
uh, don't work very
well from a practical standpoint.
And so we've seen a decline in
their use by
covert organizations or insurgent groups,
But that is a cellular network.
So it's more of an academic
theoretical than you'll
actually find in the wild.
A lattice network is where everybody
is connected to exactly
the same number of other people,
but those people are different.
What you're seeing is you're
seeing how that moves around the network.
Now, this is not a natural occurrence because
everybody is different in their preferences
for friends and network connections.
We don't see this very
often in the real world,
but it is an archetype.
It is one extreme that
compares to the one right below it,
the Erdos Reni graph
where everybody makes connections with
everybody else with some probability P and
everybody's probability of meaning
everybody else is the same.
That is a random graph.
What ends up happening
is if you go to the lattice
and you start changing
people's preference a little bit.
As you increase the number
of changes that somebody might make,
eventually you'll
introduce so much randomness
that it will become the Erdos Random Graph.
These become the difference between high
random in the Tony
and highly structured in the lattice.
That becomes like these two book ends
of stream cases that we think
about theoretically and conceptually
about how networks might behave.
The small world that you see in the middle
is somewhere in between those two, right?
That is a lattice that in
this particular case has
been rewired twice, right?
So you'll see that there's
two links that go across
those networks, right?
Again, if you keep rewiring
cross circle links,
you'll eventually get to Erdos.
There's also another type of
network Scale, free. Scale free.
We know that if you have
a node entering the network,
a person entering the network,
and they choose to connect
with the popular nodes
with greater probability.
What will end up happening is
hubs will form where there's
highly popular people that have a lot of
connections and most people have very few.
And that network becomes so
skewed it becomes what
they call free of scale.
There's no scale parameter in
the distribution of the degree,
and that's why they call it
a scale free network.
But it's really characterized by hubs.
So if you look at airline routes,
airline mappings, right, there's tons
of airports across the US.
Tend to be hub nodes, right,
Like Chicago Hare, Atlanta,
New York area, like Newark,
Laguardia, JFK, right there becomes
the nodes where people
fly in and then they get re
routed to wherever they need to go.
There is a bit of a debate
that when you see scale free networks,
it's evidence of evolution.
That's not the actual finding.
The finding is if you have a network
evolved such that nodes are entering
the network and linking
with the most popular,
then that evolution mechanism
will result in a scale free network.
But I would argue that in
the airline industry,
it is not so much about
evolution the way these
airlines naturally evolve.
As much as it is that they
have operations research engineers
actually optimized the network
and in that optimal layout,
they have designed it such that there's
hub nose for efficient routing, right?
We see this usually
when there's a lot of
work involved in the network,
somebody has to put a lot of effort and time
in to creating scale free topologies.
There is, however, debate,
because when you look at
social media connections,
you'll see that there is
this scale free topology where
there is a lot of hub nodes like celebrities,
whereas most of us have very few followers,
it does have the scale free topology.
I would argue that
the scale free topology is also
done because there's no requirement
to maintain those relationships.
If you actually have to have
a conversation with all
of your friends to be considered friends,
then you're limited in the number of
people that you can talk to.
Your ability to become
this huge hub node with
thousands of followers, right,
becomes impractical.
And then you end up
moving more towards Erdos.
Any, but these topologies allow
us to think about archetypes, extremes.
What if so that we can talk about
how social networks might
behave within these contexts of extreme?
Then it gives us some insight into what's
happening with real social networks
that we're going to study.
There's another type of
a comparison that I'd like
to draw out between traditional analysis
and network analysis.
I'm just going to highlight
a few of the key ones here.
Right? The focus of
the analysis is different.
When we're dealing with traditional analysis,
we typically think of everything as
independent and identically distributed.
We think about individuals,
if you go to a doctor's office
and a kid has strep throat,
we think about that kid will prescribe
amoxicillin and then if he
doesn't respond to the amoxicillin
because he has some other co,
pathogen, we'll come
back and we'll give augment,
but then another kid comes
in the same symptoms. Again.
We're going to treat the independent,
we're going to give them a oxacillin.
That's the typical medical protocol.
Why wouldn't we jump with augmented?
Well, if we're taking a network analysis,
we're going to recognize that
that follow on patient has
probably been exposed to
the other individual that
had to come back for augment.
We might start with augment.
Augment is just a Moxicillin
with an additional drug included in it.
We don't want to give people
the augmented right away because we
don't want to build up their immunity
to the augmented part.
But if we know that
they are more likely exposed to that co,
pathogen and we don't,
we start with oxacillin.
We've now given them
two courses of amoxicillin.
And we've made them more resistant to
the more common antibiotic
that's more widely used.
The way we look at
individuals versus diads and triads, right?
Like diads meaning two, triads meaning three.
These relationships
has important implications
in how we solve problems.
The type of data that we look at,
the traditional is attributes.
What can I say about the person?
What can I say about their age,
and their genes,
and IQ score and
all the attributes that I
can say about a person, Right?
Is this what is contributing to obesity?
Right? Relational would be
who are they connected to?
What is the body weight?
And B, M, I of the people
that are related to them.
What we find when we go to
a relational aspect is really interesting.
Things like, did you know that
obesity is socially contagious, Right?
When people are associated with
people of higher body mass,
they tend to get new ideas of what is
acceptable body mass and they
tend to become socially contagious.
Now, it doesn't go the other way around
where skinniness is socially contagious.
But there are
some other neurobiology that affects that.
There are a lot of things
that are important from
a relational perspective.
The data assumptions, as I mentioned,
we assume in traditional analysis
that everybody is independent
of those around them.
In networks, we assume high levels of
dependence when we do experiments.
We control different variables
and factors in an experimental setting.
So we can have a control group,
an experimental group,
and test the difference.
In networks, we recognize that does not work.
We have more complex experiments
that we have to design.
Beyond this slide to discuss
those traditional,
we look at correlation as
the analytical framework in networks.
We're looking at
the structure of the network.
We're looking at, is it clustered,
is it one big blob?
Right? These all tell us
important things about the problem that
we're studying and the nature of the data.
The mathematical foundations
are very different.
In traditional analysis,
it's based on calculus,
even if it's statistics is based on calculus.
But in network analysis,
we rely on graph theory,
linear algebra, discrete math.
Now you may be familiar with
these because we are
in a computer science program,
they tend to use these
a little bit more. That's great.
Most people in America have
some exposure to calculus
through high school and into college.
They're more familiar with it,
it's more comfortable.
But thinking about networks and thinking
about different types of
math than they're used to,
I would argue the math is not more difficult.
It's probably actually easier than calculus
two, but it's different.
It's that difference that takes us out of
our comfort zone and makes things
a little bit more uncomfortable.
I hope you've enjoyed this lecture
on learning some basic terminology
for social network analysis and for
graph theory that we're going to be using for
the rest of this module
and the rest of the course.
Thank you.

Is probably the simplest
social network measure to
calculate and it is
commonly used in a lot of applications.
Our learning objectives in
this lecture is to differentiate between
the four basic centrality measures
that we're going to talk
about and then how do we calculate
degree centrality by hand?
When I'll show you this network,
who do you think is the most important?
I'd like you to just pause the video
and look at it for a while.
And write down to yourself
some of the common top nodes
that you would think would be most important.
I'm going to assume
you've paused the network,
pause the video, and
have addressed who's the most important.
And now you've come back to the video here.
You might recognize this network
as a core peripheral network.
It has some central actors.
I believe agent 285-17-1839
are like the core.
And then everybody else is connected
to one of those key groups.
But when we look at
who is the most important,
it's a little bit difficult to tell.
What if I look at a network
that is more blobbih shape, right?
It's not so neat, it's
a little bit more difficult,
make a decision, right?
And you can pause the video and
try and do this exercise again.
Who do you think is most important,
assuming you've had a chance to do that?
There is no right answer on this.
By the way, it's
very difficult under this context.
What we're going to be doing with
centrality measures is finding
different ways to measure who
was central or who
is important in the network.
It's very similar to this idea of mean,
median mode with regular traditional data.
Just to make sure we're
all on the same page here.
Mean is also known as the average.
That's where we're going to sum
up a sequence of numbers.
Going to divide by the
number that there are, right?
That's how we're doing.
Mean median is we're
going to sort the list from smallest,
still largest, and we're going to
pick the value that
is in the middle of the data.
The mode is we're going to simply count
the number that has
the highest frequency, right?
And I'll show you the analogy
here to networks in a moment.
I want you to pause
the video here in a moment.
And I want you to take a moment to think
of ten numbers that have a mean of six,
a median of five, and a mode of four.
This is going to be important for you to
think about the bridge
between what we know
about independent
identically distributed numbers where we do
mean median and mode to
graph theory where we're
going to take degree,
closeness between, and degree centrality.
Take a moment and
please just do this exercise.
Think of ten numbers that have a mean of six,
a median of five, and a mode
of four, All right?
I'm going to assume you have taken
a moment to do that. There's no right answer.
This. The way I
would solve the problem, right,
is I would know that I
have ten numbers, right?
That are going to sum to
the value of 60, right?
Then I would probably
say I'm going to need to make a mode of four,
so I'm going to have to have at least
two of those numbers or four.
I have 4.4 and then I would know that
a median to get five
exactly that would mean that the
fifth and six numbers have to be five.
That means I have 5544 and
then I have to have another number.
You know, they can be lower than that, right?
I would have to have another two
numbers that are lower than that.
Maybe I add another
four or maybe I'd just add all four.
It doesn't matter. Then I
can make the other numbers arbitrarily.
Whatever I need to do, as long as I don't
run out of that 60 on the other end.
Right? That's a vague description,
but it gives you a direction as far as
how you can come up with a mean of six,
median of five, and a mode four.
The more important piece however,
is that all of these measures,
although calculated differently and
different on a set of ten numbers,
are all measures of central.
They're measures that are
trying to get at this idea of centrality.
And we know that when we
have a symmetric distribution,
right, we have a bell curve. All right?
There's as many high numbers
as there are low numbers.
The mean works really great
and we tend to use mean a lot.
Why do we use means so much?
We use mean because one,
it's maybe a little bit easier
to calculate the median.
A lot of times you don't
have to do a sorting function.
But the other issue that you have with mean
is there is something
called
the Central Limit Theorem in statistics.
Which is if I take
an average right of 30 numbers or more,
I know the distribution of that average even
if the numbers are
highly skewed in their distribution.
If I'm sampling and
taking the average of that,
I know the distribution which allows me.
Have statistical inference about comparing
two groups or something changed.
We tend to use mean a lot because we can
then invoke other properties that
we don't take the time to teach people about.
But when you have highly skewed data, right,
we use this a lot in economics or
politics because there's a lot of
haves and have nots when
you have
that population that's highly skewed.
If we were to take the average
we're going to be reasoning
or inferencing about something that's not
really representative of either group.
We use median as
a more effective way to
measure censure when there's
high structure or skewness in
the data mode is not used that often,
even though it's perhaps the
easiest one to measure.
In a similar way, we can look at
this archetype network from
Dave Crack the network
just to give you some background,
is one of Dave cracks
students red on the bottom here.
Red was not me.
I know I had red hair, but it wasn't me.
But he was a military student
in Dave Crack's class.
And then his assignment following
grad school was at the Pentagon.
This network in the upper right over
by degree was
the one star general
that was in charge of this group.
In the Pentagon, two
different groups had been merged together.
Sam was in charge and Red thought he
would show social network
analysis to the group.
Turned out to not be a great idea.
But we do get these great archetypal networks
from this exercise, right, with Dave.
What we're seeing here is
a network that has structure.
So there's a cluster in
the upper right and
a cluster in the lower left.
And you see Conrad in
between when we look at these terms,
right degree between closeness,
eigenvector, they're
all different ways of measuring center.
When I look at degree,
Linda has the most
physical connections in the network.
She is connected to more
people than anybody else.
I think Roger comes second,
but Linda has
more connections than anybody else.
But Linda is center
in that upper right cluster.
She is not as close
to the people in the lower left cluster.
If you look at Roger,
Roger is closer to everybody else on average.
If we were to take the ***gth
of the shortest paths
between all pairs of nodes,
right, and then average them,
we would see that Roger has
the shortest distance on
average to everybody else in the network.
That's a different type of centrality, right?
Then the one that
jumps out for people is Rad, right?
Because Conrad is
a single bridge or broker between
the two clusters and he
is a high in what we call between us.
If you look at the shortest path and say how
frequently do nodes fall
along that short path,
Conrad falls on the middle of
more shortest paths between
actors than anybody else, right?
These are different ways of looking at
center eigenvector centrality is
used in Google Page.
In what it is doing is it's saying if
you were to take a random walk
through the network, right, no constraint.
You're just going to randomly walk.
How frequently would you,
would a certain node
occur on that random walk?
What ends up happening when you have
structure is the likelihood that you're
going to go from one cluster
to another is relatively
low then the likelihood
that you're going to be
within a single cluster,
in a network like this, because
that upper right cluster
is a little bit bigger,
it's more likely that a node is just going to
circulate in that cluster
up there in the upper right.
And that's why you're going to see
particularly central actor in
that upper right cluster is going to pop up.
We see that eg,
the top eigenvectors tend to be highly
correlated with the highest degree
within that upper cluster.
But it's used to get
a sense of if we're taking
random movements through
the network frequently.
Or how central or how
influential is a person going to be a right.
These are the four basic centrality measures
and we're going to learn how to conduct,
calculate degree centrality in this lecture.
Just a quick definitions,
you have these in your notes here is
degree is the number
of edges connected to a node.
Between is the extent to
which it lies on
the shortest path between nodes.
Closeness is the average of
the shortest distances to
all other nodes in the network.
And eigenvector measures the extent to
which a node is connected
to influential others, right?
It's not, it's not
who's connected to you as
much as who you're connected to.
Are you connected to influential others?
What did the measures tell me?
Right, So it's a little bit different degree
is exposure to the network
when you're thinking about getting
out some shocking news
or something like that, Right?
The node that has a lot of connections is
going to get that initial information
seated to the network.
The most people, initially
we find though that people that
are high in degree do not
have very much influential power, right?
They do not change minds.
They do not hold real power to
motivate or persuade, right?
But it's a way to just
get the information out there.
So even if your likelihood
of persuading is low,
you're starting with more people, right?
So that's where degree is
telling you exposure to
the network between this,
this is the idea of informal power,
it's the idea of brokering
knowledge and resources
across the organization.
You've all been in organizations
where there's maybe somebody
that's not in charge.
They know where that form is,
they know how to get things done,
they get their hands
dirty and they know how
to solve problems, right?
Those people build informal power
and they have a lot of connections in
other places that informal brokerage
gate keeping between
a centrality like Conrad.
Conrad had the ability
to broker knowledge from
the cluster on the right to
the bottom cluster on the left.
Sometimes that can be a great power position,
other times it can be cognitively draining
where you're the go to
person between the two groups.
In the case of Conrad, he eventually
quit and the organization crumbled.
As a result, the general
retired and it wasn't
exactly a success story.
That's between closeness is
oftentimes used in information diffusion
because it's time to hear info.
It's like if rumors are flowing through
the network or you want to start
a rumor flowing through the network.
If you can find that point,
a person of high closeness,
that's a point of rapid diffusion.
Then, as we mentioned for eigenvector
getting you connected to nodes
of high degrees, you can sometimes,
when you can find a node that is high in
eigenvector centrality
but low in degree, right,
You're finding a node that is a great point
of getting rumors or disinformation released.
That is not necessarily going to
be as visible because
most of the algorithms people
use are looking for nodes high in degree.
Because it's
the easiest measure to calculate.
If you can find a node that
is low in degree
but high in one of these other values,
right, that becomes an interesting target.
And if you want to get better at
detecting disinformation,
then you need to look at more clever ways
to find those nodes that
can start rumor diffusion
without necessarily being detected.
All right, so we're going to start looking
at degree centrality.
Degrees is simply the number of
links connected to a node.
And so if I look at this network
right here as an example,
right, the first step that I'm going to
do is I'm going to jot out the equation here,
which is centrality degree for
a given node I is going to be the sum of,
of the rows of
their elements in adjacency matrix,
and we're going to divide
that by N minus one.
So what does that look like? Let me
make an adjacency matrix.
Now, one of the other things
about the adjacency matrix is
the diagonal of Cc matrix
is undefined, right?
What does it mean that an agent
is connected to itself?
What does it mean that an agent
is friends with itself?
In one argument you could say,
oh yeah, I really know who I am.
Another one is I'm not like I choosing
infinite time spent with myself, am I right?
It's a weird concept
in social network analysis.
We just consider the diagonal,
for the most part, undefined.
If I look at an agent, right?
I can see here agent
one is connected to only agent four,
none of the others, I
can do the same thing for agent two,
same thing for agent three.
Agent four is connected
to the different agents,
and then agent five, right?
That is the adjacency matrix.
From the adjacency matrix,
I can just simply sum across
the row and I can get the value there one.
And I can do that for each
agent in the network.
Okay? And then I'm going
to divide by N minus one.
So there are how many possible links
If a node was connected to everybody, right?
There's five agents in this network.
If a node is connected to everybody else,
the most they could be connected
to is four other nodes, right?
Because they're not going to
be connected to themselves.
That N minus one is four.
And that gives me a degree of
141 fourth, 234.1 fourth.
All right, that becomes
the degree of each node in the network.
I can also then
size the nodes by their relative degree,
and that gives you a more visual view
of who's
the most central actors in the network.
Here's an example of another network for you.
What I would ask you to do is
pause the video and
follow along and calculate
that degree centrality yourself.
If you get stuck, go back to the video,
but just try and do this
with what you've just seen.
If you can't do the project problem
independently without help,
you have not mastered it,
you have not learned it yet.
It's really important that
you take the opportunity,
not just skip ahead and
see how I solve another problem,
but you try and do
it independently for yourself.
I'm going to assume you have taking
a chance to work this problem.
You've paused the video and
now you're ready to resume.
First thing we're going to do is we're
going to create the adjacency matrix.
As we sum across the rows,
you get the values that you see here.
We're dividing again by
four because there's
five agents in the network,
and you'll see different degree centrality.
Here is the network sized
by degree centrality.
I'm Dr. Ian Mcculloch
and this has been a short lecture
on how to calculate degree centrality.
Thank you for joining me.

Hello, I'm Dr. An Mccullough and this lecture
will be focused on Between centrality.
Between centrality, going back to crack
hearts toy social network between
centrality is indicated here by Conrad.
Betweenness, centrality doesn't necessarily
have to be a sole broker.
Conrad is unique in that he
is a node that is high in between
us and so low
in degree relative to
some of the other actors in the network.
What you'll typically find is
when the network is a blob,
right, It's
generally symmetrically distributed degree,
right?
Everybody is more or less the
same or a single blob in the network.
We were to take just the upper cluster
or just the lower cluster here,
you would find
that degree between this closeness
and eigen vector are all highly
correlated with each other.
And somebody that's influential is
influential in all
aspects of that measurement.
But when the network starts
getting structure like here,
where you see two clusters,
that's when there becomes
differences in these measures between.
This is a measure of brokerage,
it's a measure of knowledge and
resource brokerage in the organization.
If there is knowledge in
the upper right cluster, this is,
these are two groups that have come
together that is
important for people in
the lower left cluster.
If it's not just obviously readily available,
there's some collaboration or cooperation.
Conrad's the one that has
relationships and respect from people in
both clusters and a lot
of that's going to end up going through him.
We also have something that we'll talk about
later in the course called Network Horizon,
which is people's awareness of
knowledge and information possessed
by people in their network.
Essentially the case to zero
at three steps through the network.
So you know the people
you interact with on a regular basis.
You know what
their strengths and weaknesses are,
what their skills are,
what they know, what they can offer.
You might have an idea if
you go one step further.
But beyond that it breaks down.
And that's where when
organizations start to get large and it
becomes impractical for everybody
to know everybody, right?
That's where
organizational structure comes in,
because that's what helps
us identify and find information,
knowledge, and resources in organizations.
But short of that,
there will be actors that instead of
occupying a central place
in a small team or cluster,
they will span between them.
That's the case here in
Conrad with, between us.
Now we'll find that some actors actually
try and occupy positions like
Conrad as a form of strategy.
They don't want Joe to meet Pete, right?
They don't want Bob to meet Pat, right?
Because then that threatens their power
and their status in the organization.
When you find that it is not
scalable and it ends up creating
toxic structures that ultimately
harm the organization or
at least limit its growth.
There are other types of actors that
are in this position that
are always meaning new people.
They're quite happy to hand off
this relationship between Bob
and Will and Roger and Pete,
and let them manage
their own relationship of brokerage.
And they're going to go find new
people and they're going to find
a new cluster that's not even depicted
here and bring those resources in.
And so when you have a person that's
constantly reaching out,
constantly meeting new actors,
that's where you're going to have
a culture of increasing knowledge,
increasing resources,
usually increasing
growth from that structure.
You also have a dark side of between this,
where when Conrad has this responsibility,
it can become overwhelming.
He can't get his own work
done because he's busy
managing the requests that
are going back and forth
between the two groups.
And brokerage is probably not
a key performance indicator
in his job description,
he has a regular job to do.
Plus he's brokering all of the communication
between these two clusters
that can be overwhelming,
high cognitive demand,
high intensive time stock for him.
That can be not
an enviable position to be in.
Right? Depending on how
organizations reward these factors.
Depending upon whether we
have somebody that's trying to be
a gatekeeper versus a true broker
and introducing people in a connector.
All of those can be measured by between.
This will be the same measure
for what we're going to talk
about in this lecture,
but what it means
to the organization might be different.
Just again, recap degree number of
edges connected to a node between, between.
What we're talking about in
this lecture is the extent to
which a node lies
on the shortest path between others.
Closeness average distance to everybody else.
Eigen vector is
connected to influential others.
What they tell me is between between.
This is your measure
of informal power gatekeeping,
brokering, controlling the flow of info,
liaison between different subcomponents.
You see some of those have
more positive or negative.
Connotations. So what we want
to know is the extent to which
a node lies on the
shortest path between others.
How are we going to do that?
Well, the first thing that we have
to go through is this notation of choose.
We have to know how many paths are possible.
Just like when we were doing degree,
the denominator was how many nodes are
there that you could be connected
to. That was n minus one.
Well, when we want to know how
many paths are possible,
right, Well we need to
say there's two nodes, right?
So it's n choose
two are going to be the paths, right?
So the n number of nodes and
I'm going to say how many pairs are there.
That's n choose two notation.
The equation for that, familiar
with combinatorics or statistics,
is n times n -1/2 right?
It says n choose two.
That ends up for this network being
ten possible paths for five agents, right?
Let's enumerate them, right?
And this is another way to do it.
I have 11121 to 31 to 41 to five, right?
Those are the five different paths
that agent one can be connected to,
but we're not going to
include that one to one.
Those self reflexive ties are undefined.
Same thing for agent two.
But now I don't have to count two to
one because it was already counted
as one to two, right?
There's not, there's no direction
here as I go across the way, Right?
This is another way of enumerating
what all of those paths are.
Right? We can
double check here that we have to screw
anything up because there should
be ten paths here.
Because I calculated that with then
choose two and then I've enumerated them.
The next step that we're going to do,
and this is the trickiest one
for us to be able to do possibly,
right, is we are going
to calculate the geodesics.
There's sometimes more than one
geodesic between two nodes.
What is the geodesic?
Is the longest shortest path, right?
It's the, we are going to look
at the shortest path between
pairs and we are going
to be looking at what those are.
That's the geodesic.
In the case of one to two,
that's simply one to two.
For one to three, right?
There's a direct connection, one to three.
It gets interesting when we're
looking at going from age at one
to four because the shortest way to get there
is going 1-3 to four.
If I go one to two to
three to four, that is a path.
But it is not a geodesic path.
It is not a shortest path. Right?
We've got to go on three to four.
That second node is superfluous,
so we have another one here.
Right, And so on.
Right. Now in this network
there's only one geodesic for each.
But it is possible, right,
that you could have two different ways
of going to a node, right?
Like if there was a node
six that was to the left of
agent 1.2 And you were saying,
well, how do you get from node three?
Well, you could go 326
or you could go 316, right?
So you would have two geodesics for
that entry, 3-6 All right.
So you can have
more than one geodesic per path.
Okay. Now we're going to
tally up what fraction of the god,
what fraction of the geodesics
a node falls in the middle of,
when you have a walk
of one ***gth, one, right?
Nothing falls in the middle of that.
We're not talking about endpoints, we're
only talking about middle points.
So they'll be zero across
here. Zeros across here.
But when we look at this next one, right,
what we find is that
node three is in the middle.
It is in the middle of all
of the geodesic paths.
So if you had a longer one, right,
Like if there's 1364, right,
and 1374, right, Well,
then three would be on both geodesics,
so it would still be a value of one.
But that 6.7 would
be only on half of the geodesics,
so they would get 0.5 0.5 again,
we see a one here for the
three in the middle, right?
And that goes on as we see here.
Now what we can do is we
can tally the number
of shortest paths that it fell on.
Right? So we see that three fell
on five of the geodesics.
Of the possible geodesic.
Then the question becomes
the numerator, right?
Is 00500 as we just calculator.
But what about the denominator?
Well, the denominator for the denominator,
we have to remove the node out, right?
It can't be a starting point or
an end point if I take any node out,
right, Like take agent
five out of the mix, right?
There's four remaining nodes.
So how many paths are there
between those four remaining nodes?
Well, it is going to be
four times 3/2 like we saw before,
right? That's four choose two.
Or another way of looking at that
is instead of n times n minus one,
the n becomes N minus one, right?
Instead of it being five nodes.
Looking at agent five
can be on the path
between one of those other four,
it's four times three,
not five times four, right?
Then that ends up being six paths, right?
Six short paths with that denominator.
We can see between
the scores as you show here.
Now, why do we do this with the denominator?
What we're trying to do is we're trying to
scale all of these centrality
measures 0-1 And it
just gives us more of
an apples to apples comparison.
When we're looking at the
relative centrality of different actors,
you will see that
some software applications scale it
0-100 Some try and just use a raw number,
which is difficult to
compare with networks of different size.
There's issues with that. But for
this course and for our use,
we're going to be scaling it 0-1
Then we can certainly size
the node by their relative centrality.
Now like we did in the previous lecture,
I would like you to take a moment to take
this network and pause
the video and try and work out
those steps by hand
that you had just seen me do.
Again, I discourage you
from moving forward in
the lecture and just watching
it and seeing how
I do the problem a second time.
Until you've actually done
it independently yourself,
you have not mastered the material,
try and take a moment to
work the problem out yourself.
Before you go through the solution,
I'm going to assume that
you've paused the video.
You've had a chance to go through
this problem and now
we're going to go through the solution.
I'll take the network and we have
to first enumerate the geodesics,
1-21 to 31 to four, right,
all the way down to five to six.
Then we have to enumerate
the paths between all of them, right?
One to two is pretty straightforward.
Same one to three. Now one to four,
I've got to go through H of five, right?
One to five is straightforward.
One to six, I got to go
through G of five again.
Now, this is an interesting one.
When we go 2-3 I have two options.
I can go 213, or I can go 253, right.
253, right.
Then we'll go through all of
these most common mistakes
here are people only have one path,
2-3 You got to pay attention to that.
That's the trickiest part
in calculating these measures.
Now I can look and see, well,
how often do nodes fall on the shortest path?
And we have 05 is on all of them.
Again, five is on all of them.
Notice here, five is only
on half of the geodesics, right?
One is on the other half of the geodesics.
As we go through there, when
we sum all those values, right,
we get 0.5 we get 7.5 then
the denominator becomes ten.
Then our betweenness scores are as such.
This is our network size by between us.
So we've just gone through
the calculation of betweeness centrality.
I hope you've enjoyed this short lecture.
I'm Dr. Mccullough.

Hello, I'm Dr. Ian Mccullough.
In this lecture, we are going to be
calculating closeness centrality by hand,
just revisiting Dave Crackhart's toy network.
Here, closeness centrality is
looking at the average distance
to everybody in the network.
So all we saw that Linda had
the most connections and Conrad was in
the position to broker
across these clusters as well.
Roger has the shortest distance
to everybody else in the network.
What are the definition?
Degree, number of edges
between extent to which
a node falls on
the shortest path between others.
Closeness is the average
of the shortest distance
to all other nodes in the graph.
When you look at every node and you say,
how many steps does it
take to get to everybody, Right?
Closeness is going to, on average,
have the shortest distances to
everybody An eigenvector is looking at,
are you connected to influential others?
What do they tell you? Well, degree,
direct exposure not necessarily
influence is your ability to gate,
keep in broker knowledge
and resources between clusters.
Closeness is this meaning
your time to hear information.
It is your ability to get information or
knowledge out to people with
the fewest average number of steps.
It's a point of
rapid diffusion for information.
Closeness is pretty useful in that respect.
We're now going to go through an example of
how we calculate closeness centrality.
Now for whatever reason,
when I've taught this material
for almost 20 years now,
it always seems that when
I teach closeness centrality,
people immediately forget between
centrality and other measures.
I think it comes to the fact that
the matrix we're using
is a little bit different.
What we're doing is we
are going to take this example.
And I am not creating
an adjacency matrix, right, for closeness.
We're not using an adjacency matrix.
It looks like it is.
I'll show you what I mean.
It is a distance matrix.
See that? Two there at the end
of the first row.
When I'm saying agent one to five,
I'm not saying is
there a connection or not, right?
That would be a zero in a adjacency matrix.
I'm saying what is
the ***gth of the geodesic?
What is the ***gth of the shortest path?
Well, it takes two steps to get to
agent five. That's a two.
Um, and as I go through this, right,
you'll see going from agent two
to four or three
requires two steps. We have a two.
When I get to agent three, right?
We have actually three steps it takes to get
from agent three to five, right?
This is
not an adjacency matrix for closeness,
it is the distance matrix.
The reason why I teach it in
the order of degree
between closeness is when
you've calculated between centrality,
you have enumerated all of
the geodesics and it's easy for you to count,
well, what is the ***gth
of the geodesic, right?
It's easy for you to make
this table from your
between this centrality calculation.
But do not be confused.
This is not an adjacency matrix,
it's a distance matrix.
Now with the distance matrix we're averaging.
We're going to add up all the distances.
We are going to then divide
by the n minus one, right?
How many nodes you could be connected to?
That becomes your measure, right?
You're going to invert it.
So instead of being five fourths,
you're going to do four fifths.
Why do we invert it?
Well, we invert it because
then a node that has very small distance,
right, like one connection to everybody,
right, is four, then that's
a one that's a higher number.
And a node that takes many,
many pass to get to everybody is relatively
low and that becomes a small number.
Then it scales similarly
to these other measures.
We can score size
the nodes according to their closeness score.
Now there's a couple chal***ges that
happen with
closeness centrality and different software.
We'll treat this differently.
The problem number one
is what happens if you have
a node or set of nodes
that is not connected to the cluster, right?
They're isolates. Well, what
is their distance now?
Well, their distance is infinite.
What happens now when I'm measuring minus
one and I divide that by an
infinite, infinite number, Right?
Well,
that's undefined unless you're in France,
in which they believe in infinitesimals,
and then the number is zero.
Some software will just
make the closeness centrality zero,
so that can become an issue.
What happens when you have two clusters?
Right? Do you do cluster specific?
Closeness is closeness undefined.
Closeness has a lot of problems with that.
And that means that different
people treat it differently.
What I've just presented here
is the purest version of
closeness neutrality that can be
calculated on a single component.
When you start doing something different,
there's some choices you
have to make and you need to
define that if you're
using it in an academic paper.
All right, We're going to now
have the time where you guys
do this by yourself by hand.
I would like you to pause the video and
calculate closeness neutrality by hand.
Again, refrain from just
looking at how I do it Until
you've tried to do it yourself,
until you've done it independently,
you've not mastered the content.
All right, I'm assuming you've
worked this out yourself and
now you're going to go through the solution.
We have the distance matrix
that you see here.
And you can pause this
to check your work if you like.
We can sum across the rows,
divide by N minus one,
which gives us the following closeness.
And you'll see the network size
by closeness centrality above.
I'm Dr. A Mcculloch.
Thank you for watching
this short lecture on
calculating closeness centrality.

Hello, I'm Dr. Mccullough.
In this short lecture, we
are going to work through
a practical exercise of
calculating centrality measures by hand.
In the practical exercise,
I'm going to ask you to pause
the video and answer the following questions.
Calculate the degree centrality of
the nodes, closeness centrality.
Then I'm going to ask you
to define
what the diameter of the network is.
We haven't really addressed that yet.
The diameter is
the shortest path in the network.
So you'll see there will be
a lot of geodesics of
***gth one like mag one
to two or one to four, right?
Those are of ***gth one, right?
So there's always
some geodesic of ***gth one,
that's not that interesting.
But what is the longest
of those shortest paths?
The diameter of the network.
That's like worst case.
How long is it going to take to get
from one side of the network to the other?
That's called the diameter.
So I'd like you to calculate that.
I'd like you to make some inference
about who you would target
for collecting information
about the organization, right?
This could be, I'm going to do
a change management project
for some sort of IT effort
and I want to figure out
who is the person that is going to
be having the best knowledge
of this group and why.
Right. Who's going to give me the most?
If I was doing a military thing
or looking at a criminal organization,
who would I target for capture?
And why would I do that?
You can pause this, leave this screen up,
and then work this out by hand to
see what is the degree between
this closeness diameter and
then make some inference about that.
Then come back and hit play.
And then we'll continue on.
I'm assuming that you've had a chance to work
this problem out and we're now
going to go through the solution again.
Don't move forward to the solution
if you haven't done it by hand or
you're robbing yourself of the opportunity
to try and do this independently.
There's not that many of these problems
with a small set of nodes.
It's important to get
as much practice as you can.
Then when you run into issues,
you're looking at the solution,
the first thing that we are doing is
we're going to calculate degree centrality.
For degree centrality, I'm
making an adjacency matrix.
This is the adjacency matrix.
Ones and zeros in there.
From that adjacency matrix,
I sum across the rows,
divide by the number of
potential others they could be
connected to. That's ten minus one.
And then I end up getting
my degree scores that you see here.
For between this centrality,
I enumerate all of the paths for these nodes.
I identify all the geodesics
that you'll see here,
There are columns representing
each node and does it
fall on the shortest path?
What you'll see is in
the example here of one to five,
there are three geodesics
and you'll see that there's 0.3 0.3 right?
Because they're on a third of them, right?
So I wrote 0.3 of 0.3 3333, right?
Because two is only on one third of those.
I'll draw your attention down here
to the two to three, right?
You'll see these are slightly longer path.
There's 2,543.2 143.
Well, that node one
falls on only 12 of these,
right? 12 of these.
Node five only falls on 12 of these,
but four falls on both.
So it gets a full tally.
You'll know when you sum across this row,
it's actually summing to two.
In this case, it is not the case,
it is not the case
that these are summing to one.
What we're doing is we're saying,
how frequently does a given
node fall on the
shortest path between others?
Right, When I sum down the columns there,
I get the following results.
For agent 123456,
the denominator is then going to
be six minus 16 -2/2 or ten.
Then that allows me with
the results you see there.
And then we visualized it.
The nodes size them according to
their betweeness centrality for closeness.
We do not have an adjacency matrix here.
This is not an adjacency matrix,
it is a distance matrix.
And you'll see that the
adjacency matrix has ones and zeros.
The distance matrix has
other numbers in here, right?
As I sum those across the row,
divide by how many
potential nodes they could be connected to.
I just want to make a point, eigenvector is
a lot more sophisticated and a lot more math
with doing eigenvector decomposition.
That is beyond what
we're going to do in
the scope of this course.
We will do it with software though
it's identifying agents that
are highly connected to others,
It is still an important measure.
I just figured, I should mention that again.
One of these measures tell me
degree is telling me exposure to the network.
If I'm trying to reach a
lot of people quickly,
right away, that's degree.
We find sociologically that
people that have high degree tend to have
low influence in terms of changing
behavior or being respected.
That's usually derived more from
between or closeness neutrality.
Between is the informal
power or gate keeping.
Closeness neutrality is
the time to hear people,
it's the rapid diffusion point.
Eigenvector is a little
bit more difficult to detect,
but able to share
influence by being connected
to highly connected others.
I think the only other thing that is
important to just circle
back on is that analogy of mean, median mode.
Right? I would argue that mean
is equiva***t to closeness centrality.
Right? The average distance to people
median is equiva***t
to betweenness centrality.
Right? Are you on the middle
of the path between others?
Are you in the middle of the network?
And then mode is
equiva***t to degree centrality.
Who has the most connections?
Just like you don't use
mode in that many applications,
I think you should be
hesitant against using degree in
that many applications people use degree
because it's computationally
easy to calculate,
especially in large networks as you
hopefully have some intuition now.
But that doesn't mean that it's the
best measure when we're
dealing with evenly distributed data.
Right?
It doesn't really matter if you're using
median mean or median, right.
In a normal distribution, they're the same.
Well, that's true also with
random graphs right where they're blobs.
But when they becomes structure when you
have different clusters,
then they break down.
And maybe then you're more interested in
identifying median or between the centrality.
Because it's going to give
you a better idea of who's
central in that network than closeness would.
But otherwise, closeness in many cases can
be easier to calculate
or if there's disconnected subcomponents,
then some of the fundamental metrics
in that closeness measure
are a little bit undefined.
And it gets a little tricky and
there's a lot of
different ways of doing that.
It can be problematic as
well with
that information and with that understanding.
My hope is that you can
make more informed decisions about which
centrality measures you're using and how
they work when you're using real software.
Thank you for taking the time to listen.
I'm Dr. An Mccullough.

Hello, I'm Dr. Ian Mccullough.
In this lecture, we are going to be
talking about a few graph level measures,
centrality measures,
that we have been talking about earlier.
They describe the influence of
a single node within the context of a group.
That is, how many people are
connected to direct exposure?
How often do they lie on
the shortest path between
others brokerage or between the centrality?
What's the average distance
to everybody else in the network?
That would be rapid diffusion
or closeness centrality.
Our focus now is on looking
at the group as a whole and
identifying things like cohesion,
presence of vulnerability, or single points
of failure in the network,
these sorts of things.
So the first thing we talked about
briefly in a previous lecture
was this idea of diameter,
which is the longest, goes
with
the longest shortest path in the network.
And that's a little weird to think about.
I'm giving you two examples.
The network on the left is a star pattern,
the network on the right is a ring.
If I were to look at geodesic
between Agent 3.4 well that's one,
it's one in both networks.
If I look at a geodesic of ***gth two, right?
I can go from agent three to four to
five on the node on the left.
And again on the right I can
go three to four to five,
that's the bottom part of the circle,
of the ring, three to 45.
When I look on the network on the left,
if I want to do a geodesic
of ***gth three, there are none.
There's no shortest paths
that would allow me to
go three steps through the network.
But on the one on the right,
I can go three to four to five and
I can go all the way around to six, right?
So that becomes geodesic of ***gth six.
I can't go beyond that because
if I want to keep going around agent one,
well it's faster to go
agent two to agent one.
That's only a geodesic of two, right?
If I go the other way to get to agent six,
I get a geodesic of three.
There's actually two geodesics
of step three get
from agent three to six side of the network.
We would say then that the diameter of
the network there is three, right?
Whereas the one on the left would be two.
That's how we calculate diameter.
The easiest way to do this is
when you're calculating
between a centrality and you've
enumerated all of those geodesics,
you can simply count the longest one.
Just note that geodesic link three,
when I've put that in my between
a centrality sheet,
right, there's four nodes.
But that's three steps
because we're not counting
the number of nodes,
we're counting the number
of links between them.
That's why it's diameter
three instead of four.
Another one is the density of work.
This is the general level of
linkage amongst groups in the network.
The two examples here actually come from
a study I was doing with military
platoons and military structures.
In a typical military infantry platoon,
there is a platoon leader, P,
L, platoon sergeant, PSG.
And then there's three squad leaders,
first, second, third, L for squad leader.
In this study, this is an early study I
did back in the 2000.
Where we were looking at how they responded
to not ambushes or notional enemy attacks.
Initially, there was like
low communication in the network.
The link was if there was
some verbal or radio communication
between these actors after
there's ambush on a convoy,
right, was the measure.
What you see here is with five nodes,
there are ten links
that are potential between them, right?
If everybody was connected
and everybody's talking to
everybody on the left, right,
you saw that the platoon leader is talking to
the platoon sergeant and the first
squaw leader who they were near.
And we see that there are
three edges out of a potential ten.
That density is 30% or 0.3.
And that was
a very poor organizational structure.
There wasn't a lot of communication,
so it was very vulnerable.
They were slower in
the kill zone and it took
them longer to get organized,
to get out of
the kill zone and respond to the attack.
When you look at the right, this was more
of an optimal communication pattern.
And you see the first squad leader
would be in the front of the squad
and probably the one that
was initially being hit.
They're talking to second squad leader
who was behind them and the platoon leader.
The platoon leader is talking to everybody.
The platoon sergeant is in the rear.
And he's talking to everybody back there,
making sure that they're organized and
not progressing into the kill zone and,
and able to mount a counterattack.
And when you look at this,
eight out of ten edges are present.
The first square liter in the front
of the formation is not talking to
the third square liter or
the platoon sergeant in the back.
Right. So that is a density of 80% or
0.8 There's no right
or wrong for density in general.
It can be interesting, however,
when you're dealing with how you're
getting a group of people
to respond in a crisis.
To be able to
measure and point out that, hey,
you had very low communication in this round,
you had
much higher communication in this round.
But you might also argue the volume of
communication is just as important.
Is it one message, is it multiple messages?
Now we're getting in the idea
of weighted density.
You can modify and adjust these things as you
need to depending on your application.
Also, it's important to note that
how high or low a density
is depends upon network size.
When you're dealing with five people,
it's common that there's
high density like
everybody might know everybody.
There might be communication
across a team of five people.
But when you start getting into
a group of 1,000 people,
that becomes really impractical
to think that
everybody's talking to everybody.
And you have more structure and you'll
have less cross talk
across the organization as a whole.
And your density is going
to tend to be smaller
as the networks get larger.
Networks are always going
to have a higher density.
I hope you have enjoyed
this lecture on some graph level measures,
not a lot of them.
There's certainly a lot more measures
that we could calculate.
But for the purpose of
this course and what we're doing,
this is where we're going to try
and identify measures that
we're going to calculate by hand.
Everything else that we would use,
we'll use with software,
Dr. Mcculloch. Thank you for your attention.