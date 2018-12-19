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
