None

>> Machine learning is the art of solving
your computation problem using
a computer without an explicit program.
In this first module,
we will see our first machine
learning pipeline to
develop a learning model,
and then to test
the model on never seen before data points.
Finally, we will see
how we evaluate this model.
The practical computation problem we are
solving by the use of
this learning module is recognizing
handwritten digits on snail mail envelopes,
to help Postal officers.
In our model, we will use
a support vector machine algorithm to
classify digit images taken
from the face-off letters.
We will mention
the basic performance measurements
metric, the accuracy.
Our entire pipeline will
be on a Jupyter notebook.
We will use a Jupyter notebook
in every lecture of this course.
[MUSIC]

>> [MUSIC] Let's look at
our first machine learning program.
We will use matplotlib,
which is a very popular and
very capable plotting library
in Python and we will
use matplotlib as inline.
The other possible option
for matplotlib is notebook,
where it displays the plot
as a separate widget as
opposed to inline as
we will use in this notebook.
We are importing scikit-learn.
Sk-learn is the shortcut for scikit-learn.
We will import datasets,
Support Vector Machine, and metrics.
First thing we are doing is loading our data.
Clearly, machine learning is
all about data and analytics.
So we need some data.
In order to ease teaching,
in order to have a quick start,
scikit-learn has many datasets built in.
The first dataset we will look
at is images of digits.
These digital images are
collected more than 20 years ago,
and these are actual handwritten digits.
In order to ease automation
of USPS zip codes sorting.
Now our feature engineering is
about getting the data and then
making into a matrix of
a dataset that will be
input to the machine learning program.
There can be two types of
variables at a minimum.
The first one is Numerical,
where each data value is a number.
It can be integer, it can be floating point,
or where the data values
are nominal or categorical.
There can be other data types as
we will see as we go along,
such as Boolean, text,
date, and so on.
As any one of us knows how to program
we representative variables
by declaring its type,
for example, in Java you have to declare
as integers or floating points,
or long or double.
Each one of them is represented
differently on the machine.
The type, the format of
the data is utmost
important in machine learning.
We have to represent the data right.
For example, these are digit images.
They are basically pixel colors.
Now how are we going to take
this and then make it into a dataset
so that the machine learning program can
really understand it and learn it,
or just learn it without understanding
as we will see in the following weeks?
Let's run this notebook from the very start.
It's a good practice to
start from a reset kernel.
So I will restart and clear the output.
It also resets the kernel.
Now everything gone,
and this is an actual notebook.
In the lecture content,
the HTML version of
this notebook is provided.
Let's run the first cell,
Shift Enter runs the cell.
It basically imports all the libraries.
Now let's load our data set.
We loaded our data set.
It's a very good practice to check
actually what you loaded. Let's do that.
Insert below and then enter digits.
So this is the data structure that
we loaded from that dataset.
As you see, it has
JSON like data structure,
but actually it's not.
It's basically a dictionary with
keys and with
additional data structures like array,
dictionary and other things.
I know this array is a Numpy array because
array is the name of
a regular array or a vector in numpy.
If it wasn't, then
it wouldn't write the object name
here or the class name here,
but it would be a square bracket.
Now I'm looking at
the digits because I
want to see what that data structure is.
What information do I have?
This is a standard information
for all the datasets in scikit-learn library.
So the data is array of
information and as you see,
it is a two-dimensional information.
How do I know?
Because of these two square brackets.
So this is one row,
this is the second row,
it goes like this.
So actually it's a matrix,
this data is a matrix,
the target is the target labels of
the data and it's
a single integer for all the rows.
In this data structure,
the data is represented as rows,
which are the individual data points,
and columns as features.
You can talk about the size of
the matrix, number of features,
how many you have M like in Mary,
that's the number of columns.
You have that many features.
How many data points you have?
How many instances that you
want to classify, you want to learn?
Is the number of rows,
say there are N, as in Nancy rows.
Now the target are
the labels because this data particularly is
labeled by experts so that we
can quickly use and
start our learning process.
How many should we have?
We have to have the target values
as many as the number of data points.
Not every time a target label
is an integer like here,
we might have names.
In this case, the name is
just an array of integers again,
but it doesn't have to be
in another data set,
these target names could be
some flower names, for example.
Now as you see,
the images are also stored in this data set.
We will not use this images
key for any data analytics.
It can be displayed on screen so that we can
associate - Oh this particular image
is classified as digit 5.
In order to display that
this image is provided in this dataset.
It was an optional case.
Now we have extra other
information description.
This description contains the source
of the dataset where it came from.
It's almost 20 years old,
and there are some publication
references for this data set.
Next, we will look at the classifier to
classify digits using this dataset.
[MUSIC]

[MUSIC]
>> Let's look at the number of
images in the training data set.
By looking at the length of
the images and labels that is
populated by the digits images and targets,
which is the actual label,
we see that there are 1,797 images.
Let's draw the first 40 data points.
In this case, each data point is an image.
Figure size is 20 by 10.
For index in image labeled tuple,
enumerate all the images and labels,
subplot each one of them and then
turn the axis off and then show the image.
Plot image show takes the image as a matrix,
which is captured here from the images and
labels and that shows it as an image.
It's color map is
gray labels and interpolation is nearest.
The title is training for each of the plot.
So there are basically
4 by 10 subplots in this figure,
and each one of them is a title
as training the actual label.
As you see, the data is presented to us,
labels changing from zero to
nine for every image in order.
So somebody picked
these images, labeled them,
and then entered into
the data set one by one in order.
As we will see in the following weeks,
the order of the data set for training is
very important because most of the times,
the learning algorithms
are not fully deterministic.
For example, in Random Forest algorithm,
so the order of the data effects
the model output every time,
the more random data input order is required.
Now let's see how the image
looks like as the image and the labels.
As you see, this is
the first data point which is a matrix.
How do I know? Again, row
h rows this is a matrix.
The last element, is the label
that is associated to this data point.
This data point can be used
as a matrix like this,
or it can be vectorized into
a 1-64 dimensional vector,
and this is the second data point.
It is a very good practice
to look at the data
points as we ingest the data.
Now let check the image,
and then examine the indices,
you see each size is eight,
meaning there are eight many rows
and then eight many values in every row.
This check is important
because if we make a mistake in the data
ingest that mistake will be carried over.
Those errors will be carried over
to the model because nobody in
this pipeline will tell us we
have a mistake in the pipeline, correct.
It is not like program compiling.
We have to avoid errors with
some good practice and checking
the output at every level
once we ingest the data into our pipeline,
then the next step is pre-processing.
Every data mining, machine learning,
data science book will tell you,
your model is as good as your input data.
It will also tell you 90 percent of
the effort and 90
there is a very subjective number.
You can call 70, I can call 95,
that much efforts will go into
the pre-processing of the data set.
The utmost important characteristic of
the developed model is
its generalization ability.
We do not want to fit
our model into the training data set.
We do not want every little detail,
every little wrinkle in
our data set, effect our model.
We want general models so
that we want our model to
be effected by the generality
of the input data set,
not by its outliers or exceptions.
As we go along in this course,
we will see how we can improve
the generalization ability
of a learning model.
One of the pitfalls,
very common pitfalls in
data science, machine learning is,
it's very easy to trick ourselves about
the model performance
by committing data errors,
mistakes which I just
mentioned during our preparation of the data,
any kind of error will be
reflected in the model output.
We will never know those errors
until a new data point never seen before,
unpredicted data point is seen,
which can easily throw
our model because it wasn't general enough,
because we made data errors
in the generalization,
in the training of the model.
A few examples of
stages in pre-processing the data set is,
correcting the errors,
correcting the number formats, for example,
correcting erroneously input values,
for example something like February 21 or
2,119 as the year,
or some semantic errors like
a person having a PhD degree
at a very young age.
We can also improve our data set or
improve the data set
for certain machine learning
algorithms by imputing
missing values for model generation.
Now let's see how we flatten our images.
Meaning take eight by eight matrices
and make it into a vector of
1 by 64 so that we can
input that information in
a machine learning algorithm.
We run the cell,
we look at the size of the output matrix.
This is a matrix,
data is a matrix,
each row is a data point.
We have 1,797 rows,
which is the number of
images in the data set,
and we have 64 columns,
which is the number of features.
As you can imagine,
each feature from zero to 63 or 1-64 in
matrix indices will correspond
to one of the pixels in
the eight by eight images.

>> [MUSIC] Support vector machines are
very popular and once
upon a time considered the
best machine learning algorithms.
Support vector machines were
invented after artificial neural networks,
and they were so popular because
support vector machines can
be trained much faster.
The algorithm complex the big-O n_2
opposed to the n_3
for artificial neural network algorithms.
They are very fast to train and
their generalization ability even
surpasses the artificial neural networks.
This list I'm leaving to
the readers to go and read
a comparison between Support Vector Machines
and the artificial neural networks.
These are both numerical algorithms.
They approach the machine learning problem
from different angles.
Support Vector Machine looks
for a discriminating plane,
whereas artificial neural networks
minimize an error,
the error between the input values
and the output values,
ANNs are function approximators,
support vector machines optimize
their approach reducing marginal risk.
Now let's run our support vector classifier.
First, define the SDM classifier with
a radial basis function with Gamma 0.001,
and then fit to data,
and then look at the
expected and the predicted information.
Let's create another cell
and see what the values are.
The expected values are
coming from the actual dataset.
In Python, slash slash
two is an integer division.
It will always result in an integer.
Half of the data is used for training.
The other half is used for testing.
As you see it
a Python slice all the data sets up
to half of it is used for
fitting column and samples over two.
The other half from N samples divide
by two to the end is used for testing.
Let's look what predicted contains.
How many data points there should
be in the expected N predicting?
It should be n samples 1797 divided by 2.
How do we measure
the performance of the classifier?
Before this, let me delete this cell,
which just cut so that it will
not clutter our screen.
How do we measure the performance?
The basic measurement is accuracy,
number of correct predictions
divided by number of total predictions.
There are many other metrics
which will be covered in the following weeks.
When there are 10 classes,
the best metric is a confusion matrix
where each column shows
the predicted class and
each row shows the actual class.
Luckily,
scikit-learn has all these functionalities
to display the confusion metrics properly.
Now that we trained our classifier and
even tested with half of the remaining data.
Let's look at what the performance is.
This is the report of the classification.
It's for all the 10 classes,
it reports precision recall,
F1 score, support, accuracy,
macro average, and weighted average.
We will cover all these metrics
in detail in the following weeks.
Now let's look at
the actual confusion matrix.
This was the report for each class.
Class 0, for example,
succeeded with a 100 percent accuracy
because its precision is one.
It's never missed anything.
But some other classes are mixed
up for zero because recall this is 0.99.
This is the confusion matrix.
As you see, the diagonal elements are
the actual class predicted matching.
The confusion matrix columns are
the predicted values or predicted labels,
and the rows are the actual
independent variables or labels.
For example, take 0,
1, 2, 3, 4 digit 4.
For digit 4, one percent
of the data points which
actually belong to digit
zero are classified as digit 4,
88 percent of the digit
4's are classified as digit 4,
and no other classes came into the digit 4.
However, when you look at
the row of digits 4,
some of these classes
which belong actually to
digit 4 are confused with digits 9,
4 percent of the actual digit 4's are
mixed up or predicted as digit 9's.
If you can imagine
the shape of the digit 4 like this,
actually, it is very close to digit 9.
Similarly, digit 9 is also
confused by digit 0,
1, 2, 3, 4, 5 and 3.
Confusion Matrix shows how
the class mixed up against.
There's also other useful information,
visually checking what is predicted,
which the ground should belong to what,
and what mix ups have been made,
and of course, this
is just random selections.
For example, in this case, Prediction was 8,
Ground Truth was 8.
It's doing a good job, right?
I mean, it's hard to visually even
predict this image as eight.
Prediction 8, Ground Truth 8,
Prediction 4, Ground Truth 4, Prediction 9,
Ground Truth 9, we can check
some other predictions and
ground truth comparison, visual comparison.
We will changing index to 20 to 24.
But be careful, because this index is used
in expected and it
is coming from this enumeration.
We have to add an offset
of 20 in order to match up.
So I'm adding that.
Now these are all correct.
So I'm looking for
examples where there's a mispredictions.
So 30 to 34 at 30.
I found one, Prediction
was 9, Ground Truth 5.
So it was predicted as nine
because of these great Pete cells.
But if you ask this to a person,
he, she would say this is five.
Well, suffice it to
say this deep learners has to be
trained more or should be
built as a better artificial neural network.
Things can be improved. By the way,
note that this was
a heart classification problem in
the first place because it was
50 percent training and 50 percent testing.
It is always difficult
with only half of the data
being used for training
and the other half for testing.
This concludes classification and evaluation.
In the following weeks,
we will see matrixs,
we will see data pre-processing,
and we will see different classification
and clustering problems.
[MUSIC]