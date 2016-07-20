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
xhr.open("GET", "http://127.0.0.1:8000/get_tweet/v1/get_tweet/?place=仙台");
xhr.responseType = "json";
xhr.addEventListener("loadend", function(ev) {
  console.log(ev.target.response)
  var length = Object.keys(xhr.response).length
  for (var i=0; i<length; i++) {
    // マーカーのインスタンスを作成する
    markers[i] = new google.maps.Marker({
      map: map ,
      position: new google.maps.LatLng( xhr.response[i]["geo"].coordinates[0] , xhr.response[i]["geo"].coordinates[1] ) ,
    }) ;
  }
})
xhr.send();

// マーカーのインスタンスは配列で管理しよう
var markers = [] ;


// markers[0] = new google.maps.Marker( {
//   map: map ,
//   position: new google.maps.LatLng( 38.268215, 140.8693558 ) ,
// } ) ;