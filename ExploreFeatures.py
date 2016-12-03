import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mannwhitneyu

# 1. #entities;
# 2. #entityTypes
# 3. #tweetsPosted;
# 4. sentiment.

df=pd.read_csv("/Users/keya/twitter/task2_data.csv")

nr_entities_relevant = df[df['relevanceJudge']==1]['#entities']
nr_entities_non_relevant = df[df['relevanceJudge']==0]['#entities']
print(nr_entities_relevant.describe())
print(nr_entities_non_relevant.describe())

u, p_value = mannwhitneyu(nr_entities_non_relevant, nr_entities_relevant)
print("u=",u,"p_value=",p_value)

nr_entityTypes_relevant = df[df['relevanceJudge']==1]['#entityTypes']
nr_entityTypes_non_relevant = df[df['relevanceJudge']==0]['#entityTypes']
print(nr_entityTypes_relevant.describe())
print(nr_entityTypes_non_relevant.describe())

u, p_value = mannwhitneyu(nr_entityTypes_non_relevant, nr_entityTypes_relevant)
print("u=",u,"p_value=",p_value)

nr_tweetsPosted_relevant = df[df['relevanceJudge']==1]['#tweetsPosted']
nr_tweetsPosted_non_relevant = df[df['relevanceJudge']==0]['#tweetsPosted']
print(nr_tweetsPosted_relevant.describe())
print(nr_tweetsPosted_non_relevant.describe())

u, p_value = mannwhitneyu(nr_tweetsPosted_non_relevant, nr_tweetsPosted_relevant)
print("u=",u,"p_value=",p_value)

nr_sentiment_relevant = df[df['relevanceJudge']==1]['sentiment']
nr_sentiment_non_relevant = df[df['relevanceJudge']==0]['sentiment']
print(nr_sentiment_relevant.describe())
print(nr_sentiment_non_relevant.describe())

u, p_value = mannwhitneyu(nr_sentiment_non_relevant, nr_sentiment_relevant)
print("u=",u,"p_value=",p_value)


nr_entities = df['#entities']
f1=plt.figure(1)
nr_entities.plot(kind='hist')

f1.canvas.set_window_title('#entities')


nr_entities = df['#entities']
f6=plt.figure(6)
nr_entities.plot(kind='hist')
plt.yscale('log')
f6.canvas.set_window_title('#entities log')


nr_entities = df['#entityTypes']
f2=plt.figure(2)
nr_entities.plot(kind='hist')
# plt.yscale('log')
f2.canvas.set_window_title('#entityTypes')

nr_entities = df['#entityTypes']
f5=plt.figure(5)
nr_entities.plot(kind='hist')
plt.yscale('log')
f5.canvas.set_window_title('#entityTypes log')


nr_entities = df['#tweetsPosted']
f3=plt.figure(3)
nr_entities.plot(kind='hist')
plt.yscale('log')
f3.canvas.set_window_title('#tweetsPosted')

nr_entities = df['sentiment']
f4=plt.figure(4)
nr_entities.plot(kind='hist')
f4.canvas.set_window_title('sentiment')

plt.show()

# input()