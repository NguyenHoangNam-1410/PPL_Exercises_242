"""class Program: #decl:List[Decl],stmts:List[Stmt]
class Decl(ABC): #abstract class
class VarDecl(Decl): #name:str
class FuncDecl(Decl): #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
class Stmt(ABC): #abstract class
class Assign(Stmt): #lhs:Id,rhs:Exp
class CallStmt(Stmt): #name:str,args:List[Exp]
class Exp(ABC): #abstract class
class IntLit(Exp): #val:int
class FloatLit(Exp): #val:float
class BoolLit(Exp): #val:bool
class Id(Exp): #name:str"""

# !Rewrite the body of the methods in class StaticCheck to infer the type of identifiers and check the following type constraints:

# In an Assign, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the Assign
# the type of an Id is inferred from the above constraints in the first usage, 
# if the Id is not in the declarations, exception UndeclaredIdentifier should be raised together with the name of the Id, or
# If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred should be raised together with the statement
# For static referencing environment, this language applies the scope rules of block-structured programming language where a function is a block. When there is a declaration duplication of a name in a scope, exception Redeclared should be raised together with the second declaration.
# In a call statement, the argument type must be the same as the parameter type. If there is no function declaration in the static referencing environment, exception UndeclaredIdentifier should be raised together with the function call name. If the numbers of parameters and arguments are not the same or at least one argument type is not the same as the type of the corresponding parameter, exception TypeMismatchInStatement should be raise with the call statement. If there is at least one parameter type cannot be resolved, exception TypeCannotBeInferred should be raised together with the call statement.

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

    def visitFuncDecl(self, ctx: FuncDecl, o):
        if any(ctx.name == i[0] for i in o):
            raise Redeclared(ctx)
        o1 = reduce(lambda acc, decl: acc + [self.visit(decl, acc)], ctx.param, [])
        o2 = reduce(lambda acc, decl: acc + [self.visit(decl, o1 + acc)], ctx.local, [])
        reduce(lambda _, stmt: self.visit(stmt, o1 + o2 + o), ctx.stmts, None)
        return [ctx.name, o1]

    def visitCallStmt(self, ctx: CallStmt, o):
        call_stmt = next((i for i in o if ctx.name == i[0]), None)

        if not call_stmt or not isinstance(call_stmt[1], list):
            raise UndeclaredIdentifier(ctx.name)
        param_list = call_stmt[1]
        if len(ctx.args) != len(param_list):
            raise TypeMismatchInStatement(ctx)

        for i in range(len(ctx.args)):
            _, param_type = param_list[i]
            arg_type = self.visit(ctx.args[i], o)
            if arg_type and param_type:
                if type(arg_type) is not type(param_type):
                    raise TypeMismatchInStatement(ctx)
            elif not arg_type and param_type:
                o.append(param_type)
                self.visit(ctx.args[i], o)
            elif arg_type and not param_type:
                param_list[i][1] = arg_type
            else:
                raise TypeCannotBeInferred(ctx)

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

    def visitIntLit(self,ctx,o): 
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