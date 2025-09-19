import time
import sys

def type_lyric(lines, char_delay=0.08, default_line_delay=0.01):
    for line, pause in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_delay)
        print()
        time.sleep(pause if pause is not None else default_line_delay)

if __name__ == "__main__":
    lyrics = [
        ("Enter Your Lyrics", None),
        ("Delay 10 seconds", 10),
        ("Message Delivered after 10 Seconds", None),
        ("And so on...",None)
    ]

    type_lyric(lyrics, char_delay=0.08, default_line_delay=1.0)
