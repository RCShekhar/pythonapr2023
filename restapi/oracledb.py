

import oracledb

oracledb.init_oracle_client(lib_dir="/Users/rachakonda/Downloads/instantclient_19_8")
conn = oracledb.connect(
    user='shekhar',
    password='Amkette@12345',
    config_dir="/Users/rachakonda/Downloads/Wallet_W1MDO5GZHOC1ZORE",
    wallet_location="/Users/rachakonda/Downloads/Wallet_W1MDO5GZHOC1ZORE/ewallet.pem"
)

cur= conn.cursor()
rs = cur.execute("select * from emp")
for rec in rs:
    print(rec)