def converter(amount, rate):
    return amount*rate


print("Currency Converter")

curr1 = input("Enter the currency code that has to be converted: ")
curr2 = input("Enter the currency code to convert:")
a = int(input("Enter the amount: "))

india = ["INR", "inr"]
eu = ["eur","EUR"]
uk = ["GBP", "gbp"]
us = ["USD","usd"]
canada = ["CAD", "cad"]
russia = ["rub","RUB"]
china = ["yuan","YUAN"]
japan = ["JPY","jpy"]
aus=["aud","AUD"]
singapore=["SGD","sgd"]
uae=["AED","aed"]
srilanka=["LKR","lkr"]
bangladesh=["BDT","bdt"]
nepal=["NPR","npr"]
zimbabawe=["ZWL","zwl"]
brazil=["BRL","brl"]
qatar=["QAR","qar"]
pakistan=["PKR","pkr"]
ukraine=["UAH","uah"]
afghanistan=["AFN","afn"]



inr = 0
eur = 0
gbp = 0
usd = 0
cad = 0
rub = 0
yuan = 0
jpy = 0
aud = 0
sgd = 0
aed = 0
lkr = 0
bdt = 0
npr = 0
zwl = 0
brl = 0
qar = 0
pkr = 0
uah = 0
afn = 0


# conversion rates
if curr1 in india:
     eur=0.012
     gbp=0.010
     usd=0.012
     cad=0.016
     rub=0.75
     yuan=0.087
     jpy=1.72
     aud=0.018
     sgd=0.017
     aed=0.045
     lkr=4.50
     bdt=1.26
     npr=1.60
     zwl=3.949946
     brl=0.066
     qar=0.045
     pkr=2.73
     uah=0.45
     afn=1.08

elif curr1 in eu:
    inr=84.34
    gbp=0.87
    usd=1.03
    cad=1.38
    rub=62.95
    yuan=7.37
    jpy=145.19
    aud=1.55
    sgd=1.42
    aed=3.80
    lkr=379.90
    bdt=106.53
    npr=135.09
    zwl=332.30
    brl=5.57
    qar=3.77
    pkr=230.14
    uah=38.18
    afn=91.04

elif curr1 in uk:
    inr=96.97
    eur=1.15
    usd=1.19
    cad=1.59
    rub=72.38
    yuan=8.47
    jpy=166.94
    aud=1.78
    sgd=1.64
    aed=4.37
    lkr=436.80
    bdt=122.48
    npr=155.32
    zwl=380.77
    brl=6.40
    qar=4.33
    pkr=264.60
    uah=43.90
    afn=104.68

elif curr1 in us:
    inr = 81.50
    eur = 0.97
    gbp = 0.84    
    cad = 1.34
    rub = 60.85
    yuan = 7.12
    jpy = 140.34
    aud = 1.50
    sgd = 1.38
    aed = 3.67
    lkr = 367.22
    bdt = 102.97
    npr = 130.58
    zwl = 322
    brl = 5.38
    qar = 3.64
    pkr = 222.45
    uah = 36.90
    afn = 88

elif curr1 in canada:
    inr = 60.77
    eur = 0.72
    gbp = 0.63
    usd = 0.75
    rub = 45.36
    yuan = 5.31
    jpy = 104.61
    aud = 1.12
    sgd = 1.03
    aed = 2.74
    lkr = 273.72
    bdt = 76.75
    npr = 97.33
    zwl = 240.58
    brl = 4.01
    qar = 2.71
    pkr = 165.82
    uah = 27.51
    afn = 65.60

elif curr1 in russia:
    inr = 1.34
    eur = 0.016
    gbp = 0.014
    usd = 0.016
    cad = 0.022
    yuan = 0.12
    jpy = 2.31
    aud = 0.021
    sgd = 0.023
    aed = 0.060
    lkr = 6.03
    bdt = 1.69
    npr = 2.15
    zwl = 5.33
    brl = 0.088
    qar = 0.060
    pkr = 3.66
    uah = 0.61
    afn = 1.45

elif curr1 in china:
    inr = 11.45
    eur = 0.14
    gbp = 0.12
    usd = 0.14
    cad = 0.19
    rub = 8.55
    jpy = 19.71
    aud = 0.21
    sgd = 0.19
    aed = 0.52
    lkr = 51.58
    bdt = 14.46
    npr = 18.34
    zwl = 45.22
    brl = 0.76
    qar = 0.51
    pkr = 31.24
    uah = 5.18
    afn = 12.36

elif curr1 in japan:
    inr = 0.58
    eur = 0.0069
    gbp = 0.0060
    usd = 0.0071
    cad = 0.0095
    rub = 0.43
    yuan = 0.051
    aud = 0.011
    sgd = 0.0098
    aed = 0.026
    lkr = 2.62
    bdt = 0.73
    npr = 0.93
    zwl = 2.29
    brl = 0.038
    qar = 0.026
    pkr = 1.58
    uah = 0.26
    afn = 0.63

elif curr1 in aus:
    inr = 54.41
    eur = 0.65
    gbp = 0.56
    usd = 0.67
    cad = 0.90
    rub = 40.62
    yuan = 4.75
    jpy = 94.00
    sgd = 0.92
    aed = 2.45
    lkr = 245.12
    bdt = 68.73
    npr = 87.16
    zwl = 215.24
    brl = 3.59
    qar = 2.43
    pkr = 148.49
    uah = 24.63
    afn = 58.74
elif curr1 in singapore:
    inr = 59.24
    eur = 0.70
    gbp = 0.61
    usd = 0.73
    cad = 0.97
    rub = 44.22
    yuan = 5.17
    jpy = 101.99
    aud = 1.09
    aed = 2.67
    lkr = 266.85
    bdt = 74.83
    npr = 94.89
    zwl = 234.135
    brl = 3.91
    qar = 2.65
    pkr = 161.65
    uah = 26.82
    afn = 63.95
elif curr1 in uae:
    inr = 22.19
    eur = 0.26
    gbp = 0.23
    usd = 0.27
    cad = 0.37
    rub = 16.57
    yuan = 1.94
    jpy = 38.21
    aud = 0.41
    sgd = 0.37
    lkr = 99.98
    bdt = 28.03
    npr = 35.55
    zwl = 87.66
    brl = 1.47
    qar = 0.99
    pkr = 60.56
    uah = 10.05
    afn = 23.96
elif curr1 in srilanka:
    inr = 0.22
    eur = 0.0026
    gbp = 0.0023
    usd = 0.0027
    cad = 0.0037
    rub = 0.17
    yuan = 0.019
    jpy = 0.38
    aud = 0.0041
    sgd = 0.0037
    aed = 0.010
    bdt = 0.28
    npr = 0.3556
    zwl = 0.8768
    brl = 0.015
    qar = 0.0099
    pkr = 0.61
    uah = 0.10
    afn = 0.24
elif curr1 in bangladesh:
    inr = 0.79
    eur = 0.0094
    gbp = 0.0082
    usd = 0.0097
    cad = 0.013
    rub = 0.59
    yuan = 0.069
    jpy = 1.36
    aud = 0.015
    sgd = 0.013
    aed = 0.036
    lkr = 3.57
    npr = 1.27
    zwl = 0.319
    brl = 0.052
    qar = 0.035
    pkr = 2.16
    uah = 0.36
    afn = 0.85
elif curr1 in nepal:
    inr = 0.62
    eur = 0.0075
    gbp = 0.0064
    usd = 0.0077
    cad = 0.010
    rub = 0.47
    yuan = 0.055
    jpy = 1.07
    aud = 0.011
    sgd = 0.011
    aed = 0.028
    lkr = 2.81
    bdt = 0.79
    zwl = 2.4659
    brl = 0.041
    qar = 0.028
    pkr = 1.70
    uah = 0.28
    afn = 0.67
elif curr1 in zimbabawe:
    inr = 0.2531
    eur = 0.003002
    gbp = 0.0026
    usd = 0.00310
    cad = 0.00416
    rub = 0.1889
    yuan = 0.02211
    jpy = 0.434
    aud = 0.0046
    sgd = 0.0042
    aed = 0.01140
    lkr = 1.140
    bdt = 0.319177
    npr = 0.4055
    brl = 0.016
    qar = 0.0113
    pkr = 0.69083
    uah = 0.114605
    afn = 0.2747
elif curr1 in brazil:
    inr = 15.14
    eur = 0.18
    gbp = 0.16
    usd = 0.19
    cad = 0.25
    rub = 11.30
    yuan = 1.32
    jpy = 26.07
    aud = 0.28
    sgd = 0.26
    aed = 0.68
    lkr = 68.21
    bdt = 19.13
    npr = 24.26
    zwl = 59.37
    qar = 0.68
    pkr = 41.32
    uah = 6.86
    afn = 16.35
elif curr1 in qatar:
    inr = 22.39
    eur = 0.27
    gbp = 0.23
    usd = 0.27
    cad = 0.37
    rub = 16.71
    yuan = 1.96
    jpy = 38.55
    aud = 0.41
    sgd = 0.38
    aed = 1.01
    lkr = 100.87
    bdt = 28.28
    npr = 35.87
    zwl = 88.44
    brl = 1.48
    pkr = 61.10
    uah = 10.14
    afn = 24.17
elif curr1 in pakistan:
    inr = 0.37
    eur = 0.0043
    gbp = 0.0038
    usd = 0.0045
    cad = 0.0060
    rub = 0.27
    yuan = 0.032
    jpy = 0.63
    aud = 0.0067
    sgd = 0.0062
    aed = 0.017
    lkr = 1.65
    bdt = 0.46
    npr = 0.59
    zwl = 1.4475
    brl = 0.024
    qar = 0.016
    uah = 0.17
    afn = 0.40
elif curr1 in ukraine:
    inr = 2.21
    eur = 0.026
    gbp = 0.023
    usd = 0.027
    cad = 0.036
    rub = 1.65
    yuan = 0.19
    jpy = 3.80
    aud = 0.041
    sgd = 0.037
    aed = 0.100
    lkr = 9.95
    bdt = 2.79
    npr = 3.54
    zwl = 8.72
    brl = 0.15
    qar = 0.099
    pkr = 6.03
    afn = 2.38
elif curr1 in afghanistan:
    inr = 0.93
    eur = 0.011
    gbp = 0.0096 
    usd = 0.011
    cad = 0.015
    rub = 0.69
    yuan = 0.081
    jpy = 1.60
    aud = 0.017
    sgd = 0.016
    aed = 0.042
    lkr = 4.18
    bdt = 1.17
    npr = 1.48
    zwl = 0.2747
    brl = 0.061
    qar = 0.041
    pkr = 2.53
    uah = 0.42
    

if curr2 in india:
    print(converter(a, inr))

elif curr2 in us:
    print(converter(a, usd))

elif curr2 in uk:
    print(converter(a, gbp))

elif curr2 in canada:
    print(converter(a, cad))

elif curr2 in eu:
    print(converter(a, eur))

elif curr2 in russia:
    print(converter(a, rub))

elif curr2 in china:
    print(converter(a, yuan))

elif curr2 in japan:
    print(converter(a, jpy))

elif curr2 in aus:
    print(converter(a, aud))

elif curr2 in singapore:
    print(converter(a, sgd))

elif curr2 in uae:
    print(converter(a, aed))

elif curr2 in srilanka:
    print(converter(a, lkr))

elif curr2 in bangladesh:
    print(converter(a, bdt))

elif curr2 in nepal:
    print(converter(a, npr))

elif curr2 in zimbabawe:
    print(converter(a, zwl))

elif curr2 in brazil:
    print(converter(a, brl))

elif curr2 in qatar:
    print(converter(a, qar))

elif curr2 in pakistan:
    print(converter(a, pkr))

elif curr2 in ukraine:
    print(converter(a, uah))

elif curr2 in afghanistan:
    print(converter(a, afn))

else:
    print("wrong input")

print()
print("data as of 19th of November,2022")
