from flask import Flask, request, jsonify
import openai
import tweepy
import sys

app = Flask(__name__)

#paste twitter apis here


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(auth)

@app.route('/generate', methods=['POST'])
def generate():
    print("Received request for text generation.")
    user_input = request.json['input']
    openai.api_key = "your-openai-api-key-here"
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=user_input,
      max_tokens=50
    )
    generated_text = response.choices[0].text.strip()
    print("Generated text: ", generated_text)
    return jsonify({"output": generated_text})

@app.route('/postToTwitter', methods=['POST'])
def post_to_twitter():
    print("Received confirmation to post to Twitter.")
    confirmed_text = request.json['confirmedText']
    twitter_api.update_status(confirmed_text)
    print("Successfully posted to Twitter.")
    return jsonify({"status": "Posted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
