// キャンパスの要素を取得する
var canvas = document.getElementById( 'map-canvas' ) ;

// 中心の位置座標を指定する
var latlng = new google.maps.LatLng( 38.268215, 140.8693558 );

// 地図のオプションを設定する
var mapOptions = {
  zoom: 15 ,        // ズーム値
  center: latlng ,    // 中心座標 [latlng]
};

// [canvas]に、[mapOptions]の内容の、地図のインスタンス([map])を作成する
var map = new google.maps.Map( canvas , mapOptions );

// jsonを取得する
var xhr = new XMLHttpRequest();
xhr.open("GET", "get_tweet/v1/get_tweet/?place=仙台");
xhr.responseType = "json";
xhr.addEventListener("loadend", (ev) => {console.log(ev.target.response)})
xhr.send();

// マーカーのインスタンスは配列で管理しよう
var markers = [] ;

for (var i=0; i<Object.keys(xhr.response).length; i++) {
  // マーカーのインスタンスを作成する
  markers[i] = new google.maps.Marker({
    map: map ,
    position: new google.maps.LatLng( xhr.response[i]["geo"].coordinates[0] , xhr.response[i]["geo"].coordinates[1] ) ,
  }) ;
}

markers[0] = new google.maps.Marker( {
  map: map ,
  position: new google.maps.LatLng( 38.268215, 140.8693558 ) ,
} ) ;