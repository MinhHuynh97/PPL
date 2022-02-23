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
        buf.write("\u0235\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0080\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4\u0087\n\4\3\4\3\4\3\4\5\4\u008c\n")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u0094\n\5\3\6\3\6\5\6\u0098")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a1\n\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00ac\n\b\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\5\n\u00b4\n\n\3\13\3\13\3\13\3\13\5\13\u00ba")
        buf.write("\n\13\3\f\3\f\3\r\3\r\5\r\u00c0\n\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u00c6\n\r\5\r\u00c8\n\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u00d0\n\16\3\16\3\16\5\16\u00d4\n\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00e0\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\5\20\u00e7\n\20\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u00ed\n\21\3\21\3\21\3\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\5\23\u00fa\n\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u0108\n\24\3\25\3\25\3\25\3\25\5\25\u010e\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0119\n\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0121\n\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\5\30\u012a\n\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u0131\n\31\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\7\32\u0139\n\32\f\32\16\32\u013c\13\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\7\33\u0144\n\33\f\33\16\33\u0147")
        buf.write("\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u014f\n\34\f")
        buf.write("\34\16\34\u0152\13\34\3\35\3\35\3\35\5\35\u0157\n\35\3")
        buf.write("\36\3\36\3\36\5\36\u015c\n\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\7\37\u0163\n\37\f\37\16\37\u0166\13\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \5 \u0174\n \3 \7 \u0177\n \f \16")
        buf.write(" \u017a\13 \3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0185\n!\3!")
        buf.write("\3!\5!\u0189\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0190\n\"\3\"")
        buf.write("\3\"\5\"\u0194\n\"\3#\3#\3#\3#\3#\5#\u019b\n#\3$\3$\3")
        buf.write("$\3$\5$\u01a1\n$\3%\3%\3%\3%\3%\5%\u01a8\n%\3&\3&\3&\3")
        buf.write("&\3&\3&\5&\u01b0\n&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\5(\u01be\n(\3)\3)\3)\3)\3)\5)\u01c5\n)\3*\3*\3")
        buf.write("*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01d9")
        buf.write("\n,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\5\60\u01ea\n\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\5\61\u01f4\n\61\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\5\65\u0203\n\65\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\5\66\u020c\n\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\5\67\u0214\n\67\38\38\38\38\58\u021a")
        buf.write("\n8\39\39\39\39\59\u0220\n9\3:\3:\3:\3:\3:\5:\u0227\n")
        buf.write(":\3;\3;\3;\3;\3;\5;\u022e\n;\3<\3<\3<\3<\3<\3<\2\7\62")
        buf.write("\64\66<>=\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv\2\n")
        buf.write("\3\2\23\24\3\2=>\3\2-.\4\2&&(,\3\2$%\3\2\36\37\3\2 \"")
        buf.write("\3\2\3\4\2\u0245\2x\3\2\2\2\4\177\3\2\2\2\6\u0081\3\2")
        buf.write("\2\2\b\u0093\3\2\2\2\n\u0097\3\2\2\2\f\u0099\3\2\2\2\16")
        buf.write("\u00a4\3\2\2\2\20\u00af\3\2\2\2\22\u00b3\3\2\2\2\24\u00b9")
        buf.write("\3\2\2\2\26\u00bb\3\2\2\2\30\u00c7\3\2\2\2\32\u00d3\3")
        buf.write("\2\2\2\34\u00df\3\2\2\2\36\u00e6\3\2\2\2 \u00e8\3\2\2")
        buf.write("\2\"\u00f1\3\2\2\2$\u00f6\3\2\2\2&\u0107\3\2\2\2(\u010d")
        buf.write("\3\2\2\2*\u0118\3\2\2\2,\u011a\3\2\2\2.\u0129\3\2\2\2")
        buf.write("\60\u0130\3\2\2\2\62\u0132\3\2\2\2\64\u013d\3\2\2\2\66")
        buf.write("\u0148\3\2\2\28\u0156\3\2\2\2:\u015b\3\2\2\2<\u015d\3")
        buf.write("\2\2\2>\u0167\3\2\2\2@\u0188\3\2\2\2B\u0193\3\2\2\2D\u019a")
        buf.write("\3\2\2\2F\u01a0\3\2\2\2H\u01a7\3\2\2\2J\u01af\3\2\2\2")
        buf.write("L\u01b1\3\2\2\2N\u01b6\3\2\2\2P\u01c4\3\2\2\2R\u01c6\3")
        buf.write("\2\2\2T\u01cc\3\2\2\2V\u01cf\3\2\2\2X\u01dd\3\2\2\2Z\u01e0")
        buf.write("\3\2\2\2\\\u01e3\3\2\2\2^\u01e6\3\2\2\2`\u01f3\3\2\2\2")
        buf.write("b\u01f5\3\2\2\2d\u01f7\3\2\2\2f\u01fe\3\2\2\2h\u0202\3")
        buf.write("\2\2\2j\u0204\3\2\2\2l\u0213\3\2\2\2n\u0219\3\2\2\2p\u021f")
        buf.write("\3\2\2\2r\u0226\3\2\2\2t\u022d\3\2\2\2v\u022f\3\2\2\2")
        buf.write("xy\5\4\3\2yz\7\2\2\3z\3\3\2\2\2{|\5\6\4\2|}\5\4\3\2}\u0080")
        buf.write("\3\2\2\2~\u0080\5\6\4\2\177{\3\2\2\2\177~\3\2\2\2\u0080")
        buf.write("\5\3\2\2\2\u0081\u0086\7\22\2\2\u0082\u0087\7=\2\2\u0083")
        buf.write("\u0084\7=\2\2\u0084\u0085\7\63\2\2\u0085\u0087\7=\2\2")
        buf.write("\u0086\u0082\3\2\2\2\u0086\u0083\3\2\2\2\u0087\u0088\3")
        buf.write("\2\2\2\u0088\u008b\7\67\2\2\u0089\u008c\5\b\5\2\u008a")
        buf.write("\u008c\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\u008e\78\2\2\u008e\7\3\2\2")
        buf.write("\2\u008f\u0090\5\n\6\2\u0090\u0091\5\b\5\2\u0091\u0094")
        buf.write("\3\2\2\2\u0092\u0094\5\n\6\2\u0093\u008f\3\2\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094\t\3\2\2\2\u0095\u0098\5\22\n\2\u0096")
        buf.write("\u0098\5\32\16\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2")
        buf.write("\2\u0098\13\3\2\2\2\u0099\u009a\7\24\2\2\u009a\u009b\5")
        buf.write("\24\13\2\u009b\u009c\7\63\2\2\u009c\u00a0\5`\61\2\u009d")
        buf.write("\u009e\7\'\2\2\u009e\u00a1\5\30\r\2\u009f\u00a1\3\2\2")
        buf.write("\2\u00a0\u009d\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\u00a3\7\66\2\2\u00a3\r\3\2\2\2\u00a4\u00a5")
        buf.write("\7\23\2\2\u00a5\u00a6\5\24\13\2\u00a6\u00a7\7\63\2\2\u00a7")
        buf.write("\u00ab\5`\61\2\u00a8\u00a9\7\'\2\2\u00a9\u00ac\5\30\r")
        buf.write("\2\u00aa\u00ac\3\2\2\2\u00ab\u00a8\3\2\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\7\66\2\2\u00ae")
        buf.write("\17\3\2\2\2\u00af\u00b0\t\2\2\2\u00b0\21\3\2\2\2\u00b1")
        buf.write("\u00b4\5\f\7\2\u00b2\u00b4\5\16\b\2\u00b3\u00b1\3\2\2")
        buf.write("\2\u00b3\u00b2\3\2\2\2\u00b4\23\3\2\2\2\u00b5\u00b6\t")
        buf.write("\3\2\2\u00b6\u00b7\7\65\2\2\u00b7\u00ba\5\24\13\2\u00b8")
        buf.write("\u00ba\t\3\2\2\u00b9\u00b5\3\2\2\2\u00b9\u00b8\3\2\2\2")
        buf.write("\u00ba\25\3\2\2\2\u00bb\u00bc\t\3\2\2\u00bc\27\3\2\2\2")
        buf.write("\u00bd\u00c0\5.\30\2\u00be\u00c0\7\20\2\2\u00bf\u00bd")
        buf.write("\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1")
        buf.write("\u00c2\7\65\2\2\u00c2\u00c8\5\30\r\2\u00c3\u00c6\5.\30")
        buf.write("\2\u00c4\u00c6\7\20\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4")
        buf.write("\3\2\2\2\u00c6\u00c8\3\2\2\2\u00c7\u00bf\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c8\31\3\2\2\2\u00c9\u00d4\5 \21\2\u00ca")
        buf.write("\u00d4\5\"\22\2\u00cb\u00cc\t\3\2\2\u00cc\u00cf\7/\2\2")
        buf.write("\u00cd\u00d0\5\34\17\2\u00ce\u00d0\3\2\2\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("\u00d2\7\60\2\2\u00d2\u00d4\5$\23\2\u00d3\u00c9\3\2\2")
        buf.write("\2\u00d3\u00ca\3\2\2\2\u00d3\u00cb\3\2\2\2\u00d4\33\3")
        buf.write("\2\2\2\u00d5\u00d6\5\36\20\2\u00d6\u00d7\7\63\2\2\u00d7")
        buf.write("\u00d8\5`\61\2\u00d8\u00d9\7\66\2\2\u00d9\u00da\5\34\17")
        buf.write("\2\u00da\u00e0\3\2\2\2\u00db\u00dc\5\36\20\2\u00dc\u00dd")
        buf.write("\7\63\2\2\u00dd\u00de\5`\61\2\u00de\u00e0\3\2\2\2\u00df")
        buf.write("\u00d5\3\2\2\2\u00df\u00db\3\2\2\2\u00e0\35\3\2\2\2\u00e1")
        buf.write("\u00e2\5\26\f\2\u00e2\u00e3\7\65\2\2\u00e3\u00e4\5\36")
        buf.write("\20\2\u00e4\u00e7\3\2\2\2\u00e5\u00e7\5\26\f\2\u00e6\u00e1")
        buf.write("\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\37\3\2\2\2\u00e8\u00e9")
        buf.write("\7\30\2\2\u00e9\u00ec\7/\2\2\u00ea\u00ed\5\34\17\2\u00eb")
        buf.write("\u00ed\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee\u00ef\7\60\2\2\u00ef\u00f0")
        buf.write("\5$\23\2\u00f0!\3\2\2\2\u00f1\u00f2\7\31\2\2\u00f2\u00f3")
        buf.write("\7/\2\2\u00f3\u00f4\7\60\2\2\u00f4\u00f5\5$\23\2\u00f5")
        buf.write("#\3\2\2\2\u00f6\u00f9\7\67\2\2\u00f7\u00fa\5(\25\2\u00f8")
        buf.write("\u00fa\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb\u00fc\78\2\2\u00fc%\3\2\2\2")
        buf.write("\u00fd\u0108\5\f\7\2\u00fe\u0108\5L\'\2\u00ff\u0108\5")
        buf.write("N(\2\u0100\u0108\5V,\2\u0101\u0108\5X-\2\u0102\u0108\5")
        buf.write("Z.\2\u0103\u0108\5\\/\2\u0104\u0108\5^\60\2\u0105\u0108")
        buf.write("\5$\23\2\u0106\u0108\5J&\2\u0107\u00fd\3\2\2\2\u0107\u00fe")
        buf.write("\3\2\2\2\u0107\u00ff\3\2\2\2\u0107\u0100\3\2\2\2\u0107")
        buf.write("\u0101\3\2\2\2\u0107\u0102\3\2\2\2\u0107\u0103\3\2\2\2")
        buf.write("\u0107\u0104\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0106\3")
        buf.write("\2\2\2\u0108\'\3\2\2\2\u0109\u010a\5&\24\2\u010a\u010b")
        buf.write("\5(\25\2\u010b\u010e\3\2\2\2\u010c\u010e\5&\24\2\u010d")
        buf.write("\u0109\3\2\2\2\u010d\u010c\3\2\2\2\u010e)\3\2\2\2\u010f")
        buf.write("\u0110\7\61\2\2\u0110\u0111\5.\30\2\u0111\u0112\7\62\2")
        buf.write("\2\u0112\u0113\5*\26\2\u0113\u0119\3\2\2\2\u0114\u0115")
        buf.write("\7\61\2\2\u0115\u0116\5.\30\2\u0116\u0117\7\62\2\2\u0117")
        buf.write("\u0119\3\2\2\2\u0118\u010f\3\2\2\2\u0118\u0114\3\2\2\2")
        buf.write("\u0119+\3\2\2\2\u011a\u011b\5.\30\2\u011b\u011c\7\64\2")
        buf.write("\2\u011c\u011d\5\26\f\2\u011d\u0120\7/\2\2\u011e\u0121")
        buf.write("\5\34\17\2\u011f\u0121\3\2\2\2\u0120\u011e\3\2\2\2\u0120")
        buf.write("\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\7\60\2")
        buf.write("\2\u0123-\3\2\2\2\u0124\u0125\5\60\31\2\u0125\u0126\t")
        buf.write("\4\2\2\u0126\u0127\5\60\31\2\u0127\u012a\3\2\2\2\u0128")
        buf.write("\u012a\5\60\31\2\u0129\u0124\3\2\2\2\u0129\u0128\3\2\2")
        buf.write("\2\u012a/\3\2\2\2\u012b\u012c\5\62\32\2\u012c\u012d\t")
        buf.write("\5\2\2\u012d\u012e\5\62\32\2\u012e\u0131\3\2\2\2\u012f")
        buf.write("\u0131\5\62\32\2\u0130\u012b\3\2\2\2\u0130\u012f\3\2\2")
        buf.write("\2\u0131\61\3\2\2\2\u0132\u0133\b\32\1\2\u0133\u0134\5")
        buf.write("\64\33\2\u0134\u013a\3\2\2\2\u0135\u0136\f\4\2\2\u0136")
        buf.write("\u0137\t\6\2\2\u0137\u0139\5\64\33\2\u0138\u0135\3\2\2")
        buf.write("\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b")
        buf.write("\3\2\2\2\u013b\63\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013e")
        buf.write("\b\33\1\2\u013e\u013f\5\66\34\2\u013f\u0145\3\2\2\2\u0140")
        buf.write("\u0141\f\4\2\2\u0141\u0142\t\7\2\2\u0142\u0144\5\66\34")
        buf.write("\2\u0143\u0140\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146\65\3\2\2\2\u0147\u0145")
        buf.write("\3\2\2\2\u0148\u0149\b\34\1\2\u0149\u014a\58\35\2\u014a")
        buf.write("\u0150\3\2\2\2\u014b\u014c\f\4\2\2\u014c\u014d\t\b\2\2")
        buf.write("\u014d\u014f\58\35\2\u014e\u014b\3\2\2\2\u014f\u0152\3")
        buf.write("\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151\67")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0154\7#\2\2\u0154")
        buf.write("\u0157\58\35\2\u0155\u0157\5:\36\2\u0156\u0153\3\2\2\2")
        buf.write("\u0156\u0155\3\2\2\2\u01579\3\2\2\2\u0158\u0159\7\37\2")
        buf.write("\2\u0159\u015c\5:\36\2\u015a\u015c\5<\37\2\u015b\u0158")
        buf.write("\3\2\2\2\u015b\u015a\3\2\2\2\u015c;\3\2\2\2\u015d\u015e")
        buf.write("\b\37\1\2\u015e\u015f\5> \2\u015f\u0164\3\2\2\2\u0160")
        buf.write("\u0161\f\4\2\2\u0161\u0163\5*\26\2\u0162\u0160\3\2\2\2")
        buf.write("\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165=\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168")
        buf.write("\b \1\2\u0168\u0169\5@!\2\u0169\u0178\3\2\2\2\u016a\u016b")
        buf.write("\f\5\2\2\u016b\u016c\7\64\2\2\u016c\u0177\7=\2\2\u016d")
        buf.write("\u016e\f\4\2\2\u016e\u016f\7\64\2\2\u016f\u0170\7=\2\2")
        buf.write("\u0170\u0173\7/\2\2\u0171\u0174\5\30\r\2\u0172\u0174\3")
        buf.write("\2\2\2\u0173\u0171\3\2\2\2\u0173\u0172\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0177\7\60\2\2\u0176\u016a\3\2\2\2\u0176")
        buf.write("\u016d\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179?\3\2\2\2\u017a\u0178\3\2\2")
        buf.write("\2\u017b\u017c\7=\2\2\u017c\u017d\79\2\2\u017d\u0189\7")
        buf.write(">\2\2\u017e\u017f\7=\2\2\u017f\u0180\79\2\2\u0180\u0181")
        buf.write("\7>\2\2\u0181\u0184\7/\2\2\u0182\u0185\5\30\r\2\u0183")
        buf.write("\u0185\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0183\3\2\2\2")
        buf.write("\u0185\u0186\3\2\2\2\u0186\u0189\7\60\2\2\u0187\u0189")
        buf.write("\5B\"\2\u0188\u017b\3\2\2\2\u0188\u017e\3\2\2\2\u0188")
        buf.write("\u0187\3\2\2\2\u0189A\3\2\2\2\u018a\u018b\7\25\2\2\u018b")
        buf.write("\u018c\7=\2\2\u018c\u018f\7/\2\2\u018d\u0190\5\30\r\2")
        buf.write("\u018e\u0190\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u018e\3")
        buf.write("\2\2\2\u0190\u0191\3\2\2\2\u0191\u0194\7\60\2\2\u0192")
        buf.write("\u0194\5D#\2\u0193\u018a\3\2\2\2\u0193\u0192\3\2\2\2\u0194")
        buf.write("C\3\2\2\2\u0195\u0196\7/\2\2\u0196\u0197\5.\30\2\u0197")
        buf.write("\u0198\7\60\2\2\u0198\u019b\3\2\2\2\u0199\u019b\5F$\2")
        buf.write("\u019a\u0195\3\2\2\2\u019a\u0199\3\2\2\2\u019bE\3\2\2")
        buf.write("\2\u019c\u01a1\7\32\2\2\u019d\u01a1\7\20\2\2\u019e\u01a1")
        buf.write("\5\26\f\2\u019f\u01a1\5H%\2\u01a0\u019c\3\2\2\2\u01a0")
        buf.write("\u019d\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u019f\3\2\2\2")
        buf.write("\u01a1G\3\2\2\2\u01a2\u01a8\7:\2\2\u01a3\u01a8\7;\2\2")
        buf.write("\u01a4\u01a8\5f\64\2\u01a5\u01a8\7<\2\2\u01a6\u01a8\5")
        buf.write("h\65\2\u01a7\u01a2\3\2\2\2\u01a7\u01a3\3\2\2\2\u01a7\u01a4")
        buf.write("\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8")
        buf.write("I\3\2\2\2\u01a9\u01aa\5> \2\u01aa\u01ab\7\66\2\2\u01ab")
        buf.write("\u01b0\3\2\2\2\u01ac\u01ad\5@!\2\u01ad\u01ae\7\66\2\2")
        buf.write("\u01ae\u01b0\3\2\2\2\u01af\u01a9\3\2\2\2\u01af\u01ac\3")
        buf.write("\2\2\2\u01b0K\3\2\2\2\u01b1\u01b2\5.\30\2\u01b2\u01b3")
        buf.write("\7\'\2\2\u01b3\u01b4\5.\30\2\u01b4\u01b5\7\66\2\2\u01b5")
        buf.write("M\3\2\2\2\u01b6\u01b7\7\7\2\2\u01b7\u01b8\7/\2\2\u01b8")
        buf.write("\u01b9\5.\30\2\u01b9\u01ba\7\60\2\2\u01ba\u01bd\5$\23")
        buf.write("\2\u01bb\u01be\5P)\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3")
        buf.write("\2\2\2\u01bd\u01bc\3\2\2\2\u01beO\3\2\2\2\u01bf\u01c0")
        buf.write("\5R*\2\u01c0\u01c1\5P)\2\u01c1\u01c5\3\2\2\2\u01c2\u01c5")
        buf.write("\5R*\2\u01c3\u01c5\5T+\2\u01c4\u01bf\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5Q\3\2\2\2\u01c6\u01c7")
        buf.write("\7\b\2\2\u01c7\u01c8\7/\2\2\u01c8\u01c9\5.\30\2\u01c9")
        buf.write("\u01ca\7\60\2\2\u01ca\u01cb\5$\23\2\u01cbS\3\2\2\2\u01cc")
        buf.write("\u01cd\7\t\2\2\u01cd\u01ce\5$\23\2\u01ceU\3\2\2\2\u01cf")
        buf.write("\u01d0\7\n\2\2\u01d0\u01d1\7/\2\2\u01d1\u01d2\7=\2\2\u01d2")
        buf.write("\u01d3\7\27\2\2\u01d3\u01d4\7:\2\2\u01d4\u01d5\7\33\2")
        buf.write("\2\u01d5\u01d8\7:\2\2\u01d6\u01d7\7\21\2\2\u01d7\u01d9")
        buf.write("\7:\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9")
        buf.write("\u01da\3\2\2\2\u01da\u01db\7\60\2\2\u01db\u01dc\5$\23")
        buf.write("\2\u01dcW\3\2\2\2\u01dd\u01de\7\5\2\2\u01de\u01df\7\66")
        buf.write("\2\2\u01dfY\3\2\2\2\u01e0\u01e1\7\6\2\2\u01e1\u01e2\7")
        buf.write("\66\2\2\u01e2[\3\2\2\2\u01e3\u01e4\5,\27\2\u01e4\u01e5")
        buf.write("\7\66\2\2\u01e5]\3\2\2\2\u01e6\u01e9\7\26\2\2\u01e7\u01ea")
        buf.write("\5.\30\2\u01e8\u01ea\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9")
        buf.write("\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\7\66\2")
        buf.write("\2\u01ec_\3\2\2\2\u01ed\u01f4\7\f\2\2\u01ee\u01f4\7\r")
        buf.write("\2\2\u01ef\u01f4\7\16\2\2\u01f0\u01f4\7\17\2\2\u01f1\u01f4")
        buf.write("\5d\63\2\u01f2\u01f4\5b\62\2\u01f3\u01ed\3\2\2\2\u01f3")
        buf.write("\u01ee\3\2\2\2\u01f3\u01ef\3\2\2\2\u01f3\u01f0\3\2\2\2")
        buf.write("\u01f3\u01f1\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4a\3\2\2")
        buf.write("\2\u01f5\u01f6\7=\2\2\u01f6c\3\2\2\2\u01f7\u01f8\7\13")
        buf.write("\2\2\u01f8\u01f9\7\61\2\2\u01f9\u01fa\5`\61\2\u01fa\u01fb")
        buf.write("\7\65\2\2\u01fb\u01fc\7:\2\2\u01fc\u01fd\7\62\2\2\u01fd")
        buf.write("e\3\2\2\2\u01fe\u01ff\t\t\2\2\u01ffg\3\2\2\2\u0200\u0203")
        buf.write("\5j\66\2\u0201\u0203\5v<\2\u0202\u0200\3\2\2\2\u0202\u0201")
        buf.write("\3\2\2\2\u0203i\3\2\2\2\u0204\u0205\7\13\2\2\u0205\u020b")
        buf.write("\7/\2\2\u0206\u020c\5l\67\2\u0207\u020c\5n8\2\u0208\u020c")
        buf.write("\5p9\2\u0209\u020c\5r:\2\u020a\u020c\3\2\2\2\u020b\u0206")
        buf.write("\3\2\2\2\u020b\u0207\3\2\2\2\u020b\u0208\3\2\2\2\u020b")
        buf.write("\u0209\3\2\2\2\u020b\u020a\3\2\2\2\u020c\u020d\3\2\2\2")
        buf.write("\u020d\u020e\7\60\2\2\u020ek\3\2\2\2\u020f\u0210\7:\2")
        buf.write("\2\u0210\u0211\7\65\2\2\u0211\u0214\5l\67\2\u0212\u0214")
        buf.write("\7:\2\2\u0213\u020f\3\2\2\2\u0213\u0212\3\2\2\2\u0214")
        buf.write("m\3\2\2\2\u0215\u0216\7;\2\2\u0216\u0217\7\65\2\2\u0217")
        buf.write("\u021a\5n8\2\u0218\u021a\7;\2\2\u0219\u0215\3\2\2\2\u0219")
        buf.write("\u0218\3\2\2\2\u021ao\3\2\2\2\u021b\u021c\7<\2\2\u021c")
        buf.write("\u021d\7\65\2\2\u021d\u0220\5p9\2\u021e\u0220\7<\2\2\u021f")
        buf.write("\u021b\3\2\2\2\u021f\u021e\3\2\2\2\u0220q\3\2\2\2\u0221")
        buf.write("\u0222\5f\64\2\u0222\u0223\7\65\2\2\u0223\u0224\5r:\2")
        buf.write("\u0224\u0227\3\2\2\2\u0225\u0227\5f\64\2\u0226\u0221\3")
        buf.write("\2\2\2\u0226\u0225\3\2\2\2\u0227s\3\2\2\2\u0228\u0229")
        buf.write("\5j\66\2\u0229\u022a\7\65\2\2\u022a\u022b\5t;\2\u022b")
        buf.write("\u022e\3\2\2\2\u022c\u022e\5j\66\2\u022d\u0228\3\2\2\2")
        buf.write("\u022d\u022c\3\2\2\2\u022eu\3\2\2\2\u022f\u0230\7\13\2")
        buf.write("\2\u0230\u0231\7/\2\2\u0231\u0232\5t;\2\u0232\u0233\7")
        buf.write("\60\2\2\u0233w\3\2\2\2\67\177\u0086\u008b\u0093\u0097")
        buf.write("\u00a0\u00ab\u00b3\u00b9\u00bf\u00c5\u00c7\u00cf\u00d3")
        buf.write("\u00df\u00e6\u00ec\u00f9\u0107\u010d\u0118\u0120\u0129")
        buf.write("\u0130\u013a\u0145\u0150\u0156\u015b\u0164\u0173\u0176")
        buf.write("\u0178\u0184\u0188\u018f\u0193\u019a\u01a0\u01a7\u01af")
        buf.write("\u01bd\u01c4\u01d8\u01e9\u01f3\u0202\u020b\u0213\u0219")
        buf.write("\u021f\u0226\u022d")
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
    RULE_member_access = 36
    RULE_assignment_statement = 37
    RULE_if_statement = 38
    RULE_elseStmt = 39
    RULE_elif_stm = 40
    RULE_else_stm = 41
    RULE_foreach_stmt = 42
    RULE_break_stmt = 43
    RULE_cont_stmt = 44
    RULE_call_stmt = 45
    RULE_return_stmt = 46
    RULE_typ_var = 47
    RULE_class_type = 48
    RULE_array = 49
    RULE_boolit = 50
    RULE_arraylit = 51
    RULE_iar = 52
    RULE_aints = 53
    RULE_afloats = 54
    RULE_astrings = 55
    RULE_asbools = 56
    RULE_marraylists = 57
    RULE_mar = 58

    ruleNames =  [ "program", "decls", "class_decl", "class_bodys", "class_body", 
                   "variable_decl", "const_decl", "typ_name", "attribute_decl", 
                   "list_name", "name_att", "list_exp", "method_decl", "parameter", 
                   "identifer_list", "constructor", "destructor", "block_stm", 
                   "statement", "statements", "index_operators", "func_call", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10", "expr11", 
                   "operand", "literal", "member_access", "assignment_statement", 
                   "if_statement", "elseStmt", "elif_stm", "else_stm", "foreach_stmt", 
                   "break_stmt", "cont_stmt", "call_stmt", "return_stmt", 
                   "typ_var", "class_type", "array", "boolit", "arraylit", 
                   "iar", "aints", "afloats", "astrings", "asbools", "marraylists", 
                   "mar" ]

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
            self.state = 118
            self.decls()
            self.state = 119
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
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.class_decl()
                self.state = 122
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
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
            self.state = 127
            self.match(D96Parser.CLASS)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 128
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 129
                self.match(D96Parser.ID)
                self.state = 130
                self.match(D96Parser.COLON)
                self.state = 131
                self.match(D96Parser.ID)
                pass


            self.state = 134
            self.match(D96Parser.LCB)
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 135
                self.class_bodys()
                pass
            elif token in [D96Parser.RCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 139
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
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.class_body()
                self.state = 142
                self.class_bodys()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
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
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.attribute_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
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
            self.state = 151
            self.match(D96Parser.VAR)
            self.state = 152
            self.list_name()
            self.state = 153
            self.match(D96Parser.COLON)
            self.state = 154
            self.typ_var()
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SET]:
                self.state = 155
                self.match(D96Parser.SET)
                self.state = 156
                self.list_exp()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 160
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
            self.state = 162
            self.match(D96Parser.VAL)
            self.state = 163
            self.list_name()
            self.state = 164
            self.match(D96Parser.COLON)
            self.state = 165
            self.typ_var()
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SET]:
                self.state = 166
                self.match(D96Parser.SET)
                self.state = 167
                self.list_exp()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 171
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
            self.state = 173
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
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.variable_decl()
                pass
            elif token in [D96Parser.VAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
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
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 180
                self.match(D96Parser.COMMA)
                self.state = 181
                self.list_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
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
            self.state = 185
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
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 187
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 188
                    self.match(D96Parser.NULL)
                    pass


                self.state = 191
                self.match(D96Parser.COMMA)
                self.state = 192
                self.list_exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 193
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 194
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
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.destructor()
                pass
            elif token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 3)
                self.state = 201
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 202
                self.match(D96Parser.LP)
                self.state = 205
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 203
                    self.parameter()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 207
                self.match(D96Parser.RP)
                self.state = 208
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
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.identifer_list()
                self.state = 212
                self.match(D96Parser.COLON)
                self.state = 213
                self.typ_var()
                self.state = 214
                self.match(D96Parser.SEMI)
                self.state = 215
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.identifer_list()
                self.state = 218
                self.match(D96Parser.COLON)
                self.state = 219
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
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.name_att()
                self.state = 224
                self.match(D96Parser.COMMA)
                self.state = 225
                self.identifer_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
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
            self.state = 230
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 231
            self.match(D96Parser.LP)
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 232
                self.parameter()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 236
            self.match(D96Parser.RP)
            self.state = 237
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
            self.state = 239
            self.match(D96Parser.DESTRUCTOR)
            self.state = 240
            self.match(D96Parser.LP)
            self.state = 241
            self.match(D96Parser.RP)
            self.state = 242
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
            self.state = 244
            self.match(D96Parser.LCB)
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NULL, D96Parser.VAR, D96Parser.NEW, D96Parser.RETURN, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.LCB, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 245
                self.statements()
                pass
            elif token in [D96Parser.RCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 249
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


        def member_access(self):
            return self.getTypedRuleContext(D96Parser.Member_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 253
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 254
                self.foreach_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 255
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 256
                self.cont_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 257
                self.call_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 258
                self.return_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 259
                self.block_stm()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 260
                self.member_access()
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
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.statement()
                self.state = 264
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
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
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(D96Parser.LSB)
                self.state = 270
                self.expr()
                self.state = 271
                self.match(D96Parser.RSB)
                self.state = 272
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.match(D96Parser.LSB)
                self.state = 275
                self.expr()
                self.state = 276
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
            self.state = 280
            self.expr()
            self.state = 281
            self.match(D96Parser.DOT)
            self.state = 282
            self.name_att()
            self.state = 283
            self.match(D96Parser.LP)
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 284
                self.parameter()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 288
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
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.expr1()
                self.state = 291
                _la = self._input.LA(1)
                if not(_la==D96Parser.ED or _la==D96Parser.AD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 292
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
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
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.expr2(0)
                self.state = 298
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NE) | (1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 299
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
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
            self.state = 305
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 309
                    self.expr3(0) 
                self.state = 314
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
            self.state = 316
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 318
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 319
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 320
                    self.expr4(0) 
                self.state = 325
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
            self.state = 327
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 329
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 330
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 331
                    self.expr5() 
                self.state = 336
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
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(D96Parser.NOT)
                self.state = 338
                self.expr5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
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
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.match(D96Parser.SUB)
                self.state = 343
                self.expr6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
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
            self.state = 348
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 350
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 351
                    self.index_operators() 
                self.state = 356
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
            self.state = 358
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 372
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 360
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 361
                        self.match(D96Parser.DOT)
                        self.state = 362
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 363
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 364
                        self.match(D96Parser.DOT)
                        self.state = 365
                        self.match(D96Parser.ID)
                        self.state = 366
                        self.match(D96Parser.LP)
                        self.state = 369
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                            self.state = 367
                            self.list_exp()
                            pass
                        elif token in [D96Parser.RP]:
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 371
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 376
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
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(D96Parser.ID)
                self.state = 378
                self.match(D96Parser.ACCESS)
                self.state = 379
                self.match(D96Parser.Dollar_id)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.match(D96Parser.ID)
                self.state = 381
                self.match(D96Parser.ACCESS)
                self.state = 382
                self.match(D96Parser.Dollar_id)
                self.state = 383
                self.match(D96Parser.LP)
                self.state = 386
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 384
                    self.list_exp()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 388
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 389
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
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(D96Parser.NEW)
                self.state = 393
                self.match(D96Parser.ID)
                self.state = 394
                self.match(D96Parser.LP)
                self.state = 397
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 395
                    self.list_exp()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 399
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
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
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(D96Parser.LP)
                self.state = 404
                self.expr()
                self.state = 405
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
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
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 3)
                self.state = 412
                self.name_att()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 413
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
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 418
                self.boolit()
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 419
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 420
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


    class Member_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_access




    def member_access(self):

        localctx = D96Parser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_member_access)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.expr8(0)
                self.state = 424
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.expr9()
                self.state = 427
                self.match(D96Parser.SEMI)
                pass


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
        self.enterRule(localctx, 74, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.expr()
            self.state = 432
            self.match(D96Parser.SET)
            self.state = 433
            self.expr()
            self.state = 434
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
        self.enterRule(localctx, 76, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(D96Parser.IF)
            self.state = 437
            self.match(D96Parser.LP)
            self.state = 438
            self.expr()
            self.state = 439
            self.match(D96Parser.RP)
            self.state = 440
            self.block_stm()
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF, D96Parser.ELSE]:
                self.state = 441
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
        self.enterRule(localctx, 78, self.RULE_elseStmt)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.elif_stm()
                self.state = 446
                self.elseStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.elif_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 449
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
        self.enterRule(localctx, 80, self.RULE_elif_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(D96Parser.ELSEIF)
            self.state = 453
            self.match(D96Parser.LP)
            self.state = 454
            self.expr()
            self.state = 455
            self.match(D96Parser.RP)
            self.state = 456
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
        self.enterRule(localctx, 82, self.RULE_else_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(D96Parser.ELSE)
            self.state = 459
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
        self.enterRule(localctx, 84, self.RULE_foreach_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(D96Parser.FOREACH)
            self.state = 462
            self.match(D96Parser.LP)
            self.state = 463
            self.match(D96Parser.ID)
            self.state = 464
            self.match(D96Parser.IN)
            self.state = 465
            self.match(D96Parser.INTLIT)
            self.state = 466
            self.match(D96Parser.DDOTS)
            self.state = 467
            self.match(D96Parser.INTLIT)
            self.state = 470
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 468
                self.match(D96Parser.BY)
                self.state = 469
                self.match(D96Parser.INTLIT)


            self.state = 472
            self.match(D96Parser.RP)
            self.state = 473
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
        self.enterRule(localctx, 86, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(D96Parser.BREAK)
            self.state = 476
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
        self.enterRule(localctx, 88, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(D96Parser.CONTINUE)
            self.state = 479
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
        self.enterRule(localctx, 90, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.func_call()
            self.state = 482
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
        self.enterRule(localctx, 92, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(D96Parser.RETURN)
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 485
                self.expr()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 489
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
        self.enterRule(localctx, 94, self.RULE_typ_var)
        try:
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 493
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 494
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 495
                self.array()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 496
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
        self.enterRule(localctx, 96, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
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
        self.enterRule(localctx, 98, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(D96Parser.ARRAY)
            self.state = 502
            self.match(D96Parser.LSB)
            self.state = 503
            self.typ_var()
            self.state = 504
            self.match(D96Parser.COMMA)
            self.state = 505
            self.match(D96Parser.INTLIT)
            self.state = 506
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
        self.enterRule(localctx, 100, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
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
        self.enterRule(localctx, 102, self.RULE_arraylit)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                self.iar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
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
        self.enterRule(localctx, 104, self.RULE_iar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(D96Parser.ARRAY)
            self.state = 515
            self.match(D96Parser.LP)
            self.state = 521
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.state = 516
                self.aints()
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.state = 517
                self.afloats()
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.state = 518
                self.astrings()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.state = 519
                self.asbools()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 523
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
        self.enterRule(localctx, 106, self.RULE_aints)
        try:
            self.state = 529
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.match(D96Parser.INTLIT)
                self.state = 526
                self.match(D96Parser.COMMA)
                self.state = 527
                self.aints()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 528
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
        self.enterRule(localctx, 108, self.RULE_afloats)
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.match(D96Parser.FLOATLIT)
                self.state = 532
                self.match(D96Parser.COMMA)
                self.state = 533
                self.afloats()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 534
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
        self.enterRule(localctx, 110, self.RULE_astrings)
        try:
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(D96Parser.STRINGLIT)
                self.state = 538
                self.match(D96Parser.COMMA)
                self.state = 539
                self.astrings()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
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
        self.enterRule(localctx, 112, self.RULE_asbools)
        try:
            self.state = 548
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                self.boolit()
                self.state = 544
                self.match(D96Parser.COMMA)
                self.state = 545
                self.asbools()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 547
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
        self.enterRule(localctx, 114, self.RULE_marraylists)
        try:
            self.state = 555
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 550
                self.iar()
                self.state = 551
                self.match(D96Parser.COMMA)
                self.state = 552
                self.marraylists()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 554
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
        self.enterRule(localctx, 116, self.RULE_mar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(D96Parser.ARRAY)
            self.state = 558
            self.match(D96Parser.LP)
            self.state = 559
            self.marraylists()
            self.state = 560
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
         




