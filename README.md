# rovi_test

## 01. 可変サイズtopicでのメモリーリーク(Python)  
std::vectorを含むtopic(ここではstd_msgs/Float32MultiArray)にて、メモリーリークが発生します。Pythonのみの現象。  
### 再現方法  
ディレクトリ01/以下のコードにて再現できます。  
1. サブスクライバーを起動します
~~~
01/sub.py
~~~

2. パブリッシャをtopic長固定で起動します
~~~
rosrun rovi_test pubarray 2000000
~~~

2000000はstd::vectorのサイズです。1秒周期でpublishされるtopicをサブスクライバーが受信しても、この状態ではリークはありません。

3. パブリッシャをtopic長可変で起動します
~~~
rosrun rovi_test pubarray 2000000 3000000
~~~  
上記にてサイズが2000000〜3000000でランダムに可変になります。この状態ではリークが発生します。

### 大容量トピックでのCPU高負荷問題  
大容量(10MBオーダ)のトピックでは、データサイズが固定でも、CPU負荷が異常に高くなる問題もある。こちらもPythonのみの現象。

### メッセージ型ごとの信頼性検証

大容量データの授受における信頼性と利便性(Numpyの利用)の要件に対して、各メッセージ型について下表のように調査した。

|Type|メモリーリーク|CPU高負荷<sup>(1)</sup>|Numpy.array相互変換<sup>(2)</sup>|
|:----|:----|:----|:----|
|rovi/Floats|NC|NC|Co(nforming)|
|std_msgs/Float32MultiArray|NC|NC|NC|
|std_msgs/String|Co|Co|Co (base64変換)|
|sensor_msgs/PointCloud|?|?|?|
|sensor_msgs/PointCloud2|?|?|?|
|sensor_msgs/Image|?|?|NC|

(1)2%程度が妥当な数値  
(2)1行で記述可能