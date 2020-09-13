import pandas as pd
import numpy as np


group = ['x','y','z']
data = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10)
    })

table1 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    })

table2 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10),
    "salary":np.random.randint(5,50,10),
    })



# 1. SELECT * FROM data;
data.loc[:]


# 2. SELECT * FROM data LIMIT 10;
data.head(10)
data.loc[:,['id','name','age']]

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
data.id
data['id']
data.loc[:,['id']]

# 4. SELECT COUNT(id) FROM data;
data['id'].count()

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
data[  (data['id']<1000) & ( data['age']>30 ) ]

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
table1.groupby('id').aggregate('count')

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(table1,table2,on='id',how='inner')

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat(table1,table2)

# 9. DELETE FROM table1 WHERE id=10;
data.drop( data[ data['id']==10 ].index )

# 10. ALTER TABLE table1 DROP COLUMN column_name;
data.drop('age', axis=1)