# Flask Echo

Sample echo-bot using [Flask](http://flask.pocoo.org/)

## Getting started Heroku line ccho bot

> 前提: git で commit しとく

```
# heroku にログイン
heroku login

# heroku プロジェクト作成
heroku create

# config セット
heroku config:set LINE_CHANNEL_SECRET="YOUR CHANNEL SECRET"
heroku config:set LINE_CHANNEL_ACCESS_TOKEN="YOUR ACCESS TOKEN"

# heroku プロジェクトに push
git push heroku master

# web 1 台で動かすよ設定
heroku ps:scale web=1

# heroku url 開く(このシステムではCONFIGで設定した CHANNEL SECRET と ACCESS TOKEN が表示されるハズ)
# やんなくてもいい。
heroku open
```

## Original URL

- https://github.com/line/line-bot-sdk-python
- https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo
- https://pypi.org/project/line-bot-sdk/
