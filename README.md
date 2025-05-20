# 🧪 MixUp_팀명 : TOBIGGY

본 레포지토리는 Grammar Error Correction Promptathon  실험을 재현하고 확장하기 위한 코드 및 가이드를 제공합니다.


## 📌 프로젝트 개요

* **목표**: Solar Pro API를 활용하여 프롬프트 만으로 한국어 맞춤법 교정 성능을 개선한다. 
* **접근 전략**: 
[intro]
  Grammer Error Correction에서는 과도한 수정으로 인해 성능이 떨어지는 경우가 많다. 그렇기에 few shot 프롬프트와 temperature, top_p 파라미터를 통해 LLM의 
과도한 문장 수장을 방지하면서도, 틀린 단어, 띄어쓰기 그리고 문장 부호등을 적절히 교정하고자 했다. 

[system prompt]
  system 프롬프트에서는 LLM에게 '문법 오류 교정 도구'라는 역할을 부여하고 띄어쓰기, 문법, 문장부호, 철자 오류를 교정하라고 명령하였다. 또한, 과도한 수정을
방지하기 위해 "최소한 적은 단어만 변경해", "문맥상 필요한 부분만 수정해", "의미를 바꾸거나, 새로운 정보를 추가하거나, 기존 정보를 삭제해서는 안돼"와 같은 
명령을 추가하였다. 최종적으로 교정된 문장만을 받고자 "최종 교정된 문장만 출력해"를 추가하였다. 

[few shot prompt]
  few shot 프롬프트에서는 이전 실험을 통해 분석한 오류들 중 명사 간 띄어쓰기 부족, 줄임말 미교정, 된소리 미교정,  조사 오류 미교정, 유사 단어 미교정등을 
보완하고자 하였으며, 데이터의 상당한 부분이 교육 관련 커뮤니티에서 발생하였음을 추정하여 이과, 과학 강의, 정리 노트 등의 단어를 수정하도록 few shot에 추가하였다. 

[parameter]
  마지막으로 temperature를 0.0으로 낮춰 문장이 창의적으로 수정되고 불필요한 부분이 추가되는 것을 방지하였으며 top_p를 0.85로 높여 단어 선택의 폭을 높였다.
이러한 파라미터 조정은 문장의 기본 골조를 유지하면서도 기본적인 오타나 줄임말에 대해 유연하게 대처할 수 있도록 하였다. 


  * ex. 오류 유형별 대응 전략 수립 → 반복 실험을 통해 개선
* **주요 실험 내용**:

  * train,validation에서의 주오류 확인:
  random seed를 42, 21, 10로 데이터의 toy_size를 100,150,200으로 조정을 하며 기본 프롬프트로 문장을 수정했을 때 어떤 오류들이 고쳐지지 않는지 확인함함.(temperature=0.3, top_p=0.0)

  * 주오류 분석 및 test에서의 주오류 확인:
  위의 과정으로 명사 간 띄어 쓰기 부족, 줄임말 미교정, 된소리 미교정, 조사 오류 미교정, 유사 단어 미교정 등을 확인하였으며 test data set에서도 submission_baseline.csv를 통해 완전히 수정되지 않았음을 확인함. 추가적으로 불필요한 수정이 발생한 것 또한 확인함. 

  * role base system prompt vs basic system prompt:
   유형별로 오류를 정리하고 role base의 system 프롬프트 + few shot vs 간단한 역할 부여를 한 system 프롬프트 + few shot을 비교한 결과로 후자의 LLM의 추론 성능에 문장 수정을 맡긴 프롬프트의 성능이 더 뛰어남을 확인함

  * parameter 실험:
   temperature=0.0, 0.01, 0.03, top_p=0.8,0.85,0.9 으로 train, validation set에서 9번 실험을 진행하고 temperature=0.0, top_p=0.85에서 가장 성능이 뛰어남을 확인함.(random seed=42)
---

## ⚙️ 환경 세팅 & 실행 방법

### 1. 사전 준비 

```bash
git clone https://github.com/your-org/your-repo.git
cd your-repo/experiment
```

### 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 실험 실행

```bash
python run_experiment.py --input sample_input.txt --output result.json
```

> 📎 실행 옵션 (예시):
> `--input`: 실험 대상 파일
> `--output`: 결과 저장 파일 경로

---


## 🚧 실험의 한계 및 향후 개선

* **한계**:

  * 줄임말, 원래 단어와 먼 오타 등 맞춤법 관련 누락되는 오류 존재
  * 문장 개선의 불안정성 및 낮은 interpretability
* **향후 개선 방향**:

  * RAG를 통한 정확한 맞춤법 DB 구축 → 맞춤법 오류 발생 시 유사도 높은 문장에서의 맞춤법 재확인 및 수정 진행
  * User Feedback loop를 통한 교정 정확도 향상 및 수정된 부분에 대한 추가 설명 제공

---

## 📂 폴더 구조

```
📁 code/
├── main.py              # 메인 실행 파일
├── config.py            # 설정 파일
├── requirements.txt     # 필요한 패키지 목록
├── __init__.py         # 패키지 초기화 파일
├── utils/              # 유틸리티 함수들
│   ├── __init__.py     # utils 패키지 초기화
│   ├── experiment.py   # 실험 실행 및 API 호출
│   └── metrics.py      # 평가 지표 계산
└── prompts/            # 프롬프트 템플릿 저장
    ├── __init__.py     # prompts 패키지 초기화
    └── templates.py    # 프롬프트 템플릿 정의
```
