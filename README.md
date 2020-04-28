# Graduation_design
毕业设计
项目地址：https://github.com/fengoxiao/Graduation_design

使用方法：
部署好环境变量之后（部署见下文）

1：按功能运行v1或v2或v3爬虫文件

2：运行creat_triple_table_v2，进行抽取

3：Knowledge_map_v2.py，知识图谱的构建


具体文件功能见下表5.1：
表5.1 文件功能表
文件夹	                  文件名	                描述
crawler	                略	                    爬虫相关的文件，后被整合弃用
EventTriplesExtraction	sentence_parse.py	     抽取和标注的预处理
	                      triple_extractio.py	   抽取和标注的主函数和辅助函数
lexicon_backup	        略	                    抽取和标注的自定义词典
miscellaneous	          略	                    小功能的文件，都已被整合弃用
根目录	                 crawler_total_v1.py	  初始数据集的构建
根目录	                 crawler_total_v2.py	  爬取更新的新闻
根目录	                 crawler_total_v3.py	  爬取指定类型的新闻及其始末页
根目录	                 creat_triple_table_v2	调用LTP模块抽取三元组
根目录	                 database_crawler_total.py	爬虫相关的数据库接口
根目录	                 database_interface.py	抽取和图谱构建的数据库接口
根目录                	Knowledge_map_v2.py	    知识图谱的构建文件
根目录	                 neo4j_interface.py	    图数据库的接口
根目录	                各个类型的记录.png	     记录各个类型的新闻数量

开发环境：
1. 操作系统：windows 10 64位
2. 开发语言：Python
3. 环境配置：Python3.5.4
4. 数据库：MySQL , Neo4j
5. 开发工具：JetBrains PyCharm 2019.1.3 , Navicat for MySQL

部署系统：
EventTriplesExtraction的sentence_parse.py的部署：
1. LTP_DIR：LTP模型的存放目录
2. Segmentor_lexicon：分词词典路径
3. Segmentor_label_lexicon：标签分词词典路径
4. Postagger_lexicon ：  词性标注词典路径
5. Postagger_label_lexicon ：标签词性标注词典路径

database_interface.py的部署：
1. user_name=用户名
2. pass_word=密码
3. database_name=数据库名
4. database_name_neo4j=图数据库名

database_crawler_total.py的部署：
1. user_name=用户名
2. pass_word=密码
3. database_name=数据库名

neo4j_interface.py的部署：
1. user_name=用户名
2. pass_word=密码

