import redshift_connector as rc

conn = rc.connect(
     host='redshift-cluster-1.cbubacqrsnjs.us-east-1.redshift.amazonaws.com',
     database='dev',
     port=5439,
     user='awsuser',
     password='Amkette1234'
  )

cur = conn.cursor()
cur.execute("select * from employee")
result = cur.fetchall()

print (result)