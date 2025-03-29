# class Program: #decl:List[VarDecl],exp:Exp
# class VarDecl: #name:str,typ:Type
# class Type(ABC): #abstract class
# class IntType(Type)
# class FloatType(Type)
# class BoolType(Type)
# class Exp(ABC): #abstract class
# class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=
# class UnOp(Exp): #op:str,e:Exp #op is -, !
# class IntLit(Exp): #val:int
# class FloatLit(Exp): #val:float
# class BoolLit(Exp): #val:bool
# class Id(Exp): #name:str
from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self, ctx:Program, o):
        env = reduce(lambda env, decl: {**env, **{decl.name: self.visit(decl.typ, env)}}, ctx.decl, {})
        return self.visit(ctx.exp, env)

    def visitVarDecl(self, ctx:VarDecl, o):
        typ = self.visit(ctx.typ, o)
        o[ctx.name] = typ
        return typ

    def visitIntType(self, ctx:IntType, o):
        return 'int'

    def visitFloatType(self, ctx:FloatType, o):
        return 'float'

    def visitBoolType(self, ctx:BoolType, o):
        return 'bool'

    def visitBinOp(self, ctx:BinOp, o):
        leftType = self.visit(ctx.e1, o)
        rightType = self.visit(ctx.e2, o)
        
        if ctx.op in ['+', '-', '*']:
            if leftType == 'float' or rightType == 'float':
                return 'float'
            elif leftType == 'int' and rightType == 'int':
                return 'int'
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op == '/':
            if leftType in ['int', 'float'] and rightType in ['int', 'float']:
                return 'float'
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['&&', '||']:
            if leftType == 'bool' and rightType == 'bool':
                return 'bool'
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['>', '<', '==', '!=']:
            if leftType == rightType and leftType in ['int', 'float']:
                return 'bool'
            else:
                raise TypeMismatchInExpression(ctx)
        else:
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx:UnOp, o):
        expType = self.visit(ctx.e, o)
        
        if ctx.op == '-':
            if expType in ['int', 'float']:
                return expType
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op == '!':
            if expType == 'bool':
                return 'bool'
            else:
                raise TypeMismatchInExpression(ctx)
        else:
            raise TypeMismatchInExpression(ctx)
            
    def visitIntLit(self, ctx:IntLit, o):
        return 'int'
        
    def visitFloatLit(self, ctx:FloatLit, o):
        return 'float'
        
    def visitBoolLit(self, ctx:BoolLit, o):
        return 'bool'
        
    def visitId(self, ctx:Id, o):
        if ctx.name in o:
            return o[ctx.name]
        else:
            raise UndeclaredIdentifier(ctx.name)