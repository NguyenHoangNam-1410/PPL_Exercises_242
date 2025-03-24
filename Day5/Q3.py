class NonTerminalCount(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return 2 + self.visit(ctx.vardecls())

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        return 2 + self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        return (
            (2 + self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()))
            if ctx.vardecl()
            else 0
        )

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return 2 + self.visit(ctx.mptype()) + self.visit(ctx.ids())

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return 0

    def visitIds(self, ctx: MPParser.IdsContext):
        return 1 + self.visit(ctx.ids()) if ctx.ids() else 0
