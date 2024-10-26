# DU Chatbot PI


## 만들게 된 계기
 현재 동서울대학교에도 chatbot이 있지만, database 기반의 한정적인 답변만 주는 chatbot이다. 이러한 문제점을 인식하고, 자연어 처리에 대한 공부를 바탕으로 더욱 업그레이드된, LLM을 사용한 chatbot을 만들 수 있을 것이라고 생각했다. 
([동서울대학교 홈페이지](https://www.du.ac.kr/main.do))  


## 무엇이 다른가요?
 기존의 chatbot과는 다르게 llm 모델을 사용하면 훨씬 많은 양의 질문(query)에 대해 유연한 답변을 얻을 수 있다. 이는 transformer의 decoder를 사용한 생성형 모델을 사용했기 때문이다. 예를 들어, "컴퓨터정보과의 전화번호는?", "컴정과의 전화번호는?", "컴정과의 번호?"와 같이 같은 답에 대한 다른 유형의 질문에 대해 유연한 답변을 얻을 수 있다.  


 ## Hallucination과 해결방안
  decoder 모델의 가장 큰 문제점은 Hallucination이다. Hallucination이란 decoder 기반의 LLM이 하는 거짓말이라고 생각하면 쉽다. 이 모델은 지금까지의 query로 다음 단어를 예측하기 때문에 답변에 대해서 옳고 그름을 판단하지 못한다. 이러한 LLM의 hallucination을 보완하기 위해 model을 특정 task로 fine tuning하는 PEFT기법(QLoRA)과 RAG 기법을 사용했다. 

  아래는 캡스톤디자인 경진대회에서 사용했던 포스터이다.  
<img src="https://github.com/user-attachments/assets/098ce8e2-2bdf-4165-975e-ed1f92ce0c77" width="600" height="800"/>

## 직면한 문제점들
 이론상으로는 쉽게 만들 수 있을 것 같았으나, 막상 만들면서 직면한 문제들이 많다.
1. streamlit의 버전 충돌
 stremalit을 사용하기 위해서 버전 설정 해주는 것이 굉장히 시간을 많이 잡아먹었다. 굉장히 한정적인 버전만 사용해야 하는데, python은 꼭 3.11.x 버전으로 설정해주길 바란다.
2. GPU 성능
 LLM 분야가 GPU의 성능을 중요시 한다고 이론적으로 알고는 있었지만, 피부로 처음 느끼게 되었다. 처음에 맥을 서버로 이용하여 챗봇에게 질문했더니 inference time이 1분씩 걸렸다. 질문 한 번 하면 1분동안 멍때리고 있어야 했다. 컴퓨터소프트웨어학과의 4060ti 16GB 컴퓨터를 지원받아서 다시 실행시켰을 때, inference time은 약 8초로 줄어들었다.  

 당연히 이 외에도 많은 자잘한 문제점들이 있었지만, 가장 극적이고 피부로 와닿았던 문제들이었다. 

 ## 느낀점
  처음에는 dacon 챗봇 대회를 나간 경험을 바탕으로 쉽게 모델을 웹상에 배포할 수 있다고 생각했다. 그러나 크고 작은 문제들을 직면했고(특히 inference time), 그럴 때마다 팀원들 덕분에 쉽게 해결할 수 있었던 것 같다. 2개월 동안 학교 챗봇이라는 큰 프로젝트를 함께 해결할 수 있어서 즐거운 시간이었다.

   

## 참고한 YouTube
 기본적인 ollama, streamlit에 대한 구상은 해당 유튜브를 참고하여 만들었고, Dacon 챗봇 대회에 나가서 쌓은 경험과 내 코드를 합쳐서 작품을 출시하게 되었다. 너무 쉽게 설명해주시고, 코드도 정리되어 있어서 쉽게 따라할 수 있었다. 

[![데모 영상](https://img.youtube.com/vi/VkcaigvTrug/0.jpg)](https://youtu.be/VkcaigvTrug)



## License
```
MIT License

Copyright (c) 2024, 테디노트

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of
