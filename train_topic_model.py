# train_topic_model.py

import nltk
nltk.download('punkt')
nltk.download('stopwords')

import pandas as pd
from agents.topic_classifier import TopicClassifier

# Sample dataset
data = pd.DataFrame({
    'abstract': [
        'This paper explores the use of AI in healthcare.',
        'This paper explores recent advances in quantum computing.',
        'This paper discusses robotics and automation techniques.'
    ],
    'topic': ['AI', 'Physics', 'Robotics']
})

classifier = TopicClassifier()
classifier.train(data)
print("Model trained and saved.")
