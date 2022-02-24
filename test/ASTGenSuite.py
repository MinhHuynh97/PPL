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
    # def test_10(self): 
    #     input = """Class Rectangle {
    #         Val a:Car;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Car),NullLiteral()))])])"
    #     self.assertTrue(TestAST.test(input,expect,309))
    # def test_11(self): 
    #     input = """Class Shape {
    #         Val $a:Int=0;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(0)))])])"
    #     self.assertTrue(TestAST.test(input,expect,310))
    # def test_12(self): 
    #     input = """Class Shape {
    #         Val $a:Int=2+3-10*3;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,BinaryOp(-,BinaryOp(+,IntLit(2),IntLit(3)),BinaryOp(*,IntLit(10),IntLit(3)))))])])"
    #     self.assertTrue(TestAST.test(input,expect,311))
    # def test_13(self): 
    #     input = """Class Shape {
    #         Val $a,b:Float=2.3/4.2+(1.e3-2.4),0.0001;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),FloatType,BinaryOp(+,BinaryOp(/,FloatLit(2.3),FloatLit(4.2)),BinaryOp(-,FloatLit(1000.0),FloatLit(2.4))))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,FloatLit(0.0001)))])])"
    #     self.assertTrue(TestAST.test(input,expect,312))
    # def test_14(self): 
    #     input = """Class Shape {
    #         Val $a:String="Minh" +. "Huynh";
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),StringType,BinaryOp(+.,StringLit(Minh),StringLit(Huynh))))])])"
    #     self.assertTrue(TestAST.test(input,expect,313))
    # def test_15(self): 
    #     input = """Class Shape {
    #         Val $a:Boolean=True + False ;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),BoolType,BinaryOp(+,BooleanLit(True),BooleanLit(False))))])])"
    #     self.assertTrue(TestAST.test(input,expect,314))
    # def test_16(self): 
    #     input = """Class Shape {
    #         Var $a,b,c:Boolean=True,False,True-False*False +True ;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,VarDecl(Id($a),BoolType,BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(b),BoolType,BooleanLit(False))),AttributeDecl(Instance,VarDecl(Id(c),BoolType,BinaryOp(+,BinaryOp(-,BooleanLit(True),BinaryOp(*,BooleanLit(False),BooleanLit(False))),BooleanLit(True))))])])"
    #     self.assertTrue(TestAST.test(input,expect,315))
    # def test_17(self): 
    #     input = """Class Shape {
    #         Val $a:Array[Int,3]=Array(1,2,3) ;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(3),IntType),[IntLit(1),IntLit(2),IntLit(3)]))])])"
    #     self.assertTrue(TestAST.test(input,expect,316))
    # def test_18(self): 
    #     input = """Class Shape {
    #         Val $a:Array[Float,2]=Array(1.2,3.1) ;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(2),FloatType),[FloatLit(1.2),FloatLit(3.1)]))])])"
    #     self.assertTrue(TestAST.test(input,expect,317))
    # def test_19(self): 
    #     input = """Class Shape {
    #         Val $a:Array[String,2]=Array("Minh","Huynh") ;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(2),StringType),[StringLit(Minh),StringLit(Huynh)]))])])"
    #     self.assertTrue(TestAST.test(input,expect,318))
    # def test_20(self): 
    #     input = """Class Shape {
    #         Val $a:Array[Boolean,2]=Array(True,False) ;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(2),BoolType),[BooleanLit(True),BooleanLit(False)]))])])"
    #     self.assertTrue(TestAST.test(input,expect,319))
    # def test_21(self): 
    #     input = """Class Shape {
    #         Val $a:Array[Array[Int,3],2] ;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(2),ArrayType(IntLit(3),IntType)),None))])])"
    #     self.assertTrue(TestAST.test(input,expect,320))
    # def test_22(self): 
    #     input = """Class Shape {
    #         Val $a:Array[Array[Array[Float,10],3],2] ;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),ArrayType(IntLit(2),ArrayType(IntLit(3),ArrayType(IntLit(10),FloatType))),None))])])"
    #     self.assertTrue(TestAST.test(input,expect,321))
    # def test_23(self): 
    #     input = """Class Shape {
    #         Val $a:Int ;
    #         Var b,c:Float=3.2,1.e2;
    #         Var myCar:Int=0;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(3.2))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(100.0))),AttributeDecl(Instance,VarDecl(Id(myCar),IntType,IntLit(0)))])])"
    #     self.assertTrue(TestAST.test(input,expect,322))
    # def test_24(self): 
    #     input = """Class Shape {
    #          ##Decl immutable##
    #         Val $a:Int ;
    #         ##Decl mutable##
    #         Var b,c:Float;
            
    #     }"""
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType))])])"
    #     self.assertTrue(TestAST.test(input,expect,323))
    # def test_25(self): 
    #     input = """Class Shape {       
    #         Val $a:Int ;
    #         Var b,c:Float;
            
    #     }
    #     Class Circle:Shape{
    #         Val $m:Int ;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType))]),ClassDecl(Id(Circle),Id(Shape),[AttributeDecl(Static,ConstDecl(Id($m),IntType,None))])])"
    #     self.assertTrue(TestAST.test(input,expect,324))
    # def test_26(self): 
    #     input = """Class Shape {       
    #         Val $a:Int ;
    #         Var b,c:Float;
    #         Hi(say:String)
    #         {
    #             Return Out.printString("Shape is ...");
    #         }
    #     }
        
        
    #     """
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType)),MethodDecl(Instance,Id(Hi),[param(Id(say),StringType)],Block([Return(CallExpr(Id(Out),Id(printString),[StringLit(Shape is ...)]))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,325))
    # def test_27(self): 
    #     input = """Class Shape {       
    #         Val $a:Int ;
    #         Var b,c:Float;
            
    #     }
    #     Class Rectangle: Shape {
    #         getArea() {
    #     Return Self.length * Self.width; }
    #     }
        
        
    #     """
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Instance,Id(getArea),[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,326))
    # def test_28(self): 
    #     input = """Class Program {
    #         main() {
    #         Out.printInt(Shape::$numOfShape); }
    #         }
        
        
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([CallExpr(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id(Shape))])]))])])"
    #     self.assertTrue(TestAST.test(input,expect,327))
    # def test_29(self): 
    #     input = """Class Program {
    #         main() {
    #         If(a>b)
    #             {
    #                 a=1;
    #             }
    #         Else
    #         {
    #             a=3;
    #         }
    #         }
    #         }
        
        
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))]),Block([AssignStmt(Id(a),IntLit(3))]))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,328))
    # def test_30(self): 
    #     input = """Class Program {
    #         main() {
    #         If(a>b)
    #             {
    #                 a=1;
    #             }
    #         Elseif(a<b)
    #         {
    #             a=3;
    #         }
    #         Else
    #         {
    #             a=4;
    #         }
    #         }
    #         }
        
        
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(3))]),Block([AssignStmt(Id(a),IntLit(4))])))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,329))
    # def test_31(self):
        
    #     input = """Class Rectangle: Shape {
    #         getArea() {
    #     Return Self.length * Self.width; }
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Instance,Id(getArea),[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,330))
    # def test_32(self):
        
    #     input = """Class Rectangle: Shape {
    #         None() {
    #     Return Null;}
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Instance,Id(None),[],Block([Return(NullLiteral())]))])])"
    #     self.assertTrue(TestAST.test(input,expect,331))
    # def test_33(self):
        
    #     input = """Class Program {
    #         main() {
    #         Out.printInt(Shape.Open()); }
    #     }"""
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([CallExpr(Id(Out),Id(printInt),[CallExpr(Id(Shape),Id(Open),[])])]))])])"
    #     self.assertTrue(TestAST.test(input,expect,332))
    # def test_34(self):
        
    #     input = """Class Program {
    #         main() {
    #         Foreach (i In 1 .. 100 By 2) { Out.printInt(i);
    #         } }
    #     }"""
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([CallExpr(Id(Out),Id(printInt),[Id(i)])])])]))])])"
    #     self.assertTrue(TestAST.test(input,expect,333))
    # def test_35(self):
        
    #     input = """Class Program {
    #         main() {
    #         Foreach (x In 5 .. 2) { Out.printInt(arr[y[1]][x]);
    #     } }
    #     }"""
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([For(Id(x),IntLit(5),IntLit(2),Block([CallExpr(Id(Out),Id(printInt),[ArrayCell(Id(arr),[ArrayCell(Id(y),[IntLit(1)]),Id(x)])])])])]))])])"
    #     self.assertTrue(TestAST.test(input,expect,334))
    # def test_36(self):
        
    #     input = """Class Program {
    #         main() {
    #         Break;
    #     } 
    #     }"""
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([Break]))])])"
    #     self.assertTrue(TestAST.test(input,expect,335))
    # def test_37(self):
        
    #     input = """Class Program {
    #         main() {
    #         If(x)
    #             {
    #             Continue;
    #             }
    #         }
    #         }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(Id(x),Block([Continue]))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,336))
    # def test_38(self):
        
    #     input = """Class Program {
    #         main() {
    #         If(x)
    #             {
    #             Shape::$getNumOfShape();
    #             }
    #         }
    #         }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(Id(x),Block([CallExpr(Id(Shape),Id(Shape),[])]))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,337))
    # def test_39(self):
        
    #     input = """Class Program {
    #         main() {
    #             Var r, s: Int;
    #             r= 2.0;
    #             }
    #         }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,338))
    def test_40(self):
        
        input = """Class Program {
            main() {
                Var a, b: Array[Int, 5]; 
                s = r * r * Self.myPI; 
                a[0] = s;

                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([VarDecl(Id(a),ArrayType(IntLit(5),IntType)),VarDecl(Id(b),ArrayType(IntLit(5),IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])"
        self.assertTrue(TestAST.test(input,expect,339))
    

    
   