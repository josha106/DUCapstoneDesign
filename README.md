# DU Chatbot PI

## 만들게 된 계기
 현재 동서울대학교에도 chatbot이 있지만, database 기반의 한정적인 답변만 주는 chatbot이다. 이러한 문제점을 인식하고, 자연어 처리에 대한 공부를 바탕으로 더욱 업그레이드된, LLM을 사용한 chatbot을 만들 수 있을 것이라고 생각했다. 
(https://dacon.io/competitions/official/236295/overview/description/)

## 무엇이 다른가요?
 기존의 chatbot과는 다르게 llm 모델을 사용하면 훨씬 많은 양의 질문(query)에 대해 유연한 답변을 얻을 수 있다. 이는 transformer의 decoder를 사용한 생성형 모델을 사용했기 때문이다. 예를 들어, "컴퓨터정보과의 전화번호는?", "컴정과의 전화번호는?", "컴정과의 번호?"와 같이 같은 답에 대한 다른 유형의 질문에 대해 유연한 답변을 얻을 수 있다.

 ## Hallucination과 해결방안
  decoder 모델의 가장 큰 문제점은 Hallucination이다. Hallucination이란 decoder 기반의 LLM이 하는 거짓말이라고 생각하면 쉽다. 이 모델은 지금까지의 query로 다음 단어를 예측하기 때문에 답변에 대해서 옳고 그름을 판단하지 못한다. 이러한 LLM의 hallucination을 보완하기 위해 model을 특정 task로 fine tuning하는 PEFT기법(QLoRA)과 RAG 기법을 사용했다. 

  아래는 캡스톤디자인에서 사용했던 포스터이다.
<img src="https://github.com/user-attachments/assets/098ce8e2-2bdf-4165-975e-ed1f92ce0c77" width="200" height="400"/>
## YouTube 튜토리얼


아래의 영상을 시청하시면서 따라서 진행하세요.

[![데모 영상](https://img.youtube.com/vi/VkcaigvTrug/0.jpg)](https://youtu.be/VkcaigvTrug)



## License
```
MIT License

Copyright (c) 2024, 테디노트

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of
