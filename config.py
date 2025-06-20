"""
Application configuration and constants
"""
from typing import Dict

# Application settings
APP_TITLE = "専門家LLMアプリ"
APP_ICON = "🤖"

# LLM settings
DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_TEMPERATURE = 0.7

# Expert profiles
EXPERT_PROFILES: Dict[str, str] = {
    "医療専門家": (
        "あなたは経験豊富な医師です。医学的な質問に対して、正確で分かりやすい説明を提供してください。"
        "ただし、診断や治療法の決定は実際の医師の診察が必要であることを必ず伝えてください。"
    ),
    "法律専門家": (
        "あなたは経験豊富な弁護士です。法律に関する質問に対して、一般的な法的知識を提供してください。"
        "ただし、具体的な法的助言には実際の弁護士への相談が必要であることを必ず伝えてください。"
    ),
    "金融専門家": (
        "あなたは経験豊富なファイナンシャルアドバイザーです。金融や投資に関する質問に対して、"
        "バランスの取れた情報を提供してください。ただし、投資判断は自己責任であることを必ず伝えてください。"
    )
}

# UI messages
SIDEBAR_INFO = (
    "このアプリは選択した専門家の視点からAIが回答を生成します。\n\n"
    "重要な決定を行う際は、必ず実際の専門家にご相談ください。"
)
API_KEY_ERROR = "OpenAI APIキーを設定してください"
EMPTY_QUESTION_WARNING = "質問を入力してください"
GENERATING_RESPONSE = "回答を生成中..."
RESPONSE_HEADER = "回答:"

# UI layout settings
COLUMN_RATIOS = [1, 3]
TEXT_AREA_HEIGHT = 100