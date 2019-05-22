import pymysql
# Tom
class Login:
    def __init__(self,database = 'user',
                 host ='localhost',
                 user ='root',
                 passwd ='5989535',
                 port =3306,
                 charset ='utf8',
                 table ='login'
                 ):
        self.database =database
        self.host =host
        self.user =user
        self.passwd =passwd
        self.port =port
        self.charset =charset
        self.table =table
        self.connect_db() # 连接数据库
    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                                  user =self.user,
                                  passwd =self.passwd,
                                  port =self.port,
                                  charset =self.charset,
                                  database =self.database
                                  )
        self.cur =self.db.cursor()
    def close_db(self):
        self.cur.close()
        self.db.close()
    def login(self,name,passwd):
        sql = 'select * from %s where name = "%s" and passwd ="%s"'%(self.table,name,passwd)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return True
        else:
            return False
    def register(self,name,passwd):
        sql = "select * from %s where name ='%s'"%(self.table,name)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return False
        sql ="insert into %s (name,passwd) values ('%s','%s');"%(self.table,name,passwd)
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception:
            self.db.rollback()
            return False
        return True

