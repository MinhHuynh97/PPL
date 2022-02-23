import unittest
from TestUtils import TestAST
from AST import *
from main.d96.utils.AST import *
class ASTGenSuite(unittest.TestCase):
    # def test_1(self):
        
    #     input = """Class Rectangle {
            
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[])])"
    #     self.assertTrue(TestAST.test(input,expect,300))
    # def test_2(self):
        
    #     input = """Class Rectangle {
    #         Var a:Int;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])"
    #     self.assertTrue(TestAST.test(input,expect,301))
    # def test_3(self):
        
    #     input = """Class Rectangle {
    #         Var a,b:Int;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])"
    #     self.assertTrue(TestAST.test(input,expect,302))
    # def test_4(self):
        
    #     input = """Class Rectangle {
    #         Var a,b,c:Int;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType))])])"
    #     self.assertTrue(TestAST.test(input,expect,303))
    # def test_5(self):
        
    #     input = """Class Rectangle {
    #         Val a:Int;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None))])])"
    #     self.assertTrue(TestAST.test(input,expect,304))
    # def test_6(self):
        
    #     input = """Class Rectangle {
    #         Val a,b:Int;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,None))])])"
    #     self.assertTrue(TestAST.test(input,expect,305))
    # def test_7(self):
        
    #     input = """Class Rectangle {
    #         Val a,b,c:Float;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,None))])])"
    #     self.assertTrue(TestAST.test(input,expect,306))
    # def test_8(self):
        
    #     input = """Class Rectangle {
    #         Val a:String;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,None))])])"
    #     self.assertTrue(TestAST.test(input,expect,307))
    # def test_9(self):
        
    #     input = """Class Rectangle {
    #         Val a:Boolean;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,None))])])"
    #     self.assertTrue(TestAST.test(input,expect,308))
    def test_10(self): 
        input = """Class Rectangle {
            Val a:Car;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Car),NullLiteral()))])])"
        self.assertTrue(TestAST.test(input,expect,309))
    def test_11(self): 
        input = """Class Shape {
            Val $a:Int=0;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input,expect,310))
    def test_12(self): 
        input = """Class Shape {
            Val $a:Int=2+3-10*3;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,BinaryOp(-,BinaryOp(+,IntLit(2),IntLit(3)),BinaryOp(*,IntLit(10),IntLit(3)))))])])"
        self.assertTrue(TestAST.test(input,expect,311))
    def test_13(self): 
        input = """Class Shape {
            Val $a,b:Float=2.3/4.2+(1.e3-2.4),0.0001;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),FloatType,BinaryOp(+,BinaryOp(/,FloatLit(2.3),FloatLit(4.2)),BinaryOp(-,FloatLit(1000.0),FloatLit(2.4))))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,FloatLit(0.0001)))])])"
        self.assertTrue(TestAST.test(input,expect,312))
    def test_14(self): 
        input = """Class Shape {
            Val $a:String="Minh" +. "Huynh";
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),StringType,BinaryOp(+.,StringLit(Minh),StringLit(Huynh))))])])"
        self.assertTrue(TestAST.test(input,expect,313))
    def test_15(self): 
        input = """Class Shape {
            Val $a:Boolean=True + False ;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),BoolType,BinaryOp(+,BooleanLit(True),BooleanLit(False))))])])"
        self.assertTrue(TestAST.test(input,expect,314))
    def test_16(self): 
        input = """Class Shape {
            Var $a,b,c:Boolean=True,False,True-False*False +True ;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,VarDecl(Id($a),BoolType,BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(b),BoolType,BooleanLit(False))),AttributeDecl(Instance,VarDecl(Id(c),BoolType,BinaryOp(+,BinaryOp(-,BooleanLit(True),BinaryOp(*,BooleanLit(False),BooleanLit(False))),BooleanLit(True))))])])"
        self.assertTrue(TestAST.test(input,expect,315))
    def test_17(self): 
        input = """Class Shape {
            Val $a:Array[Int,3]=Array(1,2,3) ;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(3),IntType),[IntLit(1),IntLit(2),IntLit(3)]))])])"
        self.assertTrue(TestAST.test(input,expect,316))
    def test_18(self): 
        input = """Class Shape {
            Val $a:Array[Float,2]=Array(1.2,3.1) ;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(2),FloatType),[FloatLit(1.2),FloatLit(3.1)]))])])"
        self.assertTrue(TestAST.test(input,expect,317))
    def test_19(self): 
        input = """Class Shape {
            Val $a:Array[String,2]=Array("Minh","Huynh") ;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(2),StringType),[StringLit(Minh),StringLit(Huynh)]))])])"
        self.assertTrue(TestAST.test(input,expect,318))
    def test_20(self): 
        input = """Class Shape {
            Val $a:Array[Boolean,2]=Array(True,False) ;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(2),BoolType),[BooleanLit(True),BooleanLit(False)]))])])"
        self.assertTrue(TestAST.test(input,expect,319))
    def test_21(self): 
        input = """Class Shape {
            Val $a:Array[Array[Int,3],2] ;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(2),ArrayType(IntLit(3),IntType)),None))])])"
        self.assertTrue(TestAST.test(input,expect,320))
    def test_22(self): 
        input = """Class Shape {
            Val $a:Array[Array[Array[Float,10],3],2] ;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(2),ArrayType(IntLit(3),ArrayType(IntLit(10),FloatType))),None))])])"
        self.assertTrue(TestAST.test(input,expect,321))
    def test_23(self): 
        input = """Class Shape {
            Val $a:Int ;
            Var b,c:Float=3.2,1.e2;
            Var myCar:Int=0;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(3.2))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(100.0))),AttributeDecl(Instance,VarDecl(Id(myCar),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input,expect,322))
    def test_24(self): 
        input = """Class Shape {
             ##Decl immutable##
            Val $a:Int ;
            ##Decl mutable##
            Var b,c:Float;
            
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType))])])"
        self.assertTrue(TestAST.test(input,expect,323))
    def test_25(self): 
        input = """Class Shape {       
            Val $a:Int ;
            Var b,c:Float;
            
        }
        Class Circle:Shape{
            Val $m:Int ;
        }
        
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType))]),ClassDecl(Id(Circle),Id(Shape),[AttributeDecl(Static,ConstDecl(Id($m),IntType,None))])])"
        self.assertTrue(TestAST.test(input,expect,324))
    def test_26(self): 
        input = """Class Shape {       
            Val $a:Int ;
            Var b,c:Float;
            Hi(say:String)
            {
                Return Out.printString("Shape is ...");
            }
        }
        
        
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType)),MethodDecl(Instance,Id(Hi),[param(Id(say),StringType)],Block([Return(CallExpr(Id(Out),Id(printString),[StringLit(Shape is ...)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,325))
    def test_27(self): 
        input = """Class Shape {       
            Val $a:Int ;
            Var b,c:Float;
            
        }
        CLass Rectangle: Shape {
            getArea() {
        Return Self.length * Self.width; }
        }
        
        
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType))])])"
        self.assertTrue(TestAST.test(input,expect,326))
    def test_28(self): 
        input = """Class Program {
            main() {
            Out.printInt(Shape::$numOfShape); }
            }
        
        
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([CallExpr(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id(Shape))])]))])])"
        self.assertTrue(TestAST.test(input,expect,327))
    def test_29(self): 
        input = """Class Program {
            main() {
            If(a>b)
                {
                    a=1;
                }
            Else
            {
                a=3;
            }
            }
            }
        
        
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))]),Block([AssignStmt(Id(a),IntLit(3))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,328))
    def test_30(self): 
        input = """Class Program {
            main() {
            If(a>b)
                {
                    a=1;
                }
            Elseif(a<b)
            {
                a=3;
            }
            Else
            {
                a=4;
            }
            }
            }
        
        
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(3))]),Block([AssignStmt(Id(a),IntLit(4))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,329))
    

    
   