# Enter your code here. Read input from STDIN. Print output to STDOUT
require(fastcluster)
x <- suppressWarnings(readLines(file("stdin")));
#print(x);
firstLine <- matrix(unlist(strsplit(x[1],"\\s")),byrow=1,nrow=3);
#print(firstLine[1][1]);
x <- x[-1];
x <- apply(matrix(unlist(strsplit(paste(x,collapse = " ")," "),"\\s"),byrow=0,nrow = 2),1,as.numeric);
#print(x);
#print(firstLine[3][1]);
if(firstLine[3][1]=="0"){
    result <- cutree( hclust(dist(x),method = "single"),as.numeric(firstLine[2][1]))
    result <- matrix(unlist(result),byrow=0,nrow=1)
    result <- t(result)-1
    #print(result)
    write.table(  result ,  row.names=F, col.names=F)
}
  
if(firstLine[3][1]=="1"){
    result <- cutree( hclust(dist(x),method = "complete"),as.numeric(firstLine[2][1]))
    result <- matrix(unlist(result),byrow=0,nrow=1)
    result <- t(result)-1
    #print(result)
    write.table(  result ,  row.names=F, col.names=F)
}
if(firstLine[3][1]=="2"){
    result <- cutree( hclust(dist(x),method = "ave"),as.numeric(firstLine[2][1]))
    result <- matrix(unlist(result),byrow=0,nrow=1)
    result <- t(result)-1
    #print(result)
    write.table(  result ,  row.names=F, col.names=F)
}

#print("done")
