# class Exp(ABC): #abstract class
# class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=
# class UnOp(Exp): #op:str,e:Exp #op is -, !
# class IntLit(Exp): #val:int
# class FloatLit(Exp): #val:float
# # class BoolLit(Exp): #val:bool
# Rewrite the body of the methods in class StaticCheck to check the following type constraints:
# + , - and * accept their operands in int or float type and return float type if at least one of their operands is in float type, otherwise, return int type
# / accepts their operands in int or float type and returns float type
# !, && and || accept their operands in bool type and return bool type
# >, <, == and != accept their operands in any type but must in the same type and return bool type 
# If the expression does not conform the type constraints, the StaticCheck will raise exception TypeMismatchInExpression with the innermost sub-expression that contains type mismatch.
class StaticCheck(Visitor):
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
        elif ctx.op in ['>', '<', '>=', '<=', '==', '!=']:
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
