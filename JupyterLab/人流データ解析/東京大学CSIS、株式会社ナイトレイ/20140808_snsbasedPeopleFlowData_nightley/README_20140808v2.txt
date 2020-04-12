
【擬似人流データ　CSVデータ概要】
実データ：人々が訪れる場所や施設、時間帯(SNS ベース)、道路ネットワーク
推定データ：移動経路、居住地、勤務地、滞在時間、性別、滞在中何をしているか(買い 物やレジャーなど)
含まれないデータ：鉄道経路、個人を特定する情報、滞在施設名
エリア：東京近郊(首都圏)
対象時期：2013年7月(7/1, 7/7)、10月(10/7, 10/13)、12月(12/16, 12/22)
時間単位：5分毎(24時間分)
レコード数：各csvファイルで約70,000件
ファイルサイズ：約100MB



【ファイル構成】
１．疑似人流データ(csv形式)
—————カラム構成————————————————
1行目：ユーザー ID
2行目：性別(推定値) ※文字列型
3行目：日付・時刻
4行目：緯度
5行目：経度
6行目：滞在者カテゴリ(大分類) ※文字列型
7行目：滞在者カテゴリ(小分類) ※文字列型
8行目：状態(滞在or移動) ※文字列型
9行目：滞在者カテゴリID(6行目に対応)
※Mobmapでは文字列型は自動認識されません。ご注意ください。
——————————————-——————————————-

２．滞在者カテゴリリスト(疑似人流データの滞在カテゴリの詳細、csv形式)
３．README.txt

 

【データの利用方法】
１．擬似人流データファイルをダウンロード
２．ダウンロードしたzipファイルを解凍
３．MobmapをGoogle Chromeからダウンロードしてインストール
４．解凍したcsvファイルをMobmapにインポートしてビジュアライズ
※詳しくはFOSS4G北海道ハンズオン「Mobmap 人流データ解析入門」資料をご覧下さい。 https://sites.google.com/site/foss4ghokkaido/home/handson



【ライセンスについて】
疑似人流データはクリエイティブ・コモンズ 表示 4.0 国際 ライセンスで提供されています。



【クレジット】
株式会社ナイトレイ
東京大学　柴崎・関本研究室
マイクロジオデータ研究会
人の流れプロジェクト
東京大学空間情報科学研究センター



【関連リンク】
東京大学 柴崎・関本研究室
http://shiba.iis.u-tokyo.ac.jp

マイクロジオデータ研究会
http://geodata.csis.u-tokyo.ac.jp/mgd/

FOSS4G 北海道 ハンズオンデイ「Mobmap 人流データ解析入門」
https://sites.google.com/site/foss4ghokkaido/home/handson

FOSS4G 北海道 ハンズオンデイ「Mobmap 人流データ解析入門」　講演資料
http://www.slideshare.net/hiroakisengoku/mobmap-handson2014

Mobmap for Chrome
http://shiba.iis.u-tokyo.ac.jp/member/ueyama/mm

東京大学空間情報科学研究センター「人の流れプロジェクト」
http://pflow.csis.u-tokyo.ac.jp/index-j.html



【お問い合わせ先】
info(at)nightley.jp
担当：石川、古川






[Summary of CSV data]
Surveyed value: POI, Timestamp (SNS post), The road network.
Estimate value: Movement courses, A place of residence, Work location, Stay time, Gender, What he do during a stay (including shopping and the leisure).
Data not to be included: Railroad course, Information to identify an individual, Stay facilities.
Area: Tokyo Metropolitan Area
Target time: July, 2013 (7/1, 7/7), October (10/7, 10/13), December (12/16, 12/22)
A time unit: As for every five minutes (for 24 hours)
Geodetic datum: WGS84 (EPSG:4326)
Records: It is approximately 70,000 cases with each csv file
File size: Approximately 100MB



[File constitution]
1. SNS-based People Flow Data(csv)
―――――――――――Column constitution――――――――――― 1st. User ID
2nd. Gender (estimate) *string
3rd. Timestamp
4th. Latitude
5th. Longitude
6th. Place category (main) *String
7th. Place category (sub) *String
8th. State (stay or movement) *String
9th. Place category ID (Correspond to the sixth line)
*String is not recognized automatically in Mobmap. Please be careful,
――――――――――――――――――――――

2. List of Place categories (The details of the stay category of SNS-based People Flow Data, csv)

3. README.txt



[The proper way to use SNS-based People Flow Data]
1. Please download SNS-based People Flow Data file.
2. Unzip a download file.
3. Download Mobmap from Google Chrome and install it.
4. Import the csv file in Mobmap; and visualize.

*Specifically, look at an FOSS4G Hokkaido hands on “Introduction to person from Mobmap People Flow Data analysis" document. 
https://sites.google.com/site/foss4ghokkaido/home/handson



[License]
This data is licensed under a Creative Commons Attribution 4.0 International License.



[Attribute work to name]
Nightley, Inc.
Shibasaki & Sekimoto Laboratory, the University of Tokyo
Micro Geo Data Forum
People Flow project
Center for Spatial Information Science at the University of Tokyo



[External links]
Shibasaki & Sekimoto Laboratory, the University of Tokyo http://shiba.iis.u-tokyo.ac.jp

Micro Geo Data Forum
http://geodata.csis.u-tokyo.ac.jp/mgd/

FOSS4G Hokkaido hands on“Introduction to person from Mobmap People Flow Data analysis". https://sites.google.com/site/foss4ghokkaido/home/handson

FOSS4G Hokkaido hands on“Introduction to person from Mobmap People Flow Data analysis" document. http://www.slideshare.net/hiroakisengoku/mobmap-handson2014

Mobmap for Chrome. http://shiba.iis.u-tokyo.ac.jp/member/ueyama/mm

Center for Spatial Information Science at the University of Tokyo “People Flow Project” and “People Flow Analysis Platform”. http://pflow.csis.u-tokyo.ac.jp/index-j.html http://pflow.csis.u-tokyo.ac.jp/platform.html



[Contact] info(at)nightley.jp Ishikawa, Furukawa


最終更新日：2014/8/8
Last updated: Aug, 8, 2014