# EventTriplesExtraction
&nbsp;&nbsp;EventTriplesExtraction based on dependency parser and semantic role labeling, 基于依存句法与语义角色标注的事件三元组抽取
&nbsp;&nbsp;文本表示一直是个重要问题，如何以清晰，简介的方式对一个文本信息进行有效表示是个长远的任务  
   我尝试过使用关键词，实体之间的关联关系，并使用textgrapher的方式进行展示，但以词作为文本信息单元表示这种效果不是特别好，所以，本项目想尝试从事件三元组的方式出发，对文本进行表示．

# 使用方式

        from triples_extraction import *
        extractor = TripleExtractor()
        svos = extractor.triples_main(content)
        print('svos', svos)

# 测试样例
        content = '李克强总理今天来我家了,我感到非常荣幸'
        svos = [
                  ['李克强总理', '来', '我家'],
                  ['我', '感到', '荣幸']
                 ]

        content = ''' 以色列国防军20日对加沙地带实施轰炸，造成3名巴勒斯坦武装人员死亡。此外，巴勒斯坦人与以色列士兵当天在加沙地带与以交界地区发生冲突，一名巴勒斯坦人被打死。当天的冲突还造成210名巴勒斯坦人受伤。
    当天，数千名巴勒斯坦人在加沙地带边境地区继续“回归大游行”抗议活动。部分示威者燃烧轮胎，并向以军投掷石块、燃烧瓶等，驻守边境的以军士兵向示威人群发射催泪瓦斯并开枪射击。'''
        svos = [
                 ['以色列国防军', '实施', '轰炸'],
                 ['冲突', '发生', '巴勒斯坦人与以色列士兵'],
                 ['当天冲突', '造成', '受伤'],
                 ['数千名巴勒斯坦人', '继续', '回归大游行抗议活动'],
                 ['部分示威者', '投掷', '石块'],
                 ['驻守边境以军士兵', '发射', '催泪瓦斯']
                 ]

If any question about the project or me ,see https://liuhuanyong.github.io/
如有自然语言处理、知识图谱、事理图谱、社会计算、语言资源建设等问题或合作，可联系我：    
1、我的github项目介绍：https://liuhuanyong.github.io  
2、我的csdn博客：https://blog.csdn.net/lhy2014  
3、about me:刘焕勇，中国科学院软件研究所，lhy_in_blcu@126.com  
