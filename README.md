# Fetch Rewards Coding Exercise

The objective of this exercise is to create a program that receives two text inputs, and computes a similarity score between the two. The one caveat is that no libraries are to be used. 

This program is also implemented as a --web service--, and a --docker container-- is present to be run via Docker hub. 


## Methodology

1. Pass in the two samples of texts to be compared as strings.
2. Split each of the texts into a list of sentences, using periods as the seperator. 
3. Split each sentence into a list of words and convert it into a set. 
4. Find the intersection/union of the two sets to find the fraction of common words out of the total words. The more words in common, the higher the score for that sentence. Append each score to a score list.
5. After each sentence has been scored, average all the scores together. 


## How to run

I've created three ways to view my solution.

1. Simply run Similar_Texts.py with the three txt files (sample1.txt, sample2.txt, sample3.txt). 
```
python Similar_Texts.py
```

The program itself will call the function that performs the similarity calculations. sample1.txt and sample2.txt hard coded in lines 61, 62. You can edit these lines to change which sample you would like to use.  (Note: I would have used argparse to throw these files in the command line, but did not want to violate the 'no libraries' restriction.

2. Run webapp.py if you have flask installed or head to 

3. Get the docker container from docker hub. 
  

## Decisions
-Do I count punction or only words?
To my knowledge, without the use of the re library, the built-in split operation can only have one seperator. This does not matter since the samples do not contain any question or exclaimation marks. Punctuation at the end of a sentence I believe is negligible since a period, question mark, or exclamation mark should not be deemed any different in terms of content.

Thus, the only punctuation that exists in the samples are periods, commas, and apostrophes. My program only factors in the use of commas.  Apostrophes should be considered for a special case since two words that are contracted are the same. However this is omitted in my program. 


-Which words should matter in the similarity comparison?
I consider every word is important. Because my program splits and analyzes each text by sentences, the more words used provides better accuracy in similarity. 

-Do you care about the ordering of words?
My program does not take in account for the ordering. I do believe that this could be important in determining similarity, but given the size of the samples, I elected to stick with finding the intersection between each pair of sentences. Also, by relying on sets, it would aid the accuracy of sentences that have been rearranged using the same words.

-What metric do you use to assign a numerical value to the similarity?
I used the intersection of both text1 and text2, divided by the union of text1 and text2. This provides the fraction of words they have in common. As mentioned previously, I think this is sufficient as if someone were to rearrange a sentence but use the same words, it would still yield a high similarity.

-What type of data structures should be used?
Lists and sets are essential to this program, but if able, I believe using the Counter() function from collections library would help. That would allow me to keep tract the number of times the same words have been used. 

## How to run:

You can download the docker container at 

