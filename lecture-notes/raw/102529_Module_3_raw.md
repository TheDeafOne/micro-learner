None

[MUSIC]
>> Dear students. Today in this module,
we will look at
the preprocessing of datasets.
As you may be aware by
now and as quoted by many textbooks,
the machine learning program,
the machine learning model pipeline is as
good as its input data, and more so,
the textbooks and colleagues
would tell you 60-90 percent of
the effort of a machine
learning model development goes
into the data preparation.
This data preparation not
only includes cleaning the data,
making sure the machine learning pipeline
can ingest the data,
but also preprocessing the dataset,
so our model is refined.
You can assume that
sophisticated machine learning
algorithms can easily
work with uncleaned data.
However, when we clean the data ourselves,
we will have more control,
we will also understand what the data
is, called data exploration.
So we understand the data,
we learn the data better,
and now we can apply the machine
learning algorithms much better.
Now let's see this whole thing
in a worked example.
In this example, we
intentionally made the data bad.
We added duplicates of data lines,
we added missing values,
marked both as question mark
and not a number,
and also add some incorrect entries.
Now when it comes
to machine learning pipelines,
not all of them are created
equally or exactly the same.
For example, in Weka,
nominal variables like
this categorical value is in quotes.
However, it might be in double quotes,
it might be in single quotes.
During the ingestion of the data,
we can provide
this information to the program.
What is our quote?
Interpretation might be different.
For example, if you put quotes,
this number can be input as a string.
But maybe we do not want that.
Maybe we want the numbers being real numbers,
so that our work can be better.
In another example, using comas or
semicolons in a comma separated values file.
For example, is this
a single value, 1; 50; red?
Or is this three different values for a CSV?
We have to make sure
these confusing pieces will be
cleaned so that our machine learning pipeline
would ingest the data good,
and then our model would work.
In most cases, you might
not see an error is generated.
But when you run a model,
the performance will be low.
Or in some cases, Weka, or scikit-learn,
or Pandas ingests will
tell you what is not right.
However, that excuse,
that problem report may not
reflect the exact reason.
We have to dig in
the file to understand what's happening.
Let's do that for our example.
This is the data file we will use
in this module; module03_breast_cancer.csv.
I downloaded using Notepad++,
this is open source free editor.
You can use your own editor, of course.
As you see, the first line is the header.
Sometimes we do not have headers.
So we have to read in this file to Pandas,
for example, and create some feature names.
Each of these, let's say,
column separated by a comma,
in this case, our features.
It looks like our dependent feature
is at the last column, recurrence.
We cannot just input
this whole file in
a machine learning program just like that.
At least, we have to separate
these nine variables into an x matrix,
and the last column recurrence,
which is our dependent variable,
has the cancer recurred or not in a y vector.
Now as I go
through these, this is interesting.
I have an age minus five. I have NaNs.
When I click, I can see all the NaNs.
I have to impute these NaNs,
or I can leave them as NaN and leave
it to the scikit-learn
to impute something here.
I might have question marks,
let's look for them.
There are some question marks,
and this is an exploration.
This question, probably it will be
a question mark in another dataset,
but this could be something else as well.
Another thing I notice is,
numbers are numbers without quotes
and the values with quotes
are nominal variables,
and these are levels for
that particular nominal variable,
right and left.
This is corresponding to the breast column.
Now I explored, I will
close this window and go back to my Notebook.
Here I use Pandas and Seaborn to
download the load data
to my Notebook and then plot it.
This particular plots of Seaborn
plus according to the degree-malignant,
nominal or in this case a
numerical variable, it has 1, 2,
3 as degree-malignant,
and each plot is tumor-size and age,
and the color is the
dependent variable or target variable.
This shows me how degree-malignant
affects the discrimination
of recurrence and non-recurrence.
It looks like when it's degree-malignant one,
generally it's blue, no recurrent.
When it's degree-malignant three,
generally it's orange.
This is a very good discriminating
variable, don't you think?
Also my bad data shows up.
I have a minus five here as age,
this must be an incorrect entry.
I have 250 here,
it must be an incorrect entry.
I have to clean these.
Let's first check the duplicates,
let's work with the duplicates first.
Pandas has duplicated function
which will list all the duplicates for you.
It will list the extras for you.
In this case, I have three more of
the same data points of exactly this line.
>> I have two more exactly this slide.
Of course, recurrence has to be same as well.
If recurrence is different,
it looks like I have the same data points for
both recurrence recurred
and recurrence non-recurred.
That's a contradiction entry, isn't it?
I removed the duplicates,
five of them removed.
It's a very good practice to check
every step for sanity.
I removed five data points.
Duplicates are gone.
Now, I will look at the missing values.
When it comes to missing values,
I have two options,
one for numerical, one for nominal.
For numerical values, I can impute the mean,
and for nominal variables,
I can impute the mode.
There are sophisticated imputing approaches.
For example, stochastic.
I can use the stochastic approach.
By looking at the frequencies
of all the levels,
I can impute randomly
a level which reflects that distribution.
For the moment, we will just move on.
Our goal is primitively
showing all the options
in data pre-processing.
Now, let's check if we
have any NaNs in our dataset.
DataFrame. Any NaNs?
Give me any point,
any function gives me any point,
and the output is a Boolean.
I have NaNs for age,
no or yes, because it's true.
I have NaNs for menopause,
false, and these are false.
I will impute whenever there is a NaN,
not a number by its mean.
Here, I'm computing three means using
NumPy and I'm repeating
the work with the DataFrame mean.
These two are different functions clearly.
But, this notebook shows
what can be done with Pandas,
Scikit-Learn, so that we
will be aware of all these options.
So it is not a mistake
that NumPy mean is used
here and then repeated
the same thing with
the Pandas DataFrame mean.
It is intentional. Just to
show what are the capabilities.
Now, I have the means printed here and
I imputed the information using those means.
For example, age here,
whenever it's missing,
56 is imputed because the mean is 56.
Whenever the tumor size is
missing, 28 is imputed.
Then, whenever the inverted notes are
missing, 3.5 is imputed.
It's not visible in this list.
Missing nominal variables, I will just
compute the frequencies and
I'll impute the mode.
Now, the first thing,
I have to check the variable feature type.
Whenever it's float 64,
it's basically a real number.
Whenever it's int 64,
it's okay, it's an integer.
I may want to change this,
convert this to float.
But for the moment, it's not that important.
These objects are nominal variables.
If you remember, these were in
codes in the input data file.
Now, I will check for each of the objects,
what are the unique variables?
If all the unique variables or levels,
unique values are meaningful then,
I don't have any missing thing.
For example, menopause,
everything looks fine.
Pre-menopausal,
greater than 40, Less than 40.
But for node caps,
I have a missing value, one or more.
No, yes, should be the only answers,
but I have question marks.
Similarly, breast quad,
another one, and that's all.
Do you think we can
impute something in the recurrence?
That means we don't have the ground truth.
Most probably, I would drop if I have
a missing value of
recurrence in a particular data point.
That's not useful to us because we don't know
the ground truth for that data point.
It is useful for clustering,
but not for classification.
Now, let's check how many value counts
do I have for the node caps.
No, 227, yes, 56, and missing 10.
I had to use either
227 for missing because
that's the highest number,
or a statistical distribution accordingly,
randomly pick with a random threshold
of 56 divided by 283,
which is the probability of
56 or probability of yes.
The other probability would be
227 over 283, sorry.
This probability distribution is
reflected in the imputation.
I imputed the values.
I checked for the incorrect entry
of 250. I corrected it.
I also plotted to see
where is it in age. It's weird.
Tumor size, it's a nice distribution.
Inverted nodes, nice distribution.
Degree malignant, three different points.
I do not have the distribution.
We could color code
these plots to show the intensity.
For example, how many
recurrence events happening here.
We could show it as
color-coded for better visualization.
Now, 250 gone, minus five remains.
In most cases, we have to use
a subject matter expert to do this right.
Who says 250 is a wrong data point?
Well, in this example I can,
but in some examples I cannot because I'm
not the subject matter expert in this field.
Here, we see how to
color code the data points.
I updated the plotting to have
a Gaussian kernel density dimension.
So that the z direction,
or let's say the z variable,
is used as the color for each of
these nodes and it is computed
according to the density estimation.
So you can imagine
there's a probability distribution
here for example or
a probability distribution here.
This dot is
a discrete probability point, single value,
and it is more red,
more higher values compared
to these other two.
That means recurrence events happen
when we have degree malignant as three.
When degree malignant is two or one,
recurrence events happen less.
Similarly, this is light color,
this is even lighter.
That means the mean
of the distribution is somewhere
here and it is
more towards non-recurrent events.
So this is one way of doing it.
Now, that our cleaning is complete,
we will do discretization
as explained in the next module.
[MUSIC]

>> Let's see how we visualize
preprocessed data points in our dataset.
After a quick check to make
sure our preprocessing indeed
results in better dataset,
we will learn how to discretize
nominal features in
a dataset by utilizing
one hot encoding methods.
>> We did discretization
in the previous modules.
We converted a numerical variable
into a categorical variable by binning.
Also we can convert a nominal variable,
which are levels or categories,
to a numerical variable
with one-hot encoding.
For each of the levels,
there'll be a new column generated.
Now, lets see which ones to one-hot encode,
and why we are doing?
Because this particular classification,
random forests that we're going to
use likes numerical variables.
We know that by experience and by reading
the API of this particular implementation.
The ones that we can convert to
one-hot encoding are the nominal variables,
and remember, they're objects.
So these six variables have levels,
they are not numbers.
For each of the level, for example,
in menopause, there are three levels.
For each of those levels,
we will create three columns.
These are independent,
supposedly independent columns,
but of course we know that
they are not independent,
but it doesn't matter.
This is the only way to encode
a nominal variable into numerical variables,
values, so that we can use
this data point and this
feature in a numerical classifier.
In this case, menopause variable
has ge40 greater than 40,
less than 40 premenopausal
as three different levels,
and these are individual data points
between zero and nine.
We are displaying the first tier.
Whenever there's a one
in one particular variable,
the other two is always zero,
thus the name one-hot encoding.
We built this function, encode_ one-hot,
here, and now we are
using for the remaining four variables.
Question, are we going to encode recurrence?
Well, we will not,
because random forest classifier in this case
likes the dependent variable as 0, 1, 2, 3.
We do not have to one-hot encode.
If there are two levels,
it's binary classification.
In this case it is binary,
recurred or not recurred.
However, note that for a neural network,
this is indeed one-hot encoded.
The output layer has two values,
either it will be recurred or not
recurred, exactly one-hot encoded.
But in this case, we are not
one-hot encoding the recurrence variable.
Now, there are four ways
to evaluate a classifier.
In our case, 80 percent
random test-train split,
meaning 80 percent goes to training,
20 percent goes to testing.
Leave one data point out each
time and use everything else for training.
In this case, it's easy because the number of
data points here is less than three hundred.
If this was one million,
leave-one-out would be
totally impractical, of course.
But here, I'm showing
it for the sake of completeness.
Leave-one-out is another approach
when there are very few data points.
10-fold cross validation,
is the most common one.
Each time, one fold is kept for testing,
the rest is used for training.
Stratified is the more important version
of the 10-fold cross validation.
When the data is unbalanced,
like in our case here,
non-recurrent events 205, recurrence
events 86, it's pretty unbalanced.
It's not like 200 versus
200 or 100 versus 100.
It is 238 versus 80.
It's not terribly
unbalanced, but it's unbalanced.
So we should do stratified cross-validation,
where training and testing
datasets are created in such a way that
there is this march density
of recurred and non-recurred
events reflected.
So each fold will not
be terribly biased to one side,
but it will be biased
as much as the original dataset shows.
We defined a function here
for the random forest classifier for testing.
We create the x and y,
x is everything but recurrence.
That's our dependent variable,
we cannot include it in
the training of course,
or let's say training dataset matrix,
but we will include it in the labels,
in the feedback as y.
Sanity check, the first 10 values
of y is no recurrence recurrence.
We could easily convert this to
01 using categorical conversion.
It's not necessary.
Random forest classifier from
scikit learn you'll be
able to use in this manner,
80 percent chain tests,
every time I run this,
it will create a new evaluation measures,
and let's demonstrate that.
You see every time it changes.
Run it10 times, these are the variations.
As low as 64, as high as 77.
That's why we are doing
10-fold cross-validation
to collect statistics.
Run 100 times, collect statistics.
Here's the accuracy.
It also makes sense to
display the standard deviation of course.
Here I used
percent percent time in this cell,
it has to be at the beginning of
the cell to show
how much for my case it took.
This number, 26 seconds might be much
longer in your setup
depending on your computation power.
Here, my random forest
uses four jobs in parallel.
I could increase this to eight or more.
Number of primitive estimators
for random forests is 200.
You can play with these parameters,
it will affect
the performance of the classifier.
These parameters n estimators, max_depth,
if you use a default one
or some ballpark number,
it would be okay because random
forest classifier's very robust.
However, we can also hyperparameter
tune this using your validation dataset.
In this case, we don't have
a validation dataset.
So we just kept like this.
Random state means every time,
the randomness of
the random forest classifier
will be taken by a random seat.
If I fix this to 42 for example,
every time I run it in
the 80 percent split for
example if I set this to 33,
I have to run the cell of
course now because I have a new classifier,
and what's your guess?
Every time it will generate
the exact same result.
Because I've fixed the randomness
of the random forest,
I also fix the experimentation,
states are constant,
42 and 32 or whatever that corresponds to,
42 and 33, and this number 77 keeps same.
I want to change this to none again,
and of course I have to run this.
It doesn't pick up automatically,
the RF train test.
My changes won't be picked up automatically.
Run 100 times collects statistics,
we said, leave one out testing.
It's not terribly important this,
just for demonstration purposes.
This is important, 10 fold cross-validation.
This is more important,
stratified 10 fold cross-validation.
So in my case it's 73,
and of course this will change
if I keep the randomness.
In the next module, we will look
at the data transformation.

Now that we've looked at the data formats,
discretization and coding,
and then using a classifier
and looking at the performance.
Now let's look at data transformation.
Depending on the machine
learning pipeline we're
using or machine learning algorithm
we decide to use.
We may need to transform
the features into other things.
E.g. imagine a case
where the ground truth is not available.
So a supervised learning is not possible.
And then we want to do some clustering to see
some patterns just to see if there is
a direct relation between certain features,
such as menopause and
the recurrence of the cancer.
Here we're using matplot lips
3D plot to see information about age,
tumor size, inverted nodes, and recurrence.
Recurrence is the color.
This is our data.
As we read.
Realize I copied df dataframe
into the F2 because as you know,
all the variables on this notebook is
shared as global variables, df.
If I break the F here in this cell,
if I go back,
it will be a broken df until I reload it.
So here I just copied it.
And this is a shallow copy.
Depending on the situation,
you may need a deep copy.
Still, I'm converting every feature,
feature to number.
Like I said before,
certain algorithms
require numerical features.
Certain algorithms require nominal features.
For a clustering algorithm,
we generally require
numerical features because
the clustering is done
based on a distance measure.
In general, we can also use
some similarity measures
like set similarity, e.g.
or in some cases,
we can also use frequency distribution or
probabilistic distributions for similarities.
Those approaches are rare.
As we will see in the following modules,
most clustering algorithms,
the most popular or
most mostly use clustering algorithms.
They use numerical features.
Now let's see what the cell is doing.
We are converting every feature two numbers.
If you remember some of
the categories were objects,
we are converting them to numerical.
If it's float or integer,
we're leaving them as they are.
In general, if you convert everything to
float, that's even better.
As opposed to keeping
some variables as integer.
In this case, the plot 3D.
And okay, Well it's a blob, right?
Everything is clumped in zero hundred,
zero hundred zero to 100.
And it's not a very good dynamic range.
It's all over.
Now, if you use k-means and recall,
have the ground truth
actually the recurrence.
So training is everything but the recurrence.
Testing or ground-truth is
the recurrence that we
will measure the clustering here.
Well, clustering is 0.49.
It's not a very good value since we
only have two classes
and the random choice would be 1/2.
Now, we can normalize
and standardize the features
so that we can spherically
map the data points to these ranges.
Diminishing certain features, effects,
increasing or making the features
at the same level.
Normalization is scaling or mapping
the values of a particular feature
to the 01 range.
And it is defined by this maximum max,
minimum x, divide by that,
so that everything will be 0-1.
And then shifting by the minimum.
If you apply this function
to every feature value,
will end up with
a scale with a normalized feature.
Standardization is also another approach.
It maps everything to zero
mean one standard deviation distribution.
Sometimes this is good,
especially if you use
a probabilistic approach
like Naive Bayes, e.g.
standardizing every feature for
Naive Bayes is a good approach.
Normalization makes the optimization surface.
And what is that optimization
service surface?
Well, whatever algorithm we apply,
supervised unsupervised clustering,
SVM or any other.
Generally an optimization is involved.
Well, if that surface is spherical,
our optimizer will work better.
Now, we are scaling
using min-max scaling fit transform.
These three features, h tumor size,
emotional, as you see.
Now we have a more spread out,
equally distributed range of values.
Each feature power is
equal after the normalization.
A distance matrix in
n dimensions is given as this.
This is metric is
required for a clustering to work.
We take a single data point with
n features and
other data points with n features.
And looking at the Euclidean
distance between them.
That's the distance between
those two data points.
By minimizing the distances of data points,
we grouped them into clusters.
Let's normalized,
standardized and look at
the clustering error again.
While still it's high.
Still the error is
psi almost like random error,
but it doesn't matter.
It doesn't mean that we are clustering bad.
It just we cannot cluster.
That's all the ground-truth recurrent
01 does not map to the clusters.
So we cannot just easily to take the cancer.
That's a tough problem.
And recurrence or not recurrence,
information is
actually coming from other sources.
The patient dies. Unfortunately,
the cancer doesn't go away.
You can measure the cancer.
Thus, the data point has recurred.
However, when the cluster,
it doesn't show that easily.
Thus, we need a supervised learning.
Well, after the standardization,
as you see, this looks much better.
Recall,
the original information was like this,
is you realize, we're not injecting
or cutting out
any information from the features.
But these scales more
meaningful now we put the zero,
both zeros in the middle of this cluster.
Similarly, for each one of them,
we didn't have that in the previous dataset.
Our transformation in this manner
actually helps the clustering,
as we will see in the following modules.
And by the way, this example only
shows the three features,
h tumor size and inverted nodes.
Generally we have to scale
either normalized or
standardized every feature
on equal level.
So our clustering will work better.
This particular example doesn't
show the clustering nicely.
But remember, this was originally
a supervised learning approach.
And now we just took a different perspective.
Look at the features.
It was all over in this 3D plot.
But after normal, normalization
and standardization,
we made it more cluster like.
So it's spread on
different features are now on an equal scale.
And that scale is 010 to one.

>> [MUSIC] Data reduction does not
mean getting rid of data points.
Instead, it means getting
rid of some data features,
or in a more practical approach,
ranking the features: which feature,
which independent variable,
which measurements explains the knowledge
that I'm trying to reach?
That knowledge is captured in my model,
and which variable explains
most of that knowledge.
For example, in our previous videos,
we looked at breast cancer data
and did some supervised learning.
Our performance was around
75-77 percent accuracy.
It's a tough problem.
Now, which feature out of
those nine features explains
most of the recurrence or
non recurrence of the cancer.
We can use feature selection,
selectpercentile to find out
the particular feature or rank them.
This cell fits the data using x and y.
Recall x and y is our full dataset.
X has all the nine variables
and Y has the target variable,
which is the cancer recurred or not.
They're using NP log
minus selector probability values
and then dividing by maximum.
So this gives us
log probabilities of those scores.
Then we map them on the scale.
See that degree malignant, node-caps,
inverted-nodes gives the most
of the information about the model.
If they remove age, menopause,
breast-quad probably
out of these five variables,
removing these four, they
will test similar scores.
Well, one of the reasons
why we want to reduce
data is also improving the model,
getting rid of some unnecessary features
we may actually hinder the model.
Well, of course, maybe they
are helping, we don't know that.
However, if we can come up with
only a handful of variables,
we can show those variables to
the subject matter experts
and then ask their opinion.
I'm not an expert in
breast cancer prediction of course,
or evaluation,
but I'm guessing among all these,
the doctor might be first
looking at whatever that's node-caps,
inverted-nodes, or degree malignant are.
You can easily argue
degree malignant looks
like a derived variables.
Probably it gives most of the information.
The subject matter expert looks at
the cancer patient data and then says,
''This patient has a high
degree of malignancy.''
Well, to me, knowing nothing about cancer,
that gives some natural information
and I would say age wouldn't
matter because we can see cancer all over
and this particular dataset also shows that.
By the way, we are
not assessing anything about cancer.
It is just this dataset is this way.
Now, let's get to the off those
four and then evaluate our classifier again.
Well, it did not drop that much, 75 percent.
Recall this was at most 78 or so.
Now, we continue getting
rid of the menopause,
breast-quad and that's still
we're not losing that much information.
Depending on from run to run,
you may see a small improvement actually.
The question is asking,
even though these values
don't show them directly.
In a particular version of the Notebook,
this final run was a
bit higher than the previous one.
This one was perhaps
745 and this one was 750.
Thus, performance
accuracy increase if we bias it.
Do we accept the performance
increases if value increase?
What should be the guidelines that
a particular classification performs
higher than the performance
in another experiment.
These are two different experiments,
so are we going
to assess them as equal scores?
Is the second one better?
As can be seen in these cells,
I re-ran all notebook once more
and this particular cell gives me 747,
this particular cell gives me 750.
If you recall from
the previous discussion that
we had in this notebook,
randomness causes
the performance evaluation jump around,
even though we expect a neater,
a better results when
we use less information,
especially these very low helping features.
They might expect a performance increase,
but maybe that increase can be
considered as a variation of the errors.
Maybe these are equal.
There are some statistical studies
where the significance is assessed.
We can look at the confidence
value for each of
the statistic by running so many times.
As a guideline, when we
see a small increase like this,
I'm making an educated guess,
if it's less than five percent, three,
four percent, I would not
personally call it as an improvement.
If the data set is huge and if
I employ a good way
of collecting the statistics,
then I can assign confidence values,
confidence ranges in my statistics,
and I can say,
it is 750 with a 99 percent confidence.
There are statistical methods which
can result the evaluation like that.
Now, we completed the module, the notebook.
You can continue with the discussion.
Our first discussion question is,
researching and give one example
where data reduction actually does nothing,
maybe it also hinders.
Then the second discussion question is,
when do we consider
a performance evaluation increase,
such as inaccuracy as an increase,
as an actual improvements.
I gave you one example,
confidence values using statistics,
but then what else,
that's the discussion question [MUSIC].