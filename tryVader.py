from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


#The compound score is computed by summing the valence scores of each word in the lexicon, adjusted according to the rules, 
#and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive). This is the most useful metric 
#if you want a single unidimensional measure of sentiment for a given sentence. Calling it a 'normalized, weighted composite score' is accurate.

class SentimentAnalyzer:
        def sentimentAnalyzerScores(self,sentence):
                analyser = SentimentIntensityAnalyzer()
                score = analyser.polarity_scores(sentence)
                return score['compound']

        def computeSentiment(self,inputFile):
                compoundSum = 0
                nTweets = 0
                for line in inputFile:
                        nTweets += 1
                        compoundScore = self.sentimentAnalyzerScores(line)
                        compoundSum += compoundScore
                avgScore = compoundSum/nTweets
                print(avgScore)
                return avgScore

if __name__ == '__main__':
    inputFile = open("pos_tweets.txt","r")
    ob = SentimentAnalyzer()
    ob.computeSentiment(inputFile)


