result = "";
for(i = 0; i<= 5; i++) {
    result = result + "* " .repeat(i) + "\n";
}
console.log(result);

console.log("-----------------------------");

for(i = 1; i<= 6; i++) {
    row = "";
    for(j =1; j <= i; j++){
        row += "* "
    }
    console.log(row);
}
