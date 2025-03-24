from abc import ABC
from dataclasses import dataclass


class Visitor:
    def visit_BinExp(self):
        pass

    def visit_UnExp(self):
        pass

    def visit_IntLit(self):
        pass

    def visit_FloatLit(self):
        pass


@dataclass
class Exp(ABC):
    def accept(self):
        pass


@dataclass
class BinExp(Exp):
    left: Exp
    op: str
    right: Exp

    def accept(self, visitor: Visitor):
        return visitor.visit_BinExp(self)


@dataclass
class UnExp(Exp):
    op: str
    operand: Exp

    def accept(self, visitor: Visitor):
        return visitor.visit_UnExp(self)


@dataclass
class IntLit(Exp):
    val: int

    def accept(self, visitor: Visitor):
        return visitor.visit_IntLit(self)


@dataclass
class FloatLit(Exp):
    val: float

    def accept(self, visitor: Visitor):
        return visitor.visit_FloatLit(self)


class Eval(Visitor):
    def visit_BinExp(self, bin_exp):
        left_val = bin_exp.left.accept(self)
        right_val = bin_exp.right.accept(self)

        if bin_exp.op == "+":
            return left_val + right_val
        elif bin_exp.op == "-":
            return left_val - right_val
        elif bin_exp.op == "*":
            return left_val * right_val
        else:
            return left_val / right_val

    def visit_UnExp(self, un_exp):
        operand_val = un_exp.operand.accept(self)

        if un_exp.op == "+":
            return +operand_val
        else:
            return -operand_val

    def visit_IntLit(self, int_lit):
        return int_lit.val

    def visit_FloatLit(self, float_lit):
        return float_lit.val


class PrintPrefix(Visitor):
    def visit_BinExp(self, bin_exp):
        return f"{bin_exp.op} {bin_exp.left.accept(self)} {bin_exp.right.accept(self)}"

    def visit_UnExp(self, un_exp):
        return f"{un_exp.op}. {un_exp.operand.accept(self)}"

    def visit_IntLit(self, int_lit):
        return str(int_lit.val)

    def visit_FloatLit(self, float_lit):
        return str(float_lit.val)


class PrintPostfix(Visitor):
    def visit_BinExp(self, bin_exp):
        return f"{bin_exp.left.accept(self)} {bin_exp.right.accept(self)} {bin_exp.op}"

    def visit_UnExp(self, un_exp):
        return f"{un_exp.operand.accept(self)} {un_exp.op}."

    def visit_IntLit(self, int_lit):
        return str(int_lit.val)

    def visit_FloatLit(self, float_lit):
        return str(float_lit.val)
