# class Program: #decl:List[Decl]
# class Decl(ABC): #abstract class
# class VarDecl(Decl): #name:str,typ:Type
# class ConstDecl(Decl): #name:str,val:Lit
# class Type(ABC): #abstract class
# class IntType(Type)
# class FloatType(Type)
# class Lit(ABC): #abstract class
# class IntLit(Lit): #val:int
# and exceptions:
# class RedeclaredVariable(Exception): #name:str
# class RedeclaredConstant(Exception): #name:str
# Implement the methods of the following class Visitor to travel on the above ASST to detect redeclared declarations (throw the exception corresponding to the second declaration with the same name):

from functools import reduce


class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        return reduce(lambda a, e: a + [self.visit(e, a)], ctx.decl, [])

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return ctx.name

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return ctx.name

    def visitIntType(self, ctx: IntType, o: object):
        pass

    def visitFloatType(self, ctx: FloatType, o: object):
        pass

    def visitIntLit(self, ctx: IntLit, o: object):
        pass
