"""class Program: #decl:List[VarDecl],stmts:List[Stmt]
class VarDecl: #name:str
class Stmt(ABC): #abstract class
class Block(Stmt): #decl:List[VarDecl],stmts:List[Stmt]
class Assign(Stmt): #lhs:Id,rhs:Exp
class Exp(ABC): #abstract class
class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor
class IntLit(Exp): #val:int
class FloatLit(Exp): #val:float
class BoolLit(Exp): #val:bool
class Id(Exp): #name:str"""

# !Rewrite the body of the methods in class StaticCheck to infer the type of identifiers and check the following type constraints:

# + , - , *, / accept their operands in int type and return int type
# +., -., *., /. accept their operands in float type and return float type
# > and = accept their operands in int type and return bool type
# >. and =. accept their operands in float type and return bool type
# &&, !, ||, >b and =b accept their operands in bool type and return bool type
# i2f accepts its operand in int type and return float type
# floor accept its operand in float type and return int type
# In an assignment statement, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the assignment statement.
# the type of an Id is inferred from the above constraints in the first usage, 
# if the Id is not in the declarations, exception UndeclaredIdentifier should be raised together with the name of the Id, or
# If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred should be raised together with the assignment statement which contains the type-unresolved identifier.
# For static referencing environment, this language applies the scope rules of block-structured programming language. When there is a declaration duplication of a name in a scope, exception Redeclared should be raised together with the second declaration.
# If an expression does not conform the type constraints, the StaticCheck will raise exception TypeMismatchInExpression with the expression.

from functools import reduce

class IntType: pass
class FloatType: pass
class BoolType: pass
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = reduce(lambda acc, decl: acc + [self.visit(decl, acc)], ctx.decl, [])
        reduce(lambda acc, stmt: self.visit(stmt, acc) or acc, ctx.stmts, o)
        
    def visitVarDecl(self,ctx:VarDecl,o): 
        if any(ctx.name == i[0] for i in o):
            raise Redeclared(ctx)
        return [ctx.name, None]
        
    def visitBlock(self,ctx:Block,o):
        o1 = reduce(lambda acc, decl: acc + [self.visit(decl, acc)], ctx.decl, [])
        reduce(lambda acc, stmt: self.visit(stmt, acc) or acc, ctx.stmts, o1 + o)
    
    def visitAssign(self,ctx:Assign,o): 
        rhs_type = self.visit(ctx.rhs,o)
        lhs_type = self.visit(ctx.lhs,o)
        if lhs_type and rhs_type:
            if type(lhs_type) is not type(rhs_type):
                raise TypeMismatchInStatement(ctx)
        elif (not lhs_type) and rhs_type:
            o.append(rhs_type)
            self.visit(ctx.lhs,o)
        elif lhs_type and (not rhs_type):
            o.append(lhs_type)
            self.visit(ctx.rhs,o)
        else:
            raise TypeCannotBeInferred(ctx)
        
    def visitBinOp(self, ctx: BinOp, o):
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)
        op = ctx.op

        op_type_map = {
            ('+', '-', '*', '/'): (IntType, IntType),
            ('+.', '-.', '*.', '/.'): (FloatType, FloatType),
            ('>', '='): (IntType, BoolType),
            ('>.', '=.'): (FloatType, BoolType),
            ('!', '&&', '||', '>b', '=b'): (BoolType, BoolType),
        }

        accept_type = return_type = None
        for ops, types in op_type_map.items():
            if op in ops:
                accept_type, return_type = types[0](), types[1]()
                break

        if not accept_type:
            raise TypeMismatchInExpression(ctx)
    
        if left and right:
            if type(left) == type(accept_type) and type(right) == type(accept_type):
                return return_type
            raise TypeMismatchInExpression(ctx)
        if not left:
            o.append(accept_type)
            self.visit(ctx.e1, o)
            if right:
                if type(right) != type(accept_type):
                    raise TypeMismatchInExpression(ctx)
            else:
                o.append(accept_type)
                self.visit(ctx.e2, o)
        elif not right:
            if type(left) != type(accept_type):
                raise TypeMismatchInExpression(ctx)
            o.append(accept_type)
            self.visit(ctx.e2, o)

        return return_type
    
    def visitUnOp(self, ctx: UnOp, o):
        value = self.visit(ctx.e, o)
        op = ctx.op

        accept_type = return_type = None

        if op == "-":
            accept_type = IntType()
            return_type = IntType()
        elif op == "-.":
            accept_type = FloatType()
            return_type = FloatType()
        elif op == "!":
            accept_type = BoolType()
            return_type = BoolType()
        elif op == "i2f":
            accept_type = IntType()
            return_type = FloatType()
        elif op == "floor":
            accept_type = FloatType()
            return_type = IntType()

        if value:
            if type(value) == type(accept_type):
                return return_type
            raise TypeMismatchInExpression(ctx)
        else:
            o.append(accept_type)
            self.visit(ctx.e, o)

        return return_type

    def visitIntLit(self,ctx:IntLit,o): 
        return IntType() 
    
    def visitFloatLit(self,ctx,o): 
        return FloatType()
    
    def visitBoolLit(self,ctx,o): 
        return BoolType()
    
    def visitId(self,ctx:Id,o): 
        for id in o:
            if id[0] == ctx.name:
                if type(o[-1]) in (IntType,FloatType,BoolType): 
                    id[1] = o.pop()
                    return None
                else:
                    return id[1]
        raise UndeclaredIdentifier(ctx.name)
                
