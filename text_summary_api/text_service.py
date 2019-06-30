import nltk
import heapq
import spacy
# import lxml
import bs4 as bs
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
nltk.download('stopwords')
# nlp = spacy.load('en_core_web_lg')
nlp = spacy.load('en_core_web_sm')


def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)


def extract_topn_from_vector(feature_names, sorted_items):
    score_vals = []
    feature_vals = []

    for idx, score in sorted_items:
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    results = {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]] = score_vals[idx]

    return results


def summarizer(url):
    soup = bs.BeautifulSoup(url, 'lxml')
    text = ""
    for paragraph in soup.find_all('p'):
        text += paragraph.text

    clean_text = text.lower()
    clean_text = clean_text.replace(',', '')

    punctuations = '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~'
    stopwords = nltk.corpus.stopwords.words('english')
    doc = nlp(clean_text)
    tokens = [tok.lemma_.lower().strip() for tok in doc if tok.lemma_ != '-PRON-']
    tokens = [tok for tok in tokens if tok not in stopwords and tok not in punctuations]
    tokens = ' '.join(tokens)
    sent_tokenize = nltk.sent_tokenize(tokens)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sent_tokenize)

    feature_names = vectorizer.get_feature_names()
    sorted_items = sort_coo(X.tocoo())
    keywords = extract_topn_from_vector(feature_names, sorted_items)

    sorted_items = sort_coo(X.tocoo())
    sent2score = {}
    for sentence in doc.sents:
        for word in sentence:
            if word.text.lower() in keywords.keys():
                if len(sentence) < 25:
                    if sentence not in sent2score.keys():
                        sent2score[sentence] = keywords[word.text.lower()]
                    else:
                        sent2score[sentence] += keywords[word.text.lower()]

    best_sentences = heapq.nlargest(5, sent2score, key=sent2score.get)

    t = []
    for sentence in best_sentences:
        t.append(sentence)

    x = str(t)[1:-1]
    
    return x

