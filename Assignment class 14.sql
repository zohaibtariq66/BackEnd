# Write a query to get the number of employees who has the same job title.

select COUNT(*),JOB_ID from employees group by(JOB_ID);

# list down the lowest salary of the employee of every manager and also display the manager_id.

select MANAGER_ID,MIN(SALARY) FROM employees group by (MANAGER_ID);

# list down the total salaries of every deparment # NOTE: salary should be in ascending order

select sum(salary) AS Total_Salary,DEPARTMENT_ID from employees group by(DEPARTMENT_ID) order by Total_Salary;

# list down the average salaries of every department exluding IT Deparment

select avg(SALARY),DEPARTMENT_ID from employees where DEPARTMENT_ID != 60 group by(DEPARTMENT_ID);


# fetch the top 3 department who is taking the highest salary among all other deparment

select DEPARTMENT_ID,sum(SALARY) AS Total_Salary from employees group by(DEPARTMENT_ID) order by Total_Salary DESC limit 3;


# list down all the department (job_id) whose avg salary is more than overall avg salary of the whole company

select avg(SALARY) as AVG_SALARY,JOB_ID from employees group by JOB_ID having AVG_SALARY >(select avg(SALARY) from employees);

# Write a query to get employee ID, last name, and date of first salary of the employees.

select EMPLOYEE_ID,LAST_NAME,HIRE_DATE,DATE_ADD(HIRE_DATE,interval 1 month) as First_Salary from employees;

# find the department that contains more than 10 employees

select count(DEPARTMENT_ID) as Total_employee,DEPARTMENT_ID from employees group by(DEPARTMENT_ID) having Total_employee > 10;

# Write a query to get the years in which more than 10 employees joined.

select count(*) AS total_employee, YEAR(HIRE_DATE) AS HIRE_YEAR  from employees group by year(HIRE_DATE) having total_employee > 10;


#Find the number of employees in each department.
select count(*) as Total_Employees,DEPARTMENT_ID from employees group by(DEPARTMENT_ID);


#Calculate the average salary for each job title.

select avg(SALARY),JOB_ID from employees group by(JOB_ID);

#List the total salary expenditure for each department.
select sum(SALARY),DEPARTMENT_ID from employees group by (DEPARTMENT_ID);

#Find the maximum salary in each department.
select max(SALARY),DEPARTMENT_ID from employees group by (DEPARTMENT_ID);

#Count the number of employees hired in each year.
select count(*),year(HIRE_DATE) from employees group by year(HIRE_DATE);


#Determine the number of employees with the same manager.
select count(*),MANAGER_ID from employees group by(MANAGER_ID);

#Find the average commission percentage for each department.
#Skip this becasue Comission_PCT is 0 for all 

#Calculate the total duration (in days) that each employee spent in their job(s) from the `job_history` table.
select EMPLOYEE_ID,datediff(END_DATE,START_DATE) from job_history;

#Find the highest salary offered for each job title.
select max(SALARY),JOB_ID from employees group by (JOB_ID);

#JOIN
#List all employees along with their department names.

select * from employees as emp left join departments as dep on emp.DEPARTMENT_ID = dep.DEPARTMENT_ID;


#Find all employees and their job titles.
select * from employees as emp inner join jobs as job on emp.JOB_ID = job.JOB_ID;

#Retrieve the job history of each employee along with the department name they worked in
select * from job_history as j inner join departments as d on j.DEPARTMENT_ID = d.DEPARTMENT_ID;

#List the employees who are currently working under the same manager, displaying the manager's name.
select e.EMPLOYEE_ID,e.FIRST_NAME,e.LAST_NAME,e.MANAGER_ID,m.FIRST_NAME as Manager_First_Name,m.LAST_NAME as Manager_Last_Name from employees as e inner join employees as m on e.MANAGER_ID = m.EMPLOYEE_ID;
#How Can we group employees now by manager name


#Retrieve the details of all departments located in a specific city i.e "Tokyo".
select * from departments inner join locations on departments.LOCATION_ID = locations.LOCATION_ID where locations.CITY = 'Tokyo';

#Retrieve the details of all departments located in a specific cities i.e "Sydney" and "Toronto".
select * from departments inner join locations on departments.LOCATION_ID = locations.LOCATION_ID where locations.CITY In('Sydney','Toronto');

#List all employees and their managers, including those without managers.
select * from employees as e left join employees as m on e.MANAGER_ID = m.MANAGER_ID;

#Find all departments and their employees, including departments with no employees.
select * from departments;

#Retrieve a list of all job titles and the employees who have that job, including job titles with no employees.
select * from jobs as j left join employees as e on j.JOB_ID = e.JOB_ID;

#Find all employees and the locations they are working in, including locations without any employees.
#Don't have location in employee table

#List all countries and the regions they belong to, including regions without any countries.
select * from countries as c right join regions as r on c.REGION_ID = r.REGION_ID;


#List the number of employees working in each city.
#Don't have city details in employee table

#List the total salary expenditure for each department, along with the department name.
select sum(e.SALARY),d.DEPARTMENT_ID,d.DEPARTMENT_NAME from employees as e right join departments as d on e.DEPARTMENT_ID = d.DEPARTMENT_ID group by(DEPARTMENT_ID); 

#Count the number of employees in each city.
select count(e.EMPLOYEE_ID),l.city from employees as e inner join departments as d on e.DEPARTMENT_ID = d.DEPARTMENT_ID inner join locations as l on d.LOCATION_ID = l.LOCATION_ID group by (city);

#Calculate the average salary for each job title within each department.
select avg(e.SALARY),e.JOB_ID,d.DEPARTMENT_NAME from employees as e inner join departments as d on e.DEPARTMENT_ID = d.DEPARTMENT_ID group by d.DEPARTMENT_ID,e.JOB_ID;


#List the number of employees hired in each year for each job title.
select count(*),JOB_ID,year(HIRE_DATE) from employees group by JOB_ID,year(HIRE_DATE);

#Find the highest salary paid in each region.


#Count the number of employees in each country.
select count(e.EMPLOYEE_ID),l.COUNTRY_ID from employees as e inner join departments as d on e.DEPARTMENT_ID = d.DEPARTMENT_ID inner join locations as l on d.LOCATION_ID = l.LOCATION_ID group by l.COUNTRY_ID;

#Calculate the average salary and the number of employees for each department located in a specific region.
