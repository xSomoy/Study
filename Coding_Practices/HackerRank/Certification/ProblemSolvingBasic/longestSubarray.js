function f(arr){
    if (arr.length < 2)
      return arr.length;
      
    let best = 1;
    let bestLower = 1;
    let bestHigher = 1;
    
    for (let i=1; i<arr.length; i++){
      if (arr[i] == arr[i-1]){
        bestLower = bestLower + 1;
        bestHigher = bestHigher + 1;
      
      } else if (arr[i] - 1 == arr[i-1]){
        bestLower = 1 + bestHigher;
        bestHigher = 1;
      
      } else if (arr[i] + 1 == arr[i-1]){
        bestHigher = 1 + bestLower;
        bestLower = 1;
      
      } else {
        bestLower = 1;
        bestHigher = 1;
      }
  
      best = Math.max(best, bestLower, bestHigher);
    }
    
    return best;
  }