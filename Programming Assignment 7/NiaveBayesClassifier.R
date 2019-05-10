require(e1071)
# Enter your code here. Read input from STDIN. Print output to STDOUT
x <- suppressWarnings(readLines(file("stdin"))); 


x <- x[-1];

x <- matrix(unlist(strsplit(x,","),","),byrow=TRUE,ncol=18);
#append(x,matrix(x[x[,18] == "-1",],ncol=18))
#x <- rbind(x, c("bass",0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0,-1)) 
#print(x)
#print(subset(x, x[,18] == -1));
#print(matrix(x[x[,18] == "-1",],ncol=18));
dfTest <- matrix(x[x[,18] == "-1",],ncol=18)
#dfTest <- split(mydata,mydata$V18);
#print(dfTest);
x <- x[x[,18]!=-1,]
#print(x)
data_df=as.data.frame(x)
#print(data_df)
model <- naiveBayes(V18 ~ ., data = data_df, laplace = 0.1)
#print(as.data.frame(t(dfTest)))
result <-  predict(model, as.data.frame(dfTest),type = c("class"))
#print(result)
for(ch in result)
    cat(as.numeric(ch),"\n")
