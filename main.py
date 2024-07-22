import os
import json
import random

# JSON data for flashcards
# flashcards_json = 
'''
[
    {"front": "人 (ひと)", "back": "Person"},
    {"front": "言語 (げんご)", "back": "Language"},
    {"front": "漢字 (かんじ)", "back": "Kanji (Chinese characters used in Japanese)"},
    {"front": "難しい (むずかしい)", "back": "Difficult"},
    {"front": "問題 (もんだい)", "back": "Problem"},
    {"front": "新しい (あたらしい)", "back": "New"},
    {"front": "感じ (かんじ)", "back": "Feeling/Sense"},
    {"front": "文字 (もじ)", "back": "Character/Letter"},
    {"front": "使う (つかう)", "back": "To use"},
    {"front": "習字 (しゅうじ)", "back": "Calligraphy"},
    {"front": "書く (かく)", "back": "To write"},
    {"front": "英語 (えいご)", "back": "English (language)"},
    {"front": "発明 (はつめい)", "back": "Invention"},
    {"front": "感情 (かんじょう)", "back": "Emotion"},
    {"front": "読む (よむ)", "back": "To read"},
    {"front": "存在 (そんざい)", "back": "Existence"},
    {"front": "簡略化 (かんりゃくか)", "back": "Simplification"},
    {"front": "意味 (いみ)", "back": "Meaning"},
    {"front": "学校 (がっこう)", "back": "School"},
    {"front": "教える (おしえる)", "back": "To teach"}
]
'''

flashcards_json = '''
[
    {"front": "人 (ひと)", "back": "Person"},
    {"front": "言語 (げんご)", "back": "Language"},
    {"front": "漢字 (かんじ)", "back": "Kanji (Chinese characters used in Japanese)"},
    {"front": "難しい (むずかしい)", "back": "Difficult"},
    {"front": "問題 (もんだい)", "back": "Problem"},
    {"front": "新しい (あたらしい)", "back": "New"}
]
'''

# Load the flashcards from JSON
flashcards = json.loads(flashcards_json)

def clear_term():
    os.system("clear")

def quiz_user(flashcards):
    # Shuffle flashcards for random order
    random.shuffle(flashcards)
    
    # Initialize score
    score = 0

    # Queue to place cards to re-do
    failed_cards = []
    
    for card in flashcards:
        clear_term()
        print("\nFront: " + card["front"])
        input("Press Enter to see the back...")
        print("Back: " + card["back"])
        
        # Ask the user if they got it right
        user_input = input("Did you get it right? (y/n): ").strip().lower()
        if user_input == 'y':
            score += 1
        else:
            failed_cards.append(card)

    if len(failed_cards) > 0:
        clear_term()
        print("Now, you'll be asked to review the cards that you got wrong.")
        input("Press enter to continue...")
        for card in failed_cards:
            clear_term()
            print("\nFront: " + card["front"])
            input("Press Enter to see the back...")
            print("Back: " + card["back"])
            
            # Ask the user if they got it right
            user_input = input("Did you get it right? (y/n): ").strip().lower()

    
    # Print final score
    clear_term()
    print("\nQuiz complete! Your score: {}/{}".format(score, len(flashcards)))

if __name__ == "__main__":
    quiz_user(flashcards)
