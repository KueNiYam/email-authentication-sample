이메일 인증 과정 구현 (캡스톤 사전 조사)

## 대략적인 설명

1. 이메일로 인증 토큰 발송
 
    - HTML FORM 형식으로 전송하여 이용자가 간단히 SUBMIT 버튼을 누르는 것만으로 쉽게 인증할 수 있도록 한다.

2. 이용자가 SUBMIT 버튼을 누르면 서버에 인증 토큰 전송(POST 요청)

3. 서버에서 받은 인증 토큰이 전송한 인증 토큰과 같은지 확인한 후 같으면 인증 완료

## 헤맨 부분

이메일에 삽입된 자바스크립트 코드는 작동하지 않을 수 있다. 주의하도록 하자.

FORM 태그는 name=rintiantta&region=seoul 식으로 데이터를 전송한다(serialize()). 그런데 Flask의 requests.get_json() 함수는 '{"name":"rintiantta", "region":"seoul"}'과 같은 json 형식만 받는다. serialize된 데이터는 requests.form['key']와 같은 방법으로 얻을 수 있다.
