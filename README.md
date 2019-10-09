# BAS-explorsion

BAS is a novel optimum algorithm, which show faster convergence speed 
BAS.py includes a standard BAS 
BAS_values.py includes two improved BAS, BAS_value and BAS_gra

BAS_value applies the combination of gradient (exactly two directional derivatives) and average decline.
![image](https://github.com/Knightsll/BAS-explorsion/blob/master/image/formula.png)

Test:
Easom function
ramdom one time:  y_values:  -1.5712091404618713e-08 -8.700858255889911e-12 -0.5184496089241322
100 time results: y_means:    -0.19495767770820308 -0.08999797460596883 -0.5238536151263802
                  y_std:      0.29234763899821714 0.2861385436647583 0.2240740038392602
![image](https://github.com/Knightsll/BAS-explorsion/blob/master/image/Easom%20function.png)

eggholder function
ramdom one time:  y_values:  -93.51412271190361 -552.3535411756498 -884.7585087157593
100 time results: y_means:    -65.09998633020031 -531.5506839487141 -599.2143497033011
                  y_std:      25.58857995711236 236.862368911148 241.22103507642817
![image](https://github.com/Knightsll/BAS-explorsion/blob/master/image/eggholder.png)

Michalewicz function 100 dimension
ramdom one time:  y_values:  0.9785996560150091 3.9416710525025267 -4.744677370060398
100 time results: y_means:    3.4249047891421 -1.41334768814909 -2.9011630469216474
                  y_std:      0.8278912502233254 2.3184474297102047 1.9758462324717736
![image](https://github.com/Knightsll/BAS-explorsion/blob/master/image/Michalewicz_100.png)











