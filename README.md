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
