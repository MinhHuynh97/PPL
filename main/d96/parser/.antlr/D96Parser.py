# Generated from /Users/minh/Downloads/initial-8/src/main/d96/parser/D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u022a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3~\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4\u0085\n\4\3\4\3\4\3\4\5\4\u008a\n\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u0092\n\5\3\6\3\6\5\6\u0096\n\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u009f\n\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\5\b\u00aa\n\b\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\5\n\u00b2\n\n\3\13\3\13\3\13\3\13\5\13\u00b8\n\13")
        buf.write("\3\f\3\f\3\r\3\r\5\r\u00be\n\r\3\r\3\r\3\r\3\r\5\r\u00c4")
        buf.write("\n\r\5\r\u00c6\n\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00ce\n\16\3\16\3\16\5\16\u00d2\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00de\n\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\5\20\u00e5\n\20\3\21\3\21\3\21\3")
        buf.write("\21\5\21\u00eb\n\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\5\23\u00f8\n\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0105\n\24")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u010b\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\5\26\u0116\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u011e\n\27\3\27\3\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\5\30\u0127\n\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u012e\n\31\3\32\3\32\3\32\3\32\3\32\3\32\7")
        buf.write("\32\u0136\n\32\f\32\16\32\u0139\13\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\7\33\u0141\n\33\f\33\16\33\u0144\13\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\7\34\u014c\n\34\f\34\16\34")
        buf.write("\u014f\13\34\3\35\3\35\3\35\5\35\u0154\n\35\3\36\3\36")
        buf.write("\3\36\5\36\u0159\n\36\3\37\3\37\3\37\3\37\3\37\7\37\u0160")
        buf.write("\n\37\f\37\16\37\u0163\13\37\3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \5 \u0171\n \3 \7 \u0174\n \f \16 \u0177\13")
        buf.write(" \3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0182\n!\3!\3!\5!\u0186")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\5\"\u018d\n\"\3\"\3\"\5\"\u0191")
        buf.write("\n\"\3#\3#\3#\3#\3#\5#\u0198\n#\3$\3$\3$\3$\5$\u019e\n")
        buf.write("$\3%\3%\3%\3%\3%\5%\u01a5\n%\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\5\'\u01b3\n\'\3(\3(\3(\3(\3(\5(\u01ba")
        buf.write("\n(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\5+\u01ce\n+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3/\5/\u01df\n/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u01e9\n\60\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\5\64\u01f8\n\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\5\65\u0201\n\65\3\65\3\65\3")
        buf.write("\66\3\66\3\66\3\66\5\66\u0209\n\66\3\67\3\67\3\67\3\67")
        buf.write("\5\67\u020f\n\67\38\38\38\38\58\u0215\n8\39\39\39\39\3")
        buf.write("9\59\u021c\n9\3:\3:\3:\3:\3:\5:\u0223\n:\3;\3;\3;\3;\3")
        buf.write(";\3;\2\7\62\64\66<><\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jlnprt\2\n\3\2\23\24\3\2=>\3\2-.\4\2&&(,\3\2$%\3\2\36")
        buf.write("\37\3\2 \"\3\2\3\4\2\u0239\2v\3\2\2\2\4}\3\2\2\2\6\177")
        buf.write("\3\2\2\2\b\u0091\3\2\2\2\n\u0095\3\2\2\2\f\u0097\3\2\2")
        buf.write("\2\16\u00a2\3\2\2\2\20\u00ad\3\2\2\2\22\u00b1\3\2\2\2")
        buf.write("\24\u00b7\3\2\2\2\26\u00b9\3\2\2\2\30\u00c5\3\2\2\2\32")
        buf.write("\u00d1\3\2\2\2\34\u00dd\3\2\2\2\36\u00e4\3\2\2\2 \u00e6")
        buf.write("\3\2\2\2\"\u00ef\3\2\2\2$\u00f4\3\2\2\2&\u0104\3\2\2\2")
        buf.write("(\u010a\3\2\2\2*\u0115\3\2\2\2,\u0117\3\2\2\2.\u0126\3")
        buf.write("\2\2\2\60\u012d\3\2\2\2\62\u012f\3\2\2\2\64\u013a\3\2")
        buf.write("\2\2\66\u0145\3\2\2\28\u0153\3\2\2\2:\u0158\3\2\2\2<\u015a")
        buf.write("\3\2\2\2>\u0164\3\2\2\2@\u0185\3\2\2\2B\u0190\3\2\2\2")
        buf.write("D\u0197\3\2\2\2F\u019d\3\2\2\2H\u01a4\3\2\2\2J\u01a6\3")
        buf.write("\2\2\2L\u01ab\3\2\2\2N\u01b9\3\2\2\2P\u01bb\3\2\2\2R\u01c1")
        buf.write("\3\2\2\2T\u01c4\3\2\2\2V\u01d2\3\2\2\2X\u01d5\3\2\2\2")
        buf.write("Z\u01d8\3\2\2\2\\\u01db\3\2\2\2^\u01e8\3\2\2\2`\u01ea")
        buf.write("\3\2\2\2b\u01ec\3\2\2\2d\u01f3\3\2\2\2f\u01f7\3\2\2\2")
        buf.write("h\u01f9\3\2\2\2j\u0208\3\2\2\2l\u020e\3\2\2\2n\u0214\3")
        buf.write("\2\2\2p\u021b\3\2\2\2r\u0222\3\2\2\2t\u0224\3\2\2\2vw")
        buf.write("\5\4\3\2wx\7\2\2\3x\3\3\2\2\2yz\5\6\4\2z{\5\4\3\2{~\3")
        buf.write("\2\2\2|~\5\6\4\2}y\3\2\2\2}|\3\2\2\2~\5\3\2\2\2\177\u0084")
        buf.write("\7\22\2\2\u0080\u0085\7=\2\2\u0081\u0082\7=\2\2\u0082")
        buf.write("\u0083\7\63\2\2\u0083\u0085\7=\2\2\u0084\u0080\3\2\2\2")
        buf.write("\u0084\u0081\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0089\7")
        buf.write("\67\2\2\u0087\u008a\5\b\5\2\u0088\u008a\3\2\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a\u008b\3\2\2\2")
        buf.write("\u008b\u008c\78\2\2\u008c\7\3\2\2\2\u008d\u008e\5\n\6")
        buf.write("\2\u008e\u008f\5\b\5\2\u008f\u0092\3\2\2\2\u0090\u0092")
        buf.write("\5\n\6\2\u0091\u008d\3\2\2\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("\t\3\2\2\2\u0093\u0096\5\22\n\2\u0094\u0096\5\32\16\2")
        buf.write("\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\13\3\2")
        buf.write("\2\2\u0097\u0098\7\24\2\2\u0098\u0099\5\24\13\2\u0099")
        buf.write("\u009a\7\63\2\2\u009a\u009e\5^\60\2\u009b\u009c\7\'\2")
        buf.write("\2\u009c\u009f\5\30\r\2\u009d\u009f\3\2\2\2\u009e\u009b")
        buf.write("\3\2\2\2\u009e\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00a1\7\66\2\2\u00a1\r\3\2\2\2\u00a2\u00a3\7\23\2\2\u00a3")
        buf.write("\u00a4\5\24\13\2\u00a4\u00a5\7\63\2\2\u00a5\u00a9\5^\60")
        buf.write("\2\u00a6\u00a7\7\'\2\2\u00a7\u00aa\5\30\r\2\u00a8\u00aa")
        buf.write("\3\2\2\2\u00a9\u00a6\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa")
        buf.write("\u00ab\3\2\2\2\u00ab\u00ac\7\66\2\2\u00ac\17\3\2\2\2\u00ad")
        buf.write("\u00ae\t\2\2\2\u00ae\21\3\2\2\2\u00af\u00b2\5\f\7\2\u00b0")
        buf.write("\u00b2\5\16\b\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2")
        buf.write("\2\u00b2\23\3\2\2\2\u00b3\u00b4\t\3\2\2\u00b4\u00b5\7")
        buf.write("\65\2\2\u00b5\u00b8\5\24\13\2\u00b6\u00b8\t\3\2\2\u00b7")
        buf.write("\u00b3\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\25\3\2\2\2\u00b9")
        buf.write("\u00ba\t\3\2\2\u00ba\27\3\2\2\2\u00bb\u00be\5.\30\2\u00bc")
        buf.write("\u00be\7\20\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3\2\2")
        buf.write("\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\7\65\2\2\u00c0\u00c6")
        buf.write("\5\30\r\2\u00c1\u00c4\5.\30\2\u00c2\u00c4\7\20\2\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c6\3\2\2\2")
        buf.write("\u00c5\u00bd\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\31\3\2")
        buf.write("\2\2\u00c7\u00d2\5 \21\2\u00c8\u00d2\5\"\22\2\u00c9\u00ca")
        buf.write("\t\3\2\2\u00ca\u00cd\7/\2\2\u00cb\u00ce\5\34\17\2\u00cc")
        buf.write("\u00ce\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\u00d0\7\60\2\2\u00d0\u00d2")
        buf.write("\5$\23\2\u00d1\u00c7\3\2\2\2\u00d1\u00c8\3\2\2\2\u00d1")
        buf.write("\u00c9\3\2\2\2\u00d2\33\3\2\2\2\u00d3\u00d4\5\36\20\2")
        buf.write("\u00d4\u00d5\7\63\2\2\u00d5\u00d6\5^\60\2\u00d6\u00d7")
        buf.write("\7\66\2\2\u00d7\u00d8\5\34\17\2\u00d8\u00de\3\2\2\2\u00d9")
        buf.write("\u00da\5\36\20\2\u00da\u00db\7\63\2\2\u00db\u00dc\5^\60")
        buf.write("\2\u00dc\u00de\3\2\2\2\u00dd\u00d3\3\2\2\2\u00dd\u00d9")
        buf.write("\3\2\2\2\u00de\35\3\2\2\2\u00df\u00e0\5\26\f\2\u00e0\u00e1")
        buf.write("\7\65\2\2\u00e1\u00e2\5\36\20\2\u00e2\u00e5\3\2\2\2\u00e3")
        buf.write("\u00e5\5\26\f\2\u00e4\u00df\3\2\2\2\u00e4\u00e3\3\2\2")
        buf.write("\2\u00e5\37\3\2\2\2\u00e6\u00e7\7\30\2\2\u00e7\u00ea\7")
        buf.write("/\2\2\u00e8\u00eb\5\34\17\2\u00e9\u00eb\3\2\2\2\u00ea")
        buf.write("\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\u00ed\7\60\2\2\u00ed\u00ee\5$\23\2\u00ee!\3\2\2")
        buf.write("\2\u00ef\u00f0\7\31\2\2\u00f0\u00f1\7/\2\2\u00f1\u00f2")
        buf.write("\7\60\2\2\u00f2\u00f3\5$\23\2\u00f3#\3\2\2\2\u00f4\u00f7")
        buf.write("\7\67\2\2\u00f5\u00f8\5(\25\2\u00f6\u00f8\3\2\2\2\u00f7")
        buf.write("\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fa\78\2\2\u00fa%\3\2\2\2\u00fb\u0105\5\f\7\2")
        buf.write("\u00fc\u0105\5J&\2\u00fd\u0105\5L\'\2\u00fe\u0105\5T+")
        buf.write("\2\u00ff\u0105\5V,\2\u0100\u0105\5X-\2\u0101\u0105\5Z")
        buf.write(".\2\u0102\u0105\5\\/\2\u0103\u0105\5$\23\2\u0104\u00fb")
        buf.write("\3\2\2\2\u0104\u00fc\3\2\2\2\u0104\u00fd\3\2\2\2\u0104")
        buf.write("\u00fe\3\2\2\2\u0104\u00ff\3\2\2\2\u0104\u0100\3\2\2\2")
        buf.write("\u0104\u0101\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0103\3")
        buf.write("\2\2\2\u0105\'\3\2\2\2\u0106\u0107\5&\24\2\u0107\u0108")
        buf.write("\5(\25\2\u0108\u010b\3\2\2\2\u0109\u010b\5&\24\2\u010a")
        buf.write("\u0106\3\2\2\2\u010a\u0109\3\2\2\2\u010b)\3\2\2\2\u010c")
        buf.write("\u010d\7\61\2\2\u010d\u010e\5.\30\2\u010e\u010f\7\62\2")
        buf.write("\2\u010f\u0110\5*\26\2\u0110\u0116\3\2\2\2\u0111\u0112")
        buf.write("\7\61\2\2\u0112\u0113\5.\30\2\u0113\u0114\7\62\2\2\u0114")
        buf.write("\u0116\3\2\2\2\u0115\u010c\3\2\2\2\u0115\u0111\3\2\2\2")
        buf.write("\u0116+\3\2\2\2\u0117\u0118\5.\30\2\u0118\u0119\7\64\2")
        buf.write("\2\u0119\u011a\5\26\f\2\u011a\u011d\7/\2\2\u011b\u011e")
        buf.write("\5\34\17\2\u011c\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011d")
        buf.write("\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\7\60\2")
        buf.write("\2\u0120-\3\2\2\2\u0121\u0122\5\60\31\2\u0122\u0123\t")
        buf.write("\4\2\2\u0123\u0124\5\60\31\2\u0124\u0127\3\2\2\2\u0125")
        buf.write("\u0127\5\60\31\2\u0126\u0121\3\2\2\2\u0126\u0125\3\2\2")
        buf.write("\2\u0127/\3\2\2\2\u0128\u0129\5\62\32\2\u0129\u012a\t")
        buf.write("\5\2\2\u012a\u012b\5\62\32\2\u012b\u012e\3\2\2\2\u012c")
        buf.write("\u012e\5\62\32\2\u012d\u0128\3\2\2\2\u012d\u012c\3\2\2")
        buf.write("\2\u012e\61\3\2\2\2\u012f\u0130\b\32\1\2\u0130\u0131\5")
        buf.write("\64\33\2\u0131\u0137\3\2\2\2\u0132\u0133\f\4\2\2\u0133")
        buf.write("\u0134\t\6\2\2\u0134\u0136\5\64\33\2\u0135\u0132\3\2\2")
        buf.write("\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\63\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013b")
        buf.write("\b\33\1\2\u013b\u013c\5\66\34\2\u013c\u0142\3\2\2\2\u013d")
        buf.write("\u013e\f\4\2\2\u013e\u013f\t\7\2\2\u013f\u0141\5\66\34")
        buf.write("\2\u0140\u013d\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140")
        buf.write("\3\2\2\2\u0142\u0143\3\2\2\2\u0143\65\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0145\u0146\b\34\1\2\u0146\u0147\58\35\2\u0147")
        buf.write("\u014d\3\2\2\2\u0148\u0149\f\4\2\2\u0149\u014a\t\b\2\2")
        buf.write("\u014a\u014c\58\35\2\u014b\u0148\3\2\2\2\u014c\u014f\3")
        buf.write("\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\67")
        buf.write("\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151\7#\2\2\u0151")
        buf.write("\u0154\58\35\2\u0152\u0154\5:\36\2\u0153\u0150\3\2\2\2")
        buf.write("\u0153\u0152\3\2\2\2\u01549\3\2\2\2\u0155\u0156\7\37\2")
        buf.write("\2\u0156\u0159\5:\36\2\u0157\u0159\5<\37\2\u0158\u0155")
        buf.write("\3\2\2\2\u0158\u0157\3\2\2\2\u0159;\3\2\2\2\u015a\u015b")
        buf.write("\b\37\1\2\u015b\u015c\5> \2\u015c\u0161\3\2\2\2\u015d")
        buf.write("\u015e\f\4\2\2\u015e\u0160\5*\26\2\u015f\u015d\3\2\2\2")
        buf.write("\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3")
        buf.write("\2\2\2\u0162=\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165")
        buf.write("\b \1\2\u0165\u0166\5@!\2\u0166\u0175\3\2\2\2\u0167\u0168")
        buf.write("\f\5\2\2\u0168\u0169\7\64\2\2\u0169\u0174\7=\2\2\u016a")
        buf.write("\u016b\f\4\2\2\u016b\u016c\7\64\2\2\u016c\u016d\7=\2\2")
        buf.write("\u016d\u0170\7/\2\2\u016e\u0171\5\30\r\2\u016f\u0171\3")
        buf.write("\2\2\2\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172\u0174\7\60\2\2\u0173\u0167\3\2\2\2\u0173")
        buf.write("\u016a\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176?\3\2\2\2\u0177\u0175\3\2\2")
        buf.write("\2\u0178\u0179\7=\2\2\u0179\u017a\79\2\2\u017a\u0186\7")
        buf.write(">\2\2\u017b\u017c\7=\2\2\u017c\u017d\79\2\2\u017d\u017e")
        buf.write("\7>\2\2\u017e\u0181\7/\2\2\u017f\u0182\5\30\r\2\u0180")
        buf.write("\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0186\7\60\2\2\u0184\u0186")
        buf.write("\5B\"\2\u0185\u0178\3\2\2\2\u0185\u017b\3\2\2\2\u0185")
        buf.write("\u0184\3\2\2\2\u0186A\3\2\2\2\u0187\u0188\7\25\2\2\u0188")
        buf.write("\u0189\7=\2\2\u0189\u018c\7/\2\2\u018a\u018d\5\30\r\2")
        buf.write("\u018b\u018d\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018b\3")
        buf.write("\2\2\2\u018d\u018e\3\2\2\2\u018e\u0191\7\60\2\2\u018f")
        buf.write("\u0191\5D#\2\u0190\u0187\3\2\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("C\3\2\2\2\u0192\u0193\7/\2\2\u0193\u0194\5.\30\2\u0194")
        buf.write("\u0195\7\60\2\2\u0195\u0198\3\2\2\2\u0196\u0198\5F$\2")
        buf.write("\u0197\u0192\3\2\2\2\u0197\u0196\3\2\2\2\u0198E\3\2\2")
        buf.write("\2\u0199\u019e\7\32\2\2\u019a\u019e\7\20\2\2\u019b\u019e")
        buf.write("\5\26\f\2\u019c\u019e\5H%\2\u019d\u0199\3\2\2\2\u019d")
        buf.write("\u019a\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2")
        buf.write("\u019eG\3\2\2\2\u019f\u01a5\7:\2\2\u01a0\u01a5\7;\2\2")
        buf.write("\u01a1\u01a5\5d\63\2\u01a2\u01a5\7<\2\2\u01a3\u01a5\5")
        buf.write("f\64\2\u01a4\u019f\3\2\2\2\u01a4\u01a0\3\2\2\2\u01a4\u01a1")
        buf.write("\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5")
        buf.write("I\3\2\2\2\u01a6\u01a7\5.\30\2\u01a7\u01a8\7\'\2\2\u01a8")
        buf.write("\u01a9\5.\30\2\u01a9\u01aa\7\66\2\2\u01aaK\3\2\2\2\u01ab")
        buf.write("\u01ac\7\7\2\2\u01ac\u01ad\7/\2\2\u01ad\u01ae\5.\30\2")
        buf.write("\u01ae\u01af\7\60\2\2\u01af\u01b2\5$\23\2\u01b0\u01b3")
        buf.write("\5N(\2\u01b1\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1")
        buf.write("\3\2\2\2\u01b3M\3\2\2\2\u01b4\u01b5\5P)\2\u01b5\u01b6")
        buf.write("\5N(\2\u01b6\u01ba\3\2\2\2\u01b7\u01ba\5P)\2\u01b8\u01ba")
        buf.write("\5R*\2\u01b9\u01b4\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01baO\3\2\2\2\u01bb\u01bc\7\b\2\2\u01bc\u01bd")
        buf.write("\7/\2\2\u01bd\u01be\5.\30\2\u01be\u01bf\7\60\2\2\u01bf")
        buf.write("\u01c0\5$\23\2\u01c0Q\3\2\2\2\u01c1\u01c2\7\t\2\2\u01c2")
        buf.write("\u01c3\5$\23\2\u01c3S\3\2\2\2\u01c4\u01c5\7\n\2\2\u01c5")
        buf.write("\u01c6\7/\2\2\u01c6\u01c7\7=\2\2\u01c7\u01c8\7\27\2\2")
        buf.write("\u01c8\u01c9\7:\2\2\u01c9\u01ca\7\33\2\2\u01ca\u01cd\7")
        buf.write(":\2\2\u01cb\u01cc\7\21\2\2\u01cc\u01ce\7:\2\2\u01cd\u01cb")
        buf.write("\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01d0\7\60\2\2\u01d0\u01d1\5$\23\2\u01d1U\3\2\2\2\u01d2")
        buf.write("\u01d3\7\5\2\2\u01d3\u01d4\7\66\2\2\u01d4W\3\2\2\2\u01d5")
        buf.write("\u01d6\7\6\2\2\u01d6\u01d7\7\66\2\2\u01d7Y\3\2\2\2\u01d8")
        buf.write("\u01d9\5,\27\2\u01d9\u01da\7\66\2\2\u01da[\3\2\2\2\u01db")
        buf.write("\u01de\7\26\2\2\u01dc\u01df\5.\30\2\u01dd\u01df\3\2\2")
        buf.write("\2\u01de\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0\u01e1\7\66\2\2\u01e1]\3\2\2\2\u01e2\u01e9")
        buf.write("\7\f\2\2\u01e3\u01e9\7\r\2\2\u01e4\u01e9\7\16\2\2\u01e5")
        buf.write("\u01e9\7\17\2\2\u01e6\u01e9\5b\62\2\u01e7\u01e9\5`\61")
        buf.write("\2\u01e8\u01e2\3\2\2\2\u01e8\u01e3\3\2\2\2\u01e8\u01e4")
        buf.write("\3\2\2\2\u01e8\u01e5\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e7\3\2\2\2\u01e9_\3\2\2\2\u01ea\u01eb\7=\2\2\u01eb")
        buf.write("a\3\2\2\2\u01ec\u01ed\7\13\2\2\u01ed\u01ee\7\61\2\2\u01ee")
        buf.write("\u01ef\5^\60\2\u01ef\u01f0\7\65\2\2\u01f0\u01f1\7:\2\2")
        buf.write("\u01f1\u01f2\7\62\2\2\u01f2c\3\2\2\2\u01f3\u01f4\t\t\2")
        buf.write("\2\u01f4e\3\2\2\2\u01f5\u01f8\5h\65\2\u01f6\u01f8\5t;")
        buf.write("\2\u01f7\u01f5\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8g\3\2")
        buf.write("\2\2\u01f9\u01fa\7\13\2\2\u01fa\u0200\7/\2\2\u01fb\u0201")
        buf.write("\5j\66\2\u01fc\u0201\5l\67\2\u01fd\u0201\5n8\2\u01fe\u0201")
        buf.write("\5p9\2\u01ff\u0201\3\2\2\2\u0200\u01fb\3\2\2\2\u0200\u01fc")
        buf.write("\3\2\2\2\u0200\u01fd\3\2\2\2\u0200\u01fe\3\2\2\2\u0200")
        buf.write("\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0203\7\60\2")
        buf.write("\2\u0203i\3\2\2\2\u0204\u0205\7:\2\2\u0205\u0206\7\65")
        buf.write("\2\2\u0206\u0209\5j\66\2\u0207\u0209\7:\2\2\u0208\u0204")
        buf.write("\3\2\2\2\u0208\u0207\3\2\2\2\u0209k\3\2\2\2\u020a\u020b")
        buf.write("\7;\2\2\u020b\u020c\7\65\2\2\u020c\u020f\5l\67\2\u020d")
        buf.write("\u020f\7;\2\2\u020e\u020a\3\2\2\2\u020e\u020d\3\2\2\2")
        buf.write("\u020fm\3\2\2\2\u0210\u0211\7<\2\2\u0211\u0212\7\65\2")
        buf.write("\2\u0212\u0215\5n8\2\u0213\u0215\7<\2\2\u0214\u0210\3")
        buf.write("\2\2\2\u0214\u0213\3\2\2\2\u0215o\3\2\2\2\u0216\u0217")
        buf.write("\5d\63\2\u0217\u0218\7\65\2\2\u0218\u0219\5p9\2\u0219")
        buf.write("\u021c\3\2\2\2\u021a\u021c\5d\63\2\u021b\u0216\3\2\2\2")
        buf.write("\u021b\u021a\3\2\2\2\u021cq\3\2\2\2\u021d\u021e\5h\65")
        buf.write("\2\u021e\u021f\7\65\2\2\u021f\u0220\5r:\2\u0220\u0223")
        buf.write("\3\2\2\2\u0221\u0223\5h\65\2\u0222\u021d\3\2\2\2\u0222")
        buf.write("\u0221\3\2\2\2\u0223s\3\2\2\2\u0224\u0225\7\13\2\2\u0225")
        buf.write("\u0226\7/\2\2\u0226\u0227\5r:\2\u0227\u0228\7\60\2\2\u0228")
        buf.write("u\3\2\2\2\66}\u0084\u0089\u0091\u0095\u009e\u00a9\u00b1")
        buf.write("\u00b7\u00bd\u00c3\u00c5\u00cd\u00d1\u00dd\u00e4\u00ea")
        buf.write("\u00f7\u0104\u010a\u0115\u011d\u0126\u012d\u0137\u0142")
        buf.write("\u014d\u0153\u0158\u0161\u0170\u0173\u0175\u0181\u0185")
        buf.write("\u018c\u0190\u0197\u019d\u01a4\u01b2\u01b9\u01cd\u01de")
        buf.write("\u01e8\u01f7\u0200\u0208\u020e\u0214\u021b\u0222")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'True'", "'False'", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'", 
                     "'Int'", "'Float'", "'Boolean'", "'String'", "'Null'", 
                     "'By'", "'Class'", "'Val'", "'Var'", "'New'", "'Return'", 
                     "'In'", "'Constructor'", "'Destructor'", "'Self'", 
                     "'..'", "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", 
                     "'!='", "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", 
                     "'('", "')'", "'['", "']'", "':'", "'.'", "','", "';'", 
                     "'{'", "'}'", "'::'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "ARRAY", "INT", 
                      "FLOAT", "BOOLEAN", "STRING", "NULL", "BY", "CLASS", 
                      "VAL", "VAR", "NEW", "RETURN", "IN", "CONSTRUCTOR", 
                      "DESTRUCTOR", "SELF", "DDOTS", "WS", "COMMENT", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", 
                      "SET", "NE", "GT", "GTE", "LT", "LTE", "ED", "AD", 
                      "LP", "RP", "LSB", "RSB", "COLON", "DOT", "COMMA", 
                      "SEMI", "LCB", "RCB", "ACCESS", "INTLIT", "FLOATLIT", 
                      "STRINGLIT", "ID", "Dollar_id", "ERROR_TOKEN", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_class_decl = 2
    RULE_class_bodys = 3
    RULE_class_body = 4
    RULE_variable_decl = 5
    RULE_const_decl = 6
    RULE_typ_name = 7
    RULE_attribute_decl = 8
    RULE_list_name = 9
    RULE_name_att = 10
    RULE_list_exp = 11
    RULE_method_decl = 12
    RULE_parameter = 13
    RULE_identifer_list = 14
    RULE_constructor = 15
    RULE_destructor = 16
    RULE_block_stm = 17
    RULE_statement = 18
    RULE_statements = 19
    RULE_index_operators = 20
    RULE_func_call = 21
    RULE_expr = 22
    RULE_expr1 = 23
    RULE_expr2 = 24
    RULE_expr3 = 25
    RULE_expr4 = 26
    RULE_expr5 = 27
    RULE_expr6 = 28
    RULE_expr7 = 29
    RULE_expr8 = 30
    RULE_expr9 = 31
    RULE_expr10 = 32
    RULE_expr11 = 33
    RULE_operand = 34
    RULE_literal = 35
    RULE_assignment_statement = 36
    RULE_if_statement = 37
    RULE_elseStmt = 38
    RULE_elif_stm = 39
    RULE_else_stm = 40
    RULE_foreach_stmt = 41
    RULE_break_stmt = 42
    RULE_cont_stmt = 43
    RULE_call_stmt = 44
    RULE_return_stmt = 45
    RULE_typ_var = 46
    RULE_class_type = 47
    RULE_array = 48
    RULE_boolit = 49
    RULE_arraylit = 50
    RULE_iar = 51
    RULE_aints = 52
    RULE_afloats = 53
    RULE_astrings = 54
    RULE_asbools = 55
    RULE_marraylists = 56
    RULE_mar = 57

    ruleNames =  [ "program", "decls", "class_decl", "class_bodys", "class_body", 
                   "variable_decl", "const_decl", "typ_name", "attribute_decl", 
                   "list_name", "name_att", "list_exp", "method_decl", "parameter", 
                   "identifer_list", "constructor", "destructor", "block_stm", 
                   "statement", "statements", "index_operators", "func_call", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10", "expr11", 
                   "operand", "literal", "assignment_statement", "if_statement", 
                   "elseStmt", "elif_stm", "else_stm", "foreach_stmt", "break_stmt", 
                   "cont_stmt", "call_stmt", "return_stmt", "typ_var", "class_type", 
                   "array", "boolit", "arraylit", "iar", "aints", "afloats", 
                   "astrings", "asbools", "marraylists", "mar" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    BREAK=3
    CONTINUE=4
    IF=5
    ELSEIF=6
    ELSE=7
    FOREACH=8
    ARRAY=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    STRING=13
    NULL=14
    BY=15
    CLASS=16
    VAL=17
    VAR=18
    NEW=19
    RETURN=20
    IN=21
    CONSTRUCTOR=22
    DESTRUCTOR=23
    SELF=24
    DDOTS=25
    WS=26
    COMMENT=27
    ADD=28
    SUB=29
    MUL=30
    DIV=31
    MOD=32
    NOT=33
    AND=34
    OR=35
    EQ=36
    SET=37
    NE=38
    GT=39
    GTE=40
    LT=41
    LTE=42
    ED=43
    AD=44
    LP=45
    RP=46
    LSB=47
    RSB=48
    COLON=49
    DOT=50
    COMMA=51
    SEMI=52
    LCB=53
    RCB=54
    ACCESS=55
    INTLIT=56
    FLOATLIT=57
    STRINGLIT=58
    ID=59
    Dollar_id=60
    ERROR_TOKEN=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    UNTERMINATED_COMMENT=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(D96Parser.DeclsContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.decls()
            self.state = 117
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl(self):
            return self.getTypedRuleContext(D96Parser.Class_declContext,0)


        def decls(self):
            return self.getTypedRuleContext(D96Parser.DeclsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_decls




    def decls(self):

        localctx = D96Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.class_decl()
                self.state = 120
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.class_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def class_bodys(self):
            return self.getTypedRuleContext(D96Parser.Class_bodysContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_decl




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(D96Parser.CLASS)
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 126
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 127
                self.match(D96Parser.ID)
                self.state = 128
                self.match(D96Parser.COLON)
                self.state = 129
                self.match(D96Parser.ID)
                pass


            self.state = 132
            self.match(D96Parser.LCB)
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 133
                self.class_bodys()
                pass
            elif token in [D96Parser.RCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 137
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodysContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def class_bodys(self):
            return self.getTypedRuleContext(D96Parser.Class_bodysContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_bodys




    def class_bodys(self):

        localctx = D96Parser.Class_bodysContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_bodys)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.class_body()
                self.state = 140
                self.class_bodys()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.class_body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_body)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.attribute_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.method_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def list_name(self):
            return self.getTypedRuleContext(D96Parser.List_nameContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ_var(self):
            return self.getTypedRuleContext(D96Parser.Typ_varContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def SET(self):
            return self.getToken(D96Parser.SET, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_decl




    def variable_decl(self):

        localctx = D96Parser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(D96Parser.VAR)
            self.state = 150
            self.list_name()
            self.state = 151
            self.match(D96Parser.COLON)
            self.state = 152
            self.typ_var()
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SET]:
                self.state = 153
                self.match(D96Parser.SET)
                self.state = 154
                self.list_exp()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 158
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def list_name(self):
            return self.getTypedRuleContext(D96Parser.List_nameContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ_var(self):
            return self.getTypedRuleContext(D96Parser.Typ_varContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def SET(self):
            return self.getToken(D96Parser.SET, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_const_decl




    def const_decl(self):

        localctx = D96Parser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(D96Parser.VAL)
            self.state = 161
            self.list_name()
            self.state = 162
            self.match(D96Parser.COLON)
            self.state = 163
            self.typ_var()
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SET]:
                self.state = 164
                self.match(D96Parser.SET)
                self.state = 165
                self.list_exp()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 169
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typ_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_typ_name




    def typ_name(self):

        localctx = D96Parser.Typ_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typ_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(D96Parser.Variable_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(D96Parser.Const_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_decl




    def attribute_decl(self):

        localctx = D96Parser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_decl)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.variable_decl()
                pass
            elif token in [D96Parser.VAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.const_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_name(self):
            return self.getTypedRuleContext(D96Parser.List_nameContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def Dollar_id(self):
            return self.getToken(D96Parser.Dollar_id, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_list_name




    def list_name(self):

        localctx = D96Parser.List_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_name)
        self._la = 0 # Token type
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 178
                self.match(D96Parser.COMMA)
                self.state = 179
                self.list_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_attContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def Dollar_id(self):
            return self.getToken(D96Parser.Dollar_id, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_name_att




    def name_att(self):

        localctx = D96Parser.Name_attContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_name_att)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_list_exp




    def list_exp(self):

        localctx = D96Parser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_exp)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 185
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 186
                    self.match(D96Parser.NULL)
                    pass


                self.state = 189
                self.match(D96Parser.COMMA)
                self.state = 190
                self.list_exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 191
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 192
                    self.match(D96Parser.NULL)
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def Dollar_id(self):
            return self.getToken(D96Parser.Dollar_id, 0)

        def parameter(self):
            return self.getTypedRuleContext(D96Parser.ParameterContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_decl




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.destructor()
                pass
            elif token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 200
                self.match(D96Parser.LP)
                self.state = 203
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 201
                    self.parameter()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 205
                self.match(D96Parser.RP)
                self.state = 206
                self.block_stm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifer_list(self):
            return self.getTypedRuleContext(D96Parser.Identifer_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ_var(self):
            return self.getTypedRuleContext(D96Parser.Typ_varContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def parameter(self):
            return self.getTypedRuleContext(D96Parser.ParameterContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameter




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.identifer_list()
                self.state = 210
                self.match(D96Parser.COLON)
                self.state = 211
                self.typ_var()
                self.state = 212
                self.match(D96Parser.SEMI)
                self.state = 213
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.identifer_list()
                self.state = 216
                self.match(D96Parser.COLON)
                self.state = 217
                self.typ_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifer_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_att(self):
            return self.getTypedRuleContext(D96Parser.Name_attContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def identifer_list(self):
            return self.getTypedRuleContext(D96Parser.Identifer_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_identifer_list




    def identifer_list(self):

        localctx = D96Parser.Identifer_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_identifer_list)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.name_att()
                self.state = 222
                self.match(D96Parser.COMMA)
                self.state = 223
                self.identifer_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.name_att()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def parameter(self):
            return self.getTypedRuleContext(D96Parser.ParameterContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 229
            self.match(D96Parser.LP)
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 230
                self.parameter()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 234
            self.match(D96Parser.RP)
            self.state = 235
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(D96Parser.DESTRUCTOR)
            self.state = 238
            self.match(D96Parser.LP)
            self.state = 239
            self.match(D96Parser.RP)
            self.state = 240
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stm




    def block_stm(self):

        localctx = D96Parser.Block_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(D96Parser.LCB)
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NULL, D96Parser.VAR, D96Parser.NEW, D96Parser.RETURN, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.LCB, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 243
                self.statements()
                pass
            elif token in [D96Parser.RCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 247
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(D96Parser.Variable_declContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(D96Parser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(D96Parser.If_statementContext,0)


        def foreach_stmt(self):
            return self.getTypedRuleContext(D96Parser.Foreach_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def cont_stmt(self):
            return self.getTypedRuleContext(D96Parser.Cont_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(D96Parser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.foreach_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 253
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 254
                self.cont_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 255
                self.call_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 256
                self.return_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 257
                self.block_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(D96Parser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements




    def statements(self):

        localctx = D96Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statements)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.statement()
                self.state = 261
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operators




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_index_operators)
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(D96Parser.LSB)
                self.state = 267
                self.expr()
                self.state = 268
                self.match(D96Parser.RSB)
                self.state = 269
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(D96Parser.LSB)
                self.state = 272
                self.expr()
                self.state = 273
                self.match(D96Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def name_att(self):
            return self.getTypedRuleContext(D96Parser.Name_attContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def parameter(self):
            return self.getTypedRuleContext(D96Parser.ParameterContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_func_call




    def func_call(self):

        localctx = D96Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.expr()
            self.state = 278
            self.match(D96Parser.DOT)
            self.state = 279
            self.name_att()
            self.state = 280
            self.match(D96Parser.LP)
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 281
                self.parameter()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 285
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def AD(self):
            return self.getToken(D96Parser.AD, 0)

        def ED(self):
            return self.getToken(D96Parser.ED, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.expr1()
                self.state = 288
                _la = self._input.LA(1)
                if not(_la==D96Parser.ED or _la==D96Parser.AD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 289
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def NE(self):
            return self.getToken(D96Parser.NE, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr1




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.expr2(0)
                self.state = 295
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NE) | (1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 296
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 304
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 305
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 306
                    self.expr3(0) 
                self.state = 311
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 315
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 316
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 317
                    self.expr4(0) 
                self.state = 322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 326
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 327
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 328
                    self.expr5() 
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr5)
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(D96Parser.NOT)
                self.state = 335
                self.expr5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr6)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(D96Parser.SUB)
                self.state = 340
                self.expr6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr7



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 347
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 348
                    self.index_operators() 
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr8



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 369
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 357
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 358
                        self.match(D96Parser.DOT)
                        self.state = 359
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 360
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 361
                        self.match(D96Parser.DOT)
                        self.state = 362
                        self.match(D96Parser.ID)
                        self.state = 363
                        self.match(D96Parser.LP)
                        self.state = 366
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                            self.state = 364
                            self.list_exp()
                            pass
                        elif token in [D96Parser.RP]:
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 368
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def ACCESS(self):
            return self.getToken(D96Parser.ACCESS, 0)

        def Dollar_id(self):
            return self.getToken(D96Parser.Dollar_id, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr9)
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(D96Parser.ID)
                self.state = 375
                self.match(D96Parser.ACCESS)
                self.state = 376
                self.match(D96Parser.Dollar_id)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.match(D96Parser.ID)
                self.state = 378
                self.match(D96Parser.ACCESS)
                self.state = 379
                self.match(D96Parser.Dollar_id)
                self.state = 380
                self.match(D96Parser.LP)
                self.state = 383
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 381
                    self.list_exp()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 385
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def expr11(self):
            return self.getTypedRuleContext(D96Parser.Expr11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr10)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(D96Parser.NEW)
                self.state = 390
                self.match(D96Parser.ID)
                self.state = 391
                self.match(D96Parser.LP)
                self.state = 394
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 392
                    self.list_exp()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 396
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr11




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr11)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.match(D96Parser.LP)
                self.state = 401
                self.expr()
                self.state = 402
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def name_att(self):
            return self.getTypedRuleContext(D96Parser.Name_attContext,0)


        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operand




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_operand)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.name_att()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 410
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def boolit(self):
            return self.getTypedRuleContext(D96Parser.BoolitContext,0)


        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(D96Parser.ArraylitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_literal)
        try:
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 415
                self.boolit()
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 416
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 417
                self.arraylit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def SET(self):
            return self.getToken(D96Parser.SET, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignment_statement




    def assignment_statement(self):

        localctx = D96Parser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.expr()
            self.state = 421
            self.match(D96Parser.SET)
            self.state = 422
            self.expr()
            self.state = 423
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def elseStmt(self):
            return self.getTypedRuleContext(D96Parser.ElseStmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statement




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(D96Parser.IF)
            self.state = 426
            self.match(D96Parser.LP)
            self.state = 427
            self.expr()
            self.state = 428
            self.match(D96Parser.RP)
            self.state = 429
            self.block_stm()
            self.state = 432
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF, D96Parser.ELSE]:
                self.state = 430
                self.elseStmt()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NULL, D96Parser.VAR, D96Parser.NEW, D96Parser.RETURN, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.LCB, D96Parser.RCB, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stm(self):
            return self.getTypedRuleContext(D96Parser.Elif_stmContext,0)


        def elseStmt(self):
            return self.getTypedRuleContext(D96Parser.ElseStmtContext,0)


        def else_stm(self):
            return self.getTypedRuleContext(D96Parser.Else_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseStmt




    def elseStmt(self):

        localctx = D96Parser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_elseStmt)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.elif_stm()
                self.state = 435
                self.elseStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.elif_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.else_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elif_stm




    def elif_stm(self):

        localctx = D96Parser.Elif_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_elif_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(D96Parser.ELSEIF)
            self.state = 442
            self.match(D96Parser.LP)
            self.state = 443
            self.expr()
            self.state = 444
            self.match(D96Parser.RP)
            self.state = 445
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stm




    def else_stm(self):

        localctx = D96Parser.Else_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_else_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(D96Parser.ELSE)
            self.state = 448
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foreach_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INTLIT)
            else:
                return self.getToken(D96Parser.INTLIT, i)

        def DDOTS(self):
            return self.getToken(D96Parser.DDOTS, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_foreach_stmt




    def foreach_stmt(self):

        localctx = D96Parser.Foreach_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_foreach_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(D96Parser.FOREACH)
            self.state = 451
            self.match(D96Parser.LP)
            self.state = 452
            self.match(D96Parser.ID)
            self.state = 453
            self.match(D96Parser.IN)
            self.state = 454
            self.match(D96Parser.INTLIT)
            self.state = 455
            self.match(D96Parser.DDOTS)
            self.state = 456
            self.match(D96Parser.INTLIT)
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 457
                self.match(D96Parser.BY)
                self.state = 458
                self.match(D96Parser.INTLIT)


            self.state = 461
            self.match(D96Parser.RP)
            self.state = 462
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.match(D96Parser.BREAK)
            self.state = 465
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cont_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_cont_stmt




    def cont_stmt(self):

        localctx = D96Parser.Cont_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(D96Parser.CONTINUE)
            self.state = 468
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(D96Parser.Func_callContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_call_stmt




    def call_stmt(self):

        localctx = D96Parser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.func_call()
            self.state = 471
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(D96Parser.RETURN)
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 474
                self.expr()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 478
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typ_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(D96Parser.ArrayContext,0)


        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_typ_var




    def typ_var(self):

        localctx = D96Parser.Typ_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_typ_var)
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 482
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 483
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 484
                self.array()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 485
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def typ_var(self):
            return self.getTypedRuleContext(D96Parser.Typ_varContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array




    def array(self):

        localctx = D96Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(D96Parser.ARRAY)
            self.state = 491
            self.match(D96Parser.LSB)
            self.state = 492
            self.typ_var()
            self.state = 493
            self.match(D96Parser.COMMA)
            self.state = 494
            self.match(D96Parser.INTLIT)
            self.state = 495
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_boolit




    def boolit(self):

        localctx = D96Parser.BoolitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            _la = self._input.LA(1)
            if not(_la==D96Parser.TRUE or _la==D96Parser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iar(self):
            return self.getTypedRuleContext(D96Parser.IarContext,0)


        def mar(self):
            return self.getTypedRuleContext(D96Parser.MarContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arraylit




    def arraylit(self):

        localctx = D96Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arraylit)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.iar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.mar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def aints(self):
            return self.getTypedRuleContext(D96Parser.AintsContext,0)


        def afloats(self):
            return self.getTypedRuleContext(D96Parser.AfloatsContext,0)


        def astrings(self):
            return self.getTypedRuleContext(D96Parser.AstringsContext,0)


        def asbools(self):
            return self.getTypedRuleContext(D96Parser.AsboolsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_iar




    def iar(self):

        localctx = D96Parser.IarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_iar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(D96Parser.ARRAY)
            self.state = 504
            self.match(D96Parser.LP)
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.state = 505
                self.aints()
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.state = 506
                self.afloats()
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.state = 507
                self.astrings()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.state = 508
                self.asbools()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 512
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AintsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def aints(self):
            return self.getTypedRuleContext(D96Parser.AintsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_aints




    def aints(self):

        localctx = D96Parser.AintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_aints)
        try:
            self.state = 518
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.match(D96Parser.INTLIT)
                self.state = 515
                self.match(D96Parser.COMMA)
                self.state = 516
                self.aints()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(D96Parser.INTLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AfloatsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def afloats(self):
            return self.getTypedRuleContext(D96Parser.AfloatsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_afloats




    def afloats(self):

        localctx = D96Parser.AfloatsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_afloats)
        try:
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.match(D96Parser.FLOATLIT)
                self.state = 521
                self.match(D96Parser.COMMA)
                self.state = 522
                self.afloats()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 523
                self.match(D96Parser.FLOATLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AstringsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def astrings(self):
            return self.getTypedRuleContext(D96Parser.AstringsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_astrings




    def astrings(self):

        localctx = D96Parser.AstringsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_astrings)
        try:
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.match(D96Parser.STRINGLIT)
                self.state = 527
                self.match(D96Parser.COMMA)
                self.state = 528
                self.astrings()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                self.match(D96Parser.STRINGLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsboolsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolit(self):
            return self.getTypedRuleContext(D96Parser.BoolitContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def asbools(self):
            return self.getTypedRuleContext(D96Parser.AsboolsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_asbools




    def asbools(self):

        localctx = D96Parser.AsboolsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_asbools)
        try:
            self.state = 537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.boolit()
                self.state = 533
                self.match(D96Parser.COMMA)
                self.state = 534
                self.asbools()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.boolit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MarraylistsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iar(self):
            return self.getTypedRuleContext(D96Parser.IarContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def marraylists(self):
            return self.getTypedRuleContext(D96Parser.MarraylistsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_marraylists




    def marraylists(self):

        localctx = D96Parser.MarraylistsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_marraylists)
        try:
            self.state = 544
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.iar()
                self.state = 540
                self.match(D96Parser.COMMA)
                self.state = 541
                self.marraylists()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 543
                self.iar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def marraylists(self):
            return self.getTypedRuleContext(D96Parser.MarraylistsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mar




    def mar(self):

        localctx = D96Parser.MarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_mar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.match(D96Parser.ARRAY)
            self.state = 547
            self.match(D96Parser.LP)
            self.state = 548
            self.marraylists()
            self.state = 549
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.expr2_sempred
        self._predicates[25] = self.expr3_sempred
        self._predicates[26] = self.expr4_sempred
        self._predicates[29] = self.expr7_sempred
        self._predicates[30] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




