# class Program: #decl:List[Decl]
# class Decl(ABC): #abstract class
# class VarDecl(Decl): #name:str,typ:Type
# class ConstDecl(Decl): #name:str,val:Lit
# class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
# class Type(ABC): #abstract class
# class IntType(Type)
# class FloatType(Type)
# class Expr(ABC): #abstract class
# class Lit(Expr): #abstract class
# class IntLit(Lit): #val:int
# class Id(Expr): #name:str
# and exceptions:
# class RedeclaredVariable(Exception): #name:str
# class RedeclaredConstant(Exception): #name:str
# class RedeclaredFunction(Exception): #name:str
# class UndeclaredIdentifier(Exception): #name:str

from functools import reduce


class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o: object):
        reduce(lambda acc, decl: acc + [self.visit(decl, acc)], ctx.decl, [])

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return ctx.name

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return ctx.name
    
    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        o1 = [o]
        o1 = reduce(lambda acc, param: acc + [self.visit(param, acc)], ctx.param, o1)
        o1 = reduce(lambda acc, decl: acc + [self.visit(decl, acc + [ctx.name])], ctx.body[0], o1)
        o1 = reduce(lambda acc, decl: acc + [self.visit(decl, acc + [ctx.name])], ctx.body[1], o1)
        return ctx.name

    def visitIntType(self, ctx: IntType, o: object): pass

    def visitFloatType(self, ctx: FloatType, o: object): pass

    def visitIntLit(self, ctx: IntLit, o: object): pass

    def visitId(self, ctx: Id, o: object):
        def check_nested(obj):
            if ctx.name in obj:
                return True
            return reduce(
                lambda found, item: found or (check_nested(item) if isinstance(item, list) else False),
                obj,
                False
            )
        if check_nested(o):
            return
        raise UndeclaredIdentifier(ctx.name)
