>> [MUSIC] It is of utmost importance to
evaluate machine learning
performance objectively,
as it is easy to skew
our view of the capabilities of
far model and experience
a failure after deployment.
In this module, we will study how to
evaluate our learning model
in terms of performance.
First, we will list
the popular and common metrics used in
machine learning and talk
about their circumstantial uses.
Next, we will talk about
the generalization of a machine
learning model and
find why the generalization of
a learning model is
the most important property
of the learning model.
We will present which
classifier algorithms are
good generalizes and then
we will look at
the classical evaluation method,
the receiver operating characteristic,
show how to generate
it in a learning pipeline.
Then we will talk about how to pick
your learning model depending
on the operating points
on ROC by optimizing
the true positive rate
versus the false positive rates.
[MUSIC]

>> [MUSIC] Dear students. In this module,
we will look at model evaluation.
Clearly, we are building an analytical model,
an AI model, a machinery model.
Do we think we built the right model?
How can we test or evaluate it?
How can we predict the performance
of the model when we deploy it?
Supposedly, we are building
a predictor machine learning model,
but can we predict this predictor machine
earning model's performance when we deploy it?
In order to build the model,
as we know, we need data.
We divide the data set into three pieces.
The first piece is training.
When we build the model,
we will train using that training
data set and then the testing.
Again, building the machine learning model,
we will use the testing to
check the error of the training.
Then a third piece,
most of the times it might be used,
sometimes it's not crucial
is the validation data set.
If we have model parameters,
then we will use the validation data
set to tune those model parameters.
Notice that, all three pieces
are mutually exclusive,
and then they add up to
the 100 percent of the data set that we have.
When we built the model,
we fine-tune the model
using the validation data set.
This fine tuning happens if
the particular machine
learning algorithm has parameters.
Sometimes these parameters can
be set by ad hoc values,
but sometimes we have
to tune those parameters.
For example, a good example
from random forest,
say, the death of the trees may not be tuned.
We can set it to say five under asset.
However, for a support vector machine example,
we use a radial basis function kernel.
The Gamma parameter has
a say in the
wiggly off the discrimination plan.
So we will use the validation data set
to tune the Gamma parameters
of a support vector machine.
In the random forest example,
we can use all the data for training
and testing only, skipping the validation,
but the support vector machine requires
devalues the validation data
set to tune the Gamma parameters.
The biggest mistake would
be running training and testing
multiple times and then finding
out the Gamma parameter
without a validation data
set by picking the best accuracy that we
achieve with that
training testing iterations.
This is definitely
a wrong approach because it
biases our model with
the data set that we have.
When we deploy it in the field,
this model has a chance that it will fail.
It will not be general enough.
As you guess by now, by model evaluation,
there making sure that
our machine learning model is general.
That's the utmost important feature or
characteristic of any machine learning model,
is the generality.
What is the simplest classifier
that you can come up with?
Classify zero no matter
what is the simplest classifier.
It doesn't use any data as training.
The classifier says,
whatever your data give me,
I will clarify as zero.
There is no even an if else condition.
Imagine, if we have
five classes that we are trying to predict,
and if this simplest classifier
classify zero all the time,
what is the performance of that model
assuming each class has
equal representation in the data set?
Meaning to any person
of the data-points are Class 0,
20 percent of the class
data-points are Class 1,
20 percent Class 2, and so on.
Well, clearly, it will be 20 percent success.
Every time I classify as zero,
I'm hitting one of the Class zeros.
Well, I know that one-fifth
of the data set is all Class 0,
then my performances 20 percent
accuracy is not zero.
If I have two binary classes,
equal representation,
meaning balanced data set,
50 percent accuracy.
That's my smallest value that I can
achieve with the simplest
classifier that I have.
Imagine you are having 10 percent accuracy in
a binary classification scheme
where the data set is
balanced, what would it tell you?
Yes, you have a bug in your program.
>> Now that we say generalization,
the models generalability is
the utmost important feature
of the machine learning model.
The second concept that
we're handling is the false alarm rate.
When it comes to machine learning models,
we have two metrics.
Probability of detect, true positive rate
or probability of false alarm,
false positive rates.
If we maximize our false positive rate,
maximizing false alarm rate,
we can also maximize the true positive rates.
We will see in a moment
these are working against each other.
We do not want a high false alarm rate.
Imagining a cyber security problem
where every file is marked with a virus.
Say, you are building game,
predictive cyber security model,
and then your model marks
each of the file with a virus.
Though you're catching all the viruses
because all of them are
marked as there's a virus.
It is similar to that simplistic classifier
where our model
classifies everything with zero.
Well, okay, my probability of
detection is a 100 percent,
I'm detecting everything.
But then my false alarm rate
is also a 100 percent because
the ones that do not have
a virus are also marked with a virus.
Can we compromise the false alarm rate
versus the probability of
detection so that we can
have a manageable false alarm rate,
and then a good probability of detect.
You will see that momentarily,
in a receiver operating characteristic curve.
We have model evaluation methods,
clearly training-testing-validation.
Train and now look at
the test with everything you have.
This is called reclassification.
It's a good first test
to do reclassification.
I trained my model with all the data I have,
and I tested my model
with all the data I have.
You should expect a high
reclassification performance,
almost a 100 percent.
If it's a 100 percent,
it means you over-fit your model.
If it's 90 percent, it's good.
If it's 10 percent,
you have a bug in your program.
The common approach is
k-fold cross-validation.
We shuffle the data,
we pick 10 percent of
the data each time for testing,
and 90 percent of the data for testing.
This is 10-fold cross-validation.
If it's 5-fold, we fold the data into five,
20 percent testing, 80 percent training.
They are not overlapping,
they are mutually exclusive,
and on the average,
accuracy is the one that to report.
This is the best step approach.
K-fold cross-validation.
Leave-one-out cross-validation can be
used when the data set is very, very small.
Say, I have only 10 data points
in bio-informatics example,
I have a long gene,
I'm using a support vector
machine, which is excellent.
When the data set is unbalanced, for example,
you deal with cancer data,
99 percent of the patients live,
1 percent of the patients die.
It means, your predictive classes,
cancer survivability is unbalanced.
Ninety-nine percent of the data is
labeled as survive, zero.
One percent is labeled as
one, dies of cancer.
Well, in order to evaluate this correctly,
in order to evaluate
with k-fold cross-validation,
for example, we have to do stratification.
Meaning, your test set should
contain equal amounts from each class.
The most important aspect
of model evaluation is measuring
the expected real-world performance.
If we build the model generally enough,
than when we evaluate the model,
we will also expect
an expected real-world performance
from those evaluations.
Just to give an idea,
and of course, these
may be somewhat circumstantial.
Support vector machines, they have
very good generalization ability.
They are basically optimized for that.
Random forest, ensemble classifiers,
any ensemble classifier is
also have very good generalization.
Principal component analysis, because we
reduce the dimensions of
the data set, again, good.
Deep learning neural networks with
dropout ratio and L2 regularization.
They also generalize well, and of course,
human beings are
excellent generalizer machines.
Then we look at the evaluation metrics,
the math part of it.
We will see the classification as number of
correct predictions divided by
total number of predictions.
If your data set is sizes n,
if you correctly predicted
90 percent of the data points,
then your accuracy is 90 percent.
The confusion matrix is
a very good indicator how your model behaves.
The top side is the ground truth.
This can be also the labels.
Like the data labeled with A,
the data labeled with B,
and on the vertical sides is how
my model actually behaves
on the testing data set.
If I use a k-fold cross-validation then I
can accumulate all these
into one confusion matrix.
Now historically, Type 1
and Type 2 errors are important.
When I have an unbalanced data
set like the cancer data set,
I have to fix my class A
as the cancer is there and I'm detecting it.
So Type 1 miss like patient has cancer,
predicted patients has the cancer.
The first element in
this confusion matrix gives
you the probability of detection,
and thus the most
important metric in my model.
Why? Because I'm detecting the cancer or not.
If the patient has it or not.
Imagine if I detect here,
patient has cancer predicted A,
and the patient doesn't
have cancer in reality.
What's my cost? Well, we
will alarm the patient,
"Oh, you have cancer,
we have to start treatment process".
But other than that,
there is no cancer because
the patient doesn't have the cancer.
So other than a really bad false alarm rates,
I'm not missing anything.
But if I miss, like here in the two,
one element of this matrix,
the cancer has the patients,
truth A is here,
cancer is there, and I
predict the patient doesn't have the cancer.
Oh, this is really bad.
This is Type 1 errors.
Missing the positive,
miss-predicting class A,
because the patient had
the cancer and I missed it.
Like I sent the patient to home,
you don't have any cancer
but then in a few months,
the symptoms got worse,
but now I miss the treatments timeline and
the model gave
a gravely incorrect information.
Type 1 errors are very, very high cost.
Type 2 errors are high cost,
but not that much. I'm alarming everyone.
I'm probably spending unnecessary money
for treatments, for additional diagnosis.
But at the end, I'm not
missing that disease, that malady.
Type 1 errors are
the most costly errors I'm committing.
A few other math pieces,
true positive, true negative,
false positive, false negative.
We can build a truth table to mark these.
Basically, if my prediction is A,
and if the ground truth is A,
count them, that's
your true positive rates. I'm sorry.
True positive numbers.
The true positive rate
is the rate when I make it into a rate,
meaning take the true positive number.
How many I have? 10. How many
true positive I have?
This column. That's all the cases
where the patient has the cancer.
Now I made it into a rate.
True negative rate, similarly,
20 divided by this column.
I can also use precision recall
from information retrieval.
F1-score can combine true positive rate,
true negative rate in
somewhat an accuracy like metric.
However, it's more important to use F1-score,
because accuracy thinks truth A
and truth B are equally important.
Basically, count how many
times you predict it right,
and then divide total.
Well, it is giving less value to the Type 1.
It is giving equal value
to Type 1 and Type 2.
However, F1-score is giving
high value to Type 1,
low value to Type 2, I can control it.
So if I'm dealing with a cancer detection,
cancer prediction like machine learning model,
I have to use F1-score, not accuracy.
Area under curve, we will see that
shortly in a receiver
operating characteristic approach.
Mean absolute error is
the error between the
original and the predicted.
This is of course,
values for the regression problems,
and also we have a logarithmic loss,
a more sophisticated metric
for measuring the errors of the model.
Next, we will look at
the receiver operating characteristic curve.
[MUSIC]

[MUSIC]
>> Historically, detection prediction
and analytical approaches for
classification were not called
machine learning or artificial intelligence,
neither did we have certain terms
like F1 score or the confusion matrix,
and of course, historically
means this was like 30-40 years ago.
However,
imagine a radar target detection problem.
The problem is a particular object on
the radar screen and if we can
detect that object coming towards the radar,
can we detect an object on
the radar screen? What are the metrics?
What are the evaluation methods?
We were talking about probability of detect,
probability of means or false alarm rate.
Now in order to compromise
between the probability of
detection and probability of false alarm,
we use a tool
called receiver
operating characteristic curve.
The name is totally historical.
As I explained, receivers are
the radio receivers from
electrical and
electronics engineering fields.
I will jump to
the actual plot and
come back how we generated.
This is an ROC curve.
My y-axis is true positive rate,
probability of detection,
my x-axis is
false positive rates
probability of false alarm.
This is a binary classification problem.
The line here from 0,0-1,1 is the line that
shows what would be
my probability of detection if
I just determined if there
is a target or not by a coin flip.
A little bit more less simplistic classifier
like randomly selects zero or one.
Remember in the previous video,
we were saying the simplest classifier
there can be is always takes zero.
Now we moved one step
forward again, incredibly simplistic.
Randomly pick zero or one, and of course,
a true random generation is impossible,
so it is kind of arbitrary.
Now if this is ROC,
if I have run time parameters like
a threshold setting
a particular signal level,
if the signal level is
higher than my threshold,
then I decide I'm picking
as a target is out there.
If my signal is less than threshold,
then I'm saying there is no targets.
So the operating point is
determined by that simplest threshold.
In the next module,
we will see how a perceptron behaves.
It is the very same thing.
The perceptron training finds
out a particular division line
between the data points.
In this case, the threshold,
a single value in
one-dimensional space represents that plane.
So if my input signal
is higher than the threshold then,
I decide I have a class one case.
If my signal level
is lower than the threshold,
then I decide I have a class zero case.
Thus, these operating points
are determined by the threshold.
By moving the threshold
between low and high values,
I move along the ROC line.
In a more sophisticated example,
these parameters are model parameters.
For example, in a support vector machine,
they are the gamma values.
In a deep learners,
they are any parameter that you can think of,
size of batch, number
of iterations, all those.
In a random forest,
they can be the death of the trees
or minimum number of items per node.
In a logistic regression,
it can be another threshold
that we will see in a moment.
Now let's see what we do with this ROC.
We will generate a lot of
results and then each result
will be used to generate
the true positive rate and
false positive rates,
and of course, if I have
multiple data points in my testing set,
I can compute accordingly.
Each one of them is contributing
to the TPR and FPR.
In this example, we use
breast cancer data
from the Scikit-learn datasets,
and we are developing
a regular classifier model.
Pull the data frame, name the columns,
add the dependent variable,
cancer at the end,
this will be malignant
or benign, it's nominal.
So all my features here,
all my columns except for the cancer column,
the last column will be used for
model development and of course,
X my dataset for training,
the whole matrix actually.
I have not discriminated
between the testing and training.
This X will be the entire datasets.
I'm picking everything but cancer.
I cannot put the ground truth
in my dataset of course,
otherwise it will
be a perfect classification.
It's like fortunetelling or
knowing the reality, knowing the truth.
In the Y values,
remember these are the ground truth values
for computing the error of the testing.
I'm not getting any column
except for the cancer and of course,
X and Y are in sync.
For every index X,
it will be the relevant Y on
that index with
the cancer value malignant or not.
I'm running multiple data points
and that fitting a logistic regression.
Before that, I'm using standard scalar.
This is very typical.
I'm scaling every value here to a value
between zero and one so
that the logistic regression,
which is a probabilistic classifier,
can use each of them as
a probability and I give equal importance.
I can also use a support vector machine,
which is a distance based classifier.
As you see, we are running
two, four, six, eight,
nine times because we're just
varying the parameter c
from 0.2-100 as reflected here, 0.2-100.
In Python, you can write
with the e annotation,
so you don't have to deal with lots of zeros.
These are my operating points.
This parameter c,
which is also called a hyperparameter,
is used to mark
the operating points on the ROC.
Here is my classifier,
random state none, penalty L1.
You can play with this L2 solver
because logistic relation use an optimizer.
That's solver is the name of the optimizer,
class weight is balanced.
Clearly you can check this for yourself,
our cancer malignant and
benign are not balanced.
It's an unbalanced dataset.
So by passing class weight balance,
the logistic regression scikit-learn
logistic regression program applies
proper penalty to each class
so that it will be reflected in the cost.
I'm getting the c from this tuple list,
multi-class auto, maximum iterations 10,000.
Similar to deep learning,
logistic regression is solving
an optimization problem.
So the more iterations,
the better convergence it will be.
But of course, I cannot
set this to 100 million,
I will wait forever, and it will be
definitely the case of diminishing returns.
The more iterations doesn't mean
that I'm getting better and better results.
It is basically like wandering
around in a small space with very,
very small improvements maybe,
or it can be oscillating.
Of course, maximum iterations
is a magic number.
You will just have to run
this, see your results,
increase this, see the results,
how much accuracy you are
having? Is there any change?
Then decide on the maximum
number of iterations.
Now I computed all the operating points.
Here is a TPR, FPR
for each of the operating point,
I have nine operating points.
Let's plot them.
These are just the plots for
plotting the points nicely on this curve,
sorting and such,
and I'm annotating certain points,
operating point 1, 2, 3, 4.
I have nine red dots and of
course every time you run this,
if you start from a different seat
like random state none,
it will generate a different one.
However, I'm fixing them.
So the random state and everything,
so that every time I run this notebook,
I will have the exact same set of results.
Now the question is,
say we're predicting cancer
where all the datasets is breast cancer data.
Will you pick operating one,
will you pick operating two, three,
four? Which operating points?
Or in other words, which c you will pick and
then generate this model and then
deploy to the field to detect cancer?
The answer is probability of
detection is very important for cancer.
I would pick operating 0.4 with
a 35 percent false alarm rate.
There will be a lot of false alarm rates.
I will be doing a lot of re-diagnosis,
making some patients angry,
but I'm catching all the cancer that I can,
and of course you can argue the difference
between on the y axis,
the difference between operating three and
operating four is not that much,
I can agree with that,
but my point is go as high as on
the probability of detection for
a problem like cancer detection.
What could be the counterarguments,
false alarm rate?
Imagine you are predicting
the attack from
the other parties, a nuclear attack.
If your detection results in
some nuclear missiles fired,
we are all down.
A high false alarm rate might
cause the end of the world.
Why? Because you didn't detect it
right it was a false alarm
and then you fired your missiles,
third world war, end of the world.
Probably I would pick operating one with
the lowest false alarm rate as
possible for a nuclear attack detection.
Probably there's a very good chance
I'm not detecting it right?
But of course, these are all circumstantial.
You will compute this ROC
based on your model,
based on your dataset,
and then based on your hyperparameters,
and then leave this decision
to the higher pay grades.
You'll leave the decision
to the decision-makers.
Our job as the model developer
is laying out the capabilities of the model,
the hyperparameters behaviors,
and then leaving
the decision about picking
which operating point should it
run to the decision-makers.
If this was a cybersecurity problem,
there will be a knob
controlling the sea and then
your security officer would
put the knob somewhere,
let's say five percent, 10 percent.
It will load a lot of work to
the analyst if you
have a lot of false alarm rates,
so there's a cost and
now when you are dealing
with false alarm rate,
you may miss the actual thing.
So the ideal position should be somewhere
in-between OP1 and OP4. What are we doing?
We're maximizing the generalization ability
of our machine learning model.
Well, why?
Because we do not know
the underlying joint probability
distribution of the data.
We will never notice
since we didn't create this universe or
since we do not have the
monitored the observation to have that data,
they will never ever have
an idea about the
underlying joint probability distribution.
We will always have
an estimate of that probability distribution.
By the way, this statement
is totally mathematical.
We can never know the
underlying real population of the data,
population in terms of
probability distribution function.
Thus, we will never know what to model.
In fact, machine learning models estimate
the underlying probability distribution of
the data and then
built the model accordingly.
If we knew the
underlying data probability distribution,
we wouldn't need
any machine learning problem.
We will just pick one
of the data points according to
that probability distribution function
using regular statistical approaches.
That's all for this module.
[MUSIC]