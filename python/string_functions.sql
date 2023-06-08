
select to_char(10) + 2 from dual;

select * from emp;

select sal+nvl(comm, 0) from emp;


select to_number('10.3'), '10.3' from dual;

select to_char(sal), sal from emp;

--select trim(both '*'from '####hello*****') as trim from dual;

--if i want to trim both # and * how to do


select trim(both '#' from trim(both '*' from '####hello*****')) from dual;

select rtrim(ltrim('*****####hello*****####', '*#'), '*#') from dual;





