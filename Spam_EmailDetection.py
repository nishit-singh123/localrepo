import pandas  as pd # to handle our dataset


from sklearn.feature_extraction.text import CountVectorizer #for converting text data into numerical data
from sklearn.model_selection import  train_test_split # split data
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from tkinter import *  # <-- Tkinter GUI import
dataset=pd.read_csv('C:/Users/sonal/Downloads/mail_data.csv')
print(dataset)
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(dataset['Message'])
x_train,x_test,y_train,y_test=train_test_split(x,dataset['Category'],test_size=0.2)
model=MultinomialNB()
model.fit(x_train,y_train)
yPred=model.predict(x_test)
#Evaluate the model

accuracy=accuracy_score(y_test,yPred)
print("Accuracy: {:.2f}%".format(accuracy * 100))
print(accuracy)

# function to predict for GUI

def predict():
    msg = entry.get()
    msg_vector = vectorizer.transform([msg])
    result = model.predict(msg_vector)
    result_label.config(text=f"The message is: {'Spam 🚫' if result[0] == 'spam' else 'Ham ✅'}")



# GUI SETUP

root = Tk()
root.title("Spam Email Detector")
root.geometry("400x200")

Label(root, text="Enter your message:", font=("Arial", 12)).pack(pady=10)
entry = Entry(root, width=50)
entry.pack()

Button(root, text="Check", command=predict, bg='blue', fg='white').pack(pady=10)
result_label = Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()