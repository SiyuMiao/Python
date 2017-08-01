#Siyu Miao
import re
#based on this file
filename = "sample.txt"
#Use function to compute the amount of the letters in the file.
def comp_letter(text):
    #lower the letters and replace the black
    text = text.lower().replace(" ","")
    dic = {}
    #use to count
    letter = "abcdefghijklmnopqrstuvwxyz,.-"
    #for loop to use compute the amount of the letters
    #if the letter in the list, then the amount add 1
    for i in text:
        if i in letter:
            dic[i] = dic.get(i,0)+1


    try:
        #output create a file
        output = file("statistics.txt","a")
        #print out the amount of each letter
        for j in letter:
##            print "The number of " + j + "'s is "+ str(dic[j])
            s = "The number of " + j +"'s is "+ str(dic[j])+"\n"
            #write to the file
            output.write(s)
        #close the file
        output.close()
    #skip the error
    except Exception,e:
        raise e
    #no matter what happens, just close the file at the end
    finally:
        output.close()


#Use function to compute the amount of the words in the file.
def comp_word(text):
    try:
        #output create a file
        output = file("statistics.txt","a")
##        print "-"*40
        output.write("-"*40+"\n")
        words = text.split()
        letter1 = "abcdefghijklmnopqrstuvwxyz"
        #for loop: remove the punctuations and compute the single word
        for i in range(len(words)):
            word = words[i]
            if word.lower()[-1] not in letter1:
                words[i] = word[:-1]
##        print "The number of words in the file are "+str(len(words))
        s = "The number of words in the file are "+str(len(words))+"\n"
        output.write(s)

        #create a new dictionary
        dic = {}
        #if the word in the list, then compute the amount of the words in the list
        for word in words:
            dic[word] = dic.get(word,0)+1

        #sort the list from large to small
        dic_sorted = sorted(dic.items(), key = lambda k:-k[1])
        
        fre_word = 0
##        print "The most frequently occurring word is: "
        s = "The most frequently occurring word is: \n"
        output.write(s)
        #find out the most frequently occurring word
        for i in dic_sorted:
            if i[1] >= fre_word:
##                print "'"+i[0]+"' occurring " + str(i[1])+ " times"
                s = "'"+i[0]+"' occurring " + str(i[1])+ " times\n"
                output.write(s)
                fre_word = i[1]
            else:
                break
        output.close()
    except Exception,e:
        raise e
    finally:
        output.close()
#the main function
def main():
    try:
        #read the file
        text = file(filename,"r").read()
        #use the function of the letter
        comp_letter(text)
        #use the function of hte word
        comp_word(text)
    except Exception,e:
        raise e
main()
