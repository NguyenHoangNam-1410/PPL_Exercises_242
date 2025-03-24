"""program: mptype EOF;
arraytype:  primtype dimens  ;
mptype: primtype | arraytype;
primtype: INTTYPE | FLOATTYPE; 
dimens: dimen+;
dimen: '[' num '..' num ']';
num: '-'? INTLIT;
INTLIT: [0-9]+ ;
INTTYPE: 'integer';
FLOATTYPE: 'real';
and AST classes as follows:
class Type():abstract
class CompoundType(Type):abstract
class UnionType(CompoundType):#firstType:Type,secondType:primType
class ArrayType(CompoundType):#indexType:Type,eleType:primType
class PrimType(Type):abstract
class IntType(PrimType): pass
class FloatType(PrimType): pass
class RangeType(PrimType): #lowbound:int; highbound:int
class Id: #name:str"""

class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.visit(ctx.mptype())

    def visitMptype(self, ctx: MPParser.MptypeContext):
        if ctx.primtype():
            return self.visit(ctx.primtype())
        return self.visit(ctx.arraytype())

    def visitArraytype(self, ctx: MPParser.ArraytypeContext):
        return ArrayType(self.visit(ctx.dimens()) , self.visit(ctx.primtype()))

    def visitPrimtype(self, ctx: MPParser.PrimtypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    def visitDimens(self, ctx: MPParser.DimensContext):
        ranges = [self.visit(dimen) for dimen in ctx.dimen()]
        return reduce(lambda acc, r: UnionType(acc, r), ranges)

    def visitDimen(self, ctx: MPParser.DimenContext):
        return RangeType(self.visit(ctx.num(0)), self.visit(ctx.num(1)))

    def visitNum(self, ctx: MPParser.NumContext):
        value = int(ctx.INTLIT().getText())
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "-":
            return -value
        return value
