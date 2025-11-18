# pages/01_설문하기.py
import streamlit as st

from utils import recommend_type, save_response

st.title("📝 01. 술 취향 설문하기")

st.markdown(
    """
    간단한 설문을 바탕으로  
    당신의 취향에 맞는 술 스타일을 추천해 드립니다.
    """
)

st.markdown("---")

with st.form("preference_form"):
    nickname = st.text_input("닉네임 또는 이니셜 (선택)", "")

    flavor = st.multiselect(
        "좋아하는 맛/향을 골라보세요. (복수 선택 가능)",
        ["과일향", "꽃향", "탄향/스모키", "곡물/빵향", "쌉쌀함", "고소함", "달콤함"],
        default=["과일향"]
    )

    body = st.selectbox(
        "술의 무게감(바디감)은 어떤 걸 좋아하나요?",
        ["가볍고 산뜻한 편", "중간 정도", "무겁고 진한 편"]
    )

    sweetness = st.select_slider(
        "단맛 선호도는 어느 정도인가요?",
        options=["거의 없음", "약간 단 편", "적당히 단 편", "꽤 단 편", "아주 달게"],
        value="약간 단 편"
    )

    abv = st.slider(
        "편하게 즐기기 좋은 도수 범위는?",
        min_value=5,
        max_value=50,
        value=(10, 25),
        step=1
    )

    occasion = st.selectbox(
        "주로 어떤 상황에서 마실 술인가요?",
        ["혼술용", "친구들과 모임", "식사와 곁들이기", "선물용", "데이트/분위기용"]
    )

    budget = st.select_slider(
        "1병 기준 예산은 어느 정도를 생각하시나요?",
        options=["~2만 원", "2~5만 원", "5~10만 원", "10만 원 이상"],
        value="2~5만 원"
    )

    carbonation = st.radio(
        "탄산이 있는 술을 좋아하나요?",
        ["상관없음", "탄산 있는 게 좋다", "탄산 없는 게 좋다"],
        index=0,
        horizontal=True
    )

    prefer_type = st.multiselect(
        "특히 관심 있는 주종이 있나요? (비워두면 상관없음)",
        ["위스키", "사케", "전통주", "와인"],
        default=[]
    )

    submitted = st.form_submit_button("✨ 설문 제출 & 추천 받기")

if submitted:
    recommended = recommend_type(
        flavor, body, sweetness, abv, occasion, budget, carbonation, prefer_type
    )
    save_response(
        nickname, flavor, body, sweetness, abv,
        occasion, budget, carbonation, prefer_type,
        recommended
    )

    st.success("설문이 제출되었습니다! 아래 추천 결과를 확인해 주세요 😊")

    st.markdown("---")
    st.subheader("✅ 추천 결과")

    st.markdown(f"**당신에게 어울리는 주종 스타일:** 👉 **{recommended}**")

    st.caption("※ 실제 브랜드/제품명이 아니라, 주종 & 스타일 유형에 대한 추천입니다.")
