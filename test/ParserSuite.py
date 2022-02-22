# Huỳnh Bảo Minh -2020047
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """Class MyClass_61 {
                myMethod_61(){
                    a = (c == d) <= (b != 0);   
                }
            
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_2(self):
        input = """
            CLass Rectangle{
            Val a : Int =12;
        }

        """
        expect = "Error on line 2 col 12: CLass"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_3(self):
        input = """CLass Rectangle{
            Val a : Int =12+3*3/2;
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_4(self):
        input = """CLass Rectangle{
            Val a : Int =b[3] + c[2];
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_5(self):
        input = """CLass Rectangle{
            Val a : Int =b[3][2] + c[1][2];
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_6(self):
        input = """CLass Rectangle{
            Val a : Int =2 - (3 + 2);
            b= TruE;
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_7(self):
        input = """CLass Rectangle{
            Val a : int =2 - (3 + 2);
            
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_8(self):
        input = """CLaSS _ectangle{
            VaL a : ArRay[Int,5];
            
        }
        """
        expect = "Error on line 1 col 0: CLaSS"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_9(self):
        
        input = """cLass Rectangle{
            Val a : Array[Int,5];
            
        }
        """
        expect = "Error on line 1 col 0: cLass"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_10(self):
        input = """CLass Rectangle{
            Val a : String= "Hello" +. "World";
            
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_11(self):
        input = """Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_12(self):
        input = """Class Shape {
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_13(self):
        input = """
        CLass Rectangle: Shape {
                getArea() {
            Return Self.length * Self.width; }
            }
        """
        expect = "Error on line 2 col 8: CLass"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_14(self):
        input = """
        Class Program {
            main() {
        Out.printInt(Shape::$numOfShape); }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_15(self):
        input = """
        Class Program {
            main() {
                a= New People("Peter",23,"IT");
                
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_16(self):
        input = """
        Class Program {
            main() {
                a= New People("Peter",23,"IT");   
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_17(self):
        input = """
        Class Program {
            main() {
                a= New Vehicle();
                a.branch="BMW";
                a.model="i5";
                a.cost=100000;
                a.country="Germany" ;  
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_18(self):
        input = """
        Class Program {
            main() {
                Var a : Array[String,3]=Array("Kangxi", "Yongzheng", "Qianlong");
                a[1]="Minh";
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_19(self):
        input = """
        Class Program {
            main() {
                Var a : Array[Int,4]=Array(1, 5, 7, 12);
                a[1]=a[2]+a[3];
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_20(self):
        input = """
        Class Program {
            main() {
                Var a : Array[Array[String,3],3]=Array (
                    Array("Volvo", "22", "18"),
                    Array("Saab", "5", "2"),
                    Array("Land Rover", "17", "15")
            );
                
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_21(self):
        input = """
        Class Program {
            main() {
                Var a : Array[Boolean,3]=array(True,False,true); 
        }
        }
        """
        expect = "Error on line 4 col 46: ("
        self.assertTrue(TestParser.test(input,expect,221))
    def test_22(self):
        input = """
        Class Program {
            main() {
                Var a : Float=12.0e-123; 
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_23(self):
        
        input = """
        Class Program {
            main() {
                Var a : Float=1_234.567; 
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_24(self):
        
        input = """
        Class Program {
            main() {
                Var a : Float=7E-10 * 0.13e2 + 1_34.2; 
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_25(self):
        
        input = """
        Class Program {
            main() {
                Var a : String="He asked me: '"Where is John?'""; 
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_26(self):
        
        input = """
        Class Program {
            main() {
                If(a==True)
                {Return "Hi";}
                Else
                {ReturN "Hello";}
        }
        }
        """
        expect = "Error on line 7 col 31: ;"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_27(self):
        
        input = """
        Class Program {
            main() {
                If(a[3][2]==."Hello")
                {Return b;}
                Else
                {ReturN c;}
        }
        }
        """
        expect = "Error on line 7 col 25: ;"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_28(self):
        
        input = """
        Class Program {
            main() {
                If((a[3][2]==."Hello") && (b==2))
                {Return 3;}
                Else
                {ReturN 5;}
        }
        }
        """
        expect = "Error on line 7 col 25: ;"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_29(self):
        
        input = """
        Class Program {
            main() {
                If((a.Name ==."World") || (c==2))
                {Return True;}
                Else
                {ReturN False;}
        }
        }
        """
        expect = "Error on line 7 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_30(self):
        
        input = """
        Class Program {
            main() {
                If(!(a.Name ==."World"))
                {Return True;}
                Else
                {ReturN False;}
        }
        }
        """
        expect = "Error on line 7 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_31(self):
        
        input = """
        Class Program {
            main() {
                If(a.Count>= 18)
                {a.Name="Adult";}
                Else
                {a.Name="Teen";}
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_32(self):
        
        input = """
        Class Program {
            main() {
                If((a.Count>= 18) && (a.Address ==. "HCM"))
                {a.isWork=TruE;}
                Else
                {a.isWork=False;}
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_33(self):
        
        input = """
        Class Program {
            main() {
                If((a.Count > 18))
                {Return "More than 18";}
                Elseif (a.Count == 18)
                {Return "Equal 18";}
                Elseif (a.Count <12)
                {Return "Less than 12";}
                Else
                {Return "Others";}
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_34(self):
        
        input = """
        Class Program {
            main() {
                Foreach(i In 1 .. 10 By 2)
                {Out.printInt(i);}
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_35(self):
        
        input = """
        Class Program {
            main() {
                Foreach(x In 1 .. 10)
                {Out.printInt(arr[i]);}
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_36(self):
        
        input = """
        Class Program {
            main() {
                Foreach(x In 1 .. 10 By 2)
                {
                    If(x==3)
                    {Break;}
                    Else
                    {
                        Out.printInt(arr[i]);
                    }
                }
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_37(self):
        
        input = """
        Class Program {
            main() {
                Foreach(x In 1 .. 10 By 2)
                {
                    If(x==3)
                    {Continue;}
                    Else
                    {
                        Out.printInt(arr[i]);
                    }
                }
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_38(self):
        
        input = """
        Class Program {
            main() {
                Out.printInt(3);
                Return ;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_39(self):
        
        input = """
        Class Program {
            main() {
                Shape::$getNumOfShape();
                Return ;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_40(self):
        
        input = """
        Class Program {
            main() {
                s = r * r * Self.myPI;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_41(self):
        
        input = """
        Class Program {
            main() {
                var r, s: Int;
                r = 2.0;
                var a, b: Array[Int, 5];
                }
        }
        """
        expect = "Error on line 4 col 21: ,"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_42(self):
        
        input = """
        Class Hello {
            Destructor() {
                
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_43(self):
        
        input = """
        Class Hello {
            Constructor() {
                
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_44(self):
        
        input = """
        Class Hello {
            Val a : Int= b +c[3];
            remove()
            {
                a=Null;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_45(self):
        
        input = """
        Class Hello {
            Val a : String;
            Contructor()
            {
                Self.Intro="Hello";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_46(self):
        
        input = """
        Class Hello {
            Val a : Int= b +c[3];
            Var $numSay : String="Hello";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_47(self):
        
        input = """
        Class Hello {
            Val a : Int= b +c[3];
            Var $numSay : String="Hello";
            increase(b:Int){
                a=b+3;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_48(self):
        
        input = """
        Class Hello {
            Val a : Int= 10;
            Var $numSay : String="Hello";
            condition(c:Int; d: String){
                If(c<a)
                {
                    Return d;
                }
                Else
                {
                    Return;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_49(self):
        
        input = """
        Class Hello {
            Val a : Int= 10;
            
            setValue(c:Int){
                a=c;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_50(self):
        
        input = """
        Class Hello {
            Val a : Int= 10;
            
            Alert(){
               Return "THis is information";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_51(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_52(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_53(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_54(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_55(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_56(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Int,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_57(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_58(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
                ID=1234567;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_59(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
                ID=1234567;
                major="IT";
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_60(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            Destructor()
            {
                
            }
            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_61(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            setName(a:Int)
            {
                self.name=a;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_62(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            setName(a:Int)
            {
                self.name=a;
            }
            getName()
            {
                Return self.name;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_63(self):
        
        input = """
        Class Student {
            Var name : String;
            Var age: Int;
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                age=22;
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            setName(a:String)
            {
                self.name=a;
            }
            getName()
            {
                Return self.name;
            }
            setAge(a:Int)
            {
                self.age=a;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_64(self):
        
        input = """
        Class Student {
            Var name : String;
            Var age: Int;
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                age=22;
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            setName(a:String)
            {
                self.name=a;
            }
            getName()
            {
                Return self.name;
            }
            setAge(a:Int)
            {
                self.age=a;
            }
            getAge()
            {
                Return self.age;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
    def test_65(self):
        
        input = """
        Class Student {
            Var name : String;
            Var age: Int;
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                age=22;
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            setName(a:String)
            {
                self.name=a;
            }
            getName()
            {
                Return self.name;
            }
            setAge(a:Int)
            {
                If(a<=0)
                {
                    Out.printLn("So tuoi khong dung!!");
                }
                self.age=a;
            }
            getAge()
            {
                Return self.age;
            }
            setMajor(a:String){
                self.major=a;
            }
            getMajor()
            {
                Return self.major;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_66(self):
        
        input = """
        Class Animal {
            Var Weight : Float;
            Var Height : Float;
            Info(){
                Out.printLn("Height: " +. Height + "Weight: " +. Weight );
            }
        }
        """
        expect = "Error on line 6 col 62: +."
        self.assertTrue(TestParser.test(input,expect,266))
    def test_67(self):
        
        input = """
        Class Animal {
            Var Weight : Float;
            Var Height : Float;
            Info(){
                Out.printLn("Height: " +. Height + "Weight: " +. Weight );
            }

        }
        Class Program{
            main(){
                Dog= New Animal();
                Dog.Weight=2;## don vi kg##
                Dog.Height=50;## don vi cm##
                Dog.Info();
            }
        }
        """
        expect = "Error on line 6 col 62: +."
        self.assertTrue(TestParser.test(input,expect,267))
    def test_68(self):
        
        input = """
        
        Class Cat{
            Var Weight : Float;
            Var Height : Float;
            Cat(){
                Weight = 800;
                Height = 10;
            }
            Cat(w:Int; h:Int)
            {

            Weight = w;
            Height = h;

            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))
    def test_69(self):
        
        input = """
        
        Class Cat{
            Var Weight : Float;
            Var Height : Float;
            Cat(){
                Weight = 800;
                Height = 10;
            }
            Cat(w:Int; h:Int)
            {

            Weight = w;
            Height = h;

            }
        }
        Class Program{
            main(){
                BlackCat = New Cat();
                BlackCat.Info();
                WhiteCat = New Cat(1200, 30);
                WhiteCat.Info();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_70(self):
        
        input = """
        
        Class SinhVien
    {
        Var MASV:String;
        Var HoTen:String;
        Var DiemToan:Float;
        Var DiemVan:Float;

        InThongTinDiemTB()
        {
            Var DTB :Float = (DiemToan + DiemVan) / 2;
            Console.WriteLine(" Sinh vien " +. HoTen );
            Console.WriteLine("co diem TB la: " +. DTB);
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_71(self):
        
        input = """
        
        Class SinhVien
    {
        Var MASV:String;
        Var HoTen:String;
        Var DiemToan:Float;
        Var DiemVan:Float;

        setDiemToan(a:Float)
        {
            DiemToan=a;
        }
        setDiemVan(a:Float)
        {
            DiemVan=a;
        }

    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
    def test_72(self):
        
        input = """
        
        Class SinhVien
    {
        Var MASV:String;
        Var HoTen:String;
        Var DiemToan:Float;
        Var DiemVan:Float;

        setDiemToan(a:Float)
        {
            DiemToan=a;
        }
        setDiemVan(a:Float)
        {
            DiemVan=a;
        }
        result(){
            If((DiemToan>=8)&&(DiemVan>=8))
            {
                Out.printLn("Hoc sinh gioi");
            }
            Elseif((DiemToan>=7)&&(DiemVan>=7))
            {
                Out.printLn("Hoc sinh Kha");
            }
            Elseif((DiemToan>=5)&&(DiemVan>=5))
            {
                Out.printLn("Hoc sinh Trung binh kha");
            }
            Else{
                Out.printLn("Hoc sinh Yeu");
            }

        }

    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_73(self):
        
        input = """
        
        Class Animal
    {
        Var Weight : Float;
        Var Height : Float;
        Var Legs : Int;

        Info()
        {
            Console.WriteLine(" Weight: " + Weight + " Height: " + Height + " Legs: " + Legs);
        }
    }


    Class Cat : Animal
    {
        Cat()
        {
            
            Weight = 500;
            Height = 20;
            Legs = 2;
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_74(self):
        
        input = """
        
        Class Animal
    {
        Var Weight : Float;
        Var Height : Float;
        Var Legs : Int;

        Info()
        {
            Console.WriteLine(" Weight: " + Weight + " Height: " + Height + " Legs: " + Legs);
        }
    }


    Class Cat : Animal
    {
        Cat()
        {
            
            Weight = 500;
            Height = 20;
            Legs = 2;
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_75(self):
        
        input = """
        
        Class Animal
    {

        Speak()
        {
            Console.WriteLine(" Animal is speaking. . .");
        }
    }


    Class Cat : Animal
    {
        Speak()
        {
            Console.WriteLine(" Cat is speaking. . .");
        }
    }


    Class Dog : Animal
    {
        Speak()
        {
            Console.WriteLine(" Dog is speaking. . .");
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_76(self):
        
        input = """
        
       Class Program{
           main(){
               Return a+3;
           }
       }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_77(self):
        
        input = """
        
       Class Program{
           main(){
               Foreach(x IN 1 .. 3)
               {
                   a[x]=x;
               }
           }
       }
        """
        expect = "Error on line 5 col 25: IN"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_78(self):
        
        input = """
        
       Class Program{
           main(){
               Foreach(x IN 1 .. 3)
               {
                   If(a[x]==1)
                   {
                       Out.printLn("Equal");
                   }
               }
           }
       }
        """
        expect = "Error on line 5 col 25: IN"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_79(self):
        
        input = """
        
       Class Program{
           main(){
            Var r, s: Int;
            r = 2.0;
            Var a, b: Array[Int, 5]; 
            s = r * r * Self.myPI; 
            a[0] = s;
           }
       }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
    def test_80(self):
        
        input = """
        
       Class Program{
           main(){
            Var r, s: Float=1.3,2.4;
            
            Var a, b: Array[String, 5]; 
           
           }
       }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_81(self):
        
        input = """
        
       Class Dog: Pet {
                getWeight() {
                    x = Self.weight;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_82(self):
        
        input = """
        
       Class Dog: Pet {
                getWeight() {
                    x = Self.weight;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_83(self):
        
        input = """
        
       Class Dog: Pet {
                Info() {
                    Out.printLn("Gau gau");
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_84(self):
        
        input = """
            Class Dog {
            Constructor(name:String; birthday:Int) {
                Self.name = name;
                Self.birthday = birthday;
            }

            ##Declare private variables##
            _attendance = 0;

            
        }
        """
        expect = "Error on line 9 col 24: ="
        self.assertTrue(TestParser.test(input,expect,284))
    def test_85(self):
        
        input = """
            Class Dog {
            getAge() {
                ##Getter##
                Return Self.calcAge();
            }

            calcAge() {
                ##calculate age using today's date and birthday##
                Return Date.now() - Self.birthday;
    }

            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_86(self):
        
        input = """
            Class Dog {
            calcAge() {
                ##calculate age using today's date and birthday##
                Return Date.now() - Self.birthday;
    }

            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_87(self):
        
        input = """
            Class MyClass {      
            Val myNum : Int;        
            Var myString : String;  
        }
            Class Program{
                main() {
            myObj=New MyClass();  
            myObj.myNum = 15; 
            myObj.myString = "Some text";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_88(self):
        
        input = """
            Class Car {
            Var brand:String;   
            Var model:String;
            Var year:Int;
            }
            Class Program{
                main() {
            carObj1=New Car();  
           carObj1.brand = "BMW";
            carObj1.model = "X5";
            carObj1.year = 1999;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_89(self):
        
        input = """
            Class MyClass {
            myMethod() {  ##Method/function defined inside the class##
                Out.printLn("Hello World!");
                }
            }
            Class Program{
                main() {
            myObj=New MyClass();     ##Create an object of MyClass##
            myObj.myMethod();  ##all the method##
            Return 0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_90(self):
        
        input = """
            Class MyClass {
            Var brand:String;  ## Attribute##
            Var model:String;  ##Attribute##
            Var year:Int;      ## Attribute##
            Car(x, y:String; z:Int) { ## Constructor with parameters##
            brand = x;
            model = y;
            year = z;
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
    def test_91(self):
        
        input = """
            Class Program {
            main(){
                Var x:Int=2+3.6E12;
                Val $metsa:String="asdasd" +. "asd";
                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_92(self):
        
        input = """
            Class Program {
            main(){
                Return x+y/c*c*(a-x);
                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_93(self):
        
        input = """
            Class Program {
            main(){
                If(a=="2")
                {
                    a="23";
                }

                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_94(self):
        
        input = """
            Class Program {
            main(){
                Foreach(asdf In 1 ... 3)
                {

                }

                
    }
        }
        """
        expect = "Error on line 4 col 36: ."
        self.assertTrue(TestParser.test(input,expect,294))
    def test_95(self):
        
        input = """
            Class Program {
            main(){
               Return Break;

                
    }
        }
        """
        expect = "Error on line 4 col 22: Break"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_96(self):
        
        input = """
            Class Program {
            main(){
               a[a[3].3]=3;

                
    }
        }
        """
        expect = "Error on line 4 col 22: 3"
        self.assertTrue(TestParser.test(input,expect,296))
    def test_97(self):
        
        input = """
            Class Program {
            main(){
               Var a :Array[Array[Array[Int,3],4],5];

                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
    def test_98(self):
        
        input = """
            Class Program {
            main(){
               Foreach (a In 1 .. 2 )
               {
                   If(b[a]==1)
                   {
                       Break;
                   }
               }

                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_99(self):
        
        input = """
            Class Program {
            main(){
               If(ac[3].a[3]==1)
               {

               }

                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    def test_100(self):
        
        input = """
            Class Program {
            main(){
               a=d.x +c[3-3]/2+(1-3)*3;

                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))
