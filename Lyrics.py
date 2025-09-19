import time
import sys

def type_lyric(lines, delay=0.1):
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # move to the next line after finishing one lyric line
        time.sleep(0.5)  # small pause between lines (optional)

if __name__ == "__main__":
    lyrics = ["Enter Your Lyrics",
              "To Be Displayed"]

    type_lyric(lyrics, delay=0.1)  # adjust delay (e.g. 0.1 sec per char)
