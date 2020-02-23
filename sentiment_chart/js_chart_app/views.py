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
