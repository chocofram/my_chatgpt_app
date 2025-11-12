# Dr. Biology's ChatGPT 🤗

生物のことならなんでも知っている、音声対話可能なAIチャットボットアプリケーションです。

## 概要

このアプリケーションは、Streamlitを使用して構築された音声対話型チャットボットです。OpenAIのGPT-3.5-turbo、Whisper、Text-to-Speech APIを活用し、ユーザーと自然な音声会話を実現します。

### 主な特徴

- 🎤 **音声入力**: マイクから直接質問を録音できます
- 🔊 **音声応答**: AIの回答を音声で自動再生します
- 🧬 **生物学の専門知識**: 生物に関する興味深いトリビアを提供します
- 💬 **会話履歴管理**: 過去の会話を記録・表示します
- 🤖 **親しみやすいキャラクター**: 小学生の女の子生物博士として振る舞います

## 必要要件

- Python 3.7以上
- OpenAI APIキー
- インターネット接続

## インストール

1. リポジトリをクローンします：
```bash
git clone https://github.com/yourusername/my_chatgpt_app.git
cd my_chatgpt_app
```

2. 必要なパッケージをインストールします：
```bash
pip install -r requirements.txt
```

## セットアップ

### OpenAI APIキーの設定

Streamlit Community Cloudでデプロイする場合は、以下の手順でAPIキーを設定してください：

1. Streamlit Community Cloudのダッシュボードにアクセス
2. アプリの設定から「Secrets」を選択
3. 以下の形式でAPIキーを追加：

```toml
[OpenAIAPI]
openai_api_key = "your-api-key-here"
```

ローカルで実行する場合は、`.streamlit/secrets.toml`ファイルを作成し、上記の内容を記述してください。

## 使い方

1. アプリケーションを起動します：
```bash
streamlit run my_chatgpt_app.py
```

2. ブラウザでアプリケーションが開きます（通常は`http://localhost:8501`）

3. 使用方法：
   - 🎤 録音ボタンをクリックして質問を話します
   - 自動的に音声がテキストに変換されます
   - テキスト入力フィールドで内容を確認・編集できます
   - AIが回答を生成し、音声で応答します
   - 会話履歴は画面に表示されます

## 技術スタック

- **Streamlit**: Webアプリケーションフレームワーク
- **LangChain**: LLMアプリケーション開発フレームワーク
- **OpenAI API**:
  - GPT-3.5-turbo: 会話生成
  - Whisper: 音声からテキストへの変換
  - TTS (Text-to-Speech): テキストから音声への変換
- **audio-recorder-streamlit**: 音声録音ウィジェット

## 依存パッケージ

```
streamlit
langchain==0.0.336
openai==1.3.2
audio_recorder_streamlit==0.0.8
```

## プロジェクト構造

```
my_chatgpt_app/
├── my_chatgpt_app.py          # メインアプリケーション
├── requirements.txt           # 依存パッケージリスト
├── README.md                  # このファイル
├── LICENSE                    # ライセンス情報
└── DALL·E 2023-11-19 19.04.23 - An anime-style, chibi (two-head-tall) female biologist character .png  # キャラクター画像
```

## 機能詳細

### 音声認識機能
- OpenAIのWhisper APIを使用して高精度な音声認識を実現
- 録音された音声は自動的にテキストに変換されます

### チャット機能
- GPT-3.5-turboを使用した自然な会話生成
- システムプロンプトにより、生物学専門の親しみやすいキャラクターを実現
- 150文字以内の簡潔で分かりやすい回答

### 音声合成機能
- OpenAIのTTS APIを使用した自然な音声生成
- 回答が生成されると自動的に音声で再生されます

## 注意事項

- OpenAI APIの使用には料金が発生する場合があります
- マイクの使用許可が必要です
- 安定したインターネット接続が必要です

## トラブルシューティング

### 音声が録音できない場合
- ブラウザでマイクの使用許可を確認してください
- HTTPSまたはlocalhostでアクセスしていることを確認してください

### APIエラーが発生する場合
- OpenAI APIキーが正しく設定されているか確認してください
- APIキーに十分なクレジットがあるか確認してください
- インターネット接続を確認してください

## ライセンス

このプロジェクトのライセンスについては、[LICENSE](LICENSE)ファイルを参照してください。

## 貢献

プルリクエストは歓迎します。大きな変更の場合は、まずissueを開いて変更内容を議論してください。

## 作者

このアプリケーションは学習・デモンストレーション目的で作成されました。

---

**Enjoy chatting with Dr. Biology! 🧬✨**
