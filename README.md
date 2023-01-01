# Moist Scraper
A simple scraper for the Moist Meter show run by penguinz0 on YouTube.

It scrapes transcripts of youtube videos then uses the OpenAI api to extract the scores given. Due to the ability of OpenAI models, I'm sure this has the ability to easily generalize to many other use cases.

## Usage
Goto main.py, add some youtube links to the list, then run the script. It will scrape the transcripts, then use the OpenAI api to extract the scores. It will print the results in the console.

You need to put an OpenAI key in key.txt in the project directory. You can get one from [here](https://beta.openai.com/account/api-keys).

You may also find that text-babbage also works quite well but I've used text-curie as I've found that text-ada hallucinates and I don't want to risk hallucinating scores.