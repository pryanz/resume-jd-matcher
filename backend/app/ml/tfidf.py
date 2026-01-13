from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(text_resume , text_jd):
    '''
    Compares two texts and returns cosine similarity
    '''
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text_resume, text_jd])
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity_matrix[0][0]

if __name__ == "__main__":
    resume = "Python developer with experience in machine learning and NLP"
    jd = "Looking for an ML engineer skilled in Python and natural language processing"
    print(compute_similarity(resume, jd))
