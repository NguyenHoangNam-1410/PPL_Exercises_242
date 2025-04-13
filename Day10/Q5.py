"""
Assume that 

class BinExpr in AST is declared with field op in str type, e1 and e2 in Expr type. op can be '+', '-', '*', '/', '>','<','>=','<=','!=','==' which can accept their operands in IntType or FloatType.  The result type of '+', '-', '*' is IntType if both operands are in IntType otherwise FloatType. The result type of '/' is FloatType and other relational operators are BoolType. Class Expr is the superclass of BinExpr, IntLiteral, FloatLiteral, BoolLiteral.
The visitor CodeGeneration has field emit keeping an object of Emitter 
Object Frame is kept in field frame of the argument passed to parameter o of visitBinExpr
The method visitBinExpr must return a pair of jasmin code of a binary expression and the type of the result (one object of a subclass of class Type)
Based on the above assumption, write method visitBinExpr(self,ctx,o) of visitor CodeGeneration? Your code is at line 160.
Remind that class Type has subclasses: IntType, FloatType, VoidType, StringType, ArrayType, MType.
"""
    def visitBinExpr(self, ctx, o):
        leftCode, leftType = self.visit(ctx.e1, o)
        rightCode, rightType = self.visit(ctx.e2, o)
        resultType = FloatType() if (isinstance(leftType, FloatType) or 
                                    isinstance(rightType, FloatType) or 
                                    ctx.op == '/') else IntType()
        if isinstance(leftType, IntType) and isinstance(resultType, FloatType):
            leftCode += self.emit.emitI2F(o.frame)
        if isinstance(rightType, IntType) and isinstance(resultType, FloatType):
            rightCode += self.emit.emitI2F(o.frame)
        if ctx.op in ['>', '<', '>=', '<=', '!=', '==']:
            opCode = self.emit.emitREOP(ctx.op, resultType, o.frame)
            finalType = BoolType()
        elif ctx.op in ['+', '-']:
            opCode = self.emit.emitADDOP(ctx.op, resultType, o.frame)
            finalType = resultType
        else:  # '*', '/'
            opCode = self.emit.emitMULOP(ctx.op, resultType, o.frame)
            finalType = resultType

        return leftCode + rightCode + opCode, finalType