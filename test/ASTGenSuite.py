import unittest
from TestUtils import TestAST
from AST import *
from main.d96.utils.AST import *
class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        
        input = """Class Rectangle {
            
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[])])"
        self.assertTrue(TestAST.test(input,expect,300))
    def test_2(self):
        
        input = """Class Rectangle {
            Var a:Int;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,301))
    def test_3(self):
        
        input = """Class Rectangle {
            Var a,b:Int;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,302))
    def test_4(self):
        
        input = """Class Rectangle {
            Var a,b,c:Int;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,303))
    def test_5(self):
        
        input = """Class Rectangle {
            Val a:Int;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None))])])"
        self.assertTrue(TestAST.test(input,expect,304))
    def test_6(self):
        
        input = """Class Rectangle {
            Val a,b:Int;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,None))])])"
        self.assertTrue(TestAST.test(input,expect,305))
    def test_7(self):
        
        input = """Class Rectangle {
            Val a,b,c:Float;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,None))])])"
        self.assertTrue(TestAST.test(input,expect,306))
    def test_8(self):
        
        input = """Class Rectangle {
            Val a:String;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,None))])])"
        self.assertTrue(TestAST.test(input,expect,307))
    def test_9(self):
        
        input = """Class Rectangle {
            Val a:Boolean;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,None))])])"
        self.assertTrue(TestAST.test(input,expect,308))
    def test_10(self):
        
        input = """Class Rectangle {
            Val a:Car;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Car),None))])])"
        self.assertTrue(TestAST.test(input,expect,309))

    
   