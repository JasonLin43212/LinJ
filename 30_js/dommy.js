// Lo, what is this? Could it be a VALUE-ADDED-KEY2SUCCESS?!?!

var changeHeading = function(e) {
    var h = document.getElementById("h");
    if (e.type === "mouseout"){
      h.innerHTML = "Hello World!";
    }
    else {
      h.innerHTML = e.target.innerHTML;
    }
};

var removeItem = function(e) {
  e.target.remove();
  var h = document.getElementById("h");
  h.innerHTML = "Hello World!";
};

var fixLi = (item) => {
  item.addEventListener('mouseover', changeHeading);
  item.addEventListener('mouseout', changeHeading);
  item.addEventListener('click', removeItem);
}

var addItem = function(e) {
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    fixLi(item);
    list.appendChild( item );
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
if(n < 2){
return 1;
    } else {
return fib(n-1) + fib(n-2);
    }

};

var addFib = function(e){
    // Check # of li items in list , return fib at that ind
    var l = document.getElementById("fiblist");
    var ll = l.getElementsByTagName("li");
    var it = document.createElement("li");
    if (ll.length <= 1){
      it.innerHTML = ll.length;
    }
    else {
      it.innerHTML = parseInt(ll[ll.length-1].innerHTML)+parseInt(ll[ll.length-2].innerHTML);
    }
    l.appendChild(it);

};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);

var lis = document.getElementsByTagName("li");

for(var i=0; i < lis.length; i++) {
    console.log(lis[i].innerHTML);
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', changeHeading);
    lis[i].addEventListener('click', removeItem);
};
