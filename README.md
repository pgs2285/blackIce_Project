# blackIce_Project
# 상태(dry-water-ice) 감지

# 세부 프로젝트 진행 상황은 아래 링크 (이미지 안뜨면 링크로 가주세요)
https://tender-king-5a0.notion.site/Android-Studio-1e3043f6e1c4456d87c789f2dd14e357
# 모바일 어플은 
https://github.com/pgs2285/blackIce_mobile_application

## 모델 선정 

## 이미지 수집

![A8D04619-9511-4EDD-A4AD-CD3D0F3D5F17_1_105_c.jpeg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7a494094-562c-41f7-9dd3-5ed2554a4678/A8D04619-9511-4EDD-A4AD-CD3D0F3D5F17_1_105_c.jpeg)

위와 같이 차에다 라즈베리파이용 적외선 카메라를 부착해, 이미지를 수집한다.

이미지는 여러 경우 - (아스팔트 색, 차선의 여부)등을 고려해 최대한 많은 이미지를 수집할 계획.

## scikit learn - SGDClassifier

![2022-01-25_02-09-11.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6cb457dd-1f1f-4855-9ca0-cf1711576cd7/2022-01-25_02-09-11.png)

scikit learn cheat sheet를 따라가 적은 이미지의 분류기인 SGDClassifier를 사용하기로 결정

**추후 이미지의 개수가 늘어나면, Linear SVC혹은 KNeighbors Classifier사용**

## SGDClassifier를 사용하기 위한 데이터 가공

SGDClassifier를 사용하기 위해 수치데이터를 모집해야 하는데, grayScale의 빈도를 이용해 수치값을 뽑아내기로 결정함

### dry-water-ice /  normal

![이미지 여러장의 grayscale 빈도값 gif파일](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8654211c-d7ae-49ba-a102-705938430071/water_dry_ice_normal.gif)

이미지 여러장의 grayscale 빈도값 gif파일

수집된 이미지들을 grayscale (0~255) 빈도 값에 따라서 그래프로 나타내 보았다.

![dry- water- ice 이미지 ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c345711b-abc1-4fe4-8bfb-15b0588b6891/normal_img.png)

dry- water- ice 이미지 

### 문제점

![좌-우 사진 water의 빛반사율 때문에 차이가 심한모습](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c345711b-abc1-4fe4-8bfb-15b0588b6891/normal_img.png)

좌-우 사진 water의 빛반사율 때문에 차이가 심한모습

![모든 그래프가 비슷하게 보이는 경우](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f48b0cad-b751-4640-b2ed-97409418ae6c/error_list.png)

모든 그래프가 비슷하게 보이는 경우

1. 특정 사진에 따라서, 육안으로도 차이를 보기힘든 사진이 있음. (그래프의 큰 차이가 없어 분류가 힘든 케이스)
2. water 의 빛 반사율의 여부에 따라 200이후의 값들이 너무 튄다. (water의 반사율의 편차가 심한경우)

### 문제 1 (그래프의 큰 차이가 없어 분류가 힘든 케이스) 해결방안 - 
dry-water-ice / sqr

위 이미지는 빈도를 분석하기에는 편차가 적어 제곱을 해본 결과값

![결과 값들을 제곱시킨 값](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90b25c64-a984-46a0-a631-045fd749a107/water_dry_ice_Sqr.gif)

결과 값들을 제곱시킨 값

![sqr이미지 비교 값 - 보다 값들마다의 차이를 보기 편했다.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ec5673c9-2351-48ea-acf0-cfc1155a492f/sqr_IMAGE.png)

sqr이미지 비교 값 - 보다 값들마다의 차이를 보기 편했다.

<aside>
💡 제곱을 하기 전보다 차이를 보기 좋았으나, 아직까지도 구분이 힘든 사진이 몇가지 존재하긴 한다. 이 문제의 해결법은 문제2 해결방안과 공유한다

</aside>

### 문제 2 (water의 반사율의 편차가 심한경우) 해결 방안

### 이미지 데이터 증강

이미지 데이터를 증강시키는 방법을 생각중이다. 아직까지는 각 종류별로 이미지의 종류가 500장도 되지않아서 정확한 분포를 알아보기는 힘들었다.

여러 이미지를 수집해 대부분의 경우의수를 많이 학습시키면 해결 될 수도 있다 생각함.

## VGG-16 을 사용한 감지방법

 빛 변수가 많은 야외환경 특성상 빛 반사율을 이용한 이전 방법은 불가능 하다 판단했다.

이미지 분류 방식인 VGG-16을 사용하기로 결정.

비록 dry, water 상태의 사진만 학습을 시켰지만,  사진데이터를 약 1500장씩으로 증가시켜, 이전 방식보다 야외에서 측정시 훨씬 높은 정확도를 보여주었다.

# 세부 프로젝트 진행 상황은 아래 링크
https://tender-king-5a0.notion.site/Android-Studio-1e3043f6e1c4456d87c789f2dd14e357
