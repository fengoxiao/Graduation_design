#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
from pyltp import SentenceSplitter,Segmentor,Postagger,NamedEntityRecognizer,Parser,SementicRoleLabeller
LTP_DATA_DIR = 'D:\python\ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
srl_model_path = os.path.join(LTP_DATA_DIR, 'pisrl_win.model')  # 语义角色标注模型目录路径，模型目录为`srl`。注意该模型路径是一个目录，而不是一个文件。

text='''
猪爷爷的年龄是15岁。猪奶奶的年龄是14岁。猪爸爸的年龄是10岁。猪妈妈的年龄是9岁。乔治的年龄是2岁。佩奇的年龄是1岁。
猪爸爸和猪妈妈的关系是夫妻。猪爷爷和猪奶奶是夫妻。乔治和佩奇是姐弟。猪爷爷和猪爸爸是父子。猪爸爸和佩奇是父子。
'''

sents = SentenceSplitter.split(text)  # 分句

segmentor = Segmentor()  # 初始化实例
#segmentor.load(cws_model_path)  # 加载模型
segmentor.load_with_lexicon(cws_model_path, 'D:\python\ltp_data_v3.4.0\lexicon')
segmentor_2 = Segmentor()  # 初始化实例
# #segmentor.load(cws_model_path)  # 加载模型
segmentor_2.load_with_lexicon(cws_model_path, 'D:\python\ltp_data_v3.4.0\lexicon_label')  # 加载模型#segmentor.load_with_lexicon(cws_model_path, 'D:\python\毕业设计\lexicon')  # 加载模型，第二个参数是您的外部词典文件路径

postagger = Postagger() # 初始化实例
postagger_2 = Postagger() # 初始化实例
postagger.load_with_lexicon(pos_model_path, 'D:\python\ltp_data_v3.4.0\lexicon_1')  # 加载模型
postagger_2.load_with_lexicon(pos_model_path, 'D:\python\ltp_data_v3.4.0\lexicon_label_1')  # 加载模型
recognizer = NamedEntityRecognizer() # 初始化实例
recognizer_2 = NamedEntityRecognizer() # 初始化实例
recognizer.load(ner_model_path)  # 加载模型
recognizer_2.load(ner_model_path)  # 加载模型
parser = Parser() # 初始化实例
parser.load(par_model_path)  # 加载模型
labeller = SementicRoleLabeller() # 初始化实例
labeller.load(srl_model_path)  # 加载模型

def is_name_entity(entity):
    return entity!='O'


def show_detail(sent):
    words = segmentor.segment(sent)  # 分词
    print('\t'.join(words))
    words_2 = segmentor_2.segment(sent)  # 分词
    print('\t'.join(words_2))
    # words = ['元芳', '你', '怎么', '看']  # 分词结果
    postags = postagger.postag(words)  # 词性标注
    postags_2 = postagger_2.postag(words_2)  # 词性标注
    print('\t'.join(postags))
    print('\t'.join(postags_2))
    netags = recognizer.recognize(words, postags)  # 命名实体识别
    netags_2 = recognizer_2.recognize(words_2, postags_2)  # 命名实体识别
    print('\t'.join(netags))
    print('\t'.join(netags_2))
    name_entity=list(filter(is_name_entity,netags))
    print('\t'.join(name_entity))

    arcs = parser.parse(words, postags)  # 句法分析
    print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))

    roles = labeller.label(words, postags, arcs)  # 语义角色标注
    # 打印结果
    for role in roles:
        print(role.index,
              "".join(["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))

if __name__ == '__main__':

    #sents = ['深圳人大代表委员','两家全球邮轮公司','三部委','招商局集团','元芳你怎么看', '猪爸爸和猪妈妈和乔治', '猪爷爷年龄', '乔治年龄', '猪爷爷和猪奶奶', '猪爸爸和佩奇']
    sents = ['他','他们','诸多挑战','深圳人大代表委员','两家全球邮轮公司','三部委','招商局集团']

    for sent in sents:
        # print(sent)
        show_detail(sent)
    segmentor.release()  # 释放模型
    postagger.release()  # 释放模型
    recognizer.release()  # 释放模型
    parser.release()  # 释放模型
    labeller.release()  # 释放模型






