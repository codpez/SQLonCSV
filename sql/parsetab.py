
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS ASC ASTERISK BY COMMA COUNT DATA DELETE DESC DOT EQUALS FILE FROM GREATER GROUP IDENTIFIER INNER INSERT INTO JOIN LESS LIMIT LPAREN NUMBER ON OR ORDER PATH RPAREN SELECT SEMICOLON SET STRING UPDATE VALUES WHEREstatement : SET DATA FROM FILE path eospath : PATHexpression : IDENTIFIER\n                     | IDENTIFIER DOT IDENTIFIER\n                     | ASTERISKstatement : SELECT columns FROM table_reference optional_clauses eosstatement : INSERT INTO table LPAREN columns RPAREN VALUES LPAREN values RPAREN eosstatement : UPDATE table SET column EQUALS value WHERE condition eosstatement : DELETE FROM table WHERE condition eosjoin_clause : INNER JOIN IDENTIFIER ON join_conditionjoin_condition : IDENTIFIER EQUALS IDENTIFIERaggregate_function : COUNT LPAREN expression RPAREN\n                              | COUNT LPAREN expression RPAREN AS IDENTIFIERtable_reference : IDENTIFIER\n                           | IDENTIFIER IDENTIFIER\n                           | table_reference join_clause\n                           | emptycolumns : columns COMMA column\n                   | ASTERISK\n                   | columncolumn : IDENTIFIER\n                  | IDENTIFIER DOT IDENTIFIER\n                  | aggregate_function\n                  | column AS IDENTIFIERtable : IDENTIFIEReos : SEMICOLONvalues : values COMMA value\n                  | valuevalue : NUMBER\n                 | STRINGcondition : column EQUALS value\n                 | column GREATER NUMBER\n                 | column LESS NUMBER\n                 | condition logical conditionwhere_clause : WHERE conditionlimit_clause : LIMIT NUMBERorder_clause : ORDER BY column\n                        | ORDER BY column DESC\n                        | ORDER BY column ASCgroup_columns : group_columns COMMA column\n                        | columngroup_clause : GROUP BY group_columnsempty :logical : AND\n                   | ORoptional_clauses : where_clause group_clause order_clause limit_clause\n                        | group_clause order_clause limit_clause\n                        | where_clause order_clause limit_clause\n                        | where_clause group_clause limit_clause\n                        | where_clause group_clause order_clause\n                        | where_clause limit_clause\n                        | where_clause order_clause\n                        | where_clause group_clause\n                        | group_clause order_clause\n                        | group_clause limit_clause\n                        | order_clause limit_clause\n                        | limit_clause\n                        | group_clause\n                        | order_clause\n                        | where_clause\n                        | empty'
    
_lr_action_items = {'SET':([0,15,16,],[2,25,-25,]),'SELECT':([0,],[3,]),'INSERT':([0,],[4,]),'UPDATE':([0,],[5,]),'DELETE':([0,],[6,]),'$end':([1,61,62,63,81,115,120,],[0,-1,-26,-6,-9,-8,-7,]),'DATA':([2,],[7,]),'ASTERISK':([3,23,37,],[10,36,10,]),'IDENTIFIER':([3,5,14,17,19,20,21,22,23,25,29,37,39,50,56,70,72,73,75,82,83,84,98,104,105,116,],[11,16,16,16,29,11,32,33,35,11,54,11,11,11,76,92,11,11,96,11,-44,-45,11,110,11,119,]),'COUNT':([3,20,25,37,39,50,72,73,82,83,84,98,105,],[13,13,13,13,13,13,13,13,13,-44,-45,13,13,]),'INTO':([4,],[14,]),'FROM':([6,7,8,9,10,11,12,31,32,33,55,96,],[17,18,19,-20,-19,-21,-23,-18,-24,-22,-12,-13,]),'COMMA':([8,9,10,11,12,31,32,33,55,57,79,80,93,94,96,112,113,114,121,],[20,-20,-19,-21,-23,-18,-24,-22,-12,20,-29,-30,105,-41,-13,-40,118,-28,-27,]),'RPAREN':([9,10,11,12,31,32,33,34,35,36,55,57,76,79,80,96,113,114,121,],[-20,-19,-21,-23,-18,-24,-22,55,-3,-5,-12,77,-4,-29,-30,-13,117,-28,-27,]),'AS':([9,11,12,31,32,33,38,55,60,94,95,96,112,],[21,-21,-23,21,-24,-22,21,75,21,21,21,-13,21,]),'EQUALS':([11,12,32,33,38,55,60,96,110,],[-21,-23,-24,-22,58,-12,85,-13,116,]),'GREATER':([11,12,32,33,55,60,96,],[-21,-23,-24,-22,-12,86,-13,]),'LESS':([11,12,32,33,55,60,96,],[-21,-23,-24,-22,-12,87,-13,]),'ORDER':([11,12,19,28,29,30,32,33,43,44,45,54,55,64,71,79,80,93,94,96,99,100,101,102,111,112,119,],[-21,-23,-43,52,-14,-17,-24,-22,-16,52,52,-15,-12,52,-35,-29,-30,-42,-41,-13,-34,-31,-32,-33,-10,-40,-11,]),'LIMIT':([11,12,19,28,29,30,32,33,43,44,45,46,54,55,64,65,67,71,79,80,88,93,94,95,96,99,100,101,102,106,107,111,112,119,],[-21,-23,-43,53,-14,-17,-24,-22,-16,53,53,53,-15,-12,53,53,53,-35,-29,-30,53,-42,-41,-37,-13,-34,-31,-32,-33,-38,-39,-10,-40,-11,]),'SEMICOLON':([11,12,19,28,29,30,32,33,40,41,42,43,44,45,46,47,48,54,55,59,64,65,66,67,68,69,71,74,79,80,88,89,90,91,93,94,95,96,99,100,101,102,103,106,107,109,111,112,117,119,],[-21,-23,-43,-43,-14,-17,-24,-22,62,-2,62,-16,-60,-58,-59,-57,-61,-15,-12,62,-53,-52,-51,-54,-55,-56,-35,-36,-29,-30,-50,-49,-48,-47,-42,-41,-37,-13,-34,-31,-32,-33,-46,-38,-39,62,-10,-40,62,-11,]),'DESC':([11,12,32,33,55,95,96,],[-21,-23,-24,-22,-12,106,-13,]),'ASC':([11,12,32,33,55,95,96,],[-21,-23,-24,-22,-12,107,-13,]),'DOT':([11,35,],[22,56,]),'LPAREN':([13,16,24,97,],[23,-25,37,108,]),'WHERE':([16,19,26,28,29,30,43,54,78,79,80,111,119,],[-25,-43,39,50,-14,-17,-16,-15,98,-29,-30,-10,-11,]),'FILE':([18,],[27,]),'INNER':([19,28,29,30,43,54,111,119,],[-43,49,-14,-17,-16,-15,-10,-11,]),'GROUP':([19,28,29,30,43,44,54,71,79,80,99,100,101,102,111,119,],[-43,51,-14,-17,-16,51,-15,-35,-29,-30,-34,-31,-32,-33,-10,-11,]),'PATH':([27,],[41,]),'JOIN':([49,],[70,]),'BY':([51,52,],[72,73,]),'NUMBER':([53,58,85,86,87,108,118,],[74,79,79,101,102,79,79,]),'STRING':([58,85,108,118,],[80,80,80,80,]),'AND':([59,71,79,80,99,100,101,102,109,],[83,83,-29,-30,83,-31,-32,-33,83,]),'OR':([59,71,79,80,99,100,101,102,109,],[84,84,-29,-30,84,-31,-32,-33,84,]),'VALUES':([77,],[97,]),'ON':([92,],[104,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'columns':([3,37,],[8,57,]),'column':([3,20,25,37,39,50,72,73,82,98,105,],[9,31,38,9,60,60,94,95,60,60,112,]),'aggregate_function':([3,20,25,37,39,50,72,73,82,98,105,],[12,12,12,12,12,12,12,12,12,12,12,]),'table':([5,14,17,],[15,24,26,]),'table_reference':([19,],[28,]),'empty':([19,28,],[30,48,]),'expression':([23,],[34,]),'path':([27,],[40,]),'optional_clauses':([28,],[42,]),'join_clause':([28,],[43,]),'where_clause':([28,],[44,]),'group_clause':([28,44,],[45,64,]),'order_clause':([28,44,45,64,],[46,65,67,88,]),'limit_clause':([28,44,45,46,64,65,67,88,],[47,66,68,69,89,90,91,103,]),'condition':([39,50,82,98,],[59,71,99,109,]),'eos':([40,42,59,109,117,],[61,63,81,115,120,]),'value':([58,85,108,118,],[78,100,114,121,]),'logical':([59,71,99,109,],[82,82,82,82,]),'group_columns':([72,],[93,]),'join_condition':([104,],[111,]),'values':([108,],[113,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> SET DATA FROM FILE path eos','statement',6,'p_statement_set_data','parser.py',15),
  ('path -> PATH','path',1,'p_path','parser.py',18),
  ('expression -> IDENTIFIER','expression',1,'p_expression','parser.py',22),
  ('expression -> IDENTIFIER DOT IDENTIFIER','expression',3,'p_expression','parser.py',23),
  ('expression -> ASTERISK','expression',1,'p_expression','parser.py',24),
  ('statement -> SELECT columns FROM table_reference optional_clauses eos','statement',6,'p_statement_select','parser.py',35),
  ('statement -> INSERT INTO table LPAREN columns RPAREN VALUES LPAREN values RPAREN eos','statement',11,'p_statement_insert','parser.py',39),
  ('statement -> UPDATE table SET column EQUALS value WHERE condition eos','statement',9,'p_statement_update','parser.py',43),
  ('statement -> DELETE FROM table WHERE condition eos','statement',6,'p_statement_delete','parser.py',47),
  ('join_clause -> INNER JOIN IDENTIFIER ON join_condition','join_clause',5,'p_join_clause','parser.py',51),
  ('join_condition -> IDENTIFIER EQUALS IDENTIFIER','join_condition',3,'p_join_condition','parser.py',55),
  ('aggregate_function -> COUNT LPAREN expression RPAREN','aggregate_function',4,'p_aggregate_function','parser.py',59),
  ('aggregate_function -> COUNT LPAREN expression RPAREN AS IDENTIFIER','aggregate_function',6,'p_aggregate_function','parser.py',60),
  ('table_reference -> IDENTIFIER','table_reference',1,'p_table_reference','parser.py',67),
  ('table_reference -> IDENTIFIER IDENTIFIER','table_reference',2,'p_table_reference','parser.py',68),
  ('table_reference -> table_reference join_clause','table_reference',2,'p_table_reference','parser.py',69),
  ('table_reference -> empty','table_reference',1,'p_table_reference','parser.py',70),
  ('columns -> columns COMMA column','columns',3,'p_columns_list','parser.py',83),
  ('columns -> ASTERISK','columns',1,'p_columns_list','parser.py',84),
  ('columns -> column','columns',1,'p_columns_list','parser.py',85),
  ('column -> IDENTIFIER','column',1,'p_column','parser.py',92),
  ('column -> IDENTIFIER DOT IDENTIFIER','column',3,'p_column','parser.py',93),
  ('column -> aggregate_function','column',1,'p_column','parser.py',94),
  ('column -> column AS IDENTIFIER','column',3,'p_column','parser.py',95),
  ('table -> IDENTIFIER','table',1,'p_table','parser.py',111),
  ('eos -> SEMICOLON','eos',1,'p_eos','parser.py',115),
  ('values -> values COMMA value','values',3,'p_values_list','parser.py',119),
  ('values -> value','values',1,'p_values_list','parser.py',120),
  ('value -> NUMBER','value',1,'p_value','parser.py',124),
  ('value -> STRING','value',1,'p_value','parser.py',125),
  ('condition -> column EQUALS value','condition',3,'p_condition','parser.py',129),
  ('condition -> column GREATER NUMBER','condition',3,'p_condition','parser.py',130),
  ('condition -> column LESS NUMBER','condition',3,'p_condition','parser.py',131),
  ('condition -> condition logical condition','condition',3,'p_condition','parser.py',132),
  ('where_clause -> WHERE condition','where_clause',2,'p_where_clause','parser.py',136),
  ('limit_clause -> LIMIT NUMBER','limit_clause',2,'p_limit_clause','parser.py',140),
  ('order_clause -> ORDER BY column','order_clause',3,'p_order_clause','parser.py',144),
  ('order_clause -> ORDER BY column DESC','order_clause',4,'p_order_clause','parser.py',145),
  ('order_clause -> ORDER BY column ASC','order_clause',4,'p_order_clause','parser.py',146),
  ('group_columns -> group_columns COMMA column','group_columns',3,'p_group_columns','parser.py',153),
  ('group_columns -> column','group_columns',1,'p_group_columns','parser.py',154),
  ('group_clause -> GROUP BY group_columns','group_clause',3,'p_group_clause','parser.py',161),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',165),
  ('logical -> AND','logical',1,'p_logical','parser.py',169),
  ('logical -> OR','logical',1,'p_logical','parser.py',170),
  ('optional_clauses -> where_clause group_clause order_clause limit_clause','optional_clauses',4,'p_optional_clauses','parser.py',174),
  ('optional_clauses -> group_clause order_clause limit_clause','optional_clauses',3,'p_optional_clauses','parser.py',175),
  ('optional_clauses -> where_clause order_clause limit_clause','optional_clauses',3,'p_optional_clauses','parser.py',176),
  ('optional_clauses -> where_clause group_clause limit_clause','optional_clauses',3,'p_optional_clauses','parser.py',177),
  ('optional_clauses -> where_clause group_clause order_clause','optional_clauses',3,'p_optional_clauses','parser.py',178),
  ('optional_clauses -> where_clause limit_clause','optional_clauses',2,'p_optional_clauses','parser.py',179),
  ('optional_clauses -> where_clause order_clause','optional_clauses',2,'p_optional_clauses','parser.py',180),
  ('optional_clauses -> where_clause group_clause','optional_clauses',2,'p_optional_clauses','parser.py',181),
  ('optional_clauses -> group_clause order_clause','optional_clauses',2,'p_optional_clauses','parser.py',182),
  ('optional_clauses -> group_clause limit_clause','optional_clauses',2,'p_optional_clauses','parser.py',183),
  ('optional_clauses -> order_clause limit_clause','optional_clauses',2,'p_optional_clauses','parser.py',184),
  ('optional_clauses -> limit_clause','optional_clauses',1,'p_optional_clauses','parser.py',185),
  ('optional_clauses -> group_clause','optional_clauses',1,'p_optional_clauses','parser.py',186),
  ('optional_clauses -> order_clause','optional_clauses',1,'p_optional_clauses','parser.py',187),
  ('optional_clauses -> where_clause','optional_clauses',1,'p_optional_clauses','parser.py',188),
  ('optional_clauses -> empty','optional_clauses',1,'p_optional_clauses','parser.py',189),
]
