ALTER TABLE "departements" ADD CONSTRAINT "fk_departements_dept_no" FOREIGN KEY("dept_no")
REFERENCES "dept_manager" ("dept_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_no_from_date_to_date" FOREIGN KEY("dept_no", "from_date", "to_date")
REFERENCES "dept_manager" ("dept_no", "from_date", "to_date");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no_from_date_to_date" FOREIGN KEY("emp_no", "from_date", "to_date")
REFERENCES "salaries" ("emp_no", "from_date", "to_date");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no_from_date_to_date" FOREIGN KEY("emp_no", "from_date", "to_date")
REFERENCES "titles" ("emp_no", "from_date", "to_date");

ALTER TABLE "titles" ADD CONSTRAINT "fk_titles_emp_no_from_date_to_date" FOREIGN KEY("emp_no", "from_date", "to_date")
REFERENCES "dept_emp" ("emp_no", "from_date", "to_date");


