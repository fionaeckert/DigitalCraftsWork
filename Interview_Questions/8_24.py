
# write a function that returns both the percentage of people that iked the movie in general and the ovrall +/- point total.
# like = +1, starry = +2, dislike = -1, hate = -2


reviews = ["\U0001F44D", "\N{thumbs up sign}",  "\N{Face with Open Mouth Vomiting}", "\U0001F44D", 
"\U0001f929", "\N{thumbs down sign}", "\U0001F44E", "\U0001F92E", "\U0001f929", "\N{thumbs down sign}", "\N{thumbs up sign}", 
"\U0001F44D", "\U0001F44D", "\N{Face with Open Mouth Vomiting}", "\N{thumbs down sign}", "\U0001F44D", "\U0001f929", "\U0001F44D", "\N{thumbs down sign}", "\N{thumbs down sign}"]
def movieReview(reviews:list):
    pointTotal = 0
    for i in reviews:
        if i == "\N{thumbs up sign}" or i == "\U0001F44D":
            pointTotal +=1
        elif i =="\N{Face with Open Mouth Vomiting}" or i == "\U0001F92E":
            pointTotal -= 2
        elif i =="\N{thumbs down sign}" or i == "\U0001F44E":
            pointTotal-=1
        elif i == "\U0001f929":
            pointTotal+=2
    percentLike = 0 
    for i in reviews:
        if i == "\N{thumbs up sign}" or i == "\U0001F44D" or i == "\U0001f929":
            percentLike +=1
    percentLike = ((percentLike)/len(reviews))*100

    print('The point total for the movie is %d points out of 20 points' % pointTotal)
    print('%d percent of users enjoyed the movie.' % percentLike)

movieReview(reviews)

