import pymysql as p

def getConnection():
    return p.connect(host='localhost',user='root',password='',database='student')

def insertData(t):
    db=getConnection()
    cr=db.cursor()
    sql= 'insert into stud values(%s,%s,%s,%s)'
    cr.execute(sql,t)
    db.commit()
    db.close()

def updateData(t):
    db=getConnection()
    cr=db.cursor()
    sql= 'update stud set name=%s,stream=%s,address=%s where id=%s'
    cr.execute(sql,t)
    db.commit()
    db.close()

def deleteData(t):
    db=getConnection()
    cr=db.cursor()
    sql= 'delete from stud where id=%s'
    cr.execute(sql,id)
    db.commit()
    db.close()


def selectAllData():
    db=getConnection()
    cr=db.cursor()
    sql= 'select * from stud'
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

def selectById(id):
    db=getConnection()
    cr=db.cursor()
    sql= 'select * from stud where id=%s'
    cr.execute(sql,id)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def selectDataByOrder():
    db=getConnection()
    cr=db.cursor()
    sql= 'select * from stud order by name'
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist


