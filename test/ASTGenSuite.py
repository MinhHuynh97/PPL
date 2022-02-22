import unittest
from TestUtils import TestAST
from AST import *
from main.d96.utils.AST import *
class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Class Rectangle {
            
            hi()
            {
                If(k)
                {

                }
                Elseif(x)
                {

                }
                Elseif(a)
                {

                }Else
                {

                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Hello"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    
   