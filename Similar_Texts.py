# Author: Raymond Hong
# Desc: Fetch Rewards excercise
# Objective: Without the use of libraries, create a program that can compute similarity scores between two text samples.



# This function ompares two text samples.
# Inputs: text1 (string): A sample of text to be compared.
#         text2 (string): A sample of text to be compared.
def compareText(text1, text2):
    # Split the text into a list, where each element is a sentence.
    textList1 = text1.split('. ')
    textList2 = text2.split('. ')

    # Intialize a list to hold the similarity scores for each sentence.
    avgList = []

    # Split each sentence into words, and convert the list into a set.
    for sentence1, sentence2 in zip(textList1, textList2):
        wordSet1 = set(sentence1.split(' '))
        wordSet2 = set(sentence2.split(' '))

        # Count the number of common words in both sets, and divide by the total
        # unique number of words from both sets
        a = len(wordSet1.intersection(wordSet2)) / len(wordSet1.union(wordSet1))

        # Append the score onto the list
        avgList.append(a)

    # After each similarity score for each sentence is calculated, average them up.
    return sum(avgList)/len(avgList)


# Function to extract text from a txt file. Not used since script is deployed in a web app, where
# the text is entered as an input.
# Input: filePath (string): file path to txt file.
def extractText(filePath):
    f = open(filePath, "r")
    text = f.read()
    f.close()
    return text


# used for intial testing.
if __name__ == '__main__':
    # sample1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. " \
    #           "If you have any participating brands on your receipt, you'll get points based on the cost of the " \
    #           "products. You don't need to clip any coupons or scan individual barcodes. " \
    #           "Just scan each grocery receipt after you shop and we'll find the savings for you."
    # sample2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. " \
    #           "If you have any eligible brands on your receipt, you will get points based on the total cost " \
    #           "of the products. You do not need to cut out any coupons or scan individual UPCs. " \
    #           "Just scan your receipt after you check out and we will find the savings for you."
    #
    # sample3 = "We are always looking for opportunities for you to earn more points, which is why we also give you " \
    #           "a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top " \
    #           "of the regular points you earn every time you purchase a participating brand. " \
    #           "No need to pre-select these offers, we'll give you the points whether or not you knew about the offer." \
    #           " We just think it is easier that way."

    text1 = extractText("sample1.txt")
    text2 = extractText("sample2.txt")
    text3 = extractText("sample3.txt")
    print("\nComparing sample1 and sample2.")
    print("Similarity: ", compareText(text1, text2))
    print("\nComparing sample1 and sample3.")
    print("Similarity: ", compareText(text1, text3))  
    print("\nComparing sample2 and sample3.")
    print("Similarity: ", compareText(text2, text3))  
