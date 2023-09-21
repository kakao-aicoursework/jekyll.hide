kakao_social = """
카카오 소셜:

#이해하기
이 문서는 카카오톡 소셜 API를 소개합니다.

#기능 소개
카카오톡 소셜 API는 서비스의 소셜 기능 구현을 위한 사용자의 카카오톡 프로필과 친구 정보를 제공합니다. 제공받은 카카오톡 친구 정보를 토대로 카카오톡 메시지를 보낼 수도 있습니다.

#카카오톡 프로필
사용자의 카카오톡 프로필 정보를 제공하는 카카오톡 프로필 API를 제공합니다. 카카오 API를 통해 제공되는 프로필은 카카오계정의 프로필과 카카오톡의 프로필 두 가지이며, 두 프로필은 서로 일치하지 않을 수 있습니다. 서비스에서 카카오톡과 밀접하게 관련된 소셜 기능을 구현하기 위해 카카오톡의 프로필을 지정하여 제공받고 싶은 경우 카카오톡 프로필 API를 사용합니다.
참고: 카카오계정 프로필
카카오 로그인의 사용자 정보 가져오기 API를 사용하면 카카오계정의 프로필 정보를 받을 수 있습니다. 사용자가 카카오톡 또는 카카오계정 관리 페이지의 [설정] > [카카오계정] > [내정보 관리] > [프로필 업데이트 설정] 메뉴에서 [프로필 정보를 항상 최신으로 유지합니다] 옵션을 켠 경우, 카카오계정 프로필 정보가 카카오톡 프로필 정보와 동일하게 유지됩니다.

#카카오톡 친구 정보
카카오톡 친구의 기본 정보와 프로필을 담은 데이터를 목록 형태로 제공합니다. 각 친구의 기본 정보는 카카오톡 메시지 전송 시 필요한 고유 ID(uuid) 값을 포함합니다.
카카오톡 친구 정보는 피커 또는 친구 목록 가져오기 API를 통해 제공받을 수 있습니다. 아래 표를 참고합니다.


구분 | 피커 |친구 목록 가져오기 API
설명 | 서비스에서 Kakao SDK를 통해 피커 호출 시,카카오에서 제공하는 친구 목록 피커 화면이 출력되고,사용자가 선택한 친구의 데이터를 서비스에 제공 | 서비스의 API 요청 및 응답을 통해 사용자의 카카오톡 친구 목록 데이터 제공
활용 |자체적인 친구 목록 UI 구현 없이 간편하게 카카오톡 친구 목록을 이용하고 싶은 경우 카카오톡 메시지 발송 등 사용자가 지정한 특정 친구의 데이터가 필요한 경우 | 서비스 UI에 맞춘 친구 목록을 직접 구현하여 제공하고 싶은 경우
친구 목록 UI | 구현 | 불필요 | 필요
사용 환경 | 웹, 앱 | 서버, 웹, 앱
지원 범위 | Kakao SDK for JavaScript, Android, iOS | REST API, Kakao SDK for JavaScript, Android, iOS, Flutter

#피커
피커는 Kakao SDK를 통해 간편하게 친구 목록 UI와 친구 정보를 제공받을 수 있는 기능입니다. 피커는 파라미터 설정을 통해 원하는 화면 표시 형태, 선택 유형, 구성 요소 지정 기능을 제공합니다. 또한 기기의 언어 설정에 따라 다국어를 지원합니다. 아래 표와 예시 이미지를 참고합니다.

기능 | 상세
화면 표시 형태 | 풀 스크린 또는 팝업, 비고: JavaScript SDK는 풀 스크린 형태만 제공
선택 유형 | 멀티 피커: 여러 대상 선택 가능, 선택 가능한 친구의 최대 및 최소 수 지정 가능 싱글 피커: 하나의 대상만 선택 가능
구성 요소 | 피커 화면 상단 제목 문구 변경, 내 프로필 표시 여부, 즐겨찾기 친구 표시 여부, 특정 친구 선택 불가 처리
다국어 지원 | 한국어, 영어, 일본어

#이용 정책

1.사용 권한 신청
피커와 친구 목록 가져오기 API는 사용 권한이 주어진 앱에서만 사용할 수 있습니다. 사용 권한 신청 방법은 아래와 같습니다.

-피커 또는 친구 목록 가져오기 API를 사용한 소셜 기능 구현
-권한을 받기 전에도 개발 및 테스트를 위해 팀원에 한해 기능 동작
-앱의 팀원뿐 아니라 일반 사용자를 대상으로 친구 정보를 받으려면 권한 필요
-앱의 팀원을 대상으로 기능이 정상 동작하는지 확인
-데브톡에서 [새글 쓰기] 클릭 후, [친구 API 사용 신청] 카테고리를 선택하여 신청 양식 작성

카카오 플랫폼 관리자가 신청 내용을 확인한 뒤 친구 목록 가져오기 API 사용 권한 제공 여부를 답변합니다. 검수를 거쳐 사용 권한을 받으면 서비스의 모든 사용자가 친구 목록 가져오기 API 기능을 이용할 수 있습니다. 또한 [내 애플리케이션] > [동의항목] > [개인정보]에서 [카카오 서비스 내 친구목록(프로필사진, 닉네임, 즐겨찾기 포함)] 항목을 [선택 동의]로도 설정할 수 있습니다. 사용 권한을 받은 후에도 피커의 친구 목록과 친구 목록 가져오기 API의 응답은 친구 정보 제공 조건을 만족하는 친구 정보만 포함하는 점에 유의합니다.

2.쿼터
카카오 API는 원활한 서비스 제공을 위해 월간 및 일일 쿼터(Quota, 사용량 제한)를 적용합니다. 현재 적용 중인 쿼터 정보는 쿼터에서 확인할 수 있습니다. 적용된 쿼터 한도를 상향하기 위해서는 협의 및 제휴가 필요하므로 별도 문의합니다.

3.프로필 공개 설정
사용자는 [이 서비스의 친구 목록에 나를 보여주기] 설정에서 각 서비스의 친구 목록에 자신을 노출할 것인지 설정할 수 있습니다. 해당 설정은 메시지 말풍선 하단의 [설정] 버튼, 또는 카카오톡 [설정] > [카카오계정] > [연결된 서비스 관리]의 각 앱 정보 페이지에 위치합니다. 메시지 말풍선의 경우, 설정 버튼이 발신자의 말풍선에는 노출되지 않고 수신자의 말풍선에만 노출됩니다.
프로필 공개 설정은 피커의 친구 목록과 친구 목록 가져오기 API 응답에 반영됩니다. 사용자가 [이 서비스의 친구 목록에 나를 보여주기]를 [비공개]로 설정했거나 [동의 철회]한 경우, 해당 사용자는 다른 사용자의 친구 목록 가져오기 응답에 포함되지 않습니다. 친구 목록 가져오기 응답의 친구 수에도 해당 사용자가 포함되지 않습니다.
카카오톡 메시지의 경우, 친구 목록 가져오기 API 응답으로 받은 uuid를 사용하므로, 프로필 공개 설정을 비공개로 설정한 사용자에게는 메시지를 보낼 수 없습니다.

4.친구 정보 제공 조건
피커의 친구 목록과 친구 목록 가져오기 API의 응답은 다음 조건을 모두 만족하는 친구만 포함합니다.

-친구가 앱과 연결된 상태일 것
-친구가 앱 연결 시 [카카오 서비스 내 친구 목록 제공] 동의 항목에 동의한 상태일 것
-친구가 숨김 또는 차단 친구가 아닐 것
-친구의 프로필 공개 설정이 공개 상태일 것

5.프로필 정보 제공 기준
피커의 친구 목록과 친구 목록 가져오기 API의 응답은 멀티프로필의 영향을 받습니다. 멀티프로필은 카카오톡 사용자가 친구마다 다른 프로필을 보여주도록 설정하는 기능입니다.
카카오톡 프로필 정보는 닉네임(nickName), 프로필 이미지 URL(profileImageUrl), 카카오톡 프로필 썸네일 이미지 URL(thumbnailUrl)로 구성되어 있으며, 이 중 닉네임과 프로필 이미지는 다음과 같은 우선순위에 따라 친구 목록 가져오기 응답에 제공됩니다.

-닉네임: 사용자가 설정한 친구 이름 > 사용자 주소록의 친구 이름 > 친구가 사용자에게 보이도록 설정한 멀티프로필 닉네임 > 친구가 설정한 기본 프로필 닉네임
-프로필 이미지 URL: 친구가 사용자에게 보이도록 설정한 멀티프로필 이미지의 URL > 친구가 설정한 기본 프로필 이미지의 URL

사용자 자신의 프로필 정보를 요청하는 프로필 가져오기 API는 항상 사용자가 설정한 기본 프로필 정보를 사용하므로, 멀티프로필의 영향을 받지 않습니다.

6.지원하는 기능
각 API 및 기능의 Kakao SDK 지원 여부는 지원 범위에서 확인할 수 있습니다.

API 및 기능 | 설명
프로필 가져오기 | 현재 로그인한 사용자의 카카오계정에 연결된 카카오톡 프로필 정보를 불러옵니다. 
피커: 친구 선택하기 | 사용자가 카카오톡 친구를 선택할 수 있는 피커를 호출합니다.
친구 목록 가져오기 | 현재 로그인한 사용자의 카카오계정에 연결된 카카오톡의 친구 정보를 불러옵니다.
"""


kakao_sync = """
카카오싱크:

#시작하기
이 문서는 카카오싱크에 대해 소개하고, 카카오싱크 도입에 필요한 검수 및 설정에 대해 안내합니다.

#기능 소개
카카오싱크는 소셜 로그인인 카카오 로그인을 통해 보다 편리하게 서비스에 가입할 수 있도록 도와주는 비즈니스 설루션입니다. 카카오싱크가 제공하는 핵심 기능은 다음 두 가지입니다.

  기능 | 설명 | 효과
  간편가입 | 동의 화면에서 서비스 약관까지 한 번에 동의받을 수 있습니다. | 서비스 약관 동의 절차 생략 가능
   더 다양한 사용자 정보 활용 | 서비스 회원 가입 시 필요한 다양한 사용자 정보를 제공받을 수 있습니다. 이름, 이메일, 전화번호, 연령대, 생일, 성별, 출생연도, 배송지 등 정보를 제공합니다. | 회원 정보 입력 절차 생략 가능


# 과정 예시
1. 카카오로 시작하기 버튼 : 사용자가 카카오싱크 도입 서비스에서 [카카오로 시작하기] 버튼을 눌러 로그인을 요청합니다. 카카오싱크 도입 서비스에서 사용자는 서비스 회원 ID와 비밀번호 입력 대신 카카오톡을 통해 손쉽게 로그인할 수 있습니다. 카카오톡 실행이 불가능한 환경이라도 카카오계정을 사용해 별도 서비스 회원 가입 절차 없이 로그인할 수 있습니다.

2. 동의하고 계속하기 : 사용자는 카카오톡 또는 카카오계정으로 로그인한 후, 동의 화면에서 정보 제공 동의 항목과 서비스 약관 모두 한 번에 동의할 수 있습니다. 카카오싱크 도입 서비스의 동의 화면은 서비스 약관 동의를 포함해, 한 화면에서 회원 가입에 필요한 동의를 모두 받을 수 있도록 지원합니다. 사용자는 동의 화면에서 서비스의 카카오톡 채널을 친구로 추가할 수도 있습니다.

3. 반갑습니다! 회원이 되신 것을 환영합니다.(문구) : 서비스는 카카오에 로그인한 사용자의 사용자 정보 제공을 요청합니다. 카카오싱크 도입 서비스는 일반적인 회원 가입 시 필요한 사용자 정보들을 카카오로부터 제공받을 수 있습니다. 서비스는 제공받은 사용자 정보로 별도 회원 정보 입력 과정을 거치지 않고 즉시 회원가입 처리를 완료할 수 있습니다.

상세 내용:위와 같이 카카오싱크는 사용자가 한 번의 동의 과정만으로도 서비스의 신규 회원으로 가입할 수 있도록 지원합니다. 또한 카카오싱크 간편가입 사용자는 가입 이후에도 ID 및 비밀번호를 입력하는 대신 카카오 로그인을 통해 서비스에 손쉽게 로그인할 수 있습니다.

서비스는 카카오가 제공하는 API를 통해 회원가입에 필요한 계정 입력 방식의 로그인 과정이나 사용자 정보 입력 절차 등을 최대한 간소화하여 보다 손쉽게 모객을 할 수 있습니다.

이밖에, 카카오싱크 서비스는 카카오톡 채널, 카카오 비즈보드, 챗봇 등 다양한 카카오 마케팅 설루션을 더욱 효과적으로 사용할 수 있습니다. 자세한 안내는 마케팅 가이드를 참고합니다. 카카오비즈니스에서도 카카오싱크에 대한 자세한 소개를 만나볼 수 있습니다. 


#도입 안내
서비스에 카카오싱크를 도입하는 과정을 안내합니다.

1. 카카오싱크 신청 시작 : 카카오비즈니스 관리자센터에서 서비스의 사업자 계정으로 로그인한 후, [카카오싱크 신청] 메뉴를 선택합니다. 카카오싱크 도입 서비스의 오류 발생 시 빠른 지원을 위한 연락처를 입력해야 합니다. 카카오계정에 인증된 연락처가 없는 경우 아래와 같이 연락처 인증 및 등록 절차가 진행됩니다. 인증된 연락처가 등록되어 있는 경우에는 바로 카카오싱크 신청이 가능합니다.

2. 쇼핑몰 호스팅 서비스 사용 여부 선택: 쇼핑몰 호스팅 서비스(이하 호스팅사) 사용 여부를 선택합니다. 호스팅사 사용 여부는 최초 선택 이후 변경 불가이므로 유의합니다. 호스팅사를 이용하지 않고 자체적으로 사이트를 개발 및 운영하고 있다면 [호스팅사에 속하지 않는 독립몰]을 선택합니다. 호스팅사를 이용 중인 경우, [호스팅사를 이용하고 있는 경우]를 선택하고, 사용 중인 호스팅사를 선택합니다. 사용 중인 호스팅사가 카카오와 직접 연동되어 있는 제휴사라면 카카오싱크 간편 설정 팝업을 통해 카카오싱크 도입이 가능하므로, 카카오비즈니스 관리자센터에서는 CI에 대한 검수만 필요에 따라 진행합니다. 이 외 호스팅사의 경우 카카오싱크가 지원되지 않으므로, 해당 호스팅사에 카카오싱크 도입 가능 시점을 문의합니다.

3. 개인정보제공 항목 검수: 카카오싱크를 처음 도입한다면 개인정보제공 항목 검수를 통해 서비스에 필요한 사용자 정보 사용을 신청합니다. 일부 사용자 정보는 반드시 검수를 거쳐야 제공받을 수 있습니다. 카카오는 뚜렷한 용도 없이 지나치게 많은 사용자 정보를 제공하는 것을 지양하며, 사용자 정보 보호를 위해 사용자 정보 제공 전 검수를 진행합니다. 검수 완료 후, 서비스 앱에 필요한 사용자 정보를 [필수] 또는 [선택] 동의 항목으로 설정할 수 있는 권한을 부여합니다. 동의 항목은 사용자 정보를 제공받기 위한 앱 설정입니다. [선택] 사용자 정보는 사용자가 동의하지 않아도 카카오싱크 간편가입을 완료할 수 있는 항목에 해당합니다. [선택]인 사용자 정보는 사용자 동의 여부에 따라 카카오로부터 제공받을 수 없는 경우가 있으므로, 서비스 가입 및 이용에 꼭 필요한 사용자 정보는 [선택]으로 설정하지 않아야 합니다. [필수] 및 [선택] 여부는 신중히 판단하고 사용 신청해야 합니다. 사용 신청된 사용자 정보의 용도가 명확하지 않거나 부적절다면 검수 시 반려될 수 있습니다. 예를 들어 배송지 정보를 의류 등 물건을 파는 쇼핑몰에서 사용 신청한다면 문제가 없지만, 배송지 정보가 불필요한 서비스에서 사용 신청한다면 검수 시 반려됩니다. 카카오는 검수 시 서비스에서 각 사용자 정보가 어떤 용도로 쓰이는지 확인하므로, 수집 사유를 반드시 입력해야 합니다. 서비스 회원가입 시 수집하는 항목을 확인할 수 있는 서비스 회원가입 페이지의 URL, 수집 사유를 증빙할 수 있는 확인 자료를 함께 첨부합니다. 사이트 개발 등으로 확인 자료 첨부가 어려울 경우, 기획안 또는 디자인 시안으로 대체할 수 있습니다. 모든 항목을 설정 완료한 후 [신청하기]를 눌러 검수를 요청합니다. 검수에 소요되는 기간은 영업일 기준 3~5일입니다. 카카오는 검수 시 입력된 정보와 추가 자료는 물론, 현재 서비스의 회원 가입 기준이나 정보 활용 범위가 사용 신청 내역과 일치하는지 두루 확인합니다.

#설정 안내
카카오싱크 신청 및 검수 완료 후, 다음 설정을 완료해야 카카오싱크 연동 개발을 진행할 수 있습니다.

항목 | 설명 | 참고
기본 정보 | 카카오싱크 간편가입 동의 화면에 노출할 서비스 정보 설정. 앱 이름, 아이콘, 회사명이 실제 서비스와 일치하도록 설정. 설정 경로: [내 애플리케이션] > [일반] | 애플리케이션
테스트 환경 | 이미 카카오 로그인을 이용 중인 서비스인 경우, 서비스 환경에 영향을 주지 않도록 테스트 앱, 개발자용 채널을 생성하여 카카오싱크 연동 개발 가능. 아직 카카오 로그인을 이용 중이지 않은 서비스라도 필요에 따라 테스트 앱 생성 및 사용 가능. 설정 경로: [내 애플리케이션] > [카카오 로그인]	| 테스트 앱  개발자용 채널
카카오 로그인 | 카카오싱크 간편가입을 사용하기 위해 카카오 로그인 활성화 필요. 이미 카카오 로그인을 사용 중인 서비스는 활성화 상태로 유지. 네이티브 앱이 아닌 웹 서비스인 경우, 카카오 로그인 Redirect URI 등록 필요. 설정 경로: [내 애플리케이션] > [카카오 로그인] | 카카오 로그인 활성화 설정. Redirect URI 등록
간편가입 | 카카오싱크 간편가입 사용 및 서비스 약관 설정. 간편가입 사용하도록 설정 시 동의 화면에 서비스 약관 동의 항목 노출. 카카오싱크 간편가입 동의 화면에 노출해 사용자로부터 동의받을 서비스 약관 등록 및 관리. 설정 경로: [내 애플리케이션] > [카카오 로그인] > [간편가입] | 간편가입 간편가입 사용 설정
동의 항목 | 카카오로부터 제공받고자 하는 사용자 정보 및 기능에 대한 동의 항목 설정. 동의 화면에 노출할 동의 항목 설정을 통해 사용자 동의를 거쳐 카카오로부터 정보를 제공받을 수 있음. 각 동의 항목의 설정 권한은 카카오싱크 도입 시 사용 신청한 내역 반영. 일부 동의 항목은 별도 검수가 필요하므로, 참고 문서에서 설정 권한 획득 방법 확인 설정 경로: [내 애플리케이션] > [카카오 로그인] | 동의 항목
대표 채널 | 카카오싱크 간편가입 동의 화면에 노출할 대표 채널 설정. 설정 경로: [내 애플리케이션] > [카카오 로그인] > [카카오톡 채널] | 대표 채널 설정
"""

kakaotalk_channel = """
카카오톡 채널:

#이해하기
이 문서는 카카오톡 채널 API를 소개합니다.

#기능 소개
카카오톡 채널(구:플러스친구)은 카카오톡 사용자들에게 다양한 서비스 소식을 메시지와 게시물 형태로 전파할 수 있는 서비스입니다. 카카오톡 채널은 친구인 사용자들에게 마케팅(Marketing) 메시지를 보내는 기능을 제공합니다. 친구란 카카오톡 채널을 친구로 추가한 사용자를 말합니다. 카카오톡 채널 메시지는 비용 절감을 위해 사용자의 성별, 나이, 지역, 등급 등 정보를 토대로 친구 그룹을 만들어서 보다 높은 효과가 기대되는 사용자들에게만 발송하는 것도 가능합니다.
카카오톡 채널을 활용하여 서비스와 사용자의 관계를 더욱 긴밀하게 유지할 수 있습니다. 예를 들면 카카오톡 채널 메시지를 통해 사용자에게 서비스 웹 페이지 방문을 유도하거나 유익한 상품 정보의 링크를 제공하는 것이 가능합니다. 1:1 채팅, 스마트채팅, 봇 등 유용한 추가 기능들도 이용할 수 있습니다.

카카오톡 채널 API는 크게 두 가지의 기능을 제공합니다. 카카오톡 사용자를 위한 카카오톡 채널 추가 및 채팅 API, 다른 카카오톡 채널 관리자가 보다 편리하게 고객 그룹을 관리할 수 있도록 도와주는 카카오톡 채널 고객 관리 API가 있습니다. 두 API 모두 카카오톡 채널 프로필 ID를 사용해 요청하지만, 각각 역할과 제공 방식이 다릅니다.

카카오톡 채널 API를 사용하려면 앱과 카카오톡 채널이 연결되어 있어야 합니다. 또한 사용자의 '카카오톡 채널 추가 상태' 제공 동의가 필요합니다. 자세한 안내 및 설정 방법은 설정하기를 참고합니다.

참고: 카카오톡 채널 프로필 ID 확인 방법
[카카오톡 채널 관리자센터] > [관리] > [상세설정]에서 카카오톡 채널의 채널 URL을 확인할 수 있습니다. 채널 URL에서 https://pf.kakao.com/ 부분을 제외한 뒷자리 값이 해당 카카오톡 채널의 프로필 ID입니다. 다음 예시를 참고합니다.


#카카오톡 채널 추가와 채팅
Kakao SDK를 통해 제공되는 카카오톡 채널 추가와 채팅 API는 카카오톡 채널로 이동할 수 있는 연결 페이지(Bridge page)를 띄우는 기능입니다. 연결 페이지는 사용자 진입 시 카카오톡 채널로 이동할지 묻는 팝업을 띄우고, 사용자가 이동에 동의하면 커스텀 URL 스킴(Custom URL Scheme)을 통해 카카오톡을 실행하고 해당 카카오톡 채널 화면으로 이동합니다. 사용자는 카카오톡 채널 화면에서 해당 카카오톡 채널을 친구로 추가하거나 1:1 채팅을 시작할 수 있습니다.

이 기능은 카카오톡 사용자만 이용할 수 있습니다. 카카오톡을 사용하지 않는 카카오계정으로 로그인한 사용자에게는 "이 계정과 연결된 카카오톡이 없습니다."라는 문구가 포함된 안내 화면이 나타납니다.

왜 사용자를 카카오톡으로 이동시키지 않고 연결 페이지만 띄우나요?
일부 플랫폼은 OS 정책상 사용자를 특정 애플리케이션으로 이동시키는 행위가 제한돼 있습니다. 사용자가 직접 특정 웹 페이지나 애플리케이션을 한 번 실행시키는 것까지는 문제없지만, 여러 차례 사용자를 임의로 이동시키는 건 정책상 문제가 될 수 있습니다. OS 정책에 따라 오픈마켓 리뷰가 거절(Reject)되는 경우와 같은 문제를 피하기 위해 이 API는 연결 페이지 실행 기능만 제공합니다.

#카카오톡 채널 고객 관리
카카오톡 채널 고객 관리 API를 사용하여 카카오톡 채널 관리자센터에서 제공하는 카카오톡 채널 고객 파일 등록 및 관리 기능을 API 방식으로 이용할 수 있습니다.

카카오톡 채널 고객 관리 API는 마케팅 시 보다 정교한 사용자 타게팅을 가능하게 합니다. 카카오 로그인이나 카카오싱크 간편가입을 적용한 서비스는 사용자 정보를 바탕으로 카카오톡 채널 고객 관리 API를 사용해 고객 파일을 등록하고, 해당 고객 파일을 대상으로 카카오톡 채널 관리자센터에서 원하는 조건에 따라 친구 그룹을 생성하여 타깃 메시지를 보낼 수 있습니다. 자세한 사항은 카카오톡 채널 관리자센터 공지사항을 참고합니다.

이 기능은 REST API 방식으로만 제공되며, 서버에서만 호출해야 합니다. 설정하기(https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/prerequisite#admin-api)와 REST API(https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/rest-api)를 참고합니다.

#더 효과적인 활용 방법
사용자가 카카오 로그인을 통해 서비스에 연결되면, 카카오톡 채널 관계 확인하기를 통해 각 사용자의 카카오톡 채널 추가 상태를 확인할 수 있습니다. 사용자의 카카오톡 채널 추가 상태에 따라 카카오톡 채널과 친구가 아닌 사용자에게 친구 추가를 유도하거나 고객 파일에서 사용자를 제외할 수 있습니다. 
다음 url을 참고합니다.

-REST API : https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/rest-api#check-relationship
-JavaScript : https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/js#check-relationship
-Android : https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/android#check-relationship
-iOS : https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/ios#check-relationship


이와 더불어 카카오톡 채널 관계 알림 기능을 적용하면 사용자가 서비스와 연결된 카카오톡 채널을 추가 또는 차단했을 때 알림을 받을 수 있습니다.

앱과 연결된 카카오톡 채널을 추가한 사용자들에게 카카오톡 채널 메시지를 보낼 때, 현재 해당 카카오톡 채널을 차단한 사용자나 별도로 카카오톡에서 친구 추가한 사용자는 자체적으로 파악이 어려울 수 있습니다. 이 경우에도 채널 관계 알림을 사용하면 알림을 통해 변동 사항을 파악할 수 있습니다.

카카오 로그인과 관계없이 [친구 추가] 버튼을 서비스에 노출하고 싶다면 Kakao SDK가 지원하는 카카오톡 채널 추가하기 기능을 사용합니다. 사용자는 서비스 이용 중 이 버튼을 눌러 쉽게 상담을 위한 1:1 대화를 시작할 수 있습니다.


#지원하는 기능
각 API 및 기능의 Kakao SDK 지원 여부는 지원 범위에서 확인할 수 있습니다.

API 및 기능 : 설명 : 문서 URL
카카오톡 채널 추가하기 |사용자가 지정된 카카오톡 채널을 친구로 추가할 수 있는 연결 페이지를 제공합니다. | JavaScript:https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/js#add-channel
카카오톡 채널 채팅하기 | 사용자가 지정된 카카오톡 채널과의 1:1 채팅방으로 진입할 수 있는 연결 페이지를 제공합니다. | JavaScript:https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/js#add-chat
카카오톡 채널 관계 확인하기 | 현재 로그인한 사용자와 앱에 연결된 카카오톡 채널의 친구 관계를 확인합니다. | REST API: https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/rest-api#check-relationship
여러 사용자 카카오톡 채널 관계 확인하기 | 앱에 연결된 카카오톡 채널과 여러 사용자의 친구 관계를 확인합니다. | REST API:https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/rest-api#check-multiple-relationship
카카오톡 채널 관계 알림 | 사용자가 앱에 연결된 카카오톡 채널을 추가하거나 차단했을 때 서비스 서버에 알려줍니다. | 콜백:https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/callback#relationship
고객 관리:고객 파일 등록하기 | 새로운 고객 파일을 만듭니다. | REST API:https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/rest-api#create-user-file
고객 관리:고객 파일 보기 | 카카오톡 채널에 등록된 고객 파일 정보들을 확인합니다. | REST API:https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/rest-api#view-user-file
고객 관리:사용자 추가하기 | 고객 파일에 사용자 정보를 추가합니다. | REST API:https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/rest-api#add-user
고객 관리:사용자 삭제하기 | 카카오톡 채널에 등록된 고객 파일에서 특정 사용자를 삭제합니다. | REST API:https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/rest-api#delete-user
"""

parse_intent = """
Your job is to select one intent from the <intent_list>.

<intent_list>
{intent_list}
</intent_list>

User: {msg}
Intent:
"""