/*
Team LearLination -- Amit Narang and Jason Lin
SoftDev1 pd7
K28 -- Sequential Progression
2018-12-18
*/


var fibonacci = (n) => {
  // 0 and 1 are less than 2 and return themselves
  if (n < 0) {
    return "Please use a non-negative number.";
  }
  if (n < 2){
    return n;
  }
  return fibonacci(n-1) + fibonacci(n-2);
}

var gcd = (a,b) => {
  // gcd(0,0) is undefined
  if (a == 0 && b == 0){
    return undefined;
  }

  // Now Euclidean Algorithm
  var x = Math.max(a,b);
  var y = Math.min(a,b);

  while (true){
    if (y == 0){
      return x;
    }
    else {
      temp = y
      y = x % y;
      x = temp;
    }
  }
}

var randomStudent = () => {
  var students = ["Amit","Jason","Clara","Jerry","Puneet","Runmin","Ivan","Rubin"];
  var randomIndex = Math.floor(Math.random()*students.length);
  return students[randomIndex];
}

var handle_fib = () => {
  var fib_input = document.getElementById("fib_input");
  var out = fibonacci(fib_input.value);
  console.log("fib output: " + out);
  var fib_result = document.getElementById("fib_result");
  fib_result.innerHTML = "Fibonacci Result: " + out;
}

var fib_button = document.getElementById("fib");
fib_button.addEventListener("click",handle_fib);

var handle_gcd = () => {
  var gcd_input1 = document.getElementById("gcd_input1");
  var gcd_input2 = document.getElementById("gcd_input2");
  var out = gcd(gcd_input1,gcd_input2);
  console.log("gcd output: " + out);
  var gcd_result = document.getElementById("gcd_result");
  gcd_result.innerHTML = "GCD Result: " + out;
}

var gcd_button = document.getElementById("gcd");
gcd_button.addEventListener("click",handle_gcd);
