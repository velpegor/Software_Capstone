# Refacing  Anonymized MRI Images Using GAN

### 개요

의료 영상의 익명화는 시험 대상자의 신원을 보호하기 위해 필요하며, 따라서 데이터 공유 에 있어서 필수적인 단계이다. 그러나 딥 러닝의 발전은 익명성을 보장하기 위해 적용해야 하는 왜곡의 양에 대한 한계를 높일 수 있다. 

따라서 이러한 가능성을 테스트하기 위해, 익명화 된 데이터에서 얼굴 특징을 재구성하기 위한 GAN을 이용해 익명화된 MRI 이미지를 재구성 할 것이다. 얼굴이 포함된 mri 이미지를 defacing tool(pydeface)을 이용해 reface한 다음 CycleGAN, DCGAN 등 GAN기법을 이용해 refacing에 대한 성능 평가를 진행하고 비교 분석한다.

### 데이터셋
* IXI Datasets
* 원본 : 581개 (224 x 224)
* Sagital 방향으로 각각 임의의 좌표 값으로 10배 증강 후 학습 (5810개)

<div align="center">
<img width="768" alt="image" src="https://user-images.githubusercontent.com/83739271/208047821-58ae1678-891b-4f1b-9830-f3f3b04f5922.png">

참고 사진
</div>

### 모델

* [CycleGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)

<img width="529" alt="image" src="https://user-images.githubusercontent.com/83739271/208051738-56c777e9-74ee-4422-a03c-a55eb1d2dc0d.png">

</br>

* [DCLGAN](https://github.com/JunlinHan/DCLGAN)

<img width="613" alt="image" src="https://user-images.githubusercontent.com/83739271/208051794-ffdaa57c-9393-4985-bd06-8c34ceedd013.png">

### 모델 성능 비교

<div align="center">

<img width="764" alt="image" src="https://user-images.githubusercontent.com/83739271/208048341-3ee3294f-95db-4562-8f50-a42a5e7bd6aa.png">

<img width="778" alt="image" src="https://user-images.githubusercontent.com/83739271/208048243-30f5330b-f1f5-4516-b40a-fbc83a6bbdb7.png">

</div>
  
### 결과
![image](https://user-images.githubusercontent.com/83739271/207845982-0052fb42-6194-4f72-b4ff-49704edcd2c8.png)


### 데모 영상


https://user-images.githubusercontent.com/83739271/208050231-dca07801-6767-4a49-a791-579f643f0265.mp4


- - - - -

### Reference

* Deface tool : https://github.com/poldracklab/pydeface
* 선행 논문 : https://arxiv.org/abs/1810.06455
