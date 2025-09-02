>> [MUSIC] The core of
the machine learning methodology is
the data that is to be learned from.
If the data is right,
then we generally do not need
a sophisticated or an
excessively complex algorithm or a model.
The characteristic of
a dataset can be analyzed
and understood by inspecting
and exploring its features,
or its independent variables.
In this module, we will
list the properties of data features,
their types, and the initial steps
of preparing the datasets
for a learning pipeline.
You will now look at
reputable online data sources that can
be used for practicing
machine learning pipelines.
Finally, we will be introduced to and employ
the Weka machine learning framework to ingest
the data file to build
our first ensemble learner,
which will be around
the first model and measure
its model performance [MUSIC].

>> [MUSIC] Dear students, in this module,
we will look at the data features.
Recall that machine learning is solving
a computation problem using
a program without an explicit program.
Data clearly is the core of machine learning.
The data is captured through
some process which might
be independent of our model development,
but we need it for any kind of data analytics,
pattern discovery or generation
of a model for some prediction problem.
For example, in the last module,
we looked at handwritten digits images for
detection of digits automatically
to help postal workers.
Now, when it comes to machine learning,
the representation of the data,
the features of the data,
and the relevancy of the data
are of utmost importance.
We will set a particular standard
for data representation,
and that is this X matrix,
which is the collection of our data points.
This X matrix dimensions are N by M,
where N is the number
of data points in this example,
from one to five data points,
and M is the number of columns.
In this example, three
corresponds to the features of the data.
Our dependent variable is stored in y.
We do not keep the dependent variable
in the X matrix
because in a classification problem
we are going to predict them.
So we keep all the data
which are independent features in X matrix,
and keep our labels or dependent variables,
dependent variable in this case
in the y column vector.
When it comes to data,
we can talk about certain types, numerical,
nominal, binary, strings, dates,
and some more complicated features.
Our data representation on
the computer is the machine representation.
It can be integers, floating points,
for example, 32-bit floating-point,
64-bit floating point, or
text as sequence of characters.
In Java, for example,
it corresponds to string.
Numerical, can be
integers or floating points,
Z or R. It is safe to convert
all numerical variables to
floating point variables.
Sometimes this is also processed
faster because of the GPUs.
We can keep the nominals as
a set of levels drawn from
an alphabet and again even though
the corresponding nominal variable
can be a long string,
for example, something like hot weather,
called weather, warm weather.
We can represent them as integers 0, 1,
2 and there will be a lookup table which will
correspond to hot weather to value 0,
warm weather to value 1,
and cold weather to value 2.
In some cases, we may need to convert
nominal to numerical and numerical nominal,
because there are a variety of
algorithms when it comes to machine learning.
Some of these algorithms work very
well with numerical features,
and some of them work very
well with nominal features.
As a guideline,
probability based approaches,
frequency-based, entropy-based approaches.
They like nominal variables
because we count them.
The other side of
the coin where the machine learning
algorithms like numerical variables
are distance-based or cost-based approaches,
such as support vector machines,
k-means clustering,
neural networks where a function
is fitted to the data.
One-hot encoding is necessary when we need
a nominal variable to be
converted to numerical variable.
If the nominal variable
takes L different levels then,
we will create L binary variables
for each of those level.
If the number of levels and nominal
variable requires is a 1000,
that means a 1000
different features are generated
and this is also
a waste of space understandably.
However, that's the most
straightforward and safe approach.
When it comes to
nominal two numerical conversion,
we will use one-hot encoding.
Numerical to nominal conversion,
as we will see,
involves histograms,
binning and bin boundaries.
Basically for the range of
that particular numerical variable,
say minus 100 to plus 100.
We will decide on
a number of bins, for example,
20 and then equally
map the numerical values to
those 20 bins and then represent
the variable with those 20 levels.
Then we can one-hot encode
those variables back to the numerical realm.
All these conversions help
the algorithms and if you do not
do these conversions ourselves,
the algorithms in their black-box programs
will do them automatically.
We will look at the online data sources in
another module where we will download,
we will visit these web pages
and then download the data sets.
An important note about all these,
when a physical data set file
is shared among teams,
that physical dataset file has to
be exactly the same with every little detail.
And also for repeatability,
a script must be saved
where the raw data is used to generate
the actual experimentation physical data
file using that script.
Multiple rounds of that script
should generate the exact same data file.
The relation between the independent
variable and the dependent
variable is important.
Machine learning model will
be built upon this relation.
One of the metrics,
Pearson correlation coefficient,
gives a measure of correlation
between variable data points.
Imagine X is an independent variable
and Y is the dependent variable.
Multiplication of each point and
the summation would give a positive value or
a negative value of one normalized by
two standard deviations is
a proper metric to
measure the correlation between variables.
Then we rank variables,
generally the independent variable
that carries the highest correlation to
the dependent variable is
generally ranked higher [MUSIC].

>> Let's discuss online datasets sources.
As our approach to machine learning
is data-driven, any available data for
our educational purposes is valuable to us.
>> There are many online datasets sources.
Three important ones are
these UCI KDD online repository,
Kaggle, and KD nuggets.
Let's start from the back.
Let's look at KD nuggets.
KD nuggets is a web page where
there is more than just data.
As you see on the menu;
software, news, top stories,
opinions, tutorials, jobs,
companies courses, data-sets, education.
When it comes to applied
machine learning, data mining,
or AI, this web page
provides a lot of information.
You will not get a particular data
from this repository.
So let's go back to our module.
Now, let's look at UCI KDD website.
UCI KDD website is relatively old but
still a well-known and
frequently used web page.
We will download a particular
dataset from here.
Let's look at by data type,
and let's get the multivariate data
of 1990 US Consensus data.
This is the data web page.
If we click on this dataset,
as you see you are not seeing it.
But if you go to this website,
you will see at the bottom,
this link is a data files in texts extension.
Now, let's download this,
with save link as,
I will download it here,
I will change the extension to
CSV because it's comma-separated file.
In fact, let's look at what it has.
Now, I will go to that downloads directory,
I downloaded the data from
and pull the file inside my editor.
This is not that plus plus,
you can use any editor.
This file is pretty big,
it's around 350 megabytes,
so your editor must be capable
of handling such big data files.
As you see the first line is header,
it's comma-separated,
meaning every individual value
is separated by a comma.
The first line carries
the names of the column names.
However, many columns here,
the data-points, continue similarly.
So how many data-points do we have?
I went to the last line and
it is around 2,458,285.
So that's the number of
data-points I have in this dataset.
As you see, the first one is case ID,
the second one is DH.
It goes like that.
Now we will save this file in
CSV extension and then we will
load it to Jupyter notebook later.
Now let's download the other two files.
This time I will go to the Kaggle web page.
Kaggle is a very
accomplished web page with many,
many datasets,
well-curated host competitions.
To be able to login to Kaggle,
you need a e-mail address.
Make sure that your e-mail address is
a disposable e-mail address
if you like of course.
In Kaggle web-page, we will
download graduate admissions data.
The easiest way is, searching that data.
The dataset we are looking for
is under the third one,
"Graduate admissions." How do I know?
It's just I picked
this particular one and
there are actually two versions of it.
Admission Predict's version
1.1 and Admission Predict.
We will download the Admission Predict,
and probably by the time you check
this module in
the following months and years,
there might be 1.2, 1.3
Admission Predict's versions.
We, will, download the data
from this web page.
As you see, there is also a notebook,
looking at the data.
You can also follow what
the other hosts of this data is doing.
We will just get the data
and use it for our purposes.
I will click this and now it is
downloaded in my downloads directory.
It's size is 13 kilobytes
and its contents is like this.
serial no GRE score,
chance of admit, it's a numerical variable.
It goes like that. There are
400 data-points in this dataset.
Now we will look at the third dataset.
The name of this dataset
is "Human freedom index."
Human freedom, here,
and it's called hfi_cc_2018.
I will click on the data.
As you see, you can also explore
the data using Kaggle resources.
Download okay.
It's downloaded by my browse search
in a zip file.
I will open the zip and copy
to my dataset's directory.
For your information,
here's the content of the data.
So this is the again,
the header it's CSV and it goes like that.
My editor shows line by line.
This blue is a single line.
The last column is called HF quartile.
First is year, second is ISO_code,
and as you can guess,
HF is human freedom.
So if you're interested in
the score that is the third one.
This particular one has 7.56 and so.
Now, we downloaded the data.
Let's go back to the Jupyter notebook.
I will run these cell where I use
pandas and load the CSV,
and then I will check
the number of rows and number of columns,
meaning number of data-points
and number of features.
I will look at
the first few lines of my dataset.
That's df.head, df is for data-frame.
It's pandas class to keep,
to carry the data points.
Df is a matrix, but of course,
in memory it's
data structure is completely different.
But for our purposes,
we are not interested in that.
We can take this and then
convert into a numpy matrix.
In the following modules,
we will see how that's done.
Now as you see,
this information is similar to
the information member looked at
the data in the Notepads.
Here it's much well organized.
The first one is caseid, dage,
and all those and last one is the DYRR.
It goes like that.
This particular display has
five rows and 69 columns.
Now, the second dataset
was Admission_Predict from Kaggle.
Let's load that again.
If you notice, I just run this cell,
but of course you will see the results
that was previously run
and it's exactly the same,
unless I have a bug of course.
It has 400 rows,
nine columns including
the dependent variables, Chance of Admit.
When we use this data as an X matrix,
we will remove this column.
As you see, pandas data-frame also
has its own serial number,
serial Id, it is like an index.
Let's run the third one.
This was the human freedom index.
Again, download it from Kaggle.
The reason I chose
these particular datasets are
because they were interesting. Maybe to me.
This is Admission Prediction is GRE score,
TOEFL score and then Chance
of Admit to colleges.
The human freedom index has
123 different columns that
carry information about a lot of things.
The number of points is 1,458.
We will use this dataset
in Weka environments.
We will continue examining
the dataset and then
generate a few classifiers in
Weka framework in the next video.

>> [MUSIC] Let's take a look
at the Weka framework.
The first thing we will do is,
in a command prompt,
check the version of the Java
development environment we downloaded.
Make sure you install the 64-bit version of
Java because as you
can imagine in machine learning,
the data size might be very,
very big and if you have
only 32-bit system on Java,
you will be limited to
two gigabytes of memory,
and generally today's computers
come with much more memory than that.
Let's go to the command prompt and
I've already run it, java -version.
So my version is 1.8.0_
231 and a 64-bit server.
This is what I want to see.
Then, I've already
downloaded the Linux distribution.
I will just run Weka directly.
Now Weka is coming up.
It tells me this because there
is a package manager which can download many,
many other libraries,
programs that Weka keeps.
So I'm leaving it to you to
explore the features of Weka like this.
This is Weka's main
Graphical User Interface chooser.
For our purposes today,
we will use the explorer.
Let's open the explorer and now as you see,
it's ready to go.
I will open a file directly.
My files are under DEP,
my lecture data sets,
and I will import
CSV because I downloaded this before.
The first thing I'll download is
Human Freedom Index not
cleaned because this is
the version that I downloaded directly,
and let's see if we can open it or not.
It failed. You see,
we were able to open this by pandas,
but Weka doesn't like it and
there's a reason why it doesn't.
Let's okay and then let's move on,
and let's open the file to
see what the problem is. There you go.
Now, the reason there's a problem is
entries like this because
this is nominal clearly.
Weka doesn't understand this
is nominal because in the header,
it doesn't say this is nominal.
Weka wants to see
quotes in the name of the variable.
Following the instruction in the notebook,
we will add single quotes around
the name region in
the header and here is the region.
I am adding this and then I'm saving this
as clean save going back to the Weka,
and then I'm opening clean problem again.
We will follow the other modification by
changing this Ivoire to this,
removing the single quote.
By adding quotes around the region,
we specified
this particular variable as nominal.
Weka will understand this,
but then the quote is somewhere else.
Let's search the quote.
You see because of this quote,
Weka in the opening up this file has problem.
I just delete this quote, that's it.
Let's see if there's another one.
There's another one.
Let's see, third one.
This was third one,
fourth one, fifth. That's all.
Now, I will save this again.
Now let's see if Weka can open it now.
You see, unfortunately, we have to
understand what Weka wants
to see in the data file.
This particular data file is
the human freedom index and Weka
is an excellent tool to show
all this information and as you see,
it's creating histogram by
showing metadata about the data.
This particular one even though it's numeric,
it can show that as nine distinct values,
minimum 2008, maximum 2016.
It goes like that.
I'm moving variable by
variable and now showing the histograms here.
So I invite you to do the same thing
and explore the data, understand the data.
Now, we will leave this data at this point.
The purpose of this demonstration was,
even though we download
the data from Kaggle, it's clean.
The quotes they were not
suitable to be opened
up by the Weka immediate.
We know this by experience.
So we open an editor,
made sure the quotes match
what Weka would would like to see,
and then Weka was able to
open the CSV file directly.
Now, we're ready to
machine learn with this data.
However, we will continue
our Weka demonstration
with another data file.
We will open the graduate admission
datasets with
Weka and then apply
some filters and develop some classifiers.
Let's see how this goes.
So back to this,
we'll open another file Admission_predict
which we downloaded from Kaggle.
It's able to open it directly because
that CSV file doesn't have
any problems that Weka wouldn't like.
As you see, there are
400 instances, meaning data points.
Its name is Admission_Predict
pulled from the file name.
There are nine attributes.
Weka calls features as
attributes and these are the features;
serial number, GRE score,
TOEFL score, university rating.
These are histograms, basically
counts of particular values.
Sometimes they are natural bins
like in this GRE score,
sometimes we have to bin it ourselves.
Research has only two distinct values,
zero or one.
Chance of admit, it is numerical.
There are 60 different values.
It doesn't mean that it's nominal,
it's just 60 different values,
and then a histogram is built.
So now let's process this further.
First thing we have to do is
create a variable which
is nominal so that
this file can be used for classification.
At this point, we can only do
some regression because the chance of admit,
which is the interesting variable that
we want to predict,
is numerical and takes
values between 0.24-0.97.
These are probabilities between zero and one.
We want to convert all these to nominal.
I suggest using 0.9 which is around
somewhere here as will be
admitted and the rest
as will not be admitted.
So let's see how we do it.
We will go to filter and
we will use AddExpression.
As you see there are lots
of different filters.
We'll use add expression and then we
will answer these arguments here.
So this will be my expression.
It is unfortunately Weka's format
and we have to look up
each time for a particular filter
how it would be applied.
If else, A9,
which is that particular
column chance of admit,
is greater than 0.9.
If yes, then it will be created as
one or the value will be set to zero.
I will click on Edit configuration
and then copy paste what I
copied from the -E for expression
''Ifelse A9>0.9" goes like that,
it is not complete of course.
This corresponds to the expression
that we provide in the Jupiter notebook,
and then we'll press Apply.
You see it created a new column,
admit and then it assigns most of
the values a zero
because they were less than 0.9,
and some of the values as one.
Now, we have to convert this
to nominal because it's still numeric.
You see, it's still numeric.
We will apply another filter.
So we will pick numeric to nominal and down,
we will use dash are last edit configuration.
We will just use
the last variable to convert to nominal.
We could give a range
so that it would convert
to multiple variables at the same time.
Remember a variable,
a feature or an attribute,
a column, all of them are same,
and independent variable, they
all correspond to the same entity.
Apply, suddenly changed. You see,
now it's nominal and Weka shows
wherever that nominal label
is zero in the data as well.
Now I can say
that by looking at the GRE score,
actually I can draw
a pattern that the chance of admit goes up.
TOEFL score similar,
universe rating, SOP, LOR,
CGPA and all the research chance
of if you have not done research,
there's a good chance you
will not be admitted.
Chance of admit, here is the balance.
We can call this particular dataset
on balance because we have
many zeros as not
admitted and very few ones as admitted.
We will just change the name from 0,
1 to yes and no.
Rename nominal values.
This is only to help us
see the variable's values nicely.
Again, the last variables
and it is like a dictionary,
zero as no and then one as yes.
Then apply.
Now, admit is no and yes,
it's a truly nominal variable now,
and then everything remains same except for
the information as data
is now labeled as yes and no.
I would suggest exporting by saving
in our format and then
seeing this particular change,
seeing what changes we made.
But I will not do that.
Now, according to the instructions,
we will classify with it all these steps,
pre-processing is done, and then we will go
classification section and we will
do a tenfold cross-validation.
Let's see what's happening.
Classify tab, choose trees,
RandomForest,
which is a popular classification.
It is only the set cross validation to 10,
and then I will just start.
It automatically picks the last variable
as the dependent variable,
which is nominal admit start.
It did run 10 times
and then it accumulated all the results.
Now, why it's 100 percent classification,
everything's correct with its super.
Let's go back to the instructions.
It asks you why it's 100 percent.
It is 100 person because
we have a biased model.
Even though in our dataset,
admit is used as dependent variable,
we have chance of admit,
which is directly correlated to
the admit and it's in your data,
your model has it,
we have to remove it.
We are not evaluating the modal rights,
they will just remove chance of admits.
Now, look a serial number from 1-400.
This is different for every data point.
I bet this is completely useless.
To prove it, let's go to
classify again. Let's start.
Now it's 97 percent.
It makes more sense.
It did some error. Our data is good enough.
We can have very high accuracy,
but it's not like
a skewed biased data
so that we will have 100 percent.
I would be very suspicious if I
see an accuracy of 100 percent.
Now let's go back and remove serial number.
I'm claiming nothing will change here,
all the results will be same.
By the way, I can click on these
two to see the previous results
and the current results.
So I will be able to compare after
I change the data
when I run the classification again.
I pick the serial, no, remove it,
and now I have
seven variables and
the dependent variable, admit.
I classify, it went down right from 97-96.5.
But maybe it's only random error,
maybe the era of the variation
is large enough
to cover from, let's say 94-99.
Then are run again, run again,
run again, run again, run again.
Well, it looks like some
of those serial numbers were
fitted in the data so
that it was helping
the classifier to determine.
There's a good chance the classifier found
out which surreal numbers we're
actually having the yes admitted answer.
Now, let's try to
answer what the module was asking.
First of all, it
was 100 percent before because we were
using a variable which
we were not supposed to use.
Second, you remove the serial number,
it went down, yes,
but the serial number was
a unique value for every data point.
Probably, the random forest was finding
out which serial numbers
were receiving the yes.
We have to remove serial number,
it will not help us.
It's a unique value for
every data point we have.
That's why the random
forest model performance
is less than 100 percent now,
but this is not a bad thing.
This concludes our module.