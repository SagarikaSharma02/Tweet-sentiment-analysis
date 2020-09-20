#!/usr/bin/env python
# coding: utf-8

# Analysis of some fictional tweets and find out whether the overall sentiment of Twitter users is happy or sad. 

# In[1]:


tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]


# **Q: How many tweets does the dataset contain?**

# In[2]:


number_of_tweets = len(tweets)
number_of_tweets


# In[3]:


happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']


# To identify whether a tweet is happy, we can simply check if contains any of the words from happy_words

# **Q: Determine the number of tweets in the dataset that can be classified as happy.**

# In[4]:


number_of_happy_tweets = 0

for i in range(len(tweets)):
    sample_tweet = tweets[i]
    for word in happy_words:
        if word in sample_tweet:
            number_of_happy_tweets = 1 + number_of_happy_tweets
        else:
            number_of_happy_tweets = number_of_happy_tweets
            
    i = i + 1


# In[5]:


print("Number of happy tweets:", number_of_happy_tweets)


# **Q: What fraction of the total number of tweets are happy?**

# In[6]:


happy_fraction = (number_of_happy_tweets)/(len(tweets))
happy_fraction


# **Q: Determine the number of tweets in the dataset that can be classified as sad.**

# In[7]:



number_of_sad_tweets = 0

for i in range(len(tweets)):
    sample_tweet = tweets[i]
    for word in sad_words:
        if word in sample_tweet:
            number_of_sad_tweets = 1+number_of_sad_tweets
            
        else:
            number_of_sad_tweets = number_of_sad_tweets
            
        i = 1 + i


# In[8]:


print("Number of sad tweets:", number_of_sad_tweets)


# **Q: What fraction of the total number of tweets are sad?**

# In[9]:


sad_fraction = (number_of_sad_tweets)/(len(tweets))
sad_fraction


# **Q: Calculate the sentiment score, which is defined as the difference betweek the fraction of happy tweets and the fraction of sad tweets.**

# In[10]:


sentiment_score = happy_fraction - sad_fraction
print("The sentiment score for the given tweets is", sentiment_score)


# **Q: Display whether the overall sentiment of the given dataset of tweets is happy or sad, using the sentiment score.**

# In[11]:


if sentiment_score>0:
    print("The overall sentiment is happy")
else:
    print("The overall sentiment is sad")


# **Q: What is the fraction of tweets that are neutral i.e. neither happy nor sad.**

# In[12]:


number_of_neutral_tweets = len(tweets)
sentiment_words = happy_words + sad_words

for i in range(len(tweets)):
    sample_tweet = tweets[i]

    for word in sentiment_words:
        if word in sample_tweet:
            number_of_neutral_tweets = number_of_neutral_tweets -1
            
        else:
            number_of_neutral_tweets = number_of_neutral_tweets
            
        i=i+1  
        
print(number_of_neutral_tweets)        


# In[13]:


neutral_fraction = (number_of_neutral_tweets)/(len(tweets))
print('The fraction of neutral tweets is', neutral_fraction)


# In[1]:


import jovian
jovian.commit(project = 'tweet_sentiment_analysis')


# In[ ]:




