# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("o\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\6\20R\n\20\r\20\16\20S\3\21\6\21")
        buf.write("W\n\21\r\21\16\21X\3\22\6\22\\\n\22\r\22\16\22]\3\22\3")
        buf.write("\22\6\22b\n\22\r\22\16\22c\3\23\6\23g\n\23\r\23\16\23")
        buf.write("h\3\23\3\23\3\24\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25\3\2\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\2s\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2\5+\3\2\2\2\7")
        buf.write("-\3\2\2\2\t/\3\2\2\2\13\61\3\2\2\2\r\63\3\2\2\2\17\65")
        buf.write("\3\2\2\2\21<\3\2\2\2\23>\3\2\2\2\25B\3\2\2\2\27H\3\2\2")
        buf.write("\2\31J\3\2\2\2\33L\3\2\2\2\35N\3\2\2\2\37Q\3\2\2\2!V\3")
        buf.write("\2\2\2#[\3\2\2\2%f\3\2\2\2\'l\3\2\2\2)*\7.\2\2*\4\3\2")
        buf.write("\2\2+,\7=\2\2,\6\3\2\2\2-.\7*\2\2.\b\3\2\2\2/\60\7+\2")
        buf.write("\2\60\n\3\2\2\2\61\62\7}\2\2\62\f\3\2\2\2\63\64\7\177")
        buf.write("\2\2\64\16\3\2\2\2\65\66\7t\2\2\66\67\7g\2\2\678\7v\2")
        buf.write("\289\7w\2\29:\7t\2\2:;\7p\2\2;\20\3\2\2\2<=\7?\2\2=\22")
        buf.write("\3\2\2\2>?\7k\2\2?@\7p\2\2@A\7v\2\2A\24\3\2\2\2BC\7h\2")
        buf.write("\2CD\7n\2\2DE\7q\2\2EF\7c\2\2FG\7v\2\2G\26\3\2\2\2HI\7")
        buf.write("-\2\2I\30\3\2\2\2JK\7/\2\2K\32\3\2\2\2LM\7,\2\2M\34\3")
        buf.write("\2\2\2NO\7\61\2\2O\36\3\2\2\2PR\t\2\2\2QP\3\2\2\2RS\3")
        buf.write("\2\2\2SQ\3\2\2\2ST\3\2\2\2T \3\2\2\2UW\t\3\2\2VU\3\2\2")
        buf.write("\2WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y\"\3\2\2\2Z\\\t\3\2\2")
        buf.write("[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^_\3\2\2\2_a")
        buf.write("\7\60\2\2`b\t\3\2\2a`\3\2\2\2bc\3\2\2\2ca\3\2\2\2cd\3")
        buf.write("\2\2\2d$\3\2\2\2eg\t\4\2\2fe\3\2\2\2gh\3\2\2\2hf\3\2\2")
        buf.write("\2hi\3\2\2\2ij\3\2\2\2jk\b\23\2\2k&\3\2\2\2lm\13\2\2\2")
        buf.write("mn\b\24\3\2n(\3\2\2\2\b\2SX]ch\4\b\2\2\3\24\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    ID = 15
    INT = 16
    FLOAT = 17
    WS = 18
    ERROR_CHAR = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "'('", "')'", "'{'", "'}'", "'return'", "'='", 
            "'int'", "'float'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "FLOAT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "ID", "INT", "FLOAT", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[18] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


