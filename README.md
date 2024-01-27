# Voice_Assistant-

<br>
1. **Initialization:**  The code initializes the necessary libraries, including SpeechRecognition for voice input, pyttsx3 for text-to-speech conversion, and others.
<br>
2. **Functions:** <br>
   - **talk(text):** This function uses pyttsx3 to convert text into speech, breaking down long texts into smaller chunks to avoid issues.
<br>   - **input_instructions():** This function captures voice input using the microphone, recognizes the speech using Google's speech recognition, and returns the recognized instructions in lowercase.
<br>   - **play_jarvis():** This function contains the main logic for processing voice commands. It continuously listens for instructions and executes corresponding actions, such as playing a song on YouTube, providing the current time or date, answering questions about itself, or searching for information on Wikipedia. The loop continues until the user says "stop."
<br>
3. **Continuous Listening:** <br> The script uses a `while True` loop to continuously listen for user commands, providing real-time responses.
<br>
4. **Error Handling:** <br>The code incorporates error handling to address potential issues during speech recognition, such as unknown audio or communication errors with the Google Speech Recognition service.
<br>
5. **Customization:** <br>Users can easily customize the script by adding or modifying command-response pairs in the `play_jarvis()` function.
<br>
Overall, the code serves as a foundation for building a voice-controlled assistant, and users can extend its functionality based on their specific requirements.
