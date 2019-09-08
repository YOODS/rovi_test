# rovi_test

## 01/1 可変サイズtopicでのメモリーリーク(Python)  
std::vectorを含むtopic(ここではstd_msgs/Float32MultiArray)にて、メモリーリークが発生します。Pythonのみの現象。  
### 再現方法  
1. サブスクライバーを起動します
~~~
01/sub.py
~~~

2. パブリッシャをtopic長固定で起動します
~~~
rosrun rovi_test pubarray 3000000
~~~

3000000はstd::vectorのサイズです。1秒周期でpublishされるtopicをサブスクライバーが受信しても、この状態ではリークはありません。

3. パブリッシャをtopic長可変で起動します
~~~
rosrun rovi_test pubarray 2000000 3000000
~~~  
上記にてサイズが2000000〜3000000でランダムに可変になります。この状態ではリークが発生します。

## 01/2 大容量トピックでのCPU高負荷(Python)
メッセージ型により、データサイズが同じでもCPU負荷が異常に高くなる問題がある。こちらもPythonのみの現象。

### 再現方法  
1. サブスクライバーを起動します
~~~
01/sub.py
~~~

2. PointCloudパブリッシャを01/1.2.と同サイズのメッセージ長となるよう、1000000点固定で起動する。
~~~
rosrun rovi_test pubpc 1000000
~~~
メッセージ長は同じにもかかわらず、01/1.2.のCPU負荷の数十倍大きい。

## 01/まとめ メッセージ型ごとの信頼性検証

大容量データの授受における信頼性と利便性(Numpyの利用)の要件に対して、各メッセージ型について下表のように調査した。

|Type|メモリーリーク|CPU負荷<sup>(1)</sup>|Numpy.array相互変換<sup>(2)</sup>|
|:----|:----|:----|:----|
|rovi/Floats|NC|Co(nforming)|Co|
|std_msgs/Float32MultiArray|NC|Co|NC|
|std_msgs/String|Co|Co|Co (base64変換)|
|sensor_msgs/PointCloud|?|NC|?|
|sensor_msgs/PointCloud2|?|?|?|
|sensor_msgs/Image|?|?|NC|

(1)2%程度が妥当な数値  
(2)1行で記述可能