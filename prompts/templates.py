TEMPLATES = {

    "cot_got_stepwise_mixed": [
    {
        "role": "system",
        "content": ("""
            너는 문법 오류 교정 도구야.\n
            입력된 문장에서 띄어쓰기, 문법, 문장부호, 철자 오류를 교정해.\n
            문장을 문법적으로 올바르게 만들기 위해 최소로 수정해.\n
            최소한 적은 단어만 변경해\n
            문맥 상 필요한 부분만 수정해\n
            의미를 바꾸거나, 새로운 정보를 추가하거나, 기존 정보를 삭제해서는 안돼\n
            최종 교정된 문장만 출력해.\n
           """
        )
    },

    # CoT-only 예시
    {"role": "user", "content": "입력: 이과기만한글제시해서욥"},
    {"role": "assistant", "content": "이과 기만한 글 게시했어요."},

    # CoT
    {"role": "user", "content": "입력: 시간이좀걸릴꺼가타요"},
    {"role": "assistant", "content": "시간이 좀 걸릴 것 같아요."},

    # GoT
    {"role": "user", "content": "입력: 과학강이정리노트를스게써요"},
    {"role": "assistant", "content": "과학 강의 정리 노트를 쓰겠어요!"},

    # GoT + 조사 오류
    {"role": "user", "content": "입력: 그사람이 느낌아 쪼끔 이상했던 거 같아요"},
    {"role": "assistant", "content": "그 사람이 느낌이 조금 이상했던 것 같아요."},

    {"role": "user", "content": "입력: 허위사실을제기하지마쇼"},
    {"role": "assistant", "content": "허위사실을 제시하지 마세요."},

    # 입력 자리
    {"role": "user", "content": "입력: {text}"}
]
}