class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        decls = []
        for vardecl in ctx.vardecl():
            decls.extend(self.visit(vardecl))
        return Program(decls)

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        var_type = self.visit(ctx.mptype())
        var_ids = self.visit(ctx.ids())
        return [VarDecl(Id(name), var_type) for name in var_ids]

    def visitMptype(self, ctx: MPParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    def visitIds(self, ctx: MPParser.IdsContext):
        return [id_token.getText() for id_token in ctx.ID()]
