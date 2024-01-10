from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
document1 = "This is a sample document."
document2 = "Here is another example document."

# Create a CountVectorizer to convert text into a bag-of-words representation
vectorizer = CountVectorizer()

# CountVectorizer is a method used to convert text data into a numerical representation, 
# commonly used in natural language processing (NLP). It operates by tokenizing the text data 
# and counting the occurrences of each token, creating a matrix where the rows represent the documents 
# and the columns represent the tokens. The cell values indicate the frequency of each token in each document

# Apply stopword removal using NLTK stopwords
stop_words = set(stopwords.words("english"))

# Stop words are commonly used words in a language, such as "a," "the," "is," and "are" in English.
# In the context of text mining and natural language processing, they are often removed from the text
# to focus on the important words.

## This helps in tasks like search engine optimization, where the system can prioritize
## relevant documents by ignoring common words. 

# Preprocess and tokenize text
def preprocess(text):
    words = text.lower().split()
    return ' '.join([word for word in words if word not in stop_words])

# Apply preprocessing and create document-term matrix
doc_matrix = vectorizer.fit_transform([preprocess(document1), preprocess(document2)])

# Calculate cosine similarity
cosine_sim = cosine_similarity(doc_matrix)

# first dimension doc1 similarity to itself and to the other doc
# second dimension doc2 similarity to doc1 and itself
print(f"Cosine Similarity:\n{cosine_sim}")
