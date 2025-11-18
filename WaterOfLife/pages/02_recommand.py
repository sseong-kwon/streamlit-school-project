# pages/02_추천보기.py
import streamlit as st
from utils import load_data

st.title("🍶 02. 응답별 추천 결과 보기")

st.markdown(
    """
    설문에 참여한 사람들의 응답 중에서  
    특정 **닉네임/이니셜**을 선택해, 어떤 술이 추천되었는지 확인할 수 있습니다.
    """
)

st.markdown("---")

df = load_data()

if df.empty:
    st.info("아직 설문 데이터가 없습니다. 먼저 `01_설문하기`에서 설문을 제출해 주세요.")
else:
    # 닉네임 목록 만들기 (비어 있는 값은 '이름 없음'으로 처리)
    nicknames = df["nickname"].fillna("이름 없음").replace("", "이름 없음").tolist()
    unique_nicknames = sorted(set(nicknames))

    selected_nick = st.selectbox("닉네임/이니셜 선택", unique_nicknames)

    # 선택된 닉네임의 마지막 응답 1건만 조회
    filtered = df.copy()
    filtered["nickname_clean"] = filtered["nickname"].fillna("이름 없음").replace("", "이름 없음")
    person_rows = filtered[filtered["nickname_clean"] == selected_nick]

    if person_rows.empty:
        st.warning("선택한 닉네임의 응답을 찾을 수 없습니다.")
    else:
        latest = person_rows.iloc[-1]

        st.subheader(f"🙋‍♂️ {selected_nick} 님의 최신 응답")
        st.write(f"- 추천 주종: **{latest['recommended_type']}**")
        st.write(f"- 선호 맛/향: {latest['flavor']}")
        st.write(f"- 바디감: {latest['body']}")
        st.write(f"- 단맛 선호: {latest['sweetness']}")
        st.write(f"- 도수 범위: {latest['abv_min']} ~ {latest['abv_max']}%")
        st.write(f"- 마시는 상황: {latest['occasion']}")
        st.write(f"- 예산: {latest['budget']}")
        st.write(f"- 탄산 선호: {latest['carbonation']}")
        st.write(f"- 관심 주종: {latest['prefer_type'] if isinstance(latest['prefer_type'], str) else ''}")

        with st.expander("원본 응답 데이터 보기"):
            st.write(latest.to_frame().to_markdown())
