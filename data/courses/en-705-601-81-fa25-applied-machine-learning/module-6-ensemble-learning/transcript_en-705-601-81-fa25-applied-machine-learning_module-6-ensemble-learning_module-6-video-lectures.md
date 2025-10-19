# Transcript for EN.705.601.81.FA25 Applied Machine Learning – Module 6: Ensemble Learning – Module 6 -  Video Lectures

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=21c73759-fb0e-4a8c-a1c4-b0c60021a466

We can improve supervised
learning when we employ
numerous weak classifiers using
subsets of features
with limited learning capability.
We will show that by their sheer numbers
and majority voting,
ensembles of classifiers are
better performance and robustness.
Dan, complex individual classifiers.
One of the best ensemble classifiers,
random forest is based
on weak decision tree classifiers.
Therefore, in this module,
we will present decision tree classifiers
and their visualizations.
Down, we will utilize
many weak classifiers using
fewer features from the dataset
and show that they're combined,
voted performance
easily surpass individual classifiers.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=4e3c5980-6e76-4826-90d1-b0c50151eccc

Sometimes quantity surpasses quality if
downright and ensemble of primitive learners,
working as a swarm of classifiers can
perform much better than
a single strong complex classifier.
Not only can the ensemble
classifiers work in parallel,
therefore producing results quicker,
but they can also result in
a much more generalized
robust classification model.
In addition, different types of
strong classifiers can also be
employed as a swarm,
as shown in recent studies.
In this module, we will show how to build
a random forest ensemble
classifier from scratch.
Ensemble learning is one of
the most powerful approaches
in machine learning.
If you remember, in last module,
we looked at several classifiers
individually cause fires.
They were strong, so scattered,
but they will not. Ensemble classifiers.
In ensemble classifiers is composed of
multiple weak learners in
the range of hundreds or thousands.
The approach is using a subset of
data points as in bagging
or boost trap aggregating,
or using a subset of features
as in random forests
and similar classifications.
The benefit of such an approach
is robustness,
higher generalization ability, as you know,
the most important feature
or concept that we want to
achieve in machine learning
is reduction of overfitting.
That means the generated models
have to be abstract enough,
general enough to avoid
any kind of overfitting
the weak learners can achieve them
because they are more abstract learners.
As an example, in curse of dimensionality,
if we have 100 datasets features,
which is a very common number.
If we want to have
five data points on each of those features,
the joint density function
would ideally have to use
500 data points so that
the space would be
covered uniformly and exhaustively.
We know that we will never
have that many data points
than what's the solution
using a subset of those features.
In addition, we will never know
those features being
dependent or independent.
We would never be able to get
the joint density function saw
on some learning helps when we use
a subset of those features
for every weak learner.
And then majority voting
the predictions of those weak learners.
Random forest is a very popular
and very robust ensemble learning approach.
The number of features m,
the square root of it, is used
as the number of features in each tree.
So here, the weak learners
are decision trees which are
using a subset of
data points and a subset of features,
the ensemble size determination
means to be a challenge.
However, the sensitivity of
the prediction to the ensemble
size is very low.
There aren't many parameters to tune.
Even if you use the default parameters,
say five level of threes,
200 or 500 of trees as the weak learners,
as the ensemble size,
square root of m as the subset,
as the size of the subset of
features for each weak learner,
the random forest would
be general enough with
very low sensitivity to these parameters.
That's one of the reasons
why random forest is
a very popular ensemble learning approach.
Note that a random forest uses
multiple decision trees.
Each of those decision trees are
built using
the decision tree building out awesome.
Now, let's see in
the next video how
those decision trees are formed.
What does it mean to have a decision tree?
The decision tree learning.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=79344ce4-bbc6-4783-a458-b0c600755943

Decision trees are the building blocks
of random forest classifier.
And it is useful to
investigate decision tree classifiers
in terms of algorithm training
and visualization.
Decision trees are popular classifiers.
One of the reasons of the popularity
is a decision tree
explains the classification very well.
It's not a blackbox classifier,
unlike a support vector machine
or a neural network.
In addition, random forest,
which is an ensemble learning approach,
uses decision trees as it's weak learners.
If we use all the available dataset,
if you use all the features,
available features,
we can build a decision tree.
This is one example.
Suppose an experiment is conducted where
a question is asked to the customers,
if the food was good or bad,
if the service was Speedy,
if the price was okay.
And then if the customers
sip the way there or not,
we can collect these data points.
And now we can build a decision tree S here.
Decision tree is built solely on this table.
Now, there might be
some conflicts in the dataset.
The same set of features
might have wildtype yes or will tip not.
Well, that only changed
the conditional probability of that
yes or no given foods
be the price with these values,
our interests is not
the particular decision tree algorithm,
but rather how to use it,
how to visualize it,
and then how to pass
the model for classification.
In scikit-learn, we can build
that data into
a DataFrame using pandas library.
We can use the label encoder for the targets,
and then we can extract
the x and the y matrices.
As you remember,
the previous modules use
these approaches at the end,
our data is like this.
This data exactly reflects
what this table has.
This table was the experimentation,
and this data is
the representation of
that experiment in pandas.
If you realize each of
the levels are mapped into numbers 012,
this is not a bad thing because
clearly we can build as the middle,
bad, as low, as good as the high.
So if I set okay to one
back to zero and go to two,
I wouldn't be wrong to mapping
these levels into a discrete value
which has a relation.
The relation is bad.
Okay.
Good In disorders or no.
Yes or no as 01?
Yes, as one shortly.
I don't have to one hot and cold
this dataset because there's
a relation between these levels.
Bad, Okay, Good is a natural order,
natural ranking to those features.
Right or wrong.
This is my data and
the decision tree can be built accordingly.
Scikit-learn has the decision tree,
and actually I can pass
this information to build
a decision tree exactly.
Basically, I will just fit
the data and then generate the model.
Again, Scikit-learn using graph,
this can create those visualization.
This is exactly the
decision tree that I've built.
And if you realize this is
exactly that decision tree
that I built manually,
we can install graph is
using Conda install Python dash graph.
And we will use the dot function to
generate the wheel set three dot, dot file.
Dot is a format for graphics.
Dot is a graph description format.
You can check it out from online resources.
And it's one of
those graph description languages
where actually you can
create not only these simple,
actually decision trees, but also more
complicated graphs, nodes, edges, curves.
And so in this particular example,
the tree that is generated by
the decision tree is
exported using these feature names,
using these class names to the graph
Description Language file to be drawn,
the image command will tip classifier
is generated here from
our decision tree classifier.
So export graph is module or
library function understands this module,
this classifier,
and then be able to generate it.
As you see, the features
are food, speedy price.
And remember the coding, we had.
Food greater than 1.5 means food was good.
So it means it's true.
True, false.
I will tip, recall
that this is the way I called
my class and this is the way I
caught or ankle my features.
So bad is zero, K is one.
Good is true in this model.
If the food is okay or bad.
I will not Let's
see if that's the case for this.
Okay. I didn't it food is bad.
I didn't tip for this okay. Identity.
That's exactly correct, Right?
It's also visible here.
It's also visible in the
decision tree learned model.
Now, if the food is good,
Yes, Dan, was it speedy?
Was the price. Okay.
Depending on situation, either I will
sit or as in blue class,
yes, or I will not set is
in class nor an orange.
So this model is
exactly the loan decision tree.
If I use another example,
the iris dataset and build a classifier,
this is the model that I get.
This model may fit to my data,
meaning the reclassification accuracy
may not be 100%,
but then this is
the model that I'm building when I learn it.
And where do I learn here?
Iris data, iris targets.
And I'm fitting the decision tree classifier
to that data and then exporting it.
This is very powerful.
This is something to be
shared by the subject matter experts.
When we work on a project.
If it's black box,
it limits the shared discussion with
the subject matter expert
because we don't have
a model like this to show to them.
You have to comments in so many words,
many metrics and so on.
But if you show
this model to the subject matter expert,
Dan, that's a very strong discussion points.
A subject matter expert might say
that the petal width is less than 1.75,
so it's definitely versicolor and so on,
which is visible in these labels.
And here and here as well.
For each of these nodes,
I'm also determining the class.
Genie is a particular index of entropy.
As you see, it will go
down as I go through the decision tree.
Here.
It's very high because
I have not decided on anything.
So by looking at the entropy,
the decision tree algorithm actually tries
to find out how to
differentiate these two branches.
And in this case, the algorithm
found out that if the petal width,
if I divide the petal data with
the petal width equals 0.8 or not.
Dan, I reduce the entropy considerably.
E.g. here it's 0.6.
Here it's zero. That means I reduce
the entropy by deciding
only on the petal width.
And here, entropy is 0.5.
That means I have to do
some more comparisons and decisions.
As I go down.
The Gini index will reflect that Ginny is
a particle or index of entropy.
Showing that how important my features and
the decision tree algorithm finds that
petal width is the most important feature,
which can reduce the entropy
much greater than the rest of the features.
Id3 algorithm is one of
the algorithms to build a decision tree.
It literally tries
all the combinations of the features.
Remember, it has to select one
of the features in
the first level and values.
So exhaustively, there might be two to
the m rows in the truth table
because I have that many features If there is
also zero at one output for each one of them,
binary classification than that truth table
becomes two to the two n. It's huge.
However, as I mentioned,
using the entropy concept,
we can reduce this logic table
considerably and build a tree accordingly.
Decision tree building algorithms are fast.
They're using greedy optimization strategy
and Occam's razor is one of them.
Occam razor tells you the decision tree.
The actual tree must be very simple.
You have to reduce the entropy
from the top levels of
the tree as we
go down while building the model,
the remainder of the details
of the algorithm is left for you to study.
But this is the intuition.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=53b4ba84-3ae3-4606-83db-b0c60178631e

Let's see how an ensemble of
weak classifiers can
challenge irregular classifiers.
Now let's see if our claims is correct.
Let's try to demonstrate an ensemble and show
that even though each of
the weak learners are not that great,
the joints, the ensemble power
of them using majority voting and such,
is much stronger than regular classifiers.
And of course, this is all
dependent on the dataset that we are using.
In the following modules,
we will look at data exploration,
understand the dataset, build an ensemble,
and then we will use the subset
of the features for training
that's more difficult than
using the subset of data for training.
Because it needs a lot of management
which feature to save
with the classifier and such.
But we will demonstrate all
these in the following cells.
We picked Titanic prep process dataset.
As I mentioned before,
not all datasets will reflect
the power of the ensemble classifier.
But this particular dataset, well,
we have 891 rolls, 6.9 columns.
This is a pre-processed dataset.
Most of the variables
actually are binary, zero-one,
some of them are regular numbers,
numerical, age and fair.
And of course not all of
the features are that useful as in
any other classification problem
or data mining data science problem.
The first thing we have to do
is data exploration.
We download the data into a pandas DataFrame.
This is the head.
Let's plot a few
just to see what's happening.
Survive, not survived is
our class that's given
and that's the last column.
Note that not all columns might be useful.
This is the information
that somebody gave you.
It's from database,
all the customers and their information.
And now we know that if they're
survived or not individually,
then they look at the plots.
You can plot each feature with
respect to survive or not survive.
If you look at the H, we see that
older people unfortunately
did not survive that.
But some younger people,
like babies, maybe they survived more.
There's any slow ground when we look
at the sex, females,
which are zero, survived more than males.
Now remember, look at the fair.
The fair goes down, not survived,
increases class one ticket,
first-class passengers.
Some of them survive, some of them not.
However, when compared to
the child class customers or travelers,
there's a higher chance
that they didn't survive.
So this is the data we're working on.
We can rank this and
pick some useful features,
feature ranking, data reduction and so on.
However, in ensemble learning,
we don't have to,
because the random forest or the ensemble
will actually simply not
use the useless features.
In this example, we are using
a naive Bayes is a primitive learner.
These are the standards cells that we
always have pulled
the x values from the DataFrame,
pull the Y values from the DataFrame,
use a tenfold cross-validation.
Here is my Gaussian Naive Bayes.
When I ran Gaussian Naive Bayes in this data,
as it is, accuracies 45 per cent.
And here's the standard deviation.
And of course, I save
all the accuracy score in an array,
pass to the evaluation.
Thus, we're able to
measure the mean and standard deviation.
This standard deviation is important.
I'm making 1% or let's say 2% error.
For each of the classification.
It can be 43%.
It can be 47 per
cent when I switch to linear SVC,
okay, 80 per cent, Not bad.
Another linear SVC when
the class weights are balanced,
74 per cent if I was an RBF kernel, 66.
If I use another RBF kernel with
different parameters,
different Gamma parameters,
73, logistic regression, 81,
neural network, network AT
the best classifier 84 per cent.
Okay, So that means ensemble learning
does a better job in
general with this kind of dataset.
Now, let's demonstrate
the ensemble of primitive learners,
where each of the weak learners and,
uh, you Bayes classifier.
And then we will use a subset of features,
not the data points in a script
like this in the following cells,
getting a sample of the data points is easy.
You will just pick
a smaller training set, train your model,
and then use each of those weak learners in
an ensemble for prediction
and now majority voted yet.
However, how would we do
the subset of the features and actually using
the subset of features
for these weak learners
is really abstract in the learning process.
So random forest is powerful because it does
bought subset features
and subset data points.
It wouldn't be as powerful
if only one of them.
We are also computing the priors for the
Unbalanced dataset.
We have only 61, in this case,
not survived, zero value and
38 per cent survived.
It's not that on balance.
Of course, if you ask
me, it's balanced dataset.
However, if I give
these priors to the Naive Bayes,
it will do a better job.
I'm helping the Naive Bayes.
My evaluation is coming from
the previous cells, tenfold cross-validation.
This is my weak learner.
I'm picking features randomly
week and be fit week.
And we predict.
Note that each of
these classifiers are weak learners.
I need an ensemble of these,
maybe hundreds of them,
and that is reflected in the ensemble.
That's my ensemble size, e.g.
I. Will pass hundreds to this value.
When I generate random
subset of the features,
I'm using choice function
from random without replacement,
I cannot have the same features
listed as twice in my list,
so it has to be without replacement.
Evaluation week.
This is not directly can be
used as in the previous evaluations
because I have to save my list of columns or
list of features with each
of those individually weak learners.
So when I generate the weak learner,
I have to save which
features it uses with it.
As you examine this code,
you will see that for each
of the ensemble members,
I'm generating a list of columns
and then I'm passing those columns,
the regular tenfold training and
testing datasets
and then saving that classifier,
passing that classifier with
the columns to how the accuracy this
particle that evaluation does
not do an ensemble evaluation.
It only does evaluate
the weak learners individually.
I have not saved in a
classifier or columns here.
And why am I doing this?
Just to see a pure Naive Bayes
and then the weak learners,
if I do the week loans,
does it improve at all?
Now you Bayes was 45, now it's 48.
It's a very low standard deviation.
I have a very high standard deviation here,
13 per cent, that's expected.
Each of those weak learners are
using a random subset of features.
Some of those features are useless
or working against the glass,
the performance increased because probably
some of those weak learners are
doing great by chance.
They found the best
features standard deviation increase
because I have a lot of
randoms in that uncertainty.
In that if I set
the number of features with three more of
those weak learners might
receive three features which are
completely same value, like zero.
So this particular cell would fail if I run
this many times with only three features,
I will see that Eric,
and in this example,
I used five features here.
Number of features is A5,
size of the ensemble is
100, 100 weak learners.
This cell demonstrates how to
build the ensemble of the weak learners.
First of all, ensemble fits receives
the ensemble columns wherever
I generate that classifier,
some information is pulled directly from the
actual ensemble features that
it goes pass to.
The length has to be the an ensemble.
It's a list of features that will be
used for weak learners.
Weak learners will use this list of features.
Each weak learner will use one of them.
I will generate the list of the features
before creation of the ensemble classifiers.
Ensemble classifier is another list,
which will be the list of the weak learners.
And here I'm generating all of
them weak and be fit from
the previous cell using
the ensemble features,
particularly list of features,
the jth index and x
y is my training and testing datasets.
At the end, ensemble ME fit will
generate a list of classifier models
which were fit by week ME fit
and the size of it will be an ensemble.
Each of those will use
a particular feature list
which I received in the ensemble columns.
So this is a list of
lists of features predict.
We'll use that list and
again the same feature list,
list of, list of features.
It will predict each one
of those and then it will
majority watts each of
the output of those weak learners.
And then it will return the maximum score.
The index, the class,
which was predicted as Pi the
most of those weak learners in the ensemble.
Now this is interesting
when we evaluate the ensemble,
we didn't see any improvement.
In fact, our performance dropped a lot.
Note that this is a new base, weak learner.
It does not have the advantage
of a decision tree learner
where the entropy is
used to pick the right features.
And now you base learner
uses all the features
available without
actually selecting any one of them.
The Naive Bayes evaluates each of
those features equally and
its performance is nine.
39 per cent, which
is less than the previous results.
Its standard deviation is
very low, almost zero.
And in this particular example,
there are 200 weak learners in the ensemble.
I'm doing ten iterations
and it's hard to collect statistics.
And I'm using seven features
for each of those weak learners.
Do I have a bug? No, I do not have a bug,
but that's what's expected.
The useless features are
hurting this particular ensemble a lot.
Why random forest is not affected by this,
because of the decision tree algorithm.
Each of those weak learners are smart enough
to differentiate between
a really bad feature and the good feature.
Naive Bayes is not.
Another question is that
why Naive Bayes classifier works with
all the features much
better than individually weak learners.
Because when we do the naive Bayes fully,
we're using all the features at once.
Saw the good features takeover.
But in the weak learners,
in the ensemble, it's all over.
Many of those weak learners do not have
any access to the good features.
So how can we improve by feature ranking,
by reducing the number of features when I ran
using pure correlation in
one of the assignments earlier,
we did the correlation.
When I look at the correlation
with respect to the class,
it will give me an idea
about the value of that particular feature.
Fair has the biggest one
that is also visible here.
When I look at this particular plots,
it's obvious that sphere goes up,
survive nuts, not survived,
is discriminated by the class,
survives as the fairest goes up,
survived are more, as the fares go down.
Not survived is more seen here.
So this is one of the most important feature.
The correlation also shows that fair age,
family size tickets and all those.
It shows these set of features show
a good correlation with
the class. These do not.
Actually it has zero correlation,
probably, maybe it's a single value tickets.
And when we pick
when the correlation is
less than or equal to two,
I get rid of all these features.
How many I had CCH, Now I have 25.
Note that this feature reduction
is very simple.
We can have better feature reductions,
but even this is
enough to improve my ensemble.
And then again, why did I need this?
Because in my ensemble,
the weak learners are
naive Bayes classifiers and
they are really hurts if
we do not pick the features right,
the decision trees in a random forest,
classifiers are much better
because they are impervious
to the bad features.
A pure ensemble Naive Bayes
classifier improved to 76 sam performance.
And we had a pure
Naive Bayes classifier without
an ensemble directly using
the reduced the ranked features,
891 data points and
25 features directly has
the performance of 76%.
It's much better than
the previous low performance of
naive Bayes random forest.
It's same, it doesn't change anything.
Random force was smart
enough to pick the right features.
It uses Occam's strategic
information gain Gini index
to be able to select the right features.
So it was always high.
And note that these two
particularly results are from
that reduced data set, SPP preprocessed.
Now let's see how
SPP is showing
the ensemble nature-based performance.
Here.
This is without ensemble jumped to
70%, is pretty good.
And this is the ensemble.
The size of the ensemble is 211 features,
ten iterations for statistics jumped to 78.
It didn't reach to A24,
but it is much better than 76.
And I can save to say that because 76
was 76 plus -4.5 per cent.
Now I have 78 per cent plus -3.5 per cent.
Did you realize the lower standard deviation?
So 78 per cent
here is much better result than 76,
more robust than 76,
you might say that I hand picked
the number of features here, 11.
What about if I pick 57920 inventory?
Okay, let's build the experiment and
compare the performance in these cells.
I set up the experiment.
I will basically change number of
features from a few to 35
to see how the number of features actually
affect and not that plane Naive Bayes,
direct Naive Bayes
implementation and ensemble
Naive Bayes is the implementation
that we had before India both cells.
This is the experiment
that you can come up with.
I'm in the extreme experiment
that you can come
up with if we don't have a bulk here,
this shows a very interesting plot for
one plane AU base have better performance,
but it's very sensitive to the features.
When I pick all the features,
actually it hurts.
These features work against the classifier.
These features are probably
the good features like up to 25.
And here, the order of
the features is the order of the correlation.
However, I ranked above
here in the experiment.
This is the first feature to use this,
these two are the second features.
These three are the chart features.
These four are
the first four features and so on.
So I'm helping the classifier In
both cases. That's straightforward.
That's what has to be done anyway,
because we are feature ranking
and then we are using
that rank to build
a classifier even with a few features,
Naive Bayes does a super job.
It starts from almost like 67 per cent.
I prefer blue because it's very robust.
It's standard deviation is
lower than the plain Naive Bayes,
where this band is always higher, bigger.
My goal does not have
to be the best accuracy,
but rather my goal has to be
the most abstracted, most generalized model.
And in this case,
the ensemble menu-based
actually use that to me.
It's very insensitive to the features.
As you see, it plateaus after 15,
using all the features here,
or using only 15 of them here
and are still having a good result of 76%.
Our conclusions of
this demonstration, and again,
note that we use
weak learners as naive Bayes classifiers,
which are by themselves,
they're limited classifiers in a way
compared to the decision tree classifiers.
So our experimentation, our approach was
really pushing it to the limits are results.
Ensemble performance is better
than plane a base
when all features are added
has better generalization. Why?
Because our standard deviation is lower,
generalization is much better.
Ensembl uses all features
randomly picked. Here.
If I pass 35, plainly
performance is very sensitive
to the features included.
As you see, it's all over.
Even with like five to ten features,
the ensemble learning really improves
considerably with a lower standard deviation,
with a lower variance of the error,
the red and the span is
the standard deviation here for the plane.
Now you base and the blue band here is
the error rate is the variance of
the error for the ensemble learning.
And as you see, it goes more
and more as I add more features.
This concludes our
ensemble learning approach.