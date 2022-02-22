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
        buf.write("\u0226\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\5\3|\n\3\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u0083\n\4\3\4\3\4\3\4\5\4\u0088\n\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\5\5\u0090\n\5\3\6\3\6\5\6\u0094\n\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7\u009d\n\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\5\b\u00a8\n\b\3\b\3\b\3\t\3\t\3\n\3\n\5")
        buf.write("\n\u00b0\n\n\3\13\3\13\3\13\3\13\5\13\u00b6\n\13\3\f\3")
        buf.write("\f\3\r\3\r\5\r\u00bc\n\r\3\r\3\r\3\r\3\r\5\r\u00c2\n\r")
        buf.write("\5\r\u00c4\n\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00cc")
        buf.write("\n\16\3\16\3\16\5\16\u00d0\n\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\5\17\u00dc\n\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00e3\n\20\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u00e9\n\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\5\23\u00f6\n\23\3\23\3\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0103\n\24\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u0109\n\25\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\5\26\u0114\n\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\5\27\u011c\n\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\5\30\u0125\n\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u012c\n\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0134")
        buf.write("\n\32\f\32\16\32\u0137\13\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\7\33\u013f\n\33\f\33\16\33\u0142\13\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\7\34\u014a\n\34\f\34\16\34\u014d")
        buf.write("\13\34\3\35\3\35\3\35\5\35\u0152\n\35\3\36\3\36\3\36\5")
        buf.write("\36\u0157\n\36\3\37\3\37\3\37\3\37\3\37\7\37\u015e\n\37")
        buf.write("\f\37\16\37\u0161\13\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \5 \u016f\n \3 \7 \u0172\n \f \16 \u0175\13 \3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0180\n!\3!\3!\5!\u0184\n")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\5\"\u018b\n\"\3\"\3\"\5\"\u018f")
        buf.write("\n\"\3#\3#\3#\3#\3#\5#\u0196\n#\3$\3$\3$\3$\5$\u019c\n")
        buf.write("$\3%\3%\3%\3%\3%\5%\u01a3\n%\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\5\'\u01b1\n\'\3(\3(\3(\3(\3(\5(\u01b8")
        buf.write("\n(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\5+\u01cc\n+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3/\5/\u01dd\n/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u01e7\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\5\63\u01f4\n\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\5\64\u01fd\n\64\3\64\3\64\3\65\3\65\3")
        buf.write("\65\3\65\5\65\u0205\n\65\3\66\3\66\3\66\3\66\5\66\u020b")
        buf.write("\n\66\3\67\3\67\3\67\3\67\5\67\u0211\n\67\38\38\38\38")
        buf.write("\38\58\u0218\n8\39\39\39\39\39\59\u021f\n9\3:\3:\3:\3")
        buf.write(":\3:\3:\2\7\62\64\66<>;\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnpr\2\n\3\2\23\24\3\2=>\3\2-.\4\2&&(,\3\2$%\3\2\36")
        buf.write("\37\3\2 \"\3\2\3\4\2\u0236\2t\3\2\2\2\4{\3\2\2\2\6}\3")
        buf.write("\2\2\2\b\u008f\3\2\2\2\n\u0093\3\2\2\2\f\u0095\3\2\2\2")
        buf.write("\16\u00a0\3\2\2\2\20\u00ab\3\2\2\2\22\u00af\3\2\2\2\24")
        buf.write("\u00b5\3\2\2\2\26\u00b7\3\2\2\2\30\u00c3\3\2\2\2\32\u00cf")
        buf.write("\3\2\2\2\34\u00db\3\2\2\2\36\u00e2\3\2\2\2 \u00e4\3\2")
        buf.write("\2\2\"\u00ed\3\2\2\2$\u00f2\3\2\2\2&\u0102\3\2\2\2(\u0108")
        buf.write("\3\2\2\2*\u0113\3\2\2\2,\u0115\3\2\2\2.\u0124\3\2\2\2")
        buf.write("\60\u012b\3\2\2\2\62\u012d\3\2\2\2\64\u0138\3\2\2\2\66")
        buf.write("\u0143\3\2\2\28\u0151\3\2\2\2:\u0156\3\2\2\2<\u0158\3")
        buf.write("\2\2\2>\u0162\3\2\2\2@\u0183\3\2\2\2B\u018e\3\2\2\2D\u0195")
        buf.write("\3\2\2\2F\u019b\3\2\2\2H\u01a2\3\2\2\2J\u01a4\3\2\2\2")
        buf.write("L\u01a9\3\2\2\2N\u01b7\3\2\2\2P\u01b9\3\2\2\2R\u01bf\3")
        buf.write("\2\2\2T\u01c2\3\2\2\2V\u01d0\3\2\2\2X\u01d3\3\2\2\2Z\u01d6")
        buf.write("\3\2\2\2\\\u01d9\3\2\2\2^\u01e6\3\2\2\2`\u01e8\3\2\2\2")
        buf.write("b\u01ef\3\2\2\2d\u01f3\3\2\2\2f\u01f5\3\2\2\2h\u0204\3")
        buf.write("\2\2\2j\u020a\3\2\2\2l\u0210\3\2\2\2n\u0217\3\2\2\2p\u021e")
        buf.write("\3\2\2\2r\u0220\3\2\2\2tu\5\4\3\2uv\7\2\2\3v\3\3\2\2\2")
        buf.write("wx\5\6\4\2xy\5\4\3\2y|\3\2\2\2z|\5\6\4\2{w\3\2\2\2{z\3")
        buf.write("\2\2\2|\5\3\2\2\2}\u0082\7\22\2\2~\u0083\7=\2\2\177\u0080")
        buf.write("\7=\2\2\u0080\u0081\7\63\2\2\u0081\u0083\7=\2\2\u0082")
        buf.write("~\3\2\2\2\u0082\177\3\2\2\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\u0087\7\67\2\2\u0085\u0088\5\b\5\2\u0086\u0088\3\2\2")
        buf.write("\2\u0087\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\u008a\78\2\2\u008a\7\3\2\2\2\u008b\u008c")
        buf.write("\5\n\6\2\u008c\u008d\5\b\5\2\u008d\u0090\3\2\2\2\u008e")
        buf.write("\u0090\5\n\6\2\u008f\u008b\3\2\2\2\u008f\u008e\3\2\2\2")
        buf.write("\u0090\t\3\2\2\2\u0091\u0094\5\22\n\2\u0092\u0094\5\32")
        buf.write("\16\2\u0093\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094\13")
        buf.write("\3\2\2\2\u0095\u0096\7\24\2\2\u0096\u0097\5\24\13\2\u0097")
        buf.write("\u0098\7\63\2\2\u0098\u009c\5^\60\2\u0099\u009a\7\'\2")
        buf.write("\2\u009a\u009d\5\30\r\2\u009b\u009d\3\2\2\2\u009c\u0099")
        buf.write("\3\2\2\2\u009c\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u009f\7\66\2\2\u009f\r\3\2\2\2\u00a0\u00a1\7\23\2\2\u00a1")
        buf.write("\u00a2\5\24\13\2\u00a2\u00a3\7\63\2\2\u00a3\u00a7\5^\60")
        buf.write("\2\u00a4\u00a5\7\'\2\2\u00a5\u00a8\5\30\r\2\u00a6\u00a8")
        buf.write("\3\2\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00aa\7\66\2\2\u00aa\17\3\2\2\2\u00ab")
        buf.write("\u00ac\t\2\2\2\u00ac\21\3\2\2\2\u00ad\u00b0\5\f\7\2\u00ae")
        buf.write("\u00b0\5\16\b\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2")
        buf.write("\2\u00b0\23\3\2\2\2\u00b1\u00b2\t\3\2\2\u00b2\u00b3\7")
        buf.write("\65\2\2\u00b3\u00b6\5\24\13\2\u00b4\u00b6\t\3\2\2\u00b5")
        buf.write("\u00b1\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\25\3\2\2\2\u00b7")
        buf.write("\u00b8\t\3\2\2\u00b8\27\3\2\2\2\u00b9\u00bc\5.\30\2\u00ba")
        buf.write("\u00bc\7\20\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2")
        buf.write("\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\7\65\2\2\u00be\u00c4")
        buf.write("\5\30\r\2\u00bf\u00c2\5.\30\2\u00c0\u00c2\7\20\2\2\u00c1")
        buf.write("\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c4\3\2\2\2")
        buf.write("\u00c3\u00bb\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\31\3\2")
        buf.write("\2\2\u00c5\u00d0\5 \21\2\u00c6\u00d0\5\"\22\2\u00c7\u00c8")
        buf.write("\t\3\2\2\u00c8\u00cb\7/\2\2\u00c9\u00cc\5\34\17\2\u00ca")
        buf.write("\u00cc\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2")
        buf.write("\u00cc\u00cd\3\2\2\2\u00cd\u00ce\7\60\2\2\u00ce\u00d0")
        buf.write("\5$\23\2\u00cf\u00c5\3\2\2\2\u00cf\u00c6\3\2\2\2\u00cf")
        buf.write("\u00c7\3\2\2\2\u00d0\33\3\2\2\2\u00d1\u00d2\5\36\20\2")
        buf.write("\u00d2\u00d3\7\63\2\2\u00d3\u00d4\5^\60\2\u00d4\u00d5")
        buf.write("\7\66\2\2\u00d5\u00d6\5\34\17\2\u00d6\u00dc\3\2\2\2\u00d7")
        buf.write("\u00d8\5\36\20\2\u00d8\u00d9\7\63\2\2\u00d9\u00da\5^\60")
        buf.write("\2\u00da\u00dc\3\2\2\2\u00db\u00d1\3\2\2\2\u00db\u00d7")
        buf.write("\3\2\2\2\u00dc\35\3\2\2\2\u00dd\u00de\5\26\f\2\u00de\u00df")
        buf.write("\7\65\2\2\u00df\u00e0\5\36\20\2\u00e0\u00e3\3\2\2\2\u00e1")
        buf.write("\u00e3\5\26\f\2\u00e2\u00dd\3\2\2\2\u00e2\u00e1\3\2\2")
        buf.write("\2\u00e3\37\3\2\2\2\u00e4\u00e5\7\30\2\2\u00e5\u00e8\7")
        buf.write("/\2\2\u00e6\u00e9\5\34\17\2\u00e7\u00e9\3\2\2\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\u00eb\7\60\2\2\u00eb\u00ec\5$\23\2\u00ec!\3\2\2")
        buf.write("\2\u00ed\u00ee\7\31\2\2\u00ee\u00ef\7/\2\2\u00ef\u00f0")
        buf.write("\7\60\2\2\u00f0\u00f1\5$\23\2\u00f1#\3\2\2\2\u00f2\u00f5")
        buf.write("\7\67\2\2\u00f3\u00f6\5(\25\2\u00f4\u00f6\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f7\u00f8\78\2\2\u00f8%\3\2\2\2\u00f9\u0103\5\f\7\2")
        buf.write("\u00fa\u0103\5J&\2\u00fb\u0103\5L\'\2\u00fc\u0103\5T+")
        buf.write("\2\u00fd\u0103\5V,\2\u00fe\u0103\5X-\2\u00ff\u0103\5Z")
        buf.write(".\2\u0100\u0103\5\\/\2\u0101\u0103\5$\23\2\u0102\u00f9")
        buf.write("\3\2\2\2\u0102\u00fa\3\2\2\2\u0102\u00fb\3\2\2\2\u0102")
        buf.write("\u00fc\3\2\2\2\u0102\u00fd\3\2\2\2\u0102\u00fe\3\2\2\2")
        buf.write("\u0102\u00ff\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0101\3")
        buf.write("\2\2\2\u0103\'\3\2\2\2\u0104\u0105\5&\24\2\u0105\u0106")
        buf.write("\5(\25\2\u0106\u0109\3\2\2\2\u0107\u0109\5&\24\2\u0108")
        buf.write("\u0104\3\2\2\2\u0108\u0107\3\2\2\2\u0109)\3\2\2\2\u010a")
        buf.write("\u010b\7\61\2\2\u010b\u010c\5.\30\2\u010c\u010d\7\62\2")
        buf.write("\2\u010d\u010e\5*\26\2\u010e\u0114\3\2\2\2\u010f\u0110")
        buf.write("\7\61\2\2\u0110\u0111\5.\30\2\u0111\u0112\7\62\2\2\u0112")
        buf.write("\u0114\3\2\2\2\u0113\u010a\3\2\2\2\u0113\u010f\3\2\2\2")
        buf.write("\u0114+\3\2\2\2\u0115\u0116\5.\30\2\u0116\u0117\7\64\2")
        buf.write("\2\u0117\u0118\5\26\f\2\u0118\u011b\7/\2\2\u0119\u011c")
        buf.write("\5\34\17\2\u011a\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011b")
        buf.write("\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e\7\60\2")
        buf.write("\2\u011e-\3\2\2\2\u011f\u0120\5\60\31\2\u0120\u0121\t")
        buf.write("\4\2\2\u0121\u0122\5\60\31\2\u0122\u0125\3\2\2\2\u0123")
        buf.write("\u0125\5\60\31\2\u0124\u011f\3\2\2\2\u0124\u0123\3\2\2")
        buf.write("\2\u0125/\3\2\2\2\u0126\u0127\5\62\32\2\u0127\u0128\t")
        buf.write("\5\2\2\u0128\u0129\5\62\32\2\u0129\u012c\3\2\2\2\u012a")
        buf.write("\u012c\5\62\32\2\u012b\u0126\3\2\2\2\u012b\u012a\3\2\2")
        buf.write("\2\u012c\61\3\2\2\2\u012d\u012e\b\32\1\2\u012e\u012f\5")
        buf.write("\64\33\2\u012f\u0135\3\2\2\2\u0130\u0131\f\4\2\2\u0131")
        buf.write("\u0132\t\6\2\2\u0132\u0134\5\64\33\2\u0133\u0130\3\2\2")
        buf.write("\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\63\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0139")
        buf.write("\b\33\1\2\u0139\u013a\5\66\34\2\u013a\u0140\3\2\2\2\u013b")
        buf.write("\u013c\f\4\2\2\u013c\u013d\t\7\2\2\u013d\u013f\5\66\34")
        buf.write("\2\u013e\u013b\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\65\3\2\2\2\u0142\u0140")
        buf.write("\3\2\2\2\u0143\u0144\b\34\1\2\u0144\u0145\58\35\2\u0145")
        buf.write("\u014b\3\2\2\2\u0146\u0147\f\4\2\2\u0147\u0148\t\b\2\2")
        buf.write("\u0148\u014a\58\35\2\u0149\u0146\3\2\2\2\u014a\u014d\3")
        buf.write("\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\67")
        buf.write("\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\7#\2\2\u014f")
        buf.write("\u0152\58\35\2\u0150\u0152\5:\36\2\u0151\u014e\3\2\2\2")
        buf.write("\u0151\u0150\3\2\2\2\u01529\3\2\2\2\u0153\u0154\7\37\2")
        buf.write("\2\u0154\u0157\5:\36\2\u0155\u0157\5<\37\2\u0156\u0153")
        buf.write("\3\2\2\2\u0156\u0155\3\2\2\2\u0157;\3\2\2\2\u0158\u0159")
        buf.write("\b\37\1\2\u0159\u015a\5> \2\u015a\u015f\3\2\2\2\u015b")
        buf.write("\u015c\f\4\2\2\u015c\u015e\5*\26\2\u015d\u015b\3\2\2\2")
        buf.write("\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3")
        buf.write("\2\2\2\u0160=\3\2\2\2\u0161\u015f\3\2\2\2\u0162\u0163")
        buf.write("\b \1\2\u0163\u0164\5@!\2\u0164\u0173\3\2\2\2\u0165\u0166")
        buf.write("\f\5\2\2\u0166\u0167\7\64\2\2\u0167\u0172\7=\2\2\u0168")
        buf.write("\u0169\f\4\2\2\u0169\u016a\7\64\2\2\u016a\u016b\7=\2\2")
        buf.write("\u016b\u016e\7/\2\2\u016c\u016f\5\30\r\2\u016d\u016f\3")
        buf.write("\2\2\2\u016e\u016c\3\2\2\2\u016e\u016d\3\2\2\2\u016f\u0170")
        buf.write("\3\2\2\2\u0170\u0172\7\60\2\2\u0171\u0165\3\2\2\2\u0171")
        buf.write("\u0168\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174?\3\2\2\2\u0175\u0173\3\2\2")
        buf.write("\2\u0176\u0177\7=\2\2\u0177\u0178\79\2\2\u0178\u0184\7")
        buf.write(">\2\2\u0179\u017a\7=\2\2\u017a\u017b\79\2\2\u017b\u017c")
        buf.write("\7>\2\2\u017c\u017f\7/\2\2\u017d\u0180\5\30\r\2\u017e")
        buf.write("\u0180\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181\u0184\7\60\2\2\u0182\u0184")
        buf.write("\5B\"\2\u0183\u0176\3\2\2\2\u0183\u0179\3\2\2\2\u0183")
        buf.write("\u0182\3\2\2\2\u0184A\3\2\2\2\u0185\u0186\7\25\2\2\u0186")
        buf.write("\u0187\7=\2\2\u0187\u018a\7/\2\2\u0188\u018b\5\30\r\2")
        buf.write("\u0189\u018b\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u0189\3")
        buf.write("\2\2\2\u018b\u018c\3\2\2\2\u018c\u018f\7\60\2\2\u018d")
        buf.write("\u018f\5D#\2\u018e\u0185\3\2\2\2\u018e\u018d\3\2\2\2\u018f")
        buf.write("C\3\2\2\2\u0190\u0191\7/\2\2\u0191\u0192\5.\30\2\u0192")
        buf.write("\u0193\7\60\2\2\u0193\u0196\3\2\2\2\u0194\u0196\5F$\2")
        buf.write("\u0195\u0190\3\2\2\2\u0195\u0194\3\2\2\2\u0196E\3\2\2")
        buf.write("\2\u0197\u019c\7\32\2\2\u0198\u019c\7\20\2\2\u0199\u019c")
        buf.write("\5\26\f\2\u019a\u019c\5H%\2\u019b\u0197\3\2\2\2\u019b")
        buf.write("\u0198\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019a\3\2\2\2")
        buf.write("\u019cG\3\2\2\2\u019d\u01a3\7:\2\2\u019e\u01a3\7;\2\2")
        buf.write("\u019f\u01a3\5b\62\2\u01a0\u01a3\7<\2\2\u01a1\u01a3\5")
        buf.write("d\63\2\u01a2\u019d\3\2\2\2\u01a2\u019e\3\2\2\2\u01a2\u019f")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3")
        buf.write("I\3\2\2\2\u01a4\u01a5\5.\30\2\u01a5\u01a6\7\'\2\2\u01a6")
        buf.write("\u01a7\5.\30\2\u01a7\u01a8\7\66\2\2\u01a8K\3\2\2\2\u01a9")
        buf.write("\u01aa\7\7\2\2\u01aa\u01ab\7/\2\2\u01ab\u01ac\5.\30\2")
        buf.write("\u01ac\u01ad\7\60\2\2\u01ad\u01b0\5$\23\2\u01ae\u01b1")
        buf.write("\5N(\2\u01af\u01b1\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1M\3\2\2\2\u01b2\u01b3\5P)\2\u01b3\u01b4")
        buf.write("\5N(\2\u01b4\u01b8\3\2\2\2\u01b5\u01b8\5P)\2\u01b6\u01b8")
        buf.write("\5R*\2\u01b7\u01b2\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6")
        buf.write("\3\2\2\2\u01b8O\3\2\2\2\u01b9\u01ba\7\b\2\2\u01ba\u01bb")
        buf.write("\7/\2\2\u01bb\u01bc\5.\30\2\u01bc\u01bd\7\60\2\2\u01bd")
        buf.write("\u01be\5$\23\2\u01beQ\3\2\2\2\u01bf\u01c0\7\t\2\2\u01c0")
        buf.write("\u01c1\5$\23\2\u01c1S\3\2\2\2\u01c2\u01c3\7\n\2\2\u01c3")
        buf.write("\u01c4\7/\2\2\u01c4\u01c5\7=\2\2\u01c5\u01c6\7\27\2\2")
        buf.write("\u01c6\u01c7\7:\2\2\u01c7\u01c8\7\33\2\2\u01c8\u01cb\7")
        buf.write(":\2\2\u01c9\u01ca\7\21\2\2\u01ca\u01cc\7:\2\2\u01cb\u01c9")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd")
        buf.write("\u01ce\7\60\2\2\u01ce\u01cf\5$\23\2\u01cfU\3\2\2\2\u01d0")
        buf.write("\u01d1\7\5\2\2\u01d1\u01d2\7\66\2\2\u01d2W\3\2\2\2\u01d3")
        buf.write("\u01d4\7\6\2\2\u01d4\u01d5\7\66\2\2\u01d5Y\3\2\2\2\u01d6")
        buf.write("\u01d7\5,\27\2\u01d7\u01d8\7\66\2\2\u01d8[\3\2\2\2\u01d9")
        buf.write("\u01dc\7\26\2\2\u01da\u01dd\5.\30\2\u01db\u01dd\3\2\2")
        buf.write("\2\u01dc\u01da\3\2\2\2\u01dc\u01db\3\2\2\2\u01dd\u01de")
        buf.write("\3\2\2\2\u01de\u01df\7\66\2\2\u01df]\3\2\2\2\u01e0\u01e7")
        buf.write("\7\f\2\2\u01e1\u01e7\7\r\2\2\u01e2\u01e7\7\16\2\2\u01e3")
        buf.write("\u01e7\7\17\2\2\u01e4\u01e7\5`\61\2\u01e5\u01e7\7=\2\2")
        buf.write("\u01e6\u01e0\3\2\2\2\u01e6\u01e1\3\2\2\2\u01e6\u01e2\3")
        buf.write("\2\2\2\u01e6\u01e3\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5")
        buf.write("\3\2\2\2\u01e7_\3\2\2\2\u01e8\u01e9\7\13\2\2\u01e9\u01ea")
        buf.write("\7\61\2\2\u01ea\u01eb\5^\60\2\u01eb\u01ec\7\65\2\2\u01ec")
        buf.write("\u01ed\7:\2\2\u01ed\u01ee\7\62\2\2\u01eea\3\2\2\2\u01ef")
        buf.write("\u01f0\t\t\2\2\u01f0c\3\2\2\2\u01f1\u01f4\5f\64\2\u01f2")
        buf.write("\u01f4\5r:\2\u01f3\u01f1\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4")
        buf.write("e\3\2\2\2\u01f5\u01f6\7\13\2\2\u01f6\u01fc\7/\2\2\u01f7")
        buf.write("\u01fd\5h\65\2\u01f8\u01fd\5j\66\2\u01f9\u01fd\5l\67\2")
        buf.write("\u01fa\u01fd\5n8\2\u01fb\u01fd\3\2\2\2\u01fc\u01f7\3\2")
        buf.write("\2\2\u01fc\u01f8\3\2\2\2\u01fc\u01f9\3\2\2\2\u01fc\u01fa")
        buf.write("\3\2\2\2\u01fc\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("\u01ff\7\60\2\2\u01ffg\3\2\2\2\u0200\u0201\7:\2\2\u0201")
        buf.write("\u0202\7\65\2\2\u0202\u0205\5h\65\2\u0203\u0205\7:\2\2")
        buf.write("\u0204\u0200\3\2\2\2\u0204\u0203\3\2\2\2\u0205i\3\2\2")
        buf.write("\2\u0206\u0207\7;\2\2\u0207\u0208\7\65\2\2\u0208\u020b")
        buf.write("\5j\66\2\u0209\u020b\7;\2\2\u020a\u0206\3\2\2\2\u020a")
        buf.write("\u0209\3\2\2\2\u020bk\3\2\2\2\u020c\u020d\7<\2\2\u020d")
        buf.write("\u020e\7\65\2\2\u020e\u0211\5l\67\2\u020f\u0211\7<\2\2")
        buf.write("\u0210\u020c\3\2\2\2\u0210\u020f\3\2\2\2\u0211m\3\2\2")
        buf.write("\2\u0212\u0213\5b\62\2\u0213\u0214\7\65\2\2\u0214\u0215")
        buf.write("\5n8\2\u0215\u0218\3\2\2\2\u0216\u0218\5b\62\2\u0217\u0212")
        buf.write("\3\2\2\2\u0217\u0216\3\2\2\2\u0218o\3\2\2\2\u0219\u021a")
        buf.write("\5f\64\2\u021a\u021b\7\65\2\2\u021b\u021c\5p9\2\u021c")
        buf.write("\u021f\3\2\2\2\u021d\u021f\5f\64\2\u021e\u0219\3\2\2\2")
        buf.write("\u021e\u021d\3\2\2\2\u021fq\3\2\2\2\u0220\u0221\7\13\2")
        buf.write("\2\u0221\u0222\7/\2\2\u0222\u0223\5p9\2\u0223\u0224\7")
        buf.write("\60\2\2\u0224s\3\2\2\2\66{\u0082\u0087\u008f\u0093\u009c")
        buf.write("\u00a7\u00af\u00b5\u00bb\u00c1\u00c3\u00cb\u00cf\u00db")
        buf.write("\u00e2\u00e8\u00f5\u0102\u0108\u0113\u011b\u0124\u012b")
        buf.write("\u0135\u0140\u014b\u0151\u0156\u015f\u016e\u0171\u0173")
        buf.write("\u017f\u0183\u018a\u018e\u0195\u019b\u01a2\u01b0\u01b7")
        buf.write("\u01cb\u01dc\u01e6\u01f3\u01fc\u0204\u020a\u0210\u0217")
        buf.write("\u021e")
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
    RULE_array = 47
    RULE_boolit = 48
    RULE_arraylit = 49
    RULE_iar = 50
    RULE_aints = 51
    RULE_afloats = 52
    RULE_astrings = 53
    RULE_asbools = 54
    RULE_marraylists = 55
    RULE_mar = 56

    ruleNames =  [ "program", "decls", "class_decl", "class_bodys", "class_body", 
                   "variable_decl", "const_decl", "typ_name", "attribute_decl", 
                   "list_name", "name_att", "list_exp", "method_decl", "parameter", 
                   "identifer_list", "constructor", "destructor", "block_stm", 
                   "statement", "statements", "index_operators", "func_call", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10", "expr11", 
                   "operand", "literal", "assignment_statement", "if_statement", 
                   "elseStmt", "elif_stm", "else_stm", "foreach_stmt", "break_stmt", 
                   "cont_stmt", "call_stmt", "return_stmt", "typ_var", "array", 
                   "boolit", "arraylit", "iar", "aints", "afloats", "astrings", 
                   "asbools", "marraylists", "mar" ]

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
            self.state = 114
            self.decls()
            self.state = 115
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
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.class_decl()
                self.state = 118
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
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
            self.state = 123
            self.match(D96Parser.CLASS)
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 124
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 125
                self.match(D96Parser.ID)
                self.state = 126
                self.match(D96Parser.COLON)
                self.state = 127
                self.match(D96Parser.ID)
                pass


            self.state = 130
            self.match(D96Parser.LCB)
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 131
                self.class_bodys()
                pass
            elif token in [D96Parser.RCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 135
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.class_body()
                self.state = 138
                self.class_bodys()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
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
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.attribute_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
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
            self.state = 147
            self.match(D96Parser.VAR)
            self.state = 148
            self.list_name()
            self.state = 149
            self.match(D96Parser.COLON)
            self.state = 150
            self.typ_var()
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SET]:
                self.state = 151
                self.match(D96Parser.SET)
                self.state = 152
                self.list_exp()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 156
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
            self.state = 158
            self.match(D96Parser.VAL)
            self.state = 159
            self.list_name()
            self.state = 160
            self.match(D96Parser.COLON)
            self.state = 161
            self.typ_var()
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SET]:
                self.state = 162
                self.match(D96Parser.SET)
                self.state = 163
                self.list_exp()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 167
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
            self.state = 169
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
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.variable_decl()
                pass
            elif token in [D96Parser.VAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
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
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self.match(D96Parser.COMMA)
                self.state = 177
                self.list_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
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
            self.state = 181
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
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 183
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 184
                    self.match(D96Parser.NULL)
                    pass


                self.state = 187
                self.match(D96Parser.COMMA)
                self.state = 188
                self.list_exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 189
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 190
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
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.destructor()
                pass
            elif token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 198
                self.match(D96Parser.LP)
                self.state = 201
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 199
                    self.parameter()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 203
                self.match(D96Parser.RP)
                self.state = 204
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
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.identifer_list()
                self.state = 208
                self.match(D96Parser.COLON)
                self.state = 209
                self.typ_var()
                self.state = 210
                self.match(D96Parser.SEMI)
                self.state = 211
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.identifer_list()
                self.state = 214
                self.match(D96Parser.COLON)
                self.state = 215
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
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.name_att()
                self.state = 220
                self.match(D96Parser.COMMA)
                self.state = 221
                self.identifer_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
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
            self.state = 226
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 227
            self.match(D96Parser.LP)
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 228
                self.parameter()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 232
            self.match(D96Parser.RP)
            self.state = 233
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
            self.state = 235
            self.match(D96Parser.DESTRUCTOR)
            self.state = 236
            self.match(D96Parser.LP)
            self.state = 237
            self.match(D96Parser.RP)
            self.state = 238
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
            self.state = 240
            self.match(D96Parser.LCB)
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NULL, D96Parser.VAR, D96Parser.NEW, D96Parser.RETURN, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.LCB, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 241
                self.statements()
                pass
            elif token in [D96Parser.RCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 245
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
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 250
                self.foreach_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 251
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 252
                self.cont_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 253
                self.call_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 254
                self.return_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 255
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
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.statement()
                self.state = 259
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
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
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(D96Parser.LSB)
                self.state = 265
                self.expr()
                self.state = 266
                self.match(D96Parser.RSB)
                self.state = 267
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(D96Parser.LSB)
                self.state = 270
                self.expr()
                self.state = 271
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
            self.state = 275
            self.expr()
            self.state = 276
            self.match(D96Parser.DOT)
            self.state = 277
            self.name_att()
            self.state = 278
            self.match(D96Parser.LP)
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 279
                self.parameter()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 283
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
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.expr1()
                self.state = 286
                _la = self._input.LA(1)
                if not(_la==D96Parser.ED or _la==D96Parser.AD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 287
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
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
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.expr2(0)
                self.state = 293
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NE) | (1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 294
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
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
            self.state = 300
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 302
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 303
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 304
                    self.expr3(0) 
                self.state = 309
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
            self.state = 311
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 313
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 314
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 315
                    self.expr4(0) 
                self.state = 320
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
            self.state = 322
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 324
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 325
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 326
                    self.expr5() 
                self.state = 331
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
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(D96Parser.NOT)
                self.state = 333
                self.expr5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
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
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(D96Parser.SUB)
                self.state = 338
                self.expr6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
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
            self.state = 343
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 345
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 346
                    self.index_operators() 
                self.state = 351
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
            self.state = 353
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 369
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 367
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 355
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 356
                        self.match(D96Parser.DOT)
                        self.state = 357
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 358
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 359
                        self.match(D96Parser.DOT)
                        self.state = 360
                        self.match(D96Parser.ID)
                        self.state = 361
                        self.match(D96Parser.LP)
                        self.state = 364
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                            self.state = 362
                            self.list_exp()
                            pass
                        elif token in [D96Parser.RP]:
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 366
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 371
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
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(D96Parser.ID)
                self.state = 373
                self.match(D96Parser.ACCESS)
                self.state = 374
                self.match(D96Parser.Dollar_id)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.match(D96Parser.ID)
                self.state = 376
                self.match(D96Parser.ACCESS)
                self.state = 377
                self.match(D96Parser.Dollar_id)
                self.state = 378
                self.match(D96Parser.LP)
                self.state = 381
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 379
                    self.list_exp()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 383
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
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
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(D96Parser.NEW)
                self.state = 388
                self.match(D96Parser.ID)
                self.state = 389
                self.match(D96Parser.LP)
                self.state = 392
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 390
                    self.list_exp()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 394
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
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
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(D96Parser.LP)
                self.state = 399
                self.expr()
                self.state = 400
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
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
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 3)
                self.state = 407
                self.name_att()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 408
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
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 413
                self.boolit()
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 414
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 415
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
            self.state = 418
            self.expr()
            self.state = 419
            self.match(D96Parser.SET)
            self.state = 420
            self.expr()
            self.state = 421
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
            self.state = 423
            self.match(D96Parser.IF)
            self.state = 424
            self.match(D96Parser.LP)
            self.state = 425
            self.expr()
            self.state = 426
            self.match(D96Parser.RP)
            self.state = 427
            self.block_stm()
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF, D96Parser.ELSE]:
                self.state = 428
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
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.elif_stm()
                self.state = 433
                self.elseStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.elif_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
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
            self.state = 439
            self.match(D96Parser.ELSEIF)
            self.state = 440
            self.match(D96Parser.LP)
            self.state = 441
            self.expr()
            self.state = 442
            self.match(D96Parser.RP)
            self.state = 443
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
            self.state = 445
            self.match(D96Parser.ELSE)
            self.state = 446
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
            self.state = 448
            self.match(D96Parser.FOREACH)
            self.state = 449
            self.match(D96Parser.LP)
            self.state = 450
            self.match(D96Parser.ID)
            self.state = 451
            self.match(D96Parser.IN)
            self.state = 452
            self.match(D96Parser.INTLIT)
            self.state = 453
            self.match(D96Parser.DDOTS)
            self.state = 454
            self.match(D96Parser.INTLIT)
            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 455
                self.match(D96Parser.BY)
                self.state = 456
                self.match(D96Parser.INTLIT)


            self.state = 459
            self.match(D96Parser.RP)
            self.state = 460
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
            self.state = 462
            self.match(D96Parser.BREAK)
            self.state = 463
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
            self.state = 465
            self.match(D96Parser.CONTINUE)
            self.state = 466
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
            self.state = 468
            self.func_call()
            self.state = 469
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
            self.state = 471
            self.match(D96Parser.RETURN)
            self.state = 474
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 472
                self.expr()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 476
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


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_typ_var




    def typ_var(self):

        localctx = D96Parser.Typ_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_typ_var)
        try:
            self.state = 484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 480
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 481
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 482
                self.array()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 483
                self.match(D96Parser.ID)
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
        self.enterRule(localctx, 94, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(D96Parser.ARRAY)
            self.state = 487
            self.match(D96Parser.LSB)
            self.state = 488
            self.typ_var()
            self.state = 489
            self.match(D96Parser.COMMA)
            self.state = 490
            self.match(D96Parser.INTLIT)
            self.state = 491
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
        self.enterRule(localctx, 96, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
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
        self.enterRule(localctx, 98, self.RULE_arraylit)
        try:
            self.state = 497
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.iar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
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
        self.enterRule(localctx, 100, self.RULE_iar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(D96Parser.ARRAY)
            self.state = 500
            self.match(D96Parser.LP)
            self.state = 506
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.state = 501
                self.aints()
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.state = 502
                self.afloats()
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.state = 503
                self.astrings()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.state = 504
                self.asbools()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 508
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
        self.enterRule(localctx, 102, self.RULE_aints)
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                self.match(D96Parser.INTLIT)
                self.state = 511
                self.match(D96Parser.COMMA)
                self.state = 512
                self.aints()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
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
        self.enterRule(localctx, 104, self.RULE_afloats)
        try:
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.match(D96Parser.FLOATLIT)
                self.state = 517
                self.match(D96Parser.COMMA)
                self.state = 518
                self.afloats()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
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
        self.enterRule(localctx, 106, self.RULE_astrings)
        try:
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.match(D96Parser.STRINGLIT)
                self.state = 523
                self.match(D96Parser.COMMA)
                self.state = 524
                self.astrings()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
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
        self.enterRule(localctx, 108, self.RULE_asbools)
        try:
            self.state = 533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.boolit()
                self.state = 529
                self.match(D96Parser.COMMA)
                self.state = 530
                self.asbools()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
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
        self.enterRule(localctx, 110, self.RULE_marraylists)
        try:
            self.state = 540
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.iar()
                self.state = 536
                self.match(D96Parser.COMMA)
                self.state = 537
                self.marraylists()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
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
        self.enterRule(localctx, 112, self.RULE_mar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(D96Parser.ARRAY)
            self.state = 543
            self.match(D96Parser.LP)
            self.state = 544
            self.marraylists()
            self.state = 545
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
         



