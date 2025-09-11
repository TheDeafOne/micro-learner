So the artificial intelligence algorithms
we've discussed so far in
this course have come mainly under
the heading of good old fashioned
artificial intelligence.
Algorithms are concerned
mostly with problem-solving.
The algorithms seek to create
general-purpose reasoners.
The results are often operational knowledge,
a plan of how to do something.
And we, we very often have to
engineer what goes into the reasoner.
We want to switch to machine learning.
Now I'm sort of modern
artificial intelligence
is concerned a little bit more
with pattern discovery.
The results tend to be more specific.
The algorithms are specific,
the results are representational.
They're going to represent a pattern
and the Verifit and data-driven.
So we're going to have
a collection of data that
we're going to be able
to learn patterns from.
Machine-learning further subdivides
into three categories,
supervised and unsupervised learning.
And that all.
So what they called
reinforcement learning is actually
a third category and machine learning,
but we already
covered reinforcement learning.
So we're going to concern ourselves
with just supervised and
unsupervised learning.
And we're actually not going to cover
unsupervised learning in this course
because it's simply too much material.
So for supervised learning,
we have known features and a known output.
For unsupervised learning,
we have just known features,
but we don't know what what they represent.
For supervised, there are
two types of supervised learning.
Broadly speaking, one results in
a numeric output, this is regression,
and one results in a class label,
and that would be classification.
So an example of regression is the weight of
a car and miles per gallon.
So we would like to predict or find
the pattern between the weight of
a car and miles per gallon.
And here we can see a whole bunch of data
about the weight of a car in pounds.
So here's a feature and there's the output.
And we can see all this goes to the data
driven aspect of modern machine learning.
So whenever the car as a feature,
miles per gallon is output,
because the output is a number
that falls under regression.
For classification, we have features,
something like weight and miles per gallon.
And we, we tried to predict
the contract manufacturer,
which is a label either
Japan or Europe or the United States.
So we have our two features here,
way to miles per gallon.
And then the yellow dots are going to be
cars made in Japan or a European Union.
And the blue dots are called
cars made in the USA.
The status from the eighties.
So again, wait in
miles per gallon or features.
And Japan is the output.
Now for each of these
supervised learning tasks, tasks,
there are a wide variety of
machine learning algorithms that
can be used for regression.
We can use what is called linear regression.
We can use artificial neural networks.
Fuzzy control systems are fuzzy rules.
Regression trees or k-nearest neighbor.
For classification,
we use something called logistic regression,
which is actually classification,
not a regression.
Support vector machines, SVMs,
decision trees, Bayesian networks,
or also k-nearest neighbor.
And a lot of these algorithms have
corresponding algorithms
for the other topics.
So they're actually support vector machines
you can use for regression.
But these basically cover
what we're going to cover in this class.
Now features have different types
of feature can be a measurement.
For example, the weight of
the car can be counts.
Rankings, dates are going to be categorical.
For our measurements, counts,
rankings and dates,
we often consider these
to be numeric features.
For measurements, these are continuous.
But for counts, rankings, dates,
and categories, we think these discrete.
And it turns out that some algorithms are
actually better able to
handle some of these different features.
So for example, k-nearest neighbor,
because you need to use a distance metric,
doesn't deal out of
the box with categorical variables.
You need to be able to
encode them differently.
And there are some transformations,
encodings that are possible
that converts one to the other.
And we'll see in
the rest of this course though,
somebody informations could be
misleading and say you need to think
about whether a particular transformation
and cutting makes sense for your,
for the variable, for the feature.
One natural question is why they are there?
So many algorithms, isn't there a best one?
And the answer is no,
there is not a best one.
And all of them have
their weaknesses and strengths.
And we'll see in a future module how
you would go about
model selection for your particular problem.
Typically you will want to
try for a particular probably will want
to try a variety
of algorithms and pick the best one.

Now we're going to start
with our first algorithm.
And that's going to be linear regression.
And we're going to pick the
same problem we had above,
but much more simplified is
the relationship between the weight of
a car and it's miles per gallon.
And here we have just four observations
instead of 3000 up above.
And we have the one feature
which is weight in
pounds and the output
which is miles per gallon.
And so we have 2774 pounds,
18 miles per gallon,
3,329 and 17 3250 United 16 and
4,341 is 15 miles per gallon.
Again, the weight is feature
MPG as the output.
So it's the relationship between
these two variables that we want to model,
the pattern that we want to model.
Now remember the equation for a line
is Y equals MX plus B,
where M is the slope,
which is the change in Y as X changes,
or you might remember rise over the run.
And b is the y-intercept.
So we want to model this pattern as
line. How do we do that?
We need to use the data to
estimate these two parameters, m and b.
And so it turns out
that modern AI is still search,
but it's the search for
parameters and often Meta parameters,
parameters for a model.
So how do we find these parameters?
There are many ways to draw a line.
Well, one approach would be to look
at the relationship between
the output and the error.
So if we look at what we would calculate is
our estimate for the miles per
gallon for given m and b.
We could say that y hat,
which is the hat, is
the symbol for an estimate.
Y hat one minus 18 is the error.
This is set could be negative or positive.
We want to square it so that
it was always a positive number.
Then we can do this for each observation.
We can calculate the squared error for
each observation for a given m and b.
And then this would be the sum of
the squared errors if we
added up all these errors.
But there are four observations.
So if we divide the sum
of squared errors by four,
we end up with the mean squared error.
So that's one metric we could use to decide
whether a line was good or not as to whether
we minimize the mean square error.
So for now let's call this line
f of x is a function.
And we're going to use j to denote
our cost function that
we're trying to minimize,
in this case, mean squared error.
So it's one over n times the sum of
f of x minus y squared.
Now for now we're going
to ignore the intercept.
And let's just ask the question of,
given this estimate of cost,
how do we find the best slope?
So here are our data points again.
And what we're gonna do is we're going to
map different choices of
slope against our cost function.
Notice here it's just a function of
m. So what if
we picked at random, I'm just picking M1.
And so M1 is going to be
associated with a particular line.
It's going to be the slope of the line.
I can draw the line here on the, on the data.
So that's M1.
Now as it turns out,
we can graphically show
what the error squared error
is by looking at the distance
between the actual point and
the line is the error.
And then the box that is
formed is the squared error.
And then the mean squared error would simply
be the average area of all of these boxes.
And so that's actually what we're trying to
minimize when we say we're trying
to minimize the mean squared error.
So let's say that the error for m1 is here.
Now what if we picked some other slope m2?
And that's a line about here.
Well, we can draw out
the squared error as we did for M1.
And it looks about the same,
maybe a little bit more.
So there's M2. Now let's
pick another line. I'm going to pick m3.
And I'm going to draw this one
a little bit closer to
the data points. This is m3.
You can see that this crater
here is very small.
In part because I picked
observations that fell roughly on a line.
That isn't going to happen
always in real life.
So here's m3. And if we find,
if we varied this all together,
we would get a parabola.
And that's because Mean Squared Error
for linear regression,
the error surface is actually a quadratic.
And then we actually, we've
seen this before, right?
This is the evaluation function
for local search.
J, just a heuristic
function or an evaluation function
for each of our parameter values.
Now the difference between
this and local search is that
in this case we have a well behaved function,
meaning that it has a nice second derivative.
So we can use the calculus to help us.
First, let's, let's talk
about the general case.
So for the general case, there's going
to be more than one feature,
so you use a slightly different notation.
We're going to switch to
thetas as being the slopes.
And these are more actually
more commonly called coefficients.
So these are the coefficients of
the regression, the Thetas.
Second, we're going to do a little trick.
And that is we assume that there's always
an implicit x sub 0, it's always one.
And if we do that, then we can
actually add x sub 0 as
a feature on the intercept here at
the start of the equation.
Now because of this, we actually end up with
a very compact notation
for representing a line.
And as we can use vector notation and show
that y hat and
the hat is traditional statistics.
Notation for an estimate
is just Theta x equals y hat.
You just doing a dot product of two vectors.
Now a little more notation here.
X sub i, we're going to say is a feature,
just plain x would say is a vector.
So that would be all of
the features for an observation.
And x-bar is going to be a particular vector.
So here we're going to say this is
our equation for mean squared error.
Again, the only difference
is that we're adding
in here a 1.5 factor,
which doesn't change the result at all.
It's, it's in there so that
the calculus result works out a little nicer.
I'll say we've switched from using
f of x two y hat,
y hat of I. Which we see is just.
So what we need is we need
the partial derivative of
the cost function with respect to
every coefficient.
Love with respect to a specific coefficient
will have to do this for every coefficient.
And it turns out that it's one over
n times the sum of the difference between
the estimate and the target
and the x value for that coefficient.
And this just comes from the chain rule,
where the change in J,
where the change of j from
y hat times the change in y hat from theta j.
So now let's look at the slope.
So essentially this is the slope
at the error surface.
And we're going to use that to change
our guess for the best theta.
So let's draw theta
against mean squared error again,
which is exactly what we did above.
Now I'm just going to draw the quadratic.
And let's look at the case where this slope,
this partial derivative up here is positive,
so it's greater than 0.
And say this is just some theta, theta j.
So the partial derivative with
respect to the Cij is greater than 0.
And so what do we want to do?
Well, it looks like we want to
decrease Theta
when the derivative is positive.
Similarly, if we have this other theta j,
we see that its slope is less than 0.
And so we're going to want to increase theta.
So basically we have
an inverse relationship here between
the desired direction of
change of theta and the partial derivative.
So as a general rule,
we don't want to uptake
the Theta Js all at once.
That is, we're not going to apply the
entire partial derivative to the theta j.
We're going to only apply
a small fraction of it,
and that's the Alpha
here is the learning rate.
And this is
sort of a shorthand for the algorithm
here I'm going to repeat until convergence.
We're going to update Theta j by taking
the current value of theta j
minus alpha times the partial derivative.
Knowing that for theta j,
this is actually a loop
because of the calculation
of the partial derivative.
And of course this is
actually a loop in here as
well because we need to do this
for all the j's.
And the convergence criteria
is basically the same as
what we had for search.
So convergence is guaranteed
in the sense that there is
a global minimum for
the error surface and there are
no local minima.
So we don't have to worry
about random restarts
or that sort of thing because
of the quadratic.
But you need to pick the right alpha.
So picking the wrong alpha could
lead to a failure of convergence.
So if you have the right size of alpha,
then you will nicely
find the bottom of the bowl.
You have the wrong size of Alpha,
normally one that's too big,
you will actually go out of the bowl.
You could actually have an Alpha 2s small.
And although you're
going towards the minimum,
it will take you in it lee
long time to get there.
So this is for alpha two
big and alpha two small.
Alpha being too big is
a bigger problem because
you're not ever going to get to convergence.
And what you can do is you can print out
the errors as you loop through.
And you, you see
if the errors are getting smaller or not,
and you stop and
decrease alpha if they aren't.
So this particular approach
is called gradient descent.
It's a very general algorithm and there
are actually many different versions of it.
This is the simplest version.
It's not actually
the usual algorithm for regression.
In statistics. There's actually
an exact solution or
an analytical solution that's
used. For machine learning.
We demonstrate the concept
of error minimization using gradient descent.
And for linear regression,
it's the easiest way.
It's the easiest way to
explain gradient descent.
And also turns out that when you have
a huge amount of data,
the analytical solution is not usable.
And therefore you need to use
gradient descent or
some other algorithm in the family.

So this video is about some practical advice,
some tips for regression and actually
other machine learning algorithms as well.
I'm going to call it part one,
but I don't actually know how
many partners there will be.
So looking specifically, regression,
you can think of it is waiting
the feature values.
So each feature, in order to make
a prediction is weighted
by each of the coefficients.
So we have Theta 0 plus Theta
1 times x1 plus Theta 2 times x2,
and Theta 3 times x equals to y hat.
Now, if x1's range is about
minus 8.792 plus 3.52.
These numbers are completely made
up and x2's range
is 3,245 to 8,765.
And z3 range is minus 0.0062 minus 000.
32 than X2 is going to have
a disproportionate effect
on the error calculation.
And so what we really need to do is we need
to rescale these values
so they're all at the same magnitude.
So you wouldn't have to do this, for example,
if all of your variables were in
the ten to 99010 to 99 range rate.
So it's the difference in
magnitude that makes a difference.
And we can rescale using
a technique called mean normalization.
So for a particular x i prime,
that's the Trump's transformed value.
It's equal to the actual value
minus the mean divided by the range.
And the range here is just
the maximum value of
XY minus the minimum value of x i
and mu sub I is as the mean here.
Now the downside of course to
this is that you need to save
these transformations to use
it as a priest processing step.
Each time you use your model
to make a prediction.
So it's going to add
a little bit of overhead there,
but not up, not a whole lot.
And if you normalize your Y as well,
you will actually need to
denormalize your model predictions.
So that's one sort
of practical issue we will see
there are actually some algorithms
require normalisation.
Another problem has to do with categories.
You'll notice it's very simple to use
numeric values in
a regression because it's just,
but how do I use something
like population density?
Actually a better description
of this variable is neighborhood type.
But suppose my neighborhood type is
urban, suburban, or rural.
How do I use these in our regression?
They're not numeric.
Now, let's look at a slightly easier case.
What about gender?
What if I want to use male and
female in my regression?
Well, the typical solution
to that problem is to use
a binary variable and set
0, male, one, female.
And what happens when you do that
is you are essentially creating.
So this would be my regression.
I'm using gender.
Gender is always going to be 0,
1 when I'm training.
Then if gender is equal to 0,
I can see that
this theta one term actually goes away.
So the effective intercept
becomes just theta 0.
And if gender is equal to one,
then I'm just adding
thetas sub 0 plus theta sub one,
and that becomes my effective intercept.
So what happens when you use
these binary encodings like that?
What you're doing is you're essentially
creating different types of intercepts,
but it can never affect the slope.
So we can see here what happens there
is y hat and x.
And we can say this is the male line.
And what happens is theta one
gets added on that's female line.
Of course, theta one could subtract
and that would actually be below.
So these are also called dummy
variables or indicator variables.
So now, getting back
to neighborhood type, what can we do?
It seems like a natural way to do
this would be sort of like urban equals 0,
suburban equals 1 and rural equals 2.
But it actually turns out
that this is problematic
because is
rural really twice the value of suburban?
Now that doesn't make any sense.
So it'd be a bit more careful about
converting variables into
numerical variables bout values.
Instead, what we tend to do is we tend to
convert this into n minus 1,
where n is the size
of the domain of the variable,
n minus 1 dummy variables.
So we're going to have a variable that's
suburban question mark 01 and rural 0, 1.
So 000 would be urban
because it's neither suburban door rural.
0100 would be it is
suburb in it isn't
or rural and then you have it the other way.
Another thing is this does add
more to your preprocessing steps.
But it makes everything turned out much
nicer and it allows you to use
categorical variables.
This is a huge topic and we won't be
able to cover everything in this course.

So let's start with
our first classification algorithm,
logistic regression.
That's not a good name for
it because it does classification.
But we'll see later why it's called that.
So imagine we wanted to use
regular regression to do
classification. How can we do that?
And let's think of our problem
that uses miles per gallon
to predict whether something
is either made in the USA or
the car is made somewhere else.
Well, we can code our output is a one,
which means the object is the class.
And we could use 0 to
say that the object is not in the classes.
We could use a binary variable.
And as we saw last time in the last video,
we can very easily use
a binary variable and a regression.
So for example, we'd have
1 would be made in the USA.
And the feature might be miles per gallon.
And so our points would be sort
of distributed like this.
Where we're axes. We have
miles per gallon as our feature.
We're going to predict USA,
which is either a one or a 0.
So all of them that are made
outside the USA are
here and all of them that are
made inside the USA are here.
And then we'd run regular regression through
these data points and
come up with a classification algorithm.
We'd use this threshold here.
Now, one problem, of course,
is that our regression actually goes
outside the bounds of 10,
which is a little weird,
but we can still use
the threshold to cap everything to 10.
But it turns out it's not very robust.
And we'll show why here.
I can copy this.
Suppose we add one more point
here and we redid the lines.
You have the red line.
If you look at the red line
matches the threshold,
our classifier is now
nearly completely inaccurate.
So just by adding one observation,
the line changes dramatically.
So one alternative would be to fit
a different function rather
than the threshold function.
And so what we could do is actually if we had
this function here and we add
another observation
than the line stays where it is.
So it's not sensitive to
these outliers anymore.
So how can we, what's
the equation for this line then?
Well, we have our regular Theta axis.
Now. We're going to say that's equal to z.
And then we can feed that into the law
to the function and get our y-hat.
So it's one over one plus e to the minus c,
where c is our old regression formula.
So our estimate y hat will
range from 10 to one.
And it can be interpreted as
the probability that X belongs to the class.
Of course, in our training data,
Y will always be either 0 or one.
So now we have
the parameters of the model we want to
fit in here for this probabilities.
Then we just say if it's less
than 50, then we say it was 0,
50 we say it was
one because eventually we need
to match the y hats against the y's.
And 0.5 is not the only possible value.
So now we have a parameter values.
How are you going to tip them?
Then we saw last time for
regression we assigned a cost to
making mistake when
the model was wrong and it
was y hat minus y squared.
Now we could do the same thing
for logistic regression,
but the result wouldn't
have a smooth derivative.
So what should we do?
Well, it turns out that we can use
logs as an error function.
So we're going to show here
is the value of y hat,
which is either between 01.
This is for an actual value of, of Y1.
So we're going to say what do we
want the error to be?
And it turns out if we use minus log y hat,
then if minus log 0 is infinity.
So that's an infinite cost to being wrong.
And the minus log of
one is 0, which means you're correct.
So here we have a 0 cost.
If I'm correct, at an infinite cost up,
I'm absolutely positively the
most wrong I can possibly, possibly be.
And we have to do the same thing
for y equal to 0.
And it turns out we just need the curb
to face the other way.
And the equation for that is minus log
times minus log of 1 minus y hat.
And we'll see that again.
If in this particular case,
one minus 0, that's correct.
One minus one is 0, then it's infinite.
So if I'm correct, the cost is 0.
If I'm incorrect, the most incorrect I
can be than the cost infinite.
But it's cumbersome to have two equations.
Well, it turns out with a little bit
of clever math,
we can make one equation.
So y times log y hat plus 1
minus Y times log of 1 minus y hat is r,
can be a combined equation for error.
And let's see all the possibilities here.
We have y equals 0,
Y hat equals 0, y equals 1, y hat equals one.
So there's the two correct cases.
Y equals 0, Y hat equals one,
and y equals 1, y hat equals 0.
And if you've worked through all of these,
you'll see that for the first two cases,
these are all 0.
B's either cancel out as 0 or equate to 0.
So all my errors is 0.
And the second two cases where I
have where there's an error
where y and y hat are in disagreement.
Oh, and by the way, y hat will never,
ever be exactly 0.
So you'd have to worry
about actually dealing with infinity.
We'll see that our costs are infinite.
And this corresponds to this case.
And when we do the final one where y
equals 1 and y hat equals 0,
this again becomes infinite width,
sort of quotation marks around it.
And that corresponds to this case.
So then we have one equation that
will work for any instance
to calculate the error.
So now we have a new j, and
it's simply the sum of
these errors divided by n.
So it's the average error.
As it turns out.
The derivative of this error function is
exactly the same as it
is for regular regression,
at least at one level of notation.
So the derivative of
J with respect to any theta j
is one over n times the sum
of the y hat minus y times x i of j.
The differences you have to remember that
y hat is it complete,
is a different function.
It is the one over
one plus e to the minus sc.
Aside from that,
the algorithm is exactly the same.
You use gradient descent.
Just use a different it's a gradient descent.
You're just using a different
error function and derivative.
Well, it's fine if you have a binary problem,
what happens if you have
three or more classes?
So what if example,
we have this problem here,
where we have X1 and X2 as features.
And this has class,
these are class circle and
class cross and class triangle.
So now how are we going to come up with
a regression for these?
Well, it turns out what we generally do,
least for logistic regression
is we're going to train three classifiers.
We're going to train the zeros
against the non zeros,
which will be the x's and triangles.
The axes against the not axes,
which is the 00, 00, 00 and triangles.
And the triangles that gets to not triangles,
which would be the circles that axis.
So essentially that's the first discriminant,
that's second discriminant.
This, these aren't curved in this space.
There are curved in
the dimension that's coming out of the,
out of the screen at you.
So to predict, to simply process an example,
the features, and you pick
the class with the highest probability.
So you'd run it against all three models.
And you pick the one
with the highest probability
in a triangle has the highest probability.
You say this one's a triangle.
Now there are classifiers that handle
non binary classification example.
In the next module,
we'll talk out on
the three modules to talk about
the decision tree.
But there are some classifiers are
only deal binary classification.
And oddly enough, the literature
suggests that multiple binary classifiers
is often superior to
using a non binary classifier.
Guesses, how would we test this hypothesis?
And you want to think
about that because when we talk
about model selection in the next module.

So there are many ways to
draw a discriminant.
Add a discriminant is just a separator,
a discriminator between
a class, between classes.
So things that are in the class,
things that are not outside the class.
So we can draw a linear discriminant in,
in, in number of ways.
So for example, if we have
the class X over here,
and when the class is 0 or circle over here,
we could draw a line
here that would discriminate
between the two classes
are we can draw a schematic here.
The last video we saw what would happen if
we used a log function
for our error function.
And it turns out our cost function,
if we use a different cost
function instead of the log,
will see that we get
a different kind of line.
So let's review what
the log cost function did.
So we have y hat.
And y hat can
be anything but generally
want it to be 0 or one.
This is the case where y is equal to one.
Let's make a quick copy of this.
And so here was the log error function.
So if we're correct,
there's no error that
were incorrect, it's infinite.
We could use this red error cost function,
which shows that there is no
cost for being between
01 and an increasing
cost when you're less than 0.
And similarly for the y equals 0 case,
we can have no costs between 0,
1 and increasing costs
when you're greater than one.
This is called the hinge loss
function because it sort
of looks like a hinge on a door.
In the more general formula for
our cost function is c times
the sum of Y times the cost of
y hat plus 1 minus y times the cost of y-hat.
You can see that almost looks like
what we had last time.
Little changes, being a
little more generic about
what cost is instead of
him putting in log directly.
And we see that if we have
our classification task again,
that this particular cost function
leads to a particular kind of discriminant.
It leads to a discriminant that
maximizes the margin between the classes.
That's margin is this space
here on either side of
the line is at a maximum between the classes.
So this loss function creates what's
called the wide margin classifier,
which is also called
the support vector machine or SVM.
So it turns out the support vector machine is
this linear discriminant that uses
a hinge loss function for its cost function.
And these vectors that
fall right on the margin, these,
these data points that fall right on
the margin here are called
the support vectors,
which is where it gets its name.
They're always at least 21
on either side of the line.
Now the role of c in the formula for cost for
the support vector machine
is in the case where
we want it to be able to classify,
but the classes are not completely separate.
So here we can see
that there can't really draw
a line that separates them completely out.
And what C does see controls where,
how we treat these outliers.
And so it'll, it'll rotate
the line around that point.
So a smaller C will
make the line more vertical.
And a larger C will make
the line more horizontal.
This is called the soft margin.
So it's still a support vector machine.
It's just dealing with the case where
the classes are not completely separated.
Now, SVMs are usually
solved with quadratic programming.
This contract, context by program,
we mean optimization like linear programming,
dynamic programming, integer programming.
But you can't actually use
gradient descent methods for it.
You know, if the SVM,
we're just another linear discriminant,
they probably wouldn't be that interesting.
So need to talk a little
more about the case where
the classes are sort of
blended together and they're
not easily separable.
This falls under linear and
non-linear separability.
So a concept which
is just a classification problem.
So the concept is made in the USA,
not made in the USA.
It's another name for the class.
So a concept is linearly separable.
If it can be perfectly
described by a hyperplane.
Otherwise, it's non-linearly separable.
So let's do a few examples.
So we have a one-dimensional line
here and one dimensional case.
And we have our classes x and circle.
And we can see here that in
this case I have a plane is a point
that the two classes could be
perfectly separated by this point.
And let's have our two-dimensional case,
which we've been dealing with.
We have our x's and our zeros.
And we can draw a line that separates them.
So all of these cases,
these are cases where
the concept is linearly separable.
But let's look at
a different one-dimensional example.
Imagine that we have these cases here.
And you see that there's,
there's really no place we
can put a point that'll separate the classes.
Similarly in the two-dimensional case,
we have XX circle, circle, circle, circle.
And there's really no place where we can draw
a line that will separate the classes.
And so we would say in these cases
the concepts are non-linearly separable.
Now, imagine that we have
a one-dimensional case like this.
And we were to use
a higher dimensional projection of
these points up the
data that we're training on.
So we're going to project into
this phi of x space.
And let's just use squared.
We're gonna use a quadratic.
So essentially we're just squaring
all of these numbers and using them
instead. That an x.
Now we have instead of one feature,
we have two features which are
x and x squared.
We see that the concept
is actually linearly separable.
So the concept becomes
separable in a higher dimension.
And so the goal would be to find
the correct per projection that
would make these linearly separable.
This phi of x is called a kernel function and
you can actually use it anytime
you have a dot-product,
such as in support vector machines.
And in other cases, we'll see later.
Embedding the kernel function in
a support vector machine is
known as the kernel trick.
And this is actually what
gives support vector machines their power.
Otherwise they are simply
linear discriminant like logistic regression.
And you can use other kernels,
you can use polynomial,
you can use Gaussian.
There are a number of
different kernels you can use.

So now that we understand what a model
is and the concepts of machine learning,
we can talk about model evaluation.
The general framework for machine learning,
at least supervised machine learning,
is that of having
some data and wanting
to model the pattern in it.
And this pattern is usually some,
some part of the data
is what we would call features.
And another part of the data is
labeled or has a target value.
And the reason we want to do this
is we want to be able to get
future instances
and predict or classify them.
So if we have the features without the label,
we can estimate what the label should be.
And so here we have training data,
which is all of the
x's and the training data is n.
We can train a model which is f of x.
And we get some acts
and we don't know what it's,
why is put into the model.
We output an estimate.
And so the same thing for classification.
So as we're doing this would
naturally sort of two questions arise
and will address the first one and
then the second one in a different video.
So the first one is how well does
the model perform on unseen instances?
And the segment, is there a battle mom,
a better model than this one?
Now this entire enterprise
depends on the assumption of
statistical inference,
which is basically that
any real-world live data we
see will be like the training data.
If you trained on something
entirely involving white swans,
it will not be able to predict or
classify a black swan or a blue swan.
So the distribution of features,
the things represented in your training data,
I need to represent
what you plan on using the models for.
So what does it mean that a model performs
well or that there is a better model?
In order to answer these questions,
we need to talk a little bit about MIT,
metrics of performance
or performance metrics.
For regression.
It's pretty easy when
it's typically used is mean squared error.
Although you can certainly use others.
For classification, it's a little
bit more difficult.
Let's assume we're dealing
with a binary variable.
We have just the two class problem.
Now.
We can look at what's actually in
the data and we can
look at what the model predicted.
So if the model predicted a one,
and it really was a one,
then we call this a true positive.
So we predicted a positive
and it really was positive.
Similarly,
if we predicted that it would not in
the class and it really wasn't in the class,
then this is a true negative.
We predicted it as negative.
And it was indeed negative.
On the off diagonals, we have
a prediction of it being a
one, but it really was a 0.
We call that a false positive.
So is falsely predicted to
be positive, false positive.
That in the lower
left we have a false negative,
which is that we predicted it to be
negative or outside the class.
And it was really inside the class.
If you sum up the columns,
that's the number of positives
and the actual dataset,
if you sum up the rows,
that would be the number of
positives in that were predicted.
And some of the table is the total examples,
and it's called a confusion matrix.
So it shows how confused your classifier is.
So true positives plus true negatives
over the total data size is accuracy.
And false negatives plus
false positives over the total data set
is the error or error rate.
Now these, although these are convenient,
they're not always the best and metrics.
And the reason for this is
that false negatives and
false positives may not be equally bad.
And the second for this is
that the classes may
not have an equal distribution
in the training set.
We see why this problem.
Suppose 70, 78% of
your training data or in the negative class.
And a 78 percent accuracy
probably isn't really
that difficult to achieve.
So we often want to look
at more specific measures.
One of these is called recall is
the true positives Over
the true positives and false negatives.
Now remember though, this denominator
here is the total number
of positives in the dataset.
So basically you're saying, yeah,
of the positives in the dataset,
how many can I identify?
What percent did we find?
Precision which is true positives over
true positives plus false positives,
which is saying,
out of all the positives predicted,
which percent were correct.
So precision is the ability to discriminate
between positives and negatives
are zeros and ones.
Recall. The ability to find them
and actually recall is used
a lot in natural language processing.
They talk about using it with search.
There's often a trade-off
between precision and recall.
Now what did I mean earlier about
false negatives and false positives
may not be equally bad.
Let's let the positive be an edible mushroom.
And let a false positive then is saying
that somebody has poisonous is edible.
And a false negative is saying that
something that's edible is poisonous.
So in this particular case,
truly false positives are
worse than false negatives.
Now let's look at a test
that says whether you
have a cancer precursor.
False positive says that
has the precursor but healthy.
And a false negative
then is a healthy result,
but really had the cancer precursor.
So in the one case,
you would want a higher false negative rate.
And the other case you may want
a higher false positive rate.
And these are actually
related to type one and
type two errors in statistics.

So now we know it better or well might mean
in the context of model evaluation.
But we still have a bit of a problem.
We only have a fixed amount of data.
And if we use
all of that data to train our model,
then how, what data
do we have to evaluate our model on?
We could wait until we got new data,
but that might be a while.
And we certainly don't
want to use the data we
used to train the model
because that would be cheating.
So one approach to this,
use cross-validation.
And what you do is you imagine
that this is your table of data.
We're going to shuffle it up and guess
the data came to you and some sort of order.
Then you split it into five equal groups.
So there'll be group 1, group 2,
group 3, group 4,
and group 5 of equal size.
Folds. Now there's
nothing mysterious about five.
It could be three or it could be ten,
depending on the features
and the size of the dataset.
Features with larger domains require
larger data sets in
general than features with smaller domains.
So it depends on both of those.
And then what you do is you're
going to rotate through
these folds each time
using one is the test set,
and then the remaining four
folds as a training set.
So for example, here you are going to
use sold one as a test set.
And then you're going to use Fold 2, 3,
4, and 5 as the training set.
So for logistic regression,
you might train on two through
five and then you test it against one.
And you'll get some sort of error rate.
And then the next time through
you're going to test with
two and train on 1345.
And you'll get another error rate.
And then you rotate through.
Now you're going to test with
set three for choosing 1,
2, 4, and 5 to train.
And then you get an error rate.
And then you can test with four and use 12,
35 to train and you get an error rate.
And then finally you're going to test
with five and train on one through four.
And it doesn't have to be the error rate.
Of course, you use
whatever measure as appropriate.
So with five-folds, we have
what's called five-fold cross-validation.
You're essentially going to estimate
five models using
the five training sets and calculate
five different metrics using
the corresponding five test sets.
And then essentially you come up
with an average metric
and you can calculate it and
standard deviation for it.
So you can get some sort of estimate
of how your performance is going to vary.
So if the data encountered in the wild,
that is data that you meet,
that you see after you train a data,
isn't anything like the test data,
it gives you an estimate
of model performance.
So now that we know how to evaluate a model,
how do we fix a model that may
be a sec if
it doesn't have very good error rate.
So we can look at further model evaluation.
Suppose we found that we have
a model and it has a 9% error rate.
Well, we'd like to fix
that and there are a lot
of different ways we might be
able to new features,
different projections of features.
Something that almost always
comes to mind though,
is that we think we need to get more data.
We need to get more data to make
the model more accurate.
And that's often time-consuming
and expensive.
And we can ask ourselves,
will this always help?
And one way that we think of this in
machine learning is in terms
of the bias-variance trade-off.
And it relates how a model
does on the training set versus a test set.
So imagine we have these data points here.
I'm going to look at three cases.
Suppose we decide to use
linear regression to model these points.
We say that this has high bias
and that's with respect to the data.
Now imagine that we use
a high degree polynomial on the day.
Instead, we say that this has
low bias with respect to the data.
Now imagine we have these purple points.
We need to classify
what we see that on average
these these errors are very small.
They're, they're not, they're not
wildly different from each other.
So we say that they have low variance.
But now look at those same predictions
against the curve that we fit very well.
Is there's a very large and
they're eager and they vary.
So we say where we have high variance.
This is related to two other concepts.
One is saying the first case
that we're actually under fitting the data.
Then the other case we
say that we're overfitting
the data where we really want a nice,
nice smooth curve like this.
What we mean by bias,
which is sometimes a difficult concept
to grasp is how much the data
or the model influence
the algorithm or the data
influences the actual model
that you get out of it.
He's seen the case of
a line that there's going to be
an upper limit on the amount of
data you can add to this
and get a different line.
So the line or the model dominates the data.
Whereas in the high, low bias,
high-variance case, the data dominates.
So now we would want to know
how do we tell which situation,
where and how do we know whether we're
in a high bias case or a low bias case.
One way to do that is
to pick your training
set folds and your test set folds.
And you're going to train on
just 5% of your training set just at random.
Pick 5% at random.
And then you calculate your metric
on the training set.
I know and I said
previously that wasn't a get an a,
but there's actually a rationale
for this in this particular case.
So you're going to do it on your training
set and then you use the test set
and calculate your metric,
let's say its error rate.
And we're going to do is to plot them.
So visually what we have is
we have our folds,
1345, we have a test set two.
And we're going to train on just
5% of my training set.
Pick 5% at random.
Then when I plot
this against the training set,
I get this low error.
And when I plotted against the test set,
I should get this higher.
And the x-axis here is
just the number of training instances.
Like to keep doing this.
I train on 10 percent at random,
and I train it 15% at
random than 20 percent of random,
all way up to a 100 percent
each time on the training set and
against to the test sets up getting
these two scores of error.
And you don't have to do it exactly this way.
You just, just using
an increasing proportion
of your training set.
Sometimes with really huge data sets you may
want to use go and 10 percent increments.
So this is the error line for
training and this is the airline for test.
And it turns out that the two cases, low,
low bias and high bias,
or low variance and high variance
have distinct patterns when you do this.
So imagine that our lines
meet or get very close to each other.
She said this is actually the high bias case.
So we can see why.
Because if at a 100 percent blind Matt,
adding more data is
not going to make anything better.
So more data won't help.
But you can do is you can add more features.
You can add feature transformations
L to look at the other case.
Here we have the training error.
Here we have the testing error. Oops.
Like these, little further apart.
We have the testing error.
And we can see that now,
but because there's a gap,
this is a high-variance case.
Essentially in my model is underfitting.
In this case, more data will help,
or it could reduce features are removed.
Transformations.
Fortunately, reality is rarely this clear.
So here's an example of plotting these lines.
And we can see that the, the,
the error rate on the test set
essentially flatlined.
And then it went
all kinds of weird directions
on the training set, but generally upward.
And it may also be
unlucky in the folds that you pick C,
you could want to rotate through
your folds and do multiple plots or average.
We can do something similar when
picking parameterizations,
some models have parameters.
For example, a polynomial
will have its degree.
Or a logistic regression,
we'll have the threshold value which
we saw was 0.5.
But you can actually
pick a different threshold
variable depending on
whether false positives or
false negatives are more
important to you or not.
So the question becomes, how do you pick?
So we can do something
for different parameterizations.
So imagine that we have on the x-axis,
we can pick the degree of the polynomial.
And we have mean squared error on the y-axis.
So we can do is you can
pick a parameter value,
use all of your training data to train.
And then do a,
and then do a metric on the
training data and a metric on
the on the test data,
which would be in
this case mean squared error.
And then you plot that error,
each of those error rates.
And then you just keep repeating
through your parameter values.
So I could do one for
a second degree polynomial, third degree,
fourth, fifth, sixth degree
polynomials. And I keep getting these.
Now, unlike what we did before,
we're going to use all of your training data.
The thing that's varying in
this case is the degree of the polynomial.
What should happen is that you will see
that the error on
your training data will decrease.
But your test will have an inflection point.
So this is what you're doing is you're
actually finding the sweet spot
between underfitting and overfitting.
And so that inflection pop,
that inflection spot in
the test error curve
probably indicates your best parameter value.