You have been invited to participate in one of the UNICEF projects - the international division of the UN,
whose mission is to improve the well-being of children around the world.
The essence of the project is to track the impact of living conditions of students aged 15 to 22 years on their performance in mathematics,
to identify students at risk at an early stage.

And this can be done with the help of a model that would predict the results of the state exam in mathematics for each student in the school.
To determine the parameters of the future model, we will conduct a reconnaissance analysis of the data and compile a report on its results. 

Exploratory data analysis (EDA)
Objectives:
- Formulate assumptions and hypotheses for the further construction of the model.
-Check data quality and clean it if necessary.
- Decide on the parameters of the model.

Description of dataset
The variables that the dataset contains are:

1 school - the abbreviation of the school in which the student is studying
2 sex - student's gender ('F' - female, 'M' - male)
3 age - student's age (from 15 to 22)
4 address - student's address type ('U' - urban, 'R' - outside the city)
5 famsize - family size ('LE3' <= 3, 'GT3'> 3)
6 Pstatus - open housing status of parents ('T' - live together 'A' - separately)
7 Medu - mother's education (0 - no, 1 - 4 classes, 2 - 5-9 classes, 3 - secondary special or 11 classes, 4 - higher)
8 Fedu - father's education (0 - no, 1 - 4 classes, 2 - 5-9 classes, 3 - secondary special or 11 classes, 4 - higher)
9 Mjob - mother’s work (“teacher” - teacher, “health” - the health sector, “services” - public service, “at_home” - does not work, “other” - other)
10 Fjob - father's work ('teacher' - teacher, 'health' - healthcare, 'services' - public service, 'at_home' - not working, 'other' - other)
11 reason - the reason for choosing a school (“home” - proximity to home, “reputation” - school reputation, “course” - educational program, “other” - other)
12 guardian - guardian ("mother" - mother, "father" - father, "other" - other)
13 traveltime - travel time to school (1 - <15 min., 2 - 15-30 min., 3 - 30-60 min., 4 -> 60 min.)
14 studytime - time to study in addition to school per week (1 - <2 hours, 2 - 2-5 hours, 3 - 5-10 hours, 4 -> 10 hours)
15 failures - the number of extracurricular failures (n if 1 <= n <= 3, otherwise 0)
16 schoolsup - additional educational support (yes or no)
17 famsup - family educational support (yes or no)
18 paid - additional paid classes in mathematics (yes or no)
19 activities - extracurricular activities (yes or no)
20 nursery - attended kindergarten (yes or no)
21 higher - wants to get a higher education (yes or no)
22 internet - Internet at home (yes or no)
23 romantic - in a romantic relationship (yes or no)
24 famrel - family relationships (from 1 - very poor to 5 - very good)
25 freetime - free time after school (from 1 - very little to 5 - very much)
26 goout - spending time with friends (from 1 - very little to 5 - very much)
27 health - current state of health (from 1 - very poor to 5 - very good)
28 absences - the number of missed classes
29 score - math exam scores

Stages of the project:

1. We carry out the initial data processing.
2. Let us estimate the number of unique values ​​for categorical variables and transform them.
3. Let us estimate the number of unique values ​​for nominative variables and transform them.
4.Let's look at the distribution of the trait for numerical variables, eliminate outliers.
5. Conduct a correlation analysis of quantitative variables
6. Select non-correlating variables.
7. Let us analyze the nominative variables and eliminate those that do not affect the predicted value (in our case, the score variable).
8. Let us formulate conclusions regarding the quality of the data and those variables that will be used in the further construction of the model.