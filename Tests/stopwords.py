from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
document1 = "This is a sample document."
document2 = "Here is another example document."

# Create a CountVectorizer to convert text into a bag-of-words representation
vectorizer = CountVectorizer()

# Apply stopword removal using NLTK stopwords
stop_words = set(stopwords.words("english"))

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
