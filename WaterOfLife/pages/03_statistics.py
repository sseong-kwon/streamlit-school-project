# pages/03_실시간통계.py
import streamlit as st
from utils import load_data

st.title("📊 03. 실시간 설문 통계")

st.markdown(
    """
    발표자가 화면을 공유하고,  
    실시간으로 들어오는 설문 결과를 통계/그래프로 확인하는 페이지입니다.
    """
)

st.markdown("---")

df = load_data()

if df.empty:
    st.info("아직 설문 응답이 없습니다. 청중에게 `01_설문하기` 페이지에서 설문에 참여하도록 안내해 주세요.")
else:
    st.subheader(f"현재까지 응답 수: **{len(df)}명**")

    with st.expander("📋 최근 응답 일부 보기", expanded=False):
        st.dataframe(df.tail(10))

    # 1) 추천 주종 분포
    st.subheader("🍶 추천 주종 분포")
    type_counts = df["recommended_type"].value_counts()
    st.bar_chart(type_counts)

    # 2) 단맛 선호도 분포
    st.subheader("🍭 단맛 선호도 분포")
    sweet_counts = df["sweetness"].value_counts().sort_index()
    st.bar_chart(sweet_counts)

    # 3) 마시는 상황 분포
    st.subheader("🎯 마시는 상황(occasion) 분포")
    occ_counts = df["occasion"].value_counts()
    st.bar_chart(occ_counts)

    # 4) 예산 분포
    st.subheader("💸 예산 분포")
    budget_counts = df["budget"].value_counts().sort_index()
    st.bar_chart(budget_counts)

    st.caption("※ 발표 중에는 브라우저 새로고침(🔄)을 눌러 최신 응답을 반영해 주세요.")
