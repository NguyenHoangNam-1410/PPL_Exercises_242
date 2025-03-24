# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("\66\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\7\4\35\n\4\f\4\16\4 \13\4\3\4\5\4#\n\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\b\6\b.\n\b\r\b\16\b/\3\b\3\b\3\t")
        buf.write("\3\t\3\t\2\2\n\3\2\5\2\7\3\t\4\13\5\r\6\17\7\21\b\3\2")
        buf.write("\6\3\2c|\3\2\62;\3\2\63;\5\2\13\f\17\17\"\"\2\67\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\3\23\3\2\2\2\5\25\3\2\2\2\7\"\3\2\2\2")
        buf.write("\t$\3\2\2\2\13&\3\2\2\2\r(\3\2\2\2\17-\3\2\2\2\21\63\3")
        buf.write("\2\2\2\23\24\t\2\2\2\24\4\3\2\2\2\25\26\t\3\2\2\26\6\3")
        buf.write("\2\2\2\27#\7\62\2\2\30\36\t\4\2\2\31\35\5\5\3\2\32\33")
        buf.write("\7a\2\2\33\35\5\5\3\2\34\31\3\2\2\2\34\32\3\2\2\2\35 ")
        buf.write("\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37!\3\2\2\2 \36\3")
        buf.write("\2\2\2!#\b\4\2\2\"\27\3\2\2\2\"\30\3\2\2\2#\b\3\2\2\2")
        buf.write("$%\7=\2\2%\n\3\2\2\2&\'\7<\2\2\'\f\3\2\2\2()\7X\2\2)*")
        buf.write("\7c\2\2*+\7t\2\2+\16\3\2\2\2,.\t\5\2\2-,\3\2\2\2./\3\2")
        buf.write("\2\2/-\3\2\2\2/\60\3\2\2\2\60\61\3\2\2\2\61\62\b\b\3\2")
        buf.write("\62\20\3\2\2\2\63\64\13\2\2\2\64\65\b\t\4\2\65\22\3\2")
        buf.write("\2\2\7\2\34\36\"/\5\3\4\2\b\2\2\3\t\3")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Php_int = 1
    SEMI = 2
    COLON = 3
    VAR = 4
    WS = 5
    ERROR_CHAR = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "Php_int", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR" ]

    ruleNames = [ "Letter", "Digit", "Php_int", "SEMI", "COLON", "VAR", 
                  "WS", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.Php_int_action 
            actions[7] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def Php_int_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text.replace('_', '')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


