"""program: mptype EOF;
mptype: primtype | arraytype;
arraytype:  primtype dimen | arraytype dimen  ;
primtype: INTTYPE | FLOATTYPE; 
dimen: '[' num '..' num ']';
num: '-'? INTLIT;
INTLIT: [0-9]+ ;
INTTYPE: 'integer';
FLOATTYPE: 'real';"""


class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.mptype())
    
    def visitMptype(self,ctx:MPParser.MptypeContext):
        type = None
        if 'integer' in ctx.getText():
            type = IntType()
        elif 'real' in ctx.getText(): type = FloatType()
        return self.visit(ctx.primtype()) if ctx.primtype() else ArrayType(self.visit(ctx.arraytype()), type)

    def visitArraytype(self,ctx:MPParser.ArraytypeContext):
        if ctx.arraytype():
            return UnionType(self.visit(ctx.arraytype()) , self.visit(ctx.dimen()))
        return self.visit(ctx.dimen())

    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitDimen(self,ctx:MPParser.DimenContext):
        return RangeType(int(ctx.num(0).getText()),int(ctx.num(1).getText()))

    def visitNum(self,ctx:MPParser.DimenContext):
        return IntLit(int(ctx.INTLIT().getText())) if ctx.getChild(0).getText() != '-' else IntLit(-int(ctx.INTLIT().getText()))
