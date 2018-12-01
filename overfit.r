rm(list = ls())
y <- rnorm(50, mean = 4, sd=.5)

data <- data.frame(y=y)

for(i in 1:50){
  #i=2
  #v_name <- paste0("x",i) # creating random predictor names x1, x2 etc
  mn <- floor(runif(1,min=0, max=100))  # this random number will be used a mean
  s_d <- runif(1,min=1, max=25) # this random number will be used as Std Dev
  x <- rnorm(50, mean = mn, sd=s_d) # creating a random x
  #assign(v_name,x) # assiging it to x1 x2 and so on
  #data <- cbind(data,eval(parse(text = v_name)))
  data <- cbind(data,x)
  c_num <- length(data)
  colnames(data)[c_num] <- paste0("x",i)
}

m1 <- lm(y~.,data = data)
summary(m1)$r.squared
    summary(m1)$adj.r.squared

# run the experiment again if you like

# lets remove some regressors
selected_col <- c(1:51)[c(1:51)%in%sample(1:50, 40)]# selecting 40 columns randomly change the last number 40
# you will notice that R2 is alsmost 1 even when you exlcude a 2-3 columns
data1 <- data[selected_col]
m2 <- lm(y~.,data = data1)
summary(m2)$r.squared
summary(m2)$adj.r.squared