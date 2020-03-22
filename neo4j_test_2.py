from database_test import neo4j_select_triple_table
from EventTriplesExtraction.triple_extraction import TripleExtractor

extractor = TripleExtractor()
attribute_columns = ('triple_subject', 'triple_object')  # 属性列
data=neo4j_select_triple_table('triple_domestic',attribute_columns)

for record in data:
  print('主语:',record[0],extractor.entity_annotation(record[0]))
  print('宾语:',record[1],extractor.entity_annotation(record[1]))


