# MIT_DS
# PCA and K-Means to Decipher Genome of Caulobacter Crescentus
In the following paper the authors have used PCA and K-means to decipher genome of a bacterium.(Caulobacter-crescentus) http://www.ihes.fr/~zinovyev/papers/14MainGorbanKeglWunschZin.pdf. 
This is also an case sturdy used by the MIT Data science course to show use of PCA and K-means clustering.
The paper and the MIT course have the necessary code in MATLAB. This is an attempt to replicate it in Python 3.x
The file needed to run this code is sourced from 
ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/Caulobacter-crescentus-NA1000-uid59307/ 
Alternatively, you can also download gene.txt

The file is combination of letters (genome sequence) 'a' 'c' 'g' and 't' repeated. The file is first split in to lines of 300 characters then each line is turned in to a sentence (for lack of better word) with hundred 3 letter words. Word frequency count from each line then makes the dataset needed to perform PCA.

Course link:
https://mitxpro.mit.edu/courses/course-v1:MITxPRO+DSx+1T2019/about

# Overfitting when n = p; 
i.e. we have as many variables as rows our regression r2 will always be 1. To convince ourselves of this theory  you can run the reproducible code https://github.com/akshaykadidal/MIT_DS/blob/master/overfit.r


# Understanding Neural networks using excel
a basic two node neural networks trying to emulate a not function in excel. this excel sheet demonstrates how you can go through the neural network calculations by hand. https://github.com/akshaykadidal/MIT_DS/blob/master/Neural%20Networks.xlsx
ofcourse it was never meant to be done by hand so here is the associated python code using numpy library.
https://github.com/akshaykadidal/MIT_DS/blob/master/Gradient%20Decent%20one%20node%20NN.ipynb
