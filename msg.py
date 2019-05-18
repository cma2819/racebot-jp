# ヘルプメッセージ

MSG_HELP = '''```
ゼルダ日本サーバー向けのレース補助Botです。

# コマンド一覧
  - [!isrunning]: 起動している場合、応答します。
  - [!start]: 実行されたチャンネルでレースを生成します。
  - [!restart]: レースを作り直します。参加者をリセットする場合などに実行します。
  - [!join]: レースに参加します。
  - [!entrant]: レースの参加者を確認します。
  - [!count]: 5秒前からのカウントダウンを開始します。
  - [!done]: ゴールをレースに通知します。
  - [!result]: レースの結果を確認します。
  - [!over]: レースを終了します。

  - [!ootbingo]: 次回のカウントダウン時に、「時のオカリナ」ビンゴのURLを同時に送信します。
  - [!mmbingo]: 次回のカウントダウン時に、「ムジュラの仮面」ビンゴのURLを同時に送信します。
  - [!unset_bingo]: 上記ビンゴの設定をすべて解除します。
  - [!seed]: ビンゴ等で利用できる、5～6桁のランダムな整数を送信します。

  - [!status]: ビンゴの設定状況等、現在の設定を確認します。

  - [!racebot]: 本ヘルプを表示します。

機能追加のご要望はcma2819#2218まで。
```'''

# *** メッセージ ***
# 起動時
MSG_RUN_THIS_BOT = 'RaceBotが起動しました。'
# レース生成時
MSG_RACE_CREATE = 'このチャンネルでレースを開始します.'
MSG_CONF_EXIST = '''
このチャンネルでは既にレースが作られています.
レースを作り直す場合は`!restart`を使用してください.
'''
MSG_RE_START = 'レースを再度開始します.'
# 生存確認
MSG_BOT_IS_RUNNING = 'RaceBotは起動しています。'
# レースが存在しない
MSG_NOT_START_RACE = 'このチャンネルでレースが作られていません.レースを始めるには`!start`を使用してください.'
# Join
MSG_USER_JOIN = 'が参加しました！'
MSG_CONF_JOINED = 'は既に参加しています.'
# Entrant
MSG_ENTRANT = '参加者を一覧表示します.'
# COUNTDOWN系
MSG_COUNT_DOWN_PREPARE = 'カウントダウンを開始します！レース参加者はスタートに備えてください！'
MSG_COUNT_DOWN_GO = 'GO!!'
MSG_NO_ENTRANT = 'レースに誰も参加していません.'
# ビンゴ系
MSG_MAKE_SEED_EXPL = 'ランダムなシード値を生成します：'
MSG_SET_OOT_BINGO = '次のレース開始時に、時のオカリナビンゴのURLを送信します。'
MSG_SET_MM_BINGO = '次のレース開始時に、ムジュラの仮面ビンゴのURLを送信します。'
MSG_UNSET_BINGO = 'ビンゴURLの送信をキャンセルしました。'
# URL
URL_OOT_BINGO = 'http://www.speedrunslive.com/tools/oot-bingo/?seed='
URL_MM_BINGO = 'http://www.speedrunslive.com/tools/mm-bingo/?seed='
# ステータス
MSG_STATUS = '現在の設定状況を表示します。'
# 終了
MSG_RACE_OVER = 'レースを終了しました.'