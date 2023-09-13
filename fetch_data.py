import yfinance as yf,psycopg2

cred={
    "host":"localhost",
    "user":"postgres",
    "password":"postgres",
    "database":"stock",
    "port":"5432"
}

connection=psycopg2.connect(**cred)
cursor=connection.cursor()

data = yf.download('IDFCFIRSTB.BO', start='2015-11-06', end='2023-09-12')
for index, row in data.iterrows():
    sql = "INSERT INTO idfc (date, high, low, open, close, volume) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (index, row['High'], row['Low'], row['Open'], row['Close'], row['Volume'])
    cursor.execute(sql, values)

connection.commit()
cursor.close()
connection.close()



