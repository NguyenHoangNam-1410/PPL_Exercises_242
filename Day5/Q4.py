class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        return []

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        var_type = self.visit(ctx.mptype())
        var_ids = self.visit(ctx.ids())
        return [VarDecl(Id(name), var_type) for name in var_ids]

    def visitMptype(self, ctx: MPParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    def visitIds(self, ctx: MPParser.IdsContext):
        if ctx.ids():
            return [ctx.ID().getText()] + self.visit(ctx.ids())
        return [ctx.ID().getText()]
