/* table employees */
/*Write a query to select first 10 records from a table.*/
select * from employees limit 10;

/*Write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name"*/
select FIRST_NAME AS "FIRST NAME", LAST_NAME AS "LAST NAME" from employees;

/*Get unique department id list*/
select distinct(DEPARTMENT_ID) from employees;

/*Write a query to get all employee details from the employee table order by first name, descending.*/
select FIRST_NAME,LAST_NAME FROM employees order by FIRST_NAME,LAST_NAME;

/*Write a query to display fullname and salary*/
SELECT CONCAT(first_name , ' ', last_name) AS full_name, Salary from employees;

/*display all employee salary wise from lowest to highest*/
select * from employees order by SALARY;

/*how much money the company is spending on employees on salary*/
select Sum(salary) from employees;

/*show min, max and avg salary of comapny staff*/
select min(salary) as "MIN SALARY", max(salary) AS "MAX SALARY", Avg(salary) AS "AVG SALARY" from employees;

/*show employee name, their salary and the avg salary of all staff*/
select FIRST_NAME,LAST_Name,salary, Avg(salary) AS "AVG SALARY" from employees;

/*how many emplyee does the company have, display the count*/
select count(*) from employees;

/*show the number of employees in the company and the avg salary of all staff*/
select count(EMPLOYEE_ID),avg(SALARY) from employees;

/*Write a query to get the number of jobs available in the employees table.*/

/*Write a query get all first name from employees table in upper case.*/
select upper(first_name) from employees;

/*Write a query to get first name from employees table after removing white spaces from both side.*/
select replace(first_name, ' ', '') from employees;

/*Write a query to get monthly salary (round 2 decimal places) of each and every employee*/
select round(salary,2) from employees;

# Note : Assume the salary field provides the 'annual salary' information.
# find the 3rd highest paid employee
# NOTE: the query should return 1 row only

select * from employees order by salary DESC limit 1 offset 2;

# Write a query to display the fullname (first_name, last_name) and salary for all employees whose salary is in the range $10,000 through $15,000.
select * from employees WHERE SALARY between 10000 and 15000;

# Write a query to display the fullname (first_name, last_name) and department ID of all employees in departments 30 or 100. sort the resulting data in ascending order department wise.
select CONCAT(first_name , ' ', last_name) AS full_name, DEPARTMENT_ID from employees where DEPARTMENT_ID = 30 or DEPARTMENT_ID = 100 order by DEPARTMENT_ID;



# Write a query to display the fullname (first_name, last_name) and salary for all employees whose salary is in the range $10,000 through $15,000 and are in department 30 or 100.
select CONCAT(first_name , ' ', last_name) AS full_name, DEPARTMENT_ID,salary from employees where (salary between 10000 and 15000) and (DEPARTMENT_ID = 30 or DEPARTMENT_ID = 100);

# Write a query to display the fullname (first_name, last_name) and hire date for all employees who were hired in 1987
select * from employees where YEAR(HIRE_DATE) = 1987;

# Write a query to display the last name, job, and salary for all employees whose job is that of a Programmer or a Shipping Clerk, and whose salary is not equal to $4,500, $10,000, or $15,000.
select last_name,job_id,salary from employees where (job_id = "IT_PROG" or job_id = "SH_CLERK") and (salary <> 4500 and salary <> 10000 and salary <> 15000);

# Write a query to select all record from employees where last name in 'BLAKE', 'SCOTT', 'KING' and 'FORD'.
select * from employees where LAST_NAME IN("BLAKE","SCOTT","KING","FORD");

## Datetime
# Write a query to get the first name and hire date from employees table where hire date between '1987-06-01' and '1987-07-30'

select FIRST_NAME,HIRE_DATE from employees where HIRE_DATE between '1987-06-01' and '1987-07-30';

# Write a query to get first name of employees who joined in 1987.

select FIRST_NAME from employees where YEAR(HIRE_DATE) = 1987;

# Write a query to get first name of employees who joined in 1987 and 1989.

Select FIRST_NAME from employees where YEAR(HIRE_DATE) IN(1987,1989);


# Write a query to get the firstname, lastname who joined in the month of June.

Select FIRST_NAME,LAST_NAME from employees where month(HIRE_DATE) = 6;

# Find employees hired within the last 90 days.

Select * from employees where month(HIRE_DATE) IN (10,11,12);

# List employees hired before the year 2010.

select * from employees where year(HIRE_DATE) < 2010;


## Aggregate 1 (Functions only)
# Fetch the name of jobs the company have using table employees
 
 select distinct JOB_ID from employees;
 
 # Write down the query to show how much company spend on salaries also display the count. Use table employees.

select sum(Salary),count(SALARY) from employees;

# Write down the query to display the minimum salary that a company is giving also display the count. Use table employees.

select min(Salary),count(Salary) from employees;

# Write down the query to display the maximum salary that a company is giving also display the count. Use table employees.

select max(Salary),count(Salary) from employees;

# Write a query to get the highest, lowest, sum, and average salary among all employees.

select max(salary), min(salary), sum(salary), avg(salary) from employees;


# Write down the query to display the maximum salary that a company is giving in the department IT_PROG

select max(salary) from employees where JOB_ID = 'IT_PROG';
