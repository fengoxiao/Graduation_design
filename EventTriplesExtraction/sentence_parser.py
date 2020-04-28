#!/usr/bin/env python3
# coding: utf-8
# File: sentence_parser.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-3-10
'''
LTP_DIR：LTP模型的存放目录
Segmentor_lexicon：分词词典路径
Segmentor_label_lexicon：标签分词词典路径
Postagger_lexicon ：  词性标注词典路径
Postagger_label_lexicon ：标签词性标注词典路径

'''
import os
from pyltp import SentenceSplitter,Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller
class LtpParser:
    def __init__(self):
        LTP_DIR = "D:\python\ltp_data_v3.4.0"
        Segmentor_lexicon='D:\python\ltp_data_v3.4.0\lexicon'
        Segmentor_label_lexicon='D:\python\ltp_data_v3.4.0\lexicon_label'
        Postagger_lexicon =  'D:\python\ltp_data_v3.4.0\lexicon_1'
        Postagger_label_lexicon =  'D:\python\ltp_data_v3.4.0\lexicon_label_1'
        self.segmentor = Segmentor()
        self.segmentor_label = Segmentor()
        cws_model_path=os.path.join(LTP_DIR, "cws.model")
        self.segmentor.load_with_lexicon(cws_model_path, Segmentor_lexicon)  # 加载模型，第二个参数是您的外部词典文件路径
        self.segmentor_label.load_with_lexicon(cws_model_path, Segmentor_label_lexicon)  # 加载模型，第二个参数是您的外部词典文件路径

        self.postagger = Postagger()
        self.postagger_label = Postagger()
        pos_model_path=os.path.join(LTP_DIR, "pos.model")
        self.postagger.load_with_lexicon(pos_model_path,Postagger_lexicon)
        self.postagger_label.load_with_lexicon(pos_model_path,Postagger_label_lexicon)

        self.parser = Parser()
        self.parser.load(os.path.join(LTP_DIR, "parser.model"))

        self.recognizer = NamedEntityRecognizer()
        self.recognizer.load(os.path.join(LTP_DIR, "ner.model"))

        self.labeller = SementicRoleLabeller()
        self.labeller.load(os.path.join(LTP_DIR, 'pisrl_win.model'))

    '''语义角色标注'''
    def format_labelrole(self, words, postags):
        arcs = self.parser.parse(words, postags)
        roles = self.labeller.label(words, postags, arcs)
        roles_dict = {}
        for role in roles:
            #print('role.index:',role.index)
            roles_dict[role.index] = {arg.name:[arg.name,arg.range.start, arg.range.end] for arg in role.arguments}
        return roles_dict

    '''句法分析---为句子中的每个词语维护一个保存句法依存儿子节点的字典'''
    def build_parse_child_dict(self, words, postags, arcs):
        child_dict_list = []
        format_parse_list = []
        for index in range(len(words)):
            child_dict = dict()
            for arc_index in range(len(arcs)):
                if arcs[arc_index].head == index+1:   #arcs的索引从1开始
                    if arcs[arc_index].relation in child_dict:
                        child_dict[arcs[arc_index].relation].append(arc_index)
                    else:
                        child_dict[arcs[arc_index].relation] = []
                        child_dict[arcs[arc_index].relation].append(arc_index)
            child_dict_list.append(child_dict)
        rely_id = [arc.head for arc in arcs]  # 提取依存父节点id
        relation = [arc.relation for arc in arcs]  # 提取依存关系
        heads = ['Root' if id == 0 else words[id - 1] for id in rely_id]  # 匹配依存父节点词语
        for i in range(len(words)):
            # ['ATT', '李克强', 0, 'nh', '总理', 1, 'n']
            a = [relation[i], words[i], i, postags[i], heads[i], rely_id[i]-1, postags[rely_id[i]-1]]
            format_parse_list.append(a)

        return child_dict_list, format_parse_list

    '''parser主函数'''
    def parser_main(self, sentence):
        words = list(self.segmentor.segment(sentence))
        postags = list(self.postagger.postag(words))
        arcs = self.parser.parse(words, postags)
        child_dict_list, format_parse_list = self.build_parse_child_dict(words, postags, arcs)
        roles_dict = self.format_labelrole(words, postags)
        return words, postags, child_dict_list, roles_dict, format_parse_list

    def tag_entity_annotation(self,entity):
        words = self.segmentor.segment(entity)
        postags = self.postagger.postag(words)
        netags = self.recognizer.recognize(words, postags)  # 命名实体识别
        #print('\t'.join(netags))
        return words,postags,netags

    def tag_entity_annotation_v2(self,entity):
        words = self.segmentor_label.segment(entity)
        postags = self.postagger_label.postag(words)
        netags = self.recognizer.recognize(words, postags)  # 命名实体识别
        #print('\t'.join(netags))
        return words,postags,netags

if __name__ == '__main__':
    parse = LtpParser()
    sentence = '李克强总理今天来我家了,我感到非常荣幸'
    words, postags, child_dict_list, roles_dict, format_parse_list = parse.parser_main(sentence)
    print(words, len(words))
    print(postags, len(postags))
    print(child_dict_list, len(child_dict_list))
    print(roles_dict)
    print(format_parse_list, len(format_parse_list))