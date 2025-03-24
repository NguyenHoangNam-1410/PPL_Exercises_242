"""program: exp EOF;
exp: term ASSIGN exp | term;
term: factor COMPARE factor | factor;
factor: factor ANDOR operand | operand;
operand: ID | INTLIT | BOOLIT | '(' exp ')';
INTLIT: [0-9]+ ;
BOOLIT: 'True' | 'False' ;
ANDOR: 'and' | 'or' ;
ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;
COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;
ID: [a-z]+ ;

class Expr(ABC):
class Binary(Expr):  #op:string;left:Expr;right:Expr
class Id(Expr): #value:string
class IntLiteral(Expr): #value:int
class BooleanLiteral(Expr): #value:boolean"""


class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self, ctx: MPParser.ExpContext):
        if ctx.exp():
            return Binary(ctx.ASSIGN().getText(), self.visit(ctx.term()), self.visit(ctx.exp()))
        return self.visit(ctx.term())

    def visitTerm(self, ctx: MPParser.TermContext):
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        return self.visit(ctx.getChild(0))

    def visitFactor(self, ctx: MPParser.FactorContext):
        if ctx.factor():
            return Binary(ctx.ANDOR().getText(), self.visit(ctx.factor()), self.visit(ctx.operand()))
        return self.visit(ctx.operand())

    def visitOperand(self, ctx: MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(bool(ctx.BOOLIT()))
        return self.visit(ctx.exp())
