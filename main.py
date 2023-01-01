import openai
import os
from getvideos import getTranscript

openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key == None:
    if os.path.exists("key.txt"):
        with open("key.txt", "r") as f:
            openai.api_key = f.read()
    else:
        print("No API Key found, using hardburned key")
        openai.api_key = ""

listOfVideoUrls = """
https://www.youtube.com/watch?v=ou_O5X0jTRM

"""

NewlistOfVideoUrls = []
for line in listOfVideoUrls.splitlines():
    if line != "":
        NewlistOfVideoUrls.append(line)

        
prompt = """
Transcript: its welcome everything in this show is mainly geared as a vessel towards more over the top and [ __ ] beautiful action and I really just appreciated that now there's only 12 episodes of this season which is a little disappointing because shows like Jujutsu Kaizen and Demon Slayer both of which had comparable levels of Animation quality as well as very similar levels of hype both of those had 24 and 26 episode long Seasons season one of demon Slayers 26 episodes season one of Jiu Jitsu Kaizen was 24 and it was able to hold this intensity like this full [ __ ] nuts butts action and jaw-dropping animation for a long time whereas chainsaw man's very bite-sized like it's giving you an appetizer so I'm hoping that it can continue this level of quality I hope it doesn't like fall off and you know suck [ __ ] because that'd be tragic but yeah it is just a little underwhelming that it's such a short season I would have liked more episodes because it's just so good and I would have really liked more time to get drawn into the entire universe and see more of it but it's still extremely good uh plugging it in the moist meter I'm going to be giving it a 90 I do highly recommend it especially if you like shows like Jujutsu Kaizen and Demon Slayer so yeah lived up to the hype so I was satisfied that's about it see you God slap is a comic book series we've been working on for a couple years now it's a hyper violent over-the-top sci-fi story about the beauty and destruction that slaps can cause issue 2 is out right now would make a wonderful Christmas gift so make sure to check it out at godslapbook.com right now we also have three variant covers that are in stock but the second those sell out those variant covers will never be restocked so definitely make sure to pick up a copy today

Write the score out as a number with nothing else.
Score: 90

Transcript: (entertranscript)

Write the score out as a number with nothing else.
Score:"""

def complete(prompt):
    response = openai.Completion.create(
        model="text-curie-001",
        prompt=prompt, 
        temperature=0, 
        max_tokens=5, 
        stop=["\n"],
        )

    return response

scores = []

for video in NewlistOfVideoUrls:
    videoData = getTranscript(video)
    transcript = videoData[0]
    videoName = videoData[1]
    # Cut the first 3/4ths of the transcript as it's usually the intro
    transcript = transcript[int(len(transcript) * (3/4)):]
    
    craftedPrompt = prompt.replace("(entertranscript)", transcript)
    
    completion = complete(craftedPrompt)
    
    score = completion.choices[0].text
    score = int(score)
    
    scores.append((videoName, score))
    
# Sort the scores
scores = sorted(scores, key=lambda x: x[1], reverse=True)

print(scores)