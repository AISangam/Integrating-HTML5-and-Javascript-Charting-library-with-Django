import nltk	
import random

from django.shortcuts import render

# This is the list with which user entered tokens will be compared.
list_of_words= ['great', 'men', 'never', 'lies']

# Function for counting occurence of user input tokens with the above list
def sentiments_with_js_chart(request):
	if request.method == 'POST':
		text = request.POST.get('user_input')
		text_split = text.lower().split()
		# logic for counting
		count = 0
		dict_to_count = dict()
		for each_token in text_split:
			if each_token in list_of_words and each_token not in dict_to_count:
				dict_to_count[each_token]=1
			elif each_token in list_of_words and each_token in dict_to_count:
				dict_to_count[each_token]+=1
			else:
				pass	
		
		return render(request, 'result_output.html', {'context': dict_to_count})
	
	return render(request, 'user_input.html')	



























# # Create your views here.
# def document_features(document):
#     document_words = set(document)
#     all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
#     word_features = list(all_words)[:2000]
#     features = {}
#     for word in word_features:
#     	features['contains({})'.format(word)] = (word in document_words)
#     return features


# def sentiments_with_js_chart(request):
# # list comprehension to categorize documents along with their categories	
# 	documents = [
# 			  	(list(movie_reviews.words(movie_file)), category)
# 			  	for category in movie_reviews.categories()
# 			  	for movie_file in movie_reviews.fileids(category)
# 			  	]
# 	random.shuffle(documents)
	
# 	featuresets = [(document_features(d), c) for (d,c) in documents]
# 	train_set, test_set = featuresets[:8], featuresets[8:]
# 	# print("Length of training set is {}".format(len(train_set)))
# 	# print("Length of testing set is {}".format(len(test_set)))
# 	classifier = nltk.NaiveBayesClassifier.train(train_set)
# 	# print(classifier)
# 	output = classifier.show_most_informative_features(5)
# 	print("=============================================")
# 	print(dir(output))