"""program: exp EOF;
exp: (term ASSIGN)* term;
term: factor COMPARE factor | factor;
factor: operand (ANDOR operand)*;
operand: ID | INTLIT | BOOLIT | '(' exp ')';
INTLIT: [0-9]+ ;
BOOLIT: 'True' | 'False' ;
ANDOR: 'and' | 'or' ;
ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;
COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;
ID: [a-z]+ ;
and AST classes as follows:
class Expr(ABC):
class Binary(Expr):  #op:string;left:Expr;right:Expr
class Id(Expr): #value:string
class IntLiteral(Expr): #value:int
class BooleanLiteral(Expr): #value:boolean"""

from functools import reduce
class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self, ctx: MPParser.ExpContext):
        if ctx.ASSIGN():
            ops = [op.getText() for op in ctx.ASSIGN()][::-1]
        else:
            return self.visit(ctx.term(0))
        terms = [self.visit(term) for term in ctx.term()][::-1]
        return reduce(lambda a, e: Binary(e[0], e[1], a), zip(ops, terms[1:]), terms[0])

    def visitTerm(self, ctx: MPParser.TermContext):
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        return self.visit(ctx.getChild(0))

    def visitFactor(self, ctx: MPParser.FactorContext):
        if ctx.ANDOR():
            ops = [op.getText() for op in ctx.ANDOR()]
        else:
            return self.visit(ctx.operand(0))
        operands = [self.visit(x) for x in ctx.operand()]
        return reduce(lambda a, e: Binary(e[0], a, e[1]), zip(ops, operands[1:]), operands[0])

    def visitOperand(self, ctx: MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(bool(ctx.BOOLIT()))
        return self.visit(ctx.exp())

