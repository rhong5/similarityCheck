# Fetch Rewards Coding Exercise

The objective of this exercise is to create a program that receives two text inputs, and computes a similarity score between the two. The one caveat is that no libraries are to be used. 

This program is also implemented as a __web service__, and a __docker container__ is present to be run via Docker hub. 


## How to run

I've created three ways to view my solution.

1. Simply run Similar_Texts.py with the three txt files (sample1.txt, sample2.txt, sample3.txt). Python 3.7.4 was used. Install the python version if required. 
```
python Similar_Texts.py
```

The program itself will call the function that performs the similarity calculations for every combination of the 3 samples and print them to the console.

2. Run as a web application.

I have deployed my flask web app at http://rhong5.pythonanywhere.com/

If you prefer to run it locally, ensure you have flask v1.1.1 and python installed if you haven't already.
```
pip install flask==1.1.1
``` 

Then run webapp.py.
```
python webapp.py
```
The output will have a address that you can click on to direct you to the application.


3. Run a docker container from docker hub
https://hub.docker.com/layers/139314065/rhong5/dockerflask/latest/images/sha256-3bb85fb4aed2e6416cc5ec386b18cf33dfcde25e8429437994b8f6317835137f?context=explore

Install docker using the documentation.
https://docs.docker.com/engine/install/

Pull docker container.

```
docker pull rhong5/dockerflask:latest
```

Run the container.
```
docker run -p <externalport>:<localport> rhong/dockerflask
```

  
## Methodology

1. Pass in the two samples of texts to be compared as strings.
2. Split each of the texts into a list of sentences, using periods as the seperator. 
3. Split each sentence into a list of words, using spaces as the seperator and convert it into a set. 
4. Find the intersection/union of the two sets to find the fraction of common words out of the total words. The more words in common, the higher the score for that sentence. Append each score to a score list.
5. After each sentence has been scored, average all the scores together. 

## Decisions
__Do I count punction or only words?__
To my knowledge, without the use of the re library, the built-in split operation can only have one seperator. This does not matter since the samples do not contain any question or exclaimation marks. Punctuation at the end of a sentence I believe is negligible since a period, question mark, or exclamation mark should not be deemed any different in terms of content.

Thus, the only punctuation that exists in the samples are periods, commas, and apostrophes. My program considered commas as a word, therefore is contributed to the computation.  Apostrophes should be considered for a special case since two words that are contracted are the same. However this is omitted in my program. 


__Which words should matter in the similarity comparison?__
I consider all words important because I compute the similarity at the sentence level. Having as much words a possible to perform the computation is better for accuracy. 

__Do you care about the ordering of words?__
My program does not take in account for the ordering. I do believe that this could be important in determining similarity, but given the size of the samples, I elected to stick with finding the intersection between each pair of sentences. Also, by relying on sets, it would aid the accuracy of sentences that have been rearranged using the same words.

__What metric do you use to assign a numerical value to the similarity?__
I used the intersection of both text1 and text2, divided by the union of text1 and text2. This provides the fraction of words they have in common. As mentioned previously, I think this is sufficient as if someone were to rearrange a sentence but use the same words, it would still yield a high similarity.

__What type of data structures should be used?__
Lists and sets are essential to this program, but if able, I believe using the Counter() function from collections library would help. That would allow me to keep track the number of times the same words have been used. 

## Thank you
I would like to express my gratitude for allowing me to attempt this excercise. I hope it is of satisfaction!

-Raymond Hong

