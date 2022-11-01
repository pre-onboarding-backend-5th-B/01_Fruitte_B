# 01_Fruitte_B

- [Fruitte](https://www.fruitte.co.kr/about)의 기업과제 백엔드 API를 만든 프로젝트입니다.
- [요구사항](https://alike-stinger-202.notion.site/Fruitte-4056875cca3543c395abf47bc92f4662)

------

# ERD

![image](https://user-images.githubusercontent.com/44486924/198189304-09757858-8ac7-43c2-bfe2-d6c139e3f722.png)
------

# 기능

## 목록

1. 회원 가입 및 로그인
2. 상품 CRUD
3. 결제 관리
4. 주문 내역

## 제약사항

- 유저는 이용자, 관리자로 나누어져 있음
- 상품 및 결재, 주문은 관리자만 입력, 수정, 삭제 가능
- 이용자는 회원가입, 결재, 주문을 제외하고 조회 권한만 허용

## API 목록
- [API docs pdf download](docs/api_docs.pdf)
- <details> 
        <summary> 
            api docs 보기 
        </summary>
    
    ![API 문서](docs/api_docs.png)
    </details>