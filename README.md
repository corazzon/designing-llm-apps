## 실무로 통하는 LLM 어플리케이션 설계

![Cover Image](cover.png)

* 원서 : Designing Large Language Model Applications: A Holistic Approach to LLMs
* 원서 github : https://github.com/piesauce/llm-playbooks
* amazon : https://www.amazon.com/Designing-Large-Language-Model-Applications/dp/1098150503

### 실습 데이터셋

#### 캐나다 의회 데이터셋 

* 이 데이터셋은 openparliament.ca에서 수집한 캐나다 의회 회의록을 포함하고 있습니다.
 * 데이터셋은 다음 링크에서 다운로드할 수 있습니다:
 * https://huggingface.co/datasets/hudson-labs/canada-training/tree/main

* 데이터셋은 다음과 같은 구성 요소로 이루어져 있습니다:
 * bills_json: 캐나다 의회에 제출된 각 법안의 전체 본문을 포함합니다.
 * political_speeches.json: 의회 진행 중 국회의원(MP, Member of Parliament)들의 발언 회의록을 포함합니다.

#### S&P 500 기업들의 연차 보고서(10-K)

* https://huggingface.co/datasets/jlohding/sp500-edgar-10k
* 각 섹션에 대한 설명은 다음 위키백과 페이지에서 확인할 수 있습니다:
 * https://en.wikipedia.org/wiki/Form_10-K