import re
from nltk.util import ngrams, pad_sequence, everygrams
from nltk.tokenize import word_tokenize
from nltk.lm import MLE, WittenBellInterpolated
import numpy as np
import plotly.graph_objects as go
from scipy.ndimage import gaussian_filter

# Training data file
train_data_file = "Artificial Intelligence (A.I.) is a multidisciplinary field whose goal is to automate activities that presently require human intelligence. Recent successes in A.I. include computerized medical diagnosticians and systems that automatically customize hardware to particular user requirements. The major problem areas addressed in A.I. can be summarized as Perception, Manipulation, Reasoning, Communication, and Learning. Perception is concerned with building models of the physical world from sensory input (visual, audio, etc.). Manipulation is concerned with articulating appendages (e.g., mechanical arms, locomotion devices) in order to effect a desired state in the physical world. Reasoning is concerned with higher level cognitive functions such as planning, drawing inferential conclusions from a world model, diagnosing, designing, etc. Communication treats the problem understanding and conveying information through the use of language. Finally, Learning treats the problem of automatically improving system performance over time based on the system's experience. Many important technical concepts have arisen from A.I. that unify these diverse problem areas and that form the foundation of the scientific discipline. Generally, A.I. systems function based on a Knowledge Base of facts and rules that characterize the system's domain of proficiency. The elements of a Knowledge Base consist of independently valid (or at least plausible) chunks of information. The system must automatically organize and utilize this information to solve the specific problems that it encounters. This organization process can be generally characterized as a Search directed toward specific goals. The search is made complex because of the need to determine the relevance of information and because of the frequent occurence of uncertain and ambiguous data. Heuristics provide the A.I. system with a mechanism for focusing its attention and controlling its searching processes."

# read training data
with open(train_data_file) as f:
    train_text = f.read().lower()

# apply preprocessing (remove text inside square and curly brackets and rem punc)
train_text = re.sub(r"\[.*\]|\{.*\}", "", train_text)
train_text = re.sub(r'[^\w\s]', "", train_text)

# set ngram number
n = 4

# pad the text and tokenize
training_data = list(pad_sequence(word_tokenize(train_text), n, 
                                  pad_left=True, 
                                  left_pad_symbol="<s>"))

# generate ngrams
ngrams = list(everygrams(training_data, max_len=n))
print("Number of ngrams:", len(ngrams))

# build ngram language models
model = WittenBellInterpolated(n)
model.fit([ngrams], vocabulary_text=training_data)
print(model.vocab)

# testing data file
test_data_file = "Artificial intelligence (AI) refers to information about the language structure that is being transmitted to the machine.It should result in a more instinctual and faster solution, based on a learning algorithm that repeats patterns in new data. Good results are obtained in emulating the cognitive process whose several layers of densely connected biological subsystems are invariant to many input transformations. This invariant so hunted after by AI and cognitive computing is in the universal structure of language, the provider of the universal language algorithm. The representation property to improve machine learning (ML) generalizes the execution of a set of underlying variation factors that must be described in the form of other straightforward underlying variation factors, preventing the “curse of dimensionality.” The universal model specifies a generalized function in the universal algorithm, serving as a framework for the algorithm to be applied in a specific circumstance or area.Artificial intelligence (AI) enables machines to extract, integrate, exchange, and analyze large heterogeneous datasets to answer complex problems in a timely manner. The promise of AI in healthcare and medicine has been adopted by many computer scientists, clinicians, and policymakers.AI collects and examines datasets, to help identify, predict, and study the origins, applicability, or qualities of data needed for processing. AI plays a significant role in health care data. It provides new and improved analytics. AI analytics are of use in the detection, diagnosis, and treatment of many diseases. In health care, it is helping to provide more targeted care for patients fighting medical conditions or issues.This is not the end of AI; it has a lot of domains to be induced in the future. But the most important thing that we need to remember is that the more prevalence it gives to us the more exigency it causes later in the future."

# Read testing data
with open(test_data_file) as f:
    test_text = f.read().lower()
test_text = re.sub(r'[^\w\s]', "", test_text)

# Tokenize and pad the text
testing_data = list(pad_sequence(word_tokenize(test_text), n, 
                                 pad_left=True,
                                 left_pad_symbol="<s>"))
print("Length of test data:", len(testing_data))

# assign scores
scores = []
for i, item in enumerate(testing_data[n-1:]):
    s = model.score(item, testing_data[i:i+n-1])
    scores.append(s)

scores_np = np.array(scores)

# set width and height
width = 8
height = np.ceil(len(testing_data)/width).astype("int32")
print("Width, Height:", width, ",", height)

# copy scores to rectangular blank array
a = np.zeros(width*height)
a[:len(scores_np)] = scores_np
diff = len(a) - len(scores_np)

# apply gaussian smoothing for aesthetics
a = gaussian_filter(a, sigma=1.0)

# reshape to fit rectangle
a = a.reshape(-1, width)

# format labels
labels = [" ".join(testing_data[i:i+width]) for i in range(n-1, len(testing_data), width)]
labels_individual = [x.split() for x in labels]
labels_individual[-1] += [""]*diff
labels = [f"{x:60.60}" for x in labels]

# create heatmap
fig = go.Figure(data=go.Heatmap(
                z=a, x0=0, dx=1,
                y=labels, zmin=0, zmax=1,
                customdata=labels_individual,
                hovertemplate='%{customdata} <br><b>Score:%{z:.3f}<extra></extra>',
                colorscale="burg"))
fig.update_layout({"height":height*28, "width":1000, "font":{"family":"Courier New"}})
fig['layout']['yaxis']['autorange'] = "reversed"
fig.show()