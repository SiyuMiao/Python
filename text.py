#-*- coding: utf-8 -*-

import re

filepath='sample.txt'

def ana_letter(text):
	'''
	handle letters and punctuations 
	
	'''
	text=text.lower().replace(" ","")#lower and repalce the black
	
	dic={}
	li='abcdefghijklmnopqrstuvwxyz.-,' # need to count

	for s in text:
		if s in li:
			dic[s]=dic.get(s,0)+1
	try:
		output=file('statistics.txt','a')
		for i in li:
			print 'number of '+i+"'s is ",dic[i]
			s='number of '+i+"'s is "+str(dic[i])+'\n'
			output.write(s)
		output.close()
	except Exception,e:
		raise e
	finally:
		output.close()



def ana_word(text):
	'''
	handle words in text
	
	'''

	#Another method：
	#words=text.split()
	#But yet need more to remove the punctuations
	#

	try:
		output=file('statistics.txt','a')
		print '*'*30
		output.write('*'*30+'\n')
		words=re.findall(r'\b[a-zA-Z]+\b',text)
		print 'The Whole txt has %d words'%len(words)	
		s='The Whole txt has %s words'%str(len(words))+'\n'
		output.write(s)
		
		#use dictionary to count the times of words 
		dic={}
		for word in words:
			dic[word]= dic.get(word,0)+1
		
		#sort for the dic to get the most  frequently occurring word
		dic_sorted=sorted(dic.items(),key=lambda k:-k[1])
		
		##find the most frequently words, 
		## there may be two or more words

		maxOftimes=0
		print 'The most frequently word is:'
		s='The most frequently word is:'
		output.write(s)
		for i in dic_sorted:
			if i[1]>=maxOftimes:
				print 'because "'+i[0],'" occurring %d times' %i[1]
				s='because "'+i[0]+'" occurring %s times' %str(i[1]) +'\n'
				output.write(s)
				maxOftimes=i[1]
			else:
				break
	except Exception,e:
		raise e
	finally:
		output.close()


def main():
	try:
		text=file(filepath,'r').read()
		ana_letter(text)
		ana_word(text)

	except Exception, e:
		raise e

if __name__ == '__main__':
	main()
