# remove_correlated_features
Removes features that have either R2 of 1 or -1. Will retain one feature from correlated groups to make matrix non-redundant. It will only calculate correlation scores for features with varying values and will ignore invariant features.

    $ python rm_cor.py [INFILE.csv] [OUTFILE.csv]

    $ cat test.csv
    INDEX,T1,T2,T3,T4
    I1,0,0,0,0
    I2,1,1,1,1
    I3,1,0,1,0
    I4,0,1,0,1
    
    $ python rm_cor.py test.csv out.csv
    
    $ cat out.csv
    INDEX,T1,T2,T3,T4
    I1,0,0,0,0
    I2,1,1,1,1
    I3,1,0,1,0
