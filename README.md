# Nova Futur Data Scientist Technical Test (A) Solution 
### requirements (script)
The solution is written in Python (3.9).  
To execute the script, two libraries are necessary:  
1. NumPy (1.23.2)  
2. SciPy (1.9.1)  
both of which are contained in the SciPy package.

### execution
The script dev.py can be called from command line like this: `$ python dev.py`  
Without additional arguments, the behaviour of the script is as requested in the assignment definition, ie  

```
5 2
3 3 2
1 1 2
2  
```

The script can also be called with the command line argument `--verbose`  
This option will print instructions to guide the user in correctly inputting the expected information, and visualise the solution.

```
Insert Z-city grid size (N) and number of pizzerias (M)
5 2

You have chosen a grid size of 5 and 2 pizzerias

For each pizzeria, please insert its coordinates X,Y and the number K of blocks it serves
3 3 2
1 1 2

You have entered the following coordinates and delivery distance for each pizzeria:
N. pizzeria         X coordinate        Y coordinate        K distance          
1                   3                   3                   2                   
2                   1                   1                   2                   

The city blocks delivery map is
0 0 1 0 0
0 1 1 1 0
2 1 1 1 1
1 2 1 1 0
1 1 2 0 0

The greatest pizzas selection is: 2
```

### requirements (notebook)
The solution script has been developed on a Jupyter notebook, which is included in this repository.  
To execute this notebook, the following libraries need to be installed in the environment:  
- jupyterlab (3.4.5)  
- matplotlib (3.5.3)