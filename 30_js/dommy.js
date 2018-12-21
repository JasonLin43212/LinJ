// Lo, what is this? Could it be a VALUE-ADDED-KEY2SUCCESS?!?!
/*
LearLination -- Amit Narang and Jason Lin
SoftDev1 pd<p7
K30 -- Sequential Progression III: Season of the Witch
2018-12-20
*/


var changeHeading = function(e) {
  // Changes heading to Hello World if the user activates the
  // mouseout event and will set it to the list element otherwise
    var h = document.getElementById("h");
    if (e.type === "mouseout"){
      h.innerHTML = "Hello World!";
    }
    else {
      h.innerHTML = e.target.innerHTML;
    }
};

var removeItem = function(e) {
  // Removes the target and sets the heading back to Hello World
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
    var ll = l.getElementsByTagName("li").length;
    var it = document.createElement("li");
    it.innerHTML = fib(ll);
    fixLi(it);
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
