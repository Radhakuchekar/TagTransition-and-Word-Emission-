# Tag Transition and Word Emission

I have implemented Bigram, Trigram, 4-gram, 5-gram model.
Training data set is Hindi labels corpus named Hindi-tagged18.txt file. Code is capable to calculate **bigrams, trigrams, 4-grams, 5-grams** and store then in the file and calculate the perplexity of the given sentences. The input
data to calculate the perplexity have to be labeled data.

#### TTP (Tag transition probabilities):
Tag-Transition Probability is calculated for all the tags pairing with all other recorded tags
from the training data set. Tags pairs with the 0 probability are also mentioned in the
submitted TTP text file. Output file contains this data in below format:
prob(PR | QT) = 0.0110803324099723
prob(PR | N_NN) = 0.06583217431617988
prob(PR | PSP) = 0.06504904491481672

#### WEP (Word-emission Probability):
Word-emission probability is calculated only for the existing pair of the words and tags to
avoid the overhead of calculations for non-existing pairs of tags and words which value will
be 0 apparently. Output file has data In below format:
prob(वह | PR) = 0.34782608695652173
prob(पचास | QT) = 0.0110803324099723
prob(वर्ष| N_NN) = 0.0037088548910523874
prob(से| PSP) = 0.5534331440371709


#### Perplexity of ngram models:
To evaluate the models perplexity factor is used. In order to calculate the perplexity of given sentence training data set is the one which is hindi tagged data named Hindi-tagged-18.txt an the input sentence is provided as bolow
**Input sentence:** जब_PR मेरे_PR पास_N_NST एक_QT पैसा_N_NN नह ीं_RP
**Output:**
Bigram perplexity = 1.001811704525849
trigram perplexity = 1.0012386564808766
4gram perplexity = 1.0010211035763825
5gram perplexity = 1.0008433370198297

**Input sentence:** आकाश_N_NN में_PSP भ षण_JJ विस्फोट_N_NN जैस _N_NN ध्ववन_N_NN के_PSP साथ_PSP हजार_N_NN सूर्यों_N_NN का_PSP उजाला_N_NN फै लता_V_VM देख_V_VM कर_V_VAUX सब_QT च ींक_N_NN गए_V_VM 
**Output:**
Bigram perplexity = 1.0015066218392483
trigram perplexity = 1.0002859183043158
4gram perplexity = 1
5gram perplexity = 1

In above to examples perplexity decreases as the N of the N-gram model increases. But the
input is small sentence sometime it may be false. Please note that for the calculation 0
probability n-grams are not considered they are ignored to do the calculations smoothly
without any exceptions like “divide by zero” or “zero can not be raised” 
