# Huỳnh Bảo Minh-2020047

import unittest
from TestUtils import TestAST
from AST import *
# from main.d96.utils.AST import *
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
        Class Rectangle: Shape {
            getArea() {
        Return Self.length * Self.width; }
        }
        
        
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Instance,Id(getArea),[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
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
    def test_31(self):
        
        input = """Class Rectangle: Shape {
            getArea() {
        Return Self.length * Self.width; }
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Instance,Id(getArea),[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,330))
    def test_32(self):
        
        input = """Class Rectangle: Shape {
            None() {
        Return Null;}
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Instance,Id(None),[],Block([Return(NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input,expect,331))
    def test_33(self):
        
        input = """Class Program {
            main() {
            Out.printInt(Shape.Open()); }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([CallExpr(Id(Out),Id(printInt),[CallExpr(Id(Shape),Id(Open),[])])]))])])"
        self.assertTrue(TestAST.test(input,expect,332))
    def test_34(self):
        
        input = """Class Program {
            main() {
            Foreach (i In 1 .. 100 By 2) { Out.printInt(i);
            } }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([CallExpr(Id(Out),Id(printInt),[Id(i)])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,333))
    def test_35(self):
        
        input = """Class Program {
            main() {
            Foreach (x In 5 .. 2) { Out.printInt(arr[y[1]][x]);
        } }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([For(Id(x),IntLit(5),IntLit(2),Block([CallExpr(Id(Out),Id(printInt),[ArrayCell(Id(arr),[ArrayCell(Id(y),[IntLit(1)]),Id(x)])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,334))
    def test_36(self):
        
        input = """Class Program {
            main() {
            Break;
        } 
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([Break]))])])"
        self.assertTrue(TestAST.test(input,expect,335))
    def test_37(self):
        
        input = """Class Program {
            main() {
            If(x)
                {
                Continue;
                }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(Id(x),Block([Continue]))]))])])"
        self.assertTrue(TestAST.test(input,expect,336))
    def test_38(self):
        
        input = """Class Program {
            main() {
            If(x)
                {
                Shape::$getNumOfShape();
                }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(Id(x),Block([CallExpr(Id(Shape),Id($getNumOfShape),[])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,337))
    def test_39(self):
        
        input = """Class Program {
            main() {
                Var r, s: Int;
                r= 2.0;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0))]))])])"
        self.assertTrue(TestAST.test(input,expect,338))
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
    def test_41(self):
        
        input = """Class Program {
            main() {
                Foreach (i In 1 .. 100 By 2) { 
                    If(i>20)
                    {
                        Out.printInt(i);
                    }
                    Else{
                        Out.printInt(i*i);
                    }
                }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([If(BinaryOp(>,Id(i),IntLit(20)),Block([CallExpr(Id(Out),Id(printInt),[Id(i)])]),Block([CallExpr(Id(Out),Id(printInt),[BinaryOp(*,Id(i),Id(i))])]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,340))
    def test_42(self):
        
        input = """Class Program {
            main() {
                    
                Car::$Type();
                    
                
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([CallExpr(Id(Car),Id($Type),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,341))
    def test_43(self):
        
        input = """Class Program {
            main() {
                    
                Return Car::$Type;
                    
                
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([Return(FieldAccess(Id(Car),Id(Car)))]))])])"
        self.assertTrue(TestAST.test(input,expect,342))
    def test_44(self):
        
        input = """Class Program {
            main() {
                    
                a= Car::$Type;
                    
                
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([AssignStmt(Id(a),FieldAccess(Id(Car),Id(Car)))]))])])"
        self.assertTrue(TestAST.test(input,expect,343))
    def test_45(self):
        
        input = """Class Program {
            main() {
                    
                a= Car::$Type(Type.Brand);
                    
                
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([AssignStmt(Id(a),CallExpr(Id(Car),Id(Car),[FieldAccess(Id(Type),Id(Brand))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,344))
    def test_46(self):
        
        input = """Class Program {
            main() {
                    
                a= Car::$Type(Type.Brand,Name::$Pre());
                    
                
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([AssignStmt(Id(a),CallExpr(Id(Car),Id(Car),[FieldAccess(Id(Type),Id(Brand)),CallExpr(Id(Name),Id(Name),[])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,345))
    def test_47(self):
        
        input = """Class Program {
            main() {
                    
                a= Car::$Type(Type.Brand+Type.Fa);
                    
                
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([AssignStmt(Id(a),CallExpr(Id(Car),Id(Car),[BinaryOp(+,FieldAccess(Id(Type),Id(Brand)),FieldAccess(Id(Type),Id(Fa)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,346))
    def test_48(self):
        
        input = """Class Program {
            main() {
                Var a, s: Int;   
                a= Car.Type(Self.Brand);
                s=m[0]+a;
                
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([VarDecl(Id(a),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(a),CallExpr(Id(Car),Id(Type),[FieldAccess(Self(),Id(Brand))])),AssignStmt(Id(s),BinaryOp(+,ArrayCell(Id(m),[IntLit(0)]),Id(a)))]))])])"
        self.assertTrue(TestAST.test(input,expect,347))
    def test_49(self):
        
        input = """Class Program {
            main() {
                Var a: Array[Float, 15]; 
                s = 12 * Self.He; 
                a[10] = s;
                
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([VarDecl(Id(a),ArrayType(IntLit(15),FloatType)),AssignStmt(Id(s),BinaryOp(*,IntLit(12),FieldAccess(Self(),Id(He)))),AssignStmt(ArrayCell(Id(a),[IntLit(10)]),Id(s))]))])])"
        self.assertTrue(TestAST.test(input,expect,348))
    def test_50(self):
        
        input = """Class Program {
            main() {
                Var a: Array[String, 15]; 
                If(a[1]=="as")
                {
                    Return "As";
                }
                
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([VarDecl(Id(a),ArrayType(IntLit(15),StringType)),If(BinaryOp(==,ArrayCell(Id(a),[IntLit(1)]),StringLit(as)),Block([Return(StringLit(As))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,349))
    def test_51(self):
        
        input = """Class Program {
            main() {           
            Val My1stCons, My2ndCons: Int = 1 + 5, 2;
            Var $x, $y : Int = 0, 0;
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5))),ConstDecl(Id(My2ndCons),IntType,IntLit(2)),VarDecl(Id($x),IntType,IntLit(0)),VarDecl(Id($y),IntType,IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,350))
    def test_52(self):
        
        input = """Class Program {
            main() {           
            ## This is a multi-line
            comment. ##
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,351))
    def test_53(self):
        
        input = """Class Program {
            main() {           
            a=Array(1, 5, 7, 12);
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([AssignStmt(Id(a),[IntLit(1),IntLit(5),IntLit(7),IntLit(12)])]))])])"
        self.assertTrue(TestAST.test(input,expect,352))
    def test_54(self):
        
        input = """Class Program {
            main() {           
            a=Array("Kangxi", "Yongzheng", "Qianlong");
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([AssignStmt(Id(a),[StringLit(Kangxi),StringLit(Yongzheng),StringLit(Qianlong)])]))])])"
        self.assertTrue(TestAST.test(input,expect,353))
    def test_55(self):
        
        input = """Class Program {
            main() {           
            a=Array (
                    Array("Volvo", "22", "18"),
                    Array("Saab", "5", "2"),
                    Array("Land Rover", "17", "15")
                    );
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([AssignStmt(Id(a),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])]))])])"
        self.assertTrue(TestAST.test(input,expect,354))
    def test_56(self):
        
        input = """Class Program {
            main() {           
            If((a)&&(b))
            {

            }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(&&,Id(a),Id(b)),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,355))
    def test_57(self):
        
        input = """Class Program {
            main() {           
            If(!a)
            {

            }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(UnaryOp(!,Id(a)),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,356))
    def test_58(self):
        
        input = """Class Program {
            main() {           
            If(a||b)
            {

            }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(||,Id(a),Id(b)),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,357))
    def test_59(self):
        
        input = """Class Program {
            main() {           
            If(a==.b)
            {

            }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(==.,Id(a),Id(b)),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,358))
    def test_60(self):
        
        input = """Class Program {
            main() {           
            a=b+.c;
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([AssignStmt(Id(a),BinaryOp(+.,Id(b),Id(c)))]))])])"
        self.assertTrue(TestAST.test(input,expect,359))
    def test_61(self):
        
        input = """Class Program {
            main() {           
            If(a==b)
            {
                Return a;
            }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,360))
    def test_62(self):
        
        input = """Class Program {
            main() {           
            If(a!=b)
            {
                Return b+a;
            }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(!=,Id(a),Id(b)),Block([Return(BinaryOp(+,Id(b),Id(a)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,361))
    def test_63(self):
        
        input = """Class Program {
            main() {           
            If(a<b)
            {
                Return a+1;
            }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(<,Id(a),Id(b)),Block([Return(BinaryOp(+,Id(a),IntLit(1)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,362))
    def test_64(self):
        
        input = """Class Program {
            main() {           
            If(a>b)
            {
                Return Car.name();
            }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Return(CallExpr(Id(Car),Id(name),[]))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,363))
    def test_65(self):
        
        input = """Class Program {
            main() {           
            If(a<=b)
            {
                a=Object::$kind;
            }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(<=,Id(a),Id(b)),Block([AssignStmt(Id(a),FieldAccess(Id(Object),Id(Object)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,364))
    def test_66(self):
        
        input = """Class Program {
            main() {           
            If(a>=b)
            {
                If(b==10)
                {
                    Return a;
                }Else{
                    Return;
                }
            }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(>=,Id(a),Id(b)),Block([If(BinaryOp(==,Id(b),IntLit(10)),Block([Return(Id(a))]),Block([Return()]))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,365))
    def test_67(self):
        
        input = """Class Program {
            main() {           
            a=b[3]+c[1][3]+d[1][3][3]+m[b[3]][c[1]];
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(+,ArrayCell(Id(b),[IntLit(3)]),ArrayCell(Id(c),[IntLit(1),IntLit(3)])),ArrayCell(Id(d),[IntLit(1),IntLit(3),IntLit(3)])),ArrayCell(Id(m),[ArrayCell(Id(b),[IntLit(3)]),ArrayCell(Id(c),[IntLit(1)])])))]))])])"
        self.assertTrue(TestAST.test(input,expect,366))
    def test_68(self):
        
        input = """Class Program {
            main() {           
            a=expr.Indetider;
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([AssignStmt(Id(a),FieldAccess(Id(expr),Id(Indetider)))]))])])"
        self.assertTrue(TestAST.test(input,expect,367))
    def test_69(self):
        
        input = """Class Program {
            main() {           
            a=indextider::$Indetider;
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([AssignStmt(Id(a),FieldAccess(Id(indextider),Id(indextider)))]))])])"
        self.assertTrue(TestAST.test(input,expect,368))
    def test_70(self):
        
        input = """Class Program {
            main() {           
            indextider::$Indetider();
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([CallExpr(Id(indextider),Id($Indetider),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,369))
    def test_71(self):
        input = """Class Program {
                main() {           
                indextider.Indetider();
                }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([CallExpr(Id(indextider),Id(Indetider),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,370))
    def test_72(self):
        input = """Class Program {
                main() {           
                {indextider.Indetider();}
                }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([Block([CallExpr(Id(indextider),Id(Indetider),[])])]))])])"
        self.assertTrue(TestAST.test(input,expect,371))
    def test_73(self):
        input = """Class Program {
                main() {
                    Var x:Int;
                {Var x : Float;}
                }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([VarDecl(Id(x),IntType),Block([VarDecl(Id(x),FloatType)])]))])])"
        self.assertTrue(TestAST.test(input,expect,372))
    def test_74(self):
        input = """Class Program {
                main() {
                 If(x && b)
                 {

                 }
                {Var x : String;}
                }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(&&,Id(x),Id(b)),Block([])),Block([VarDecl(Id(x),StringType)])]))])])"
        self.assertTrue(TestAST.test(input,expect,373))
    def test_75(self):
        input = """Class Program {
                main() {
                 If(x && b)
                 {

                 }
                {
                    If(c==b)
                    {

                    }
                }
                }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([If(BinaryOp(&&,Id(x),Id(b)),Block([])),Block([If(BinaryOp(==,Id(c),Id(b)),Block([]))])]))])])"
        self.assertTrue(TestAST.test(input,expect,374))
    def test_76(self):
        input = """Class Program {
                $Method(A:Int;C:Float)
                {
                    Return A+C;
                }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Static,Id($Method),[param(Id(A),IntType),param(Id(C),FloatType)],Block([Return(BinaryOp(+,Id(A),Id(C)))]))])])"
        self.assertTrue(TestAST.test(input,expect,375))
    def test_77(self):
        input = """Class Program {
                $Method(A:Int;C:Float)
                {
                    If(A>C)
                    {
                        Out.printInt(A);
                    }Else{
                        Return C;
                    }
                }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Static,Id($Method),[param(Id(A),IntType),param(Id(C),FloatType)],Block([If(BinaryOp(>,Id(A),Id(C)),Block([CallExpr(Id(Out),Id(printInt),[Id(A)])]),Block([Return(Id(C))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,376))
    def test_78(self):
        input = """Class Program {
                $Method(A:Int;C:Float)
                {
                    
                    Foreach (i In 1 .. 100 By 2) { 
                            If(A>C)
                        {
                            a=C;
                            Out.printInt(A);
                        }Else{
                            b=A;
                            Return C;
                            
                        }
                    }           
                }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Static,Id($Method),[param(Id(A),IntType),param(Id(C),FloatType)],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([If(BinaryOp(>,Id(A),Id(C)),Block([AssignStmt(Id(a),Id(C)),CallExpr(Id(Out),Id(printInt),[Id(A)])]),Block([AssignStmt(Id(b),Id(A)),Return(Id(C))]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,377))
    def test_79(self):
        input = """Class Program {
                $Method(A:Int;C:Float)
                {
                    
                    Return A+C;       
                }
                Name(A:String)
                {
                    Return A;
                }
                Var a:Int=0;
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Static,Id($Method),[param(Id(A),IntType),param(Id(C),FloatType)],Block([Return(BinaryOp(+,Id(A),Id(C)))])),MethodDecl(Instance,Id(Name),[param(Id(A),StringType)],Block([Return(Id(A))])),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input,expect,378))
    def test_80(self):
        input = """Class Program {
                $Method(A:Int;C:Float)
                {
                    
                    Return A+C;       
                }
                Name(A:String)
                {
                    Return A;
                }
                Var a:Int=0;
                }
                Class Main:Program{
                    Val c:String=X.Name();
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Static,Id($Method),[param(Id(A),IntType),param(Id(C),FloatType)],Block([Return(BinaryOp(+,Id(A),Id(C)))])),MethodDecl(Instance,Id(Name),[param(Id(A),StringType)],Block([Return(Id(A))])),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0)))]),ClassDecl(Id(Main),Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),StringType,CallExpr(Id(X),Id(Name),[])))])])"
        self.assertTrue(TestAST.test(input,expect,379))
    def test_81(self):
        input = """Class Program {
                
                Name(A:String)
                {
                    Return A;
                }
                Var a:Int=0;
                }
                Class Main:Program{
                    Val c:String=X.a+b/10;
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(Name),[param(Id(A),StringType)],Block([Return(Id(A))])),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0)))]),ClassDecl(Id(Main),Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),StringType,BinaryOp(+,FieldAccess(Id(X),Id(a)),BinaryOp(/,Id(b),IntLit(10)))))])])"
        self.assertTrue(TestAST.test(input,expect,380))
    def test_82(self):
        input = """Class Program {
                
                Name(A:String)
                {
                    Return A;
                }
                Var a:Int=0;
                }
                Class Main:Program{
                    Val c:String=X.a+b/10;
                }
                Class Hide:Main{
                    Var a:Program;
                    Var c:String;
                    
                    Method()
                    {
                        c=a.Name();
                        If(c=="123")
                        {
                            Return "Success";
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(Name),[param(Id(A),StringType)],Block([Return(Id(A))])),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0)))]),ClassDecl(Id(Main),Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),StringType,BinaryOp(+,FieldAccess(Id(X),Id(a)),BinaryOp(/,Id(b),IntLit(10)))))]),ClassDecl(Id(Hide),Id(Main),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Program),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),StringType)),MethodDecl(Instance,Id(Method),[],Block([AssignStmt(Id(c),CallExpr(Id(a),Id(Name),[])),If(BinaryOp(==,Id(c),StringLit(123)),Block([Return(StringLit(Success))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,381))
    def test_83(self):
        input = """
                Class Main:Program{
                    Val c:String=X.a+b/10;
                }
                Class Hide:Program{
                    Var a:Program;
                    Var c:String;
                    
                    Method()
                    {
                        c=a.c()+Self.name;
                        If(c=="123")
                        {
                            Return "Success";
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Main),Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),StringType,BinaryOp(+,FieldAccess(Id(X),Id(a)),BinaryOp(/,Id(b),IntLit(10)))))]),ClassDecl(Id(Hide),Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Program),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),StringType)),MethodDecl(Instance,Id(Method),[],Block([AssignStmt(Id(c),BinaryOp(+,CallExpr(Id(a),Id(c),[]),FieldAccess(Self(),Id(name)))),If(BinaryOp(==,Id(c),StringLit(123)),Block([Return(StringLit(Success))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,382))
    def test_84(self):
        input = """
                Class Main:Program{
                    Val c:String=X.a+b/10;
                }
                Class Hide:Program{
                    Var a:Program;
                    Var c:String;
                    
                    Method()
                    {
                        c=a.c()+Self.name;
                        If(c=="123")
                        {
                            Return "Success";
                        }
                        Else
                        {
                            Return 123;
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Main),Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),StringType,BinaryOp(+,FieldAccess(Id(X),Id(a)),BinaryOp(/,Id(b),IntLit(10)))))]),ClassDecl(Id(Hide),Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Program),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),StringType)),MethodDecl(Instance,Id(Method),[],Block([AssignStmt(Id(c),BinaryOp(+,CallExpr(Id(a),Id(c),[]),FieldAccess(Self(),Id(name)))),If(BinaryOp(==,Id(c),StringLit(123)),Block([Return(StringLit(Success))]),Block([Return(IntLit(123))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,383))
    def test_85(self):
        input = """
                
                Class Hide:Program{
                    Var a:M;
                    Var c:String;
                    
                    Method()
                    {
                        c=a.c()+Self.name;
                        If(c=="123")
                        {
                            Return "Success";
                        }
                        Else
                        {
                            Return 123;
                        }
                    }
                    Print()
                    {
                        If(x==1)
                        {
                            Return Self.Method();
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Hide),Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(M),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),StringType)),MethodDecl(Instance,Id(Method),[],Block([AssignStmt(Id(c),BinaryOp(+,CallExpr(Id(a),Id(c),[]),FieldAccess(Self(),Id(name)))),If(BinaryOp(==,Id(c),StringLit(123)),Block([Return(StringLit(Success))]),Block([Return(IntLit(123))]))])),MethodDecl(Instance,Id(Print),[],Block([If(BinaryOp(==,Id(x),IntLit(1)),Block([Return(CallExpr(Self(),Id(Method),[]))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,384))
    def test_86(self):
        input = """
                
                Class Hide:Program{
                    Var a:M;
                    Var c:String;
                    
                    Method()
                    {
                        c=a.c()+Self.name;
                        If(c==12)
                        {
                            Return "Success";
                        }
                        Else
                        {
                            Return 123;
                        }
                    }
                    Print()
                    {
                        If(x=="1")
                        {
                            Return Self.Method()+Self.Max;
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Hide),Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(M),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),StringType)),MethodDecl(Instance,Id(Method),[],Block([AssignStmt(Id(c),BinaryOp(+,CallExpr(Id(a),Id(c),[]),FieldAccess(Self(),Id(name)))),If(BinaryOp(==,Id(c),IntLit(12)),Block([Return(StringLit(Success))]),Block([Return(IntLit(123))]))])),MethodDecl(Instance,Id(Print),[],Block([If(BinaryOp(==,Id(x),StringLit(1)),Block([Return(BinaryOp(+,CallExpr(Self(),Id(Method),[]),FieldAccess(Self(),Id(Max))))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,385))
    def test_87(self):
        input = """
                
                Class Hide:Program{
                    Var a:M;
                    Var c:String;
                    
                    Method()
                    {
                        c=a.c()+Self.name;
                        If(c==12)
                        {
                            Return "Success";
                        }
                        Else
                        {
                            Return 123;
                        }
                    }
                    Print()
                    {
                        If(x=="1")
                        {
                            Return Self.Method()+Self.Max;
                        }
                        Elseif(x=="2")
                        {
                            Return Null;
                        }

                    }
                }
            """
        expect = "Program([ClassDecl(Id(Hide),Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(M),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),StringType)),MethodDecl(Instance,Id(Method),[],Block([AssignStmt(Id(c),BinaryOp(+,CallExpr(Id(a),Id(c),[]),FieldAccess(Self(),Id(name)))),If(BinaryOp(==,Id(c),IntLit(12)),Block([Return(StringLit(Success))]),Block([Return(IntLit(123))]))])),MethodDecl(Instance,Id(Print),[],Block([If(BinaryOp(==,Id(x),StringLit(1)),Block([Return(BinaryOp(+,CallExpr(Self(),Id(Method),[]),FieldAccess(Self(),Id(Max))))]),If(BinaryOp(==,Id(x),StringLit(2)),Block([Return(NullLiteral())])))]))])])"
        self.assertTrue(TestAST.test(input,expect,386))
    def test_88(self):
        input = """
                
                Class Hide:Program{
                    Var a:M;
                    Var c:String;
                    
                    Method()
                    {
                        c=a.c()+Self.name;
                        If(c==12)
                        {
                            Return "Success";
                        }
                        Else
                        {
                            Return 123;
                        }
                    }
                    Print()
                    {
                        If(x=="1")
                        {
                            Return Self.Method()+Self.Max;
                        }
                        Elseif(x=="2")
                        {
                            Return Null;
                        }
                        Else{
                            Return a+b+Self.min();
                        }

                    }
                }
            """
        expect = "Program([ClassDecl(Id(Hide),Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(M),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),StringType)),MethodDecl(Instance,Id(Method),[],Block([AssignStmt(Id(c),BinaryOp(+,CallExpr(Id(a),Id(c),[]),FieldAccess(Self(),Id(name)))),If(BinaryOp(==,Id(c),IntLit(12)),Block([Return(StringLit(Success))]),Block([Return(IntLit(123))]))])),MethodDecl(Instance,Id(Print),[],Block([If(BinaryOp(==,Id(x),StringLit(1)),Block([Return(BinaryOp(+,CallExpr(Self(),Id(Method),[]),FieldAccess(Self(),Id(Max))))]),If(BinaryOp(==,Id(x),StringLit(2)),Block([Return(NullLiteral())]),Block([Return(BinaryOp(+,BinaryOp(+,Id(a),Id(b)),CallExpr(Self(),Id(min),[])))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,387))
    def test_89(self):
        input = """
                
                Class Hide:Program{
                    Var a:M;
                    Var c:String;
                    Hi(a:Int;c:String)
                    {
                        Self.a=a;
                        Self.c=c;
                    }
                    
                    
                }
            """
        expect = "Program([ClassDecl(Id(Hide),Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(M),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),StringType)),MethodDecl(Instance,Id(Hi),[param(Id(a),IntType),param(Id(c),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(a)),AssignStmt(FieldAccess(Self(),Id(c)),Id(c))]))])])"
        self.assertTrue(TestAST.test(input,expect,388))
    def test_90(self):
        input = """
                
                Class Hide:Program{
                    Var a:M;
                    Var c:String;
                    Hi(a:Int;c:String)
                    {
                        Self.a=a;
                        Self.c=c;
                    }
                    Get()
                    {
                        Return a+c;
                    }
                    
                    
                }
            """
        expect = "Program([ClassDecl(Id(Hide),Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(M),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),StringType)),MethodDecl(Instance,Id(Hi),[param(Id(a),IntType),param(Id(c),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(a)),AssignStmt(FieldAccess(Self(),Id(c)),Id(c))])),MethodDecl(Instance,Id(Get),[],Block([Return(BinaryOp(+,Id(a),Id(c)))]))])])"
        self.assertTrue(TestAST.test(input,expect,389))
    def test_92(self):
        input = """
                
                Class Hide:Program{
                    Var a:M;
                    Var c:String;
                    Hi(a:Int;c:String)
                    {
                        Self.a=a;
                        Self.c=c;
                    }
                    Get()
                    {
                        Return a+c;
                    }
                    Sum(a,c,v:Int)
                    {
                        If(a==10)
                        {
                            Return a+v;
                        }
                        Else
                        {
                            a=a+c+v;
                        }

                    }
                    
                    
                }
            """
        expect = "Program([ClassDecl(Id(Hide),Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(M),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),StringType)),MethodDecl(Instance,Id(Hi),[param(Id(a),IntType),param(Id(c),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(a)),AssignStmt(FieldAccess(Self(),Id(c)),Id(c))])),MethodDecl(Instance,Id(Get),[],Block([Return(BinaryOp(+,Id(a),Id(c)))])),MethodDecl(Instance,Id(Sum),[param(Id(a),IntType),param(Id(c),IntType),param(Id(v),IntType)],Block([If(BinaryOp(==,Id(a),IntLit(10)),Block([Return(BinaryOp(+,Id(a),Id(v)))]),Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,Id(a),Id(c)),Id(v)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,391))
    def test_93(self):
        input = """
                
                Class Hide:Program{
                    Var a:M;
                    Var c:String;
                    Hi(a:Int;c:String)
                    {
                        Self.a=a;
                        Self.c=c;
                    }
                    Get()
                    {
                        Return a+c;
                    }
                    Sum(a,c,v:Int)
                    {
                        If(a==10)
                        {
                            Return a+v;
                        }
                        Else
                        {
                            a=a+c+v;
                        }

                    }
                    
                    
                }
            """
        expect = "Program([ClassDecl(Id(Hide),Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(M),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),StringType)),MethodDecl(Instance,Id(Hi),[param(Id(a),IntType),param(Id(c),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(a)),AssignStmt(FieldAccess(Self(),Id(c)),Id(c))])),MethodDecl(Instance,Id(Get),[],Block([Return(BinaryOp(+,Id(a),Id(c)))])),MethodDecl(Instance,Id(Sum),[param(Id(a),IntType),param(Id(c),IntType),param(Id(v),IntType)],Block([If(BinaryOp(==,Id(a),IntLit(10)),Block([Return(BinaryOp(+,Id(a),Id(v)))]),Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,Id(a),Id(c)),Id(v)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,392))
    def test_94(self): 
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
        self.assertTrue(TestAST.test(input,expect,393))
    def test_95(self): 
        input = """Class Shape {       
            Val $a:Int ;
            Var b,c:Float;
            
        }
        Class Rectangle: Shape {
            getArea() {
        Return Self.length * Self.width; }
        }
        
        
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Instance,Id(getArea),[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,394))
    def test_96(self): 
        input = """Class Program {
            main() {
            Out.printInt(Shape::$numOfShape); }
            }
        
        
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Instance,Id(main),[],Block([CallExpr(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id(Shape))])]))])])"
        self.assertTrue(TestAST.test(input,expect,395))
    def test_97(self): 
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
        self.assertTrue(TestAST.test(input,expect,396))
    def test_98(self): 
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
        self.assertTrue(TestAST.test(input,expect,397))
    def test_99(self):
        
        input = """Class Rectangle: Shape {
            getArea() {
        Return Self.length * Self.width; }
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Instance,Id(getArea),[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,398))
    def test_100(self):
        
        input = """Class Rectangle: Shape {
            None() {
        Return Null;}
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Instance,Id(None),[],Block([Return(NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input,expect,399))
    def test_101(self):
        input = """Class Rectangle: Shape {
            Print(C:String)
            {
                
                    Return "C is :" +.C;
                            
            }
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Instance,Id(Print),[param(Id(C),StringType)],Block([Return(BinaryOp(+.,StringLit(C is :),Id(C)))]))])])"
        self.assertTrue(TestAST.test(input,expect,400))
    
    

    
   