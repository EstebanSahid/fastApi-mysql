from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://elhiperdelafruta_eswordpress:123456@localhost:3306/storedb")

meta = MetaData()

con = engine.connect()