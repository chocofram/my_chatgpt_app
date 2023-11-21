import streamlit as st
from langchain.chat_models import ChatOpenAI
import openai
from openai import OpenAI
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)
import io
from streamlit.components.v1 import html
import base64
from audio_recorder_streamlit import audio_recorder
from tempfile import NamedTemporaryFile
import tempfile
import os
import audioread
import datetime

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI['openai_api_key']

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai.api_key,
)
#client = openai.api_key

def transcribe_audio_to_text(audio_bytes):
    # Use io.BytesIO to create a file-like object from bytes
    audio_stream = io.BytesIO(audio_bytes)
    try:
        # Pass the file-like object directly to the OpenAI API
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_stream
        )

        transcription_text = response.text if hasattr(response, 'text') else "No transcription attribute found."
        return transcription_text

    except openai.BadRequestError as e:
        # エラーハンドリング
        print(f"Failed to transcribe audio: {e}")
        return "音声の転写に失敗しました。"

def transcribe_audio_to_text4(audio_bytes):
    # 一時ファイルを作成し、オーディオデータを書き込む
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(audio_bytes)
        temp_file_name = temp_file.name

    try:
        # audioreadで一時ファイルを開く
        with audioread.audio_open(temp_file_name) as audio_file:
            # オーディオファイルのデータを取得
            audio_data = b''.join(chunk for chunk in audio_file)

            # OpenAIのAPIにバイトデータを渡して転写
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=io.BytesIO(audio_data)
            )

        # 転写されたテキストを取得
        transcription_text = response.text if hasattr(response, 'text') else "No transcription attribute found."
        return transcription_text

    finally:
        # 一時ファイルを削除
        os.remove(temp_file_name)

def transcribe_audio_to_text2(audio_bytes):
    # io.BytesIOオブジェクトを使用してバイトデータからオーディオファイルを読み込む
    with audioread.audio_open(io.BytesIO(audio_bytes)) as audio_file:
        # オーディオファイルのデータを取得
        audio_data = b''.join(chunk for chunk in audio_file)

        # OpenAIのAPIにバイトデータを渡して転写
        response = openai.Audio.create(
            model="whisper-1",
            file=io.BytesIO(audio_data)
        )

    # 転写されたテキストを取得
    transcription_text = response.text if hasattr(response, 'text') else "No transcription attribute found."
    return transcription_text

def transcribe_audio_to_text1(audio_bytes):
    # Use io.BytesIO to create a file-like object from bytes
    audio_stream = io.BytesIO(audio_bytes)
    try:

        # Pass the file-like object directly to the OpenAI API
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_stream
        )

        transcription_text = response.text if hasattr(response, 'text') else "No transcription attribute found."
        return transcription_text

    except openai.BadRequestError as e:
        # エラーハンドリング
        print(f"Failed to transcribe audio: {e}")
        return "音声の転写に失敗しました。"

def transcribe_audio_to_text3(audio_bytes):
    # Create a temporary file and write the audio bytes to it
    with NamedTemporaryFile(mode='w+b', suffix=".mp3") as temp_file:
        temp_file.write(audio_bytes)
        temp_file.seek(0)  # Rewind the file to the beginning

        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=temp_file.file  # Pass the file descriptor directly
        )

    # Assuming `response` has an attribute `text` with the transcribed content
    transcription_text = response.text if hasattr(response, 'text') else "No transcription attribute found."

    return transcription_text

def play_audio(byte_stream):
    # Base64エンコードされた音声データを取得
    base64_audio = base64.b64encode(byte_stream.read()).decode()

    # カスタムのHTMLとJavaScriptを使って音声を自動再生
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/ogg;base64,{base64_audio}" type="audio/ogg">
        Your browser does not support the audio element.
    </audio>
    """

    # StreamlitにカスタムのHTMLを埋め込む
    html(audio_html, height=0)  # height=0でウィジェットの表示を隠す


def main():
    llm = ChatOpenAI(model="gpt-4-1106-preview", temperature=0, openai_api_key=openai.api_key)
    #llm = ChatOpenAI(model="gpt-4-1106-preview",temperature=0)

    st.set_page_config(
        page_title="せいぶつはかせのChatGPT",
        page_icon="🤗"
    )
    st.header("Dr. Biology's ChatGPT 🤗")

    st.image("DALL·E 2023-11-19 19.04.23 - An anime-style, chibi (two-head-tall) female biologist character .png")

    # チャット履歴の初期化
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="生物のことならなんでも知っている小学生の女の子生物博士として振る舞います。ユーザーの質問に対して、みんなが驚くような新しい動物のトリビアを教えてください。トリビアの内容は150文字以内で伝える必要があります。口語的に話して、優しい友達のような話し方をしてください。")
            #SystemMessage(content="You are a helpful assistant.")
        ]

    # Record audio using Streamlit widget
    audio_bytes = audio_recorder(pause_threshold=1.0)
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # save audio file to mp3
        with open(f"audio_{timestamp}.mp3", "wb") as f:
            f.write(audio_bytes)

    # Convert audio to text using OpenAI Whisper API
    if audio_bytes:
        transcript = transcribe_audio_to_text(audio_bytes)
        #st.write("Transcribed Text:", transcript)

        # ユーザーの入力を監視
        user_input = st.text_input("メッセージを入力してね！", value=transcript)
        if user_input:
        #if user_input := st.write("Transcribed Text:", transcript):
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("ChatGPT is typing ..."):
                response = llm(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))
            # OpenAIのText-to-Speech APIを使用して応答を音声に変換openai.audio.speech.create
            try:
                audio_response = openai.audio.speech.create(
                    model="tts-1",
                    voice="nova",
                    input=response.content,
                )

                # 取得した音声データをバイトストリームに変換し、再生
                byte_stream = io.BytesIO(audio_response.content)
                # 自動再生するための関数を呼び出す
                play_audio(byte_stream)
            except Exception as e:
                st.error(f"音声生成に失敗しました: {e}")

        # チャット履歴の表示
        messages = st.session_state.get('messages', [])
        for message in messages:
            if isinstance(message, AIMessage):
                with st.chat_message('assistant'):
                    st.markdown(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message('user'):
                    st.markdown(message.content)
            # SystemMessageの処理を削除またはコメントアウト
            #else:  # isinstance(message, SystemMessage):
                #st.write(f"System message: {message.content}")

if __name__ == '__main__':
    main()