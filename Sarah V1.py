ALIVE_BLOB = [
    "   .------.   ",
    "  /        \\  ",
    " |   O   O  | ",
    " |          | ",
    " |   ----   | ",
    "  \\        /  ",
    "   '------'   "
]

DEAD_BLOB = [
    "   .------.   ",
    "  /        \\  ",
    " |   x  x   | ",
    " |          | ",
    " |   ----   | ",
    "  \\        /  ",
    "   '------'   "
]








import time
import random
import threading

def print_blobs(lives):
    """Prints 3 blobs in a row, updating for dead/alive blobs."""
    blob_list = []
    for i in range(3):
        if i < lives:
            blob_list.append(ALIVE_BLOB)
        else:
            blob_list.append(DEAD_BLOB)

    
    for line_idx in range(len(ALIVE_BLOB)):
        print("   ".join(blob[line_idx] for blob in blob_list))
   


def timed_input(prompt, timeout):
    user_input = [None]

    def get_input():
        user_input[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()

    thread.join(timeout)
    return user_input[0]  # returns None if time expired


# ------------------ MINIGAMES --------------------------

def minigame_wrong_subject():
    print("\n💣 QUICK! Choose the subject that doesn't fit before bomb blows!")
    print("Type: CHE120 / CHE100 / MATH100")
    answer = timed_input("Your choice: ", 3)

    if answer == "MATH100":
        print("😅 Correct! We don't take MATH100")
        return True
    else:
        print("💥 BOOM! You take this class!!(you should know what courses you take...")
        return False


def minigame_fail_exam():
    print("\n⌨️ TYPE FAST! Type the sentence 'input-output+generation-accumulation=0' within 15 seconds to not fail your exam!")
    answer = timed_input("Type here: ", 15)

    if answer == "input-output+generation-accumulation=0":
        print(" Nice, you didn't fail!")
        return True
    else:
        print("⏱️ Too slow or wrong, you failed your exam!")
        return False


    
def minigame_math():
    print("\n🧮 Solve this FAST or Professor Comfort will smack you: derivative of x^2+3 = ? (3 seconds)")
    answer = timed_input("Your answer: ", 3)

    if answer == "2x":
        print("👍 Correct!")
        return True
    else:
        print("❌ Times up! You should've studied more...")
        return False
    
   


# List of available minigames
MINIGAMES = [ minigame_math]


# ------------------ MAIN GAME LOOP ----------------------

def main():
    score = 0
    lives = 3

    print("🎉 Welcome to Dumb Ways to Waterloo!")
    print("Survive as many minigames as possible...or die\n")

    while lives > 0:
        game = random.choice(MINIGAMES)
        result = game()

        if result:
            score += 1
            print(f"⭐ Score = {score}")
        else:
            lives -= 1
            print(f"💔 Lives left: {lives}")

        time.sleep(1)

    print("\n☠️ GAME OVER! Final score:", score)


if __name__ == "__main__":
    main()

