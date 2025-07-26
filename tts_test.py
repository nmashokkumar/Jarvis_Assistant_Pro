import asyncio
import edge_tts

EMOTION_SETTINGS_LIMITED = {
    "happy": {"rate": "+5%", "pitch": "+3Hz", "volume": "+3%", "description": "Slightly faster, brighter."},
    "angry": {"rate": "+5%", "pitch": "+0Hz", "volume": "+5%", "description": "Slightly faster, same pitch, louder."},
    "sad": {"rate": "-3%", "pitch": "-3Hz", "volume": "+0%", "description": "Slightly slower, lower pitch."},
    "normal": {"rate": "+0%", "pitch": "+0Hz", "volume": "+0%", "description": "Neutral."},
    "caring": {"rate": "-2%", "pitch": "-2Hz", "volume": "+0%", "description": "Slightly slower, lower pitch."},
}

async def speak_with_emotion_limited(text, emotion="normal", filename="output.mp3"):
    e = EMOTION_SETTINGS_LIMITED.get(emotion, EMOTION_SETTINGS_LIMITED["normal"])
    text_to_speak = text

    communicate = edge_tts.Communicate(
        text_to_speak,
        voice="en-US-AvaNeural", # Consistent male voice
        rate=e["rate"],
        pitch=e["pitch"],
        volume=e["volume"]
    )
    await communicate.save(filename)
    print(f"✅ Saved '{filename}' with emotion '{emotion}' ({e['description']})")

if __name__ == "__main__":
    async def main():
        tests = [
            ("Wow Boss! Today is an amazing day to build Jarvis!", "happy", "happy_test.mp3"),
            ("Boss, this code keeps crashing, I’m frustrated!", "angry", "angry_test.mp3"),
            ("Boss, it’s a tough day, everything feels heavy.", "sad", "sad_test.mp3"),
            ("Hello Boss, your Jarvis is ready to work.", "normal", "normal_test.mp3"),
            ("Boss, are you feeling alright? I'm here to help you through anything.", "caring", "caring_test.mp3")
        ]

        for text, emotion, filename in tests:
            await speak_with_emotion_limited(text, emotion, filename)

        print("✅ All tests completed. Listen to MP3 files to verify clarity, emotion, and consistency.")

    asyncio.run(main())
