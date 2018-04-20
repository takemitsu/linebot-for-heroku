# -*- coding: utf-8 -*-
import os
import sys
import json

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage,
    ConfirmTemplate, MessageTemplateAction,
)

app = Flask(__name__)

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')

if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')


line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
print(channel_secret)
print(channel_access_token)

@app.route("/", methods=['GET'])
def index():
    return channel_secret + "\n" + channel_access_token

@app.route("/callback", methods=['POST'])
def callback():

    print("-")
    for header in request.headers:
        print(header)
    print("- -")
    #for key in request.headers:
    #    print(str(key) + ' : ' + str(request.headers[key]))
    print(request.get_json())
    print("-")

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("InvalidSignatureError")
        abort(400)
    except:
        import traceback
        traceback.print_exc()

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    secondMessage = TextSendMessage(text=u"改行のテストです\nエコーされてますか")
    message_confirm = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text=u"よろしいですか",
            actions=[
                MessageTemplateAction(
                    label=u'はい',
                    text=u'はい',
                ),
                MessageTemplateAction(
                    label=u'いいえ',
                    text=u'いいえ'
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text=event.message.text),
            secondMessage,
            message_confirm,
        ]
)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
