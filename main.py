from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import words
from base_skills import *
from open_apps import *
from radio import *
from voice import *
from listen import *




def recognize(data, vectorizer, clf):
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return
    
    data.replace(list(trg)[0], '')
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func_name = answer.split()[0]
    speak(answer.replace(func_name, ''))
    exec(func_name + '(user_command)')


def main():
    global user_command
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))
    
    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))  
    
    del words.data_set
    
    speak('Чпокс.')
    while True:
        user_command = listen()
        #user_command = input("Запрос --->>>  ")
        print(user_command)
        recognize(user_command, vectorizer, clf)


if __name__ == "__main__":
    main()