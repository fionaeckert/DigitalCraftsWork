//* In JavaScript, implement the bubble sort algorithm to sort an array of numbers from least to greatest. *

// lst = [343,454,24536,7864,8463,78]
// def sort(lst:list)->list:
//     for i in range(len(lst)):
//         for j in range(0,len(lst)-i-1):
//             if lst[j]>lst[j+1]:
//                 lst[j],lst[j+1]=lst[j+1],lst[j]
//     print(lst)
// sort(lst)



var lst = [343,454,24536,7864,8463,78]

for(var i = 0; i < lst.length; i++){
    for(var j = 0;j < (lst.length - i - 1);j++){
        if(lst[j] > lst[j+1]){
            var temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
            }
        }
    }
console.log(lst)


// function bubbleSort(lst) {
//     let len = lst.length
//     for(var i = 0; i < len; i++){
//         for(var j = 0;j < (len - i - 1);j++){
//             if(lst[j] > lst[j+1]){
//                 var temp = lst[j]
//                 lst[j] = lst[j+1]
//                 lst[j+1] = temp
//                 }
//             }
//         }
//     console.log(lst)
//     }
// bubbleSort()