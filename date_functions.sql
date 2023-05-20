select sysdate from dual;

select add_months('28-Feb-2023', 1) from dual;

select sysdate + 10, sysdate - 10 from dual;

select last_day('20-Feb-2000') from dual;

select to_Date('21-may-2023', 'dd-mon-yyyy') - to_date('1-may-2023') from dual;

select sysdate, trunc(sysdate) from dual;

select sysdate+50, sysdate, floor(months_between(sysdate+50, sysdate)) from dual;


