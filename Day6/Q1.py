"""program: vardecls EOF;

vardecls: vardecl vardecltail;

vardecltail: vardecl vardecltail | ;

vardecl: mptype ids ';' ;

mptype: INTTYPE | FLOATTYPE;

ids: ID ',' ids | ID;"""


class Height(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):

        return 1 + self.visit(ctx.vardecls())

    def visitVardecls(self, ctx: MPParser.VardeclsContext):

        return 1 + max(self.visit(ctx.vardecl()), self.visit(ctx.vardecltail()))

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):

        return (
            1 + max(self.visit(ctx.vardecl()), self.visit(ctx.vardecltail()))
            if ctx.vardecl()
            else 1
        )

    def visitVardecl(self, ctx: MPParser.VardeclContext):

        return 1 + max(self.visit(ctx.mptype()), self.visit(ctx.ids()))

    def visitMptype(self, ctx: MPParser.MptypeContext):

        return 2

    def visitIds(self, ctx: MPParser.IdsContext):

        return 1 + self.visit(ctx.ids()) if ctx.ids() else 2
