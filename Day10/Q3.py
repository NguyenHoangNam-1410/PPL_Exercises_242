"""
Assume that 

class BinExpr in AST is declared with field op in str type, e1 and e2 in Expr type. op can be '+', '-', '*', '/', '+.', '-.', '*.', '/.' where '+', '-', '*', '/' accept 2 operands e1, e2 in IntType and the others accept their operands in FloatType. No Type Error happens. Class Expr is the superclass of BinExpr, IntLiteral and FloatLiteral.
The visitor CodeGeneration has field emit keeping an object of Emitter 
Object Frame is kept in field frame of the argument passed to parameter o of visitBinExpr
The method visitBinExpr must return a pair of jasmin code of a binary expression and the type of the result (one object of a subclass of class Type)
Based on the above assumption, write method visitBinExpr(self,ctx,o) of visitor CodeGeneration? Your code is at line 160.
Remind that class Type has subclasses: IntType, FloatType, VoidType, StringType, ArrayType, MType.
"""
    def visitBinExpr(self, ctx, o):
        leftCode, leftType = self.visit(ctx.e1, o)
        rightCode, rightType = self.visit(ctx.e2, o)
        resultType = FloatType() if '.' in ctx.op else IntType()
        if ctx.op in ['+', '+.', '-', '-.']:
            opCode = self.emit.emitADDOP(ctx.op[0], resultType, o.frame)
        else: # ['*', '*.', '/', '/.']
            opCode = self.emit.emitMULOP(ctx.op[0], resultType, o.frame)
        finalCode = leftCode + rightCode + opCode
        return finalCode, resultType