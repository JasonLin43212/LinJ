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

var lis = document.getElementsByTagName("li");

for(var i=0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', changeHeading);
    lis[i].addEventListener('click', removeItem);
};

var addItem = function(e) {
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    item.addEventListener('mouseover', changeHeading);
    item.addEventListener('mouseout', changeHeading);
    item.addEventListener('click', removeItem);
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
    console.log(e);
    /*
 ???
 ...
 ???
 */
};

var addFib2 = function(e){
    console.log(e);
    /*
 ???
 ...see QAF re: DYNAMIC PROGRAMMING...
 ???
 */
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);

/*
document.getElementById('b').addEventListener('click',function() {
  var v = document.createElement('li');
  v.innerHTML = 'WORD';
  document.getElementById('thelist').appendChild(v);
});
document.getElementById('thelist').addEventListener('click',
function(e) {e.target.remove()});
*/
