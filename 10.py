# AI-Based Sentiment Analysis

# Define positive and negative words
positive_words = [
    "good", "great", "excellent", "happy",
    "love", "amazing", "best", "wonderful",
    "like", "enjoy"
]

negative_words = [
    "bad", "worst", "hate", "sad",
    "poor", "terrible", "awful", "dislike",
    "boring", "angry"
]

# Get input from the user
text = input("Enter a sentence: ")

# Convert text to lowercase and split into words
words = text.lower().split()

# Count positive and negative words
positive_count = 0
negative_count = 0

for word in words:
    # Remove common punctuation marks
    clean_word = word.strip(".,!?;:")

    if clean_word in positive_words:
        positive_count += 1

    elif clean_word in negative_words:
        negative_count += 1

# Determine sentiment
if positive_count > negative_count:
    sentiment = "Positive"

elif negative_count > positive_count:
    sentiment = "Negative"

else:
    sentiment = "Neutral"

# Display the result
print("\nSentiment Analysis Result")
print("-------------------------")
print("Positive Words:", positive_count)
print("Negative Words:", negative_count)
print("Sentiment:", sentiment)