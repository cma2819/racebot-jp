#coding: utf-8
from enum import Enum
from datetime import datetime as dt
from datetime import timedelta as td

"""
レース情報を管理するクラス.
"""
class Race():

    def __init__(self, channel):
        self.channel = channel
        self.status = Race.RaceStat.READY
        # レースメンバー
        self.entrant = []
        # レース結果（名前と記録のTupleで保持する）
        self.results = []
        # 時オカビンゴ準備状態
        self.bingoflag_oot = False
        # ムジュラビンゴ準備状態
        self.bingoflag_mm = False
    
    """
    レースメンバーにDiscrodのUserを追加する.
    既にUserがentrantに存在する場合、Falseを返却する.
    @return 結果
    """
    def join(self, dsc_user):
        if dsc_user not in self.entrant:
            self.entrant.append(dsc_user)
            return True
        else:
            return False

    def start(self):
        self.start_datetime = dt.now()
        self.status = Race.RaceStat.PROGRESS
        
    """
    @return 順位, タイム
    """
    def done(self, dsc_user):
        # 真っ先に現在時刻を取得しないと処理時間分ズレる
        now = dt.now()
        if dsc_user in self.entrant:
            results_time = format_timedelta(now - self.start_datetime)
            self.results.append((str(dsc_user), results_time))

            if len(self.results) == len(self.entrant):
                self.status = Race.RaceStat.FINISHED
            
            return len(self.results), results_time

    class RaceStat(Enum):
        READY = 1
        PROGRESS = 2
        FINISHED = 3

def format_timedelta(src_td):
    hours = str(int(src_td.seconds / 3600))
    minutes = str(int((src_td.seconds / 60) % 60))
    seconds = str(int(src_td.seconds % 60))
    
    return hours + ':' + minutes.zfill(2) + ':' + seconds.zfill(2)

if __name__ == '__main__':
    import time
    race = Race(123456789)
    race.start()
    time.sleep(10)
    race.done(None)