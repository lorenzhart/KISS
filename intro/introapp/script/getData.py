# -*- encoding: utf8 -*-
import gdata.spreadsheet.service
import gdata.spreadsheet.text_db
import pymongo

"""
Spreadsheetと接続する
"""
user = 'nekogusa9@gmail.com'
passwd = 'takadanobaba'
dbClient = gdata.spreadsheet.service.SpreadsheetsService(user, passwd)
dbClient.ProgrammaticLogin()

"""
シートの取得
"""
q = gdata.spreadsheet.service.ListQuery()
#q['title'] = 'testdata'
q['title'] = '新M2の名簿'
feed = dbClient.GetSpreadsheetsFeed(query=q)
spread_id = feed.entry[0].id.text.rsplit('/',1)[1]
feed =dbClient.GetWorksheetsFeed(spread_id)
sheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

"""
レコードの取得
"""
#records = dbClient.GetListFeed(self.spread_id,self.sheet_id).entry
records = dbClient.GetListFeed(spread_id, sheet_id).entry

articles = []
for entry in records:
     article = gdata.spreadsheet.text_db.Record(row_entry=entry)
     article.content['skill'] = unicode(article.content['skill']).replace(u'＃','#').split('#')
     article.content['interest'] = unicode(article.content['interest']).replace(u'＃','#').split('#')
     article.content['background'] = unicode(article.content['background']).replace(u'＃','#').split('#')
     article.content['introduce'] = unicode(article.content['introduce']).replace(u'＃','#').split('#')
     articles.append(article.content)

"""
Pymongo
"""
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['intro']
persons = db.persons

for person in articles:
    persons.update({'id':person['id']}, person, True, False)
