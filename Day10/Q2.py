    def visitFloatLiteral(self, ctx, o):
        code = self.emit.emitPUSHFCONST(ctx.value, o.frame)
        return code, FloatType()