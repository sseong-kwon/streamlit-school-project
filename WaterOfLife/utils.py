# utils.py
import os
from datetime import datetime

import pandas as pd

DATA_PATH = "survey_data.csv"


def recommend_type(flavor, body, sweetness, abv, occasion, budget, carbonation, prefer_type):
    """취향에 따라 추천 주종을 간단히 결정하는 함수"""
    min_abv, max_abv = abv
    rec = "와인"  # 기본값

    if max_abv >= 35 and ("탄향/스모키" in flavor or "곡물/빵향" in flavor):
        rec = "위스키"
    elif "달콤함" in flavor and min_abv <= 20:
        rec = "전통주"
    elif "과일향" in flavor and min_abv <= 20:
        rec = "사케"

    # 선호 주종이 있으면 그 중 첫 번째를 우선 반영 (간단 버전)
    if prefer_type:
        rec = prefer_type[0]

    return rec


def load_data():
    """설문 데이터 불러오기 (없으면 빈 DataFrame 리턴)"""
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    return pd.DataFrame()


def save_response(nickname, flavor, body, sweetness, abv, occasion, budget, carbonation, prefer_type, recommended):
    """새 응답 한 건을 CSV에 추가 저장"""
    from utils import DATA_PATH  # 순환 import 방지용

    new_row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nickname": nickname,
        "flavor": ";".join(flavor),
        "body": body,
        "sweetness": sweetness,
        "abv_min": abv[0],
        "abv_max": abv[1],
        "occasion": occasion,
        "budget": budget,
        "carbonation": carbonation,
        "prefer_type": ";".join(prefer_type) if prefer_type else "",
        "recommended_type": recommended,
    }

    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])

    df.to_csv(DATA_PATH, index=False)
