import streamlit as st
import speech_recognition as sr

st.title("🎤 Speech Processing App")

audio_file = st.file_uploader("Upload WAV file")

if audio_file:
    recognizer = sr.Recognizer()

    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())

    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        st.success(text)
    except:
        st.error("Could not process audio")
